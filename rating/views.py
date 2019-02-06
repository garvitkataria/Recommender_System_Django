from django.shortcuts import render
import requests
from rest_framework import viewsets,permissions
from .models import Rating
from .serializers import ratingSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
import pandas as pd
# Create your views here.
class ratingView(viewsets.ModelViewSet):
	queryset = Rating.objects.all()
	serializer_class = ratingSerializer


class RecommendView(APIView):

	def get(self, request, format=None):
		# print("HI")
		rating_r = requests.get('http://127.0.0.1:8000/rating/')
		rating_data=rating_r.json()
		rating = pd.DataFrame.from_dict(rating_data)
		# print(rating.head())
		userRatings = rating.pivot_table(index=['user'],columns=['movie'],values='rating')
		# print(userRatings.head())
		corrMatrix = userRatings.corr()
		# print(corrMatrix.head())

		myRatings = userRatings.loc["http://127.0.0.1:8000/user/1/"].dropna()

		simCandidates = pd.Series()
		for i in range(0, len(myRatings.index)):
		    sims = corrMatrix[myRatings.index[i]].dropna()
		    sims = sims.map(lambda x: x * myRatings[i])
		    simCandidates = simCandidates.append(sims)

		simCandidates = simCandidates.groupby(simCandidates.index).sum()
		simCandidates.sort_values(inplace = True, ascending = False)
		print (simCandidates.head())
		df1 = pd.DataFrame(data=simCandidates.index, columns=['movie'])
		df2 = pd.DataFrame(data=simCandidates.values, columns=['val'])
		df = pd.merge(df1, df2, left_index=True, right_index=True)
		return Response(df)

