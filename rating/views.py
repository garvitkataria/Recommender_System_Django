from django.shortcuts import render
import requests
from rest_framework import viewsets,permissions
from .models import Rating
from .serializers import ratingSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
import pandas as pd
import numpy as np
from scipy.sparse.linalg import svds

# Create your views here.
class ratingView(viewsets.ModelViewSet):
	queryset = Rating.objects.all()
	serializer_class = ratingSerializer

# API of Item-Based Collaborative Filtering
class RecommendView(APIView):
	
	def get(self, request, format=None):
		server = 'http://35.200.250.64:8007/'
		# User id fetch from the API
		user_id= request.GET.get('user_id')
		rating_r = requests.get(server+'rating/')
		rating_data=rating_r.json()
		rating = pd.DataFrame.from_dict(rating_data)

		userRatings = rating.pivot_table(index=['user'],columns=['movie'],values='rating')

		# pandas has a built-in corr() method that will compute a correlation score for every column pair in the matrix
		corrMatrix = userRatings.corr()

		# Movies rated by the user 
		myRatings = userRatings.loc[server+"user/"+user_id+"/"].dropna()

		#For each movie I rated, I'll retrieve the list of similar movies from our correlation matrix. 
		simCandidates = pd.Series()
		for i in range(0, len(myRatings.index)):
		    sims = corrMatrix[myRatings.index[i]].dropna()
		    sims = sims.map(lambda x: x * myRatings[i])
		    simCandidates = simCandidates.append(sims)

		# Add the movies repeated in the list and sort them by its value
		simCandidates = simCandidates.groupby(simCandidates.index).sum()
		simCandidates.sort_values(inplace = True, ascending = False)

		# Considering all the values even the ones with negative values
		simCandidates_positives=simCandidates
		simCandidates_positives

		'''So the API sends the movie as a url. Ex http://127.0.0.1:8000/movies/194/ 
		So List_rec_movies list has movie recommendations and contains movie id like 194'''
		List_rec_movies=[]
		for i in range(len(simCandidates_positives)):
		    temp=simCandidates_positives.index[i]
		    List_rec_movies.append(str(temp).split('/')[-2])
		List_rec_movies

		# List_i_rec contains the id of movies which I rated.
		List_i_rec=[]
		for i in range(len(myRatings)):
		    temp=myRatings.index[i]
		    List_i_rec.append(str(temp).split('/')[-2])
		List_i_rec

		# Removing the movies which I rated from the list of recommended movies
		Final_list=[]
		for i in List_rec_movies:
		    if i in List_i_rec:
		        pass
		    else:
		        Final_list.append(i)

		# Returning the top 10 movies from the final list of recommended movies
		Final_list_top_ten=Final_list[0:10]
		return Response(Final_list_top_ten)

