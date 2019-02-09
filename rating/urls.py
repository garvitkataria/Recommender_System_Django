from django.conf.urls import url,include
from . import views
from rest_framework import routers
from .views import RecommendView,Recommend2View,Recommend3View

router = routers.DefaultRouter()
router.register('', views.ratingView)

urlpatterns = [

	url(r'^recommend/$', RecommendView.as_view()),
	url(r'^recommend2/$', Recommend2View.as_view()),
	url(r'^recommend3/$', Recommend3View.as_view()),
	url(r'', include(router.urls)),
	
]