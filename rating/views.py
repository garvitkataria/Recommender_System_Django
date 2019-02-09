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


class RecommendView(APIView):
	
	def get(self, request, format=None):
		# print("HI")
		# user_id="4"
		user_id= request.GET.get('user_id')
		rating_r = requests.get('http://127.0.0.1:8000/rating/')
		rating_data=rating_r.json()
		rating = pd.DataFrame.from_dict(rating_data)
		# print(rating.head())
		userRatings = rating.pivot_table(index=['user'],columns=['movie'],values='rating')
		# print(userRatings.head())
		corrMatrix = userRatings.corr()
		# print(corrMatrix.head())

		myRatings = userRatings.loc["http://127.0.0.1:8000/user/"+user_id+"/"].dropna()

		simCandidates = pd.Series()
		for i in range(0, len(myRatings.index)):
		    sims = corrMatrix[myRatings.index[i]].dropna()
		    sims = sims.map(lambda x: x * myRatings[i])
		    simCandidates = simCandidates.append(sims)

		simCandidates = simCandidates.groupby(simCandidates.index).sum()
		simCandidates.sort_values(inplace = True, ascending = False)
		# print(simCandidates)

		simCandidates_positives=simCandidates
		simCandidates_positives

		List_rec_movies=[]
		for i in range(len(simCandidates_positives)):
		    temp=simCandidates_positives.index[i]
		    List_rec_movies.append(str(temp).split('/')[-2])
		List_rec_movies

		List_i_rec=[]
		for i in range(len(myRatings)):
		    temp=myRatings.index[i]
		    # print(temp)
		    List_i_rec.append(str(temp).split('/')[-2])
		List_i_rec

		Final_list=[]
		for i in List_rec_movies:
		    if i in List_i_rec:
		        pass
		    else:
		        Final_list.append(i)
		# print(Final_list)

		Final_list_top_ten=Final_list[0:10]
		return Response(Final_list_top_ten)

class Recommend2View(APIView):

	def get(self, request, format=None):
		# user_id="1"
		user_id= request.GET.get('user_id')
		rating_r = requests.get('http://127.0.0.1:8000/rating/')
		rating_data=rating_r.json()

		rating = pd.DataFrame.from_dict(rating_data)
		userRatings = rating.pivot_table(index=['movie'],columns=['user'],values='rating')
		corrMatrix = userRatings.corr()
		myRatings = userRatings.loc[:,"http://127.0.0.1:8000/user/"+user_id+"/"].dropna()
		my_releation_with_users = corrMatrix.loc[:,"http://127.0.0.1:8000/user/"+user_id+"/"].dropna()
		my_releation_with_users_positive=my_releation_with_users[my_releation_with_users>0]
		my_releation_with_users_positive_2 = my_releation_with_users_positive.drop("http://127.0.0.1:8000/user/"+user_id+"/")
		simCandidates = pd.Series()

		for i in range(len(my_releation_with_users_positive_2)):
		    sim = userRatings[my_releation_with_users_positive_2.index[i]].dropna()
		    sim = sim.map(lambda x: x * (my_releation_with_users_positive_2[i]))
		    simCandidates = simCandidates.append(sim)
		simCandidates = simCandidates.groupby(simCandidates.index).sum()
		simCandidates.sort_values(inplace = True, ascending = False)
		simCandidates_positives=simCandidates[simCandidates>0.5]
		List_rec_movies=[]
		for i in range(len(simCandidates_positives)):
		    temp=simCandidates_positives.index[i]
		    List_rec_movies.append(str(temp).split('/')[-2])
		List_i_rec=[]
		for i in range(len(myRatings)):
		    temp=myRatings.index[i]
		    List_i_rec.append(str(temp).split('/')[-2])
		Final_list=[]
		for i in List_rec_movies:
		    if not i in List_i_rec:
		        Final_list.append(i)
		Final_list_top_ten=Final_list[0:10]
		return Response(Final_list_top_ten)

class Recommend3View(APIView):
	def get(self, request, format=None):
		user_id= request.GET.get('user_id')

		rating_r = requests.get('http://127.0.0.1:8000/rating/')
		rating_data=rating_r.json()

		rating = pd.DataFrame.from_dict(rating_data)
		userRatings = rating.pivot_table(index=['user'],columns=['movie'],values='rating').fillna(0)

		R = userRatings.as_matrix()
		user_ratings_mean = np.mean(R, axis = 1)
		R_demeaned = R - user_ratings_mean.reshape(-1, 1)

		
		U, sigma, Vt = svds(R_demeaned, k = 7)
		sigma = np.diag(sigma)
		all_user_predicted_ratings = np.dot(np.dot(U, sigma), Vt) + user_ratings_mean.reshape(-1, 1)

		myRatings = userRatings.loc["http://127.0.0.1:8000/user/"+user_id+"/"]
		myRatings = myRatings[myRatings>0]

		List_i_rec=[]
		for i in range(len(myRatings)):
		    temp=myRatings.index[i]
		    print(temp)
		    List_i_rec.append(str(temp).split('/')[-2])

		preds_df = pd.DataFrame(all_user_predicted_ratings, columns = userRatings.columns,index= userRatings.index)
		preds_df_user = preds_df.loc['http://127.0.0.1:8000/user/'+user_id+'/']
		preds_df_user.sort_values(inplace = True, ascending = False)

		Final_list=[]
		for i in preds_df_user.index:
		    if i.split('/')[-2] not in List_i_rec:
		        Final_list.append(i.split('/')[-2])
		Final_list_top_ten=Final_list[0:10]
		return Response(Final_list_top_ten)