# API of User-Based Collaborative Filtering
class Recommend2View(APIView):

	def get(self, request, format=None):
		server = 'http://35.200.250.64:8007/'
		# User id fetch from the API
		user_id= request.GET.get('user_id')
		rating_r = requests.get(server+'rating/')
		rating_data=rating_r.json()

		rating = pd.DataFrame.from_dict(rating_data)
		userRatings = rating.pivot_table(index=['movie'],columns=['user'],values='rating')

		# pandas has a built-in corr() method that will compute a correlation score for every column pair in the matrix
		corrMatrix = userRatings.corr()

		# Movies rated by the user 
		myRatings = userRatings.loc[:,server+"user/"+user_id+"/"].dropna()

		''' Through Correlation matrix get the user which has similarity greater than 0 (As we have less user now).
		Drop the user himself from the condidates of similar user. '''
		my_releation_with_users = corrMatrix.loc[:,server+"user/"+user_id+"/"].dropna()
		my_releation_with_users_positive=my_releation_with_users[my_releation_with_users>0]
		my_releation_with_users_positive_2 = my_releation_with_users_positive.drop(server+"user/"+user_id+"/")
		
		#For each user in the my_releation_with_users_positive_2, I'll retrieve the list of movies rated by that user. 
		simCandidates = pd.Series()
		for i in range(len(my_releation_with_users_positive_2)):
		    sim = userRatings[my_releation_with_users_positive_2.index[i]].dropna()
		    sim = sim.map(lambda x: x * (my_releation_with_users_positive_2[i]))
		    simCandidates = simCandidates.append(sim)

		# Add the movies repeated in the list and sort them by its value
		simCandidates = simCandidates.groupby(simCandidates.index).sum()
		simCandidates.sort_values(inplace = True, ascending = False)

		# Considering all the values greater than 0.5 ratings.
		simCandidates_positives=simCandidates[simCandidates>0.5]

		'''So the API sends the movie as a url. Ex http://127.0.0.1:8000/movies/194/ 
		So List_rec_movies list has movie recommendations and contains movie id like 194'''
		List_rec_movies=[]
		for i in range(len(simCandidates_positives)):
		    temp=simCandidates_positives.index[i]
		    List_rec_movies.append(str(temp).split('/')[-2])

		# List_i_rec contains the id of movies which I rated.
		List_i_rec=[]
		for i in range(len(myRatings)):
		    temp=myRatings.index[i]
		    List_i_rec.append(str(temp).split('/')[-2])

		# Removing the movies which I rated from the list of recommended movies
		Final_list=[]
		for i in List_rec_movies:
		    if not i in List_i_rec:
		        Final_list.append(i)

		# Returning the top 10 movies from the final list of recommended movies        
		Final_list_top_ten=Final_list[0:10]
		return Response(Final_list_top_ten)

# API of Matrix Factorization via Singular Value Decomposition
class Recommend3View(APIView):
	def get(self, request, format=None):
		server = 'http://35.200.250.64:8007/'
		# User id fetch from the API
		user_id= request.GET.get('user_id')
		rating_r = requests.get(server+'rating/')
		rating_data=rating_r.json()

		rating = pd.DataFrame.from_dict(rating_data)
		userRatings = rating.pivot_table(index=['user'],columns=['movie'],values='rating').fillna(0)

		R = userRatings.as_matrix()
		user_ratings_mean = np.mean(R, axis = 1)
		R_demeaned = R - user_ratings_mean.reshape(-1, 1)

		'''Scipy and Numpy both have functions to do the singular value decomposition. 
		I'm going to use the Scipy function svds because it let's me choose how many latent factors 
		I want to use to approximate the original ratings matrix '''
		U, sigma, Vt = svds(R_demeaned, k = 7)
		sigma = np.diag(sigma)
		all_user_predicted_ratings = np.dot(np.dot(U, sigma), Vt) + user_ratings_mean.reshape(-1, 1)

		# Movies rated by the user 
		myRatings = userRatings.loc[server+"user/"+user_id+"/"]
		myRatings = myRatings[myRatings>0]
		
		# List_i_rec contains the id of movies which I rated.
		List_i_rec=[]
		for i in range(len(myRatings)):
		    temp=myRatings.index[i]
		    print(temp)
		    List_i_rec.append(str(temp).split('/')[-2])

		# Getting the predicted ratings of user from the list of all_user_predicted_ratings
		preds_df = pd.DataFrame(all_user_predicted_ratings, columns = userRatings.columns,index= userRatings.index)
		preds_df_user = preds_df.loc[server+'user/'+user_id+'/']
		preds_df_user.sort_values(inplace = True, ascending = False)

		# Removing the movies which I rated from the list of recommended movies
		Final_list=[]
		for i in preds_df_user.index:
		    if i.split('/')[-2] not in List_i_rec:
		        Final_list.append(i.split('/')[-2])

		# Returning the top 10 movies from the final list of recommended movies        
		Final_list_top_ten=Final_list[0:10]
		return Response(Final_list_top_ten)




