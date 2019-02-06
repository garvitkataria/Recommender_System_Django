from django.conf.urls import url,include
from . import views
from rest_framework import routers
from .views import RecommendView

router = routers.DefaultRouter()
router.register('', views.ratingView)

urlpatterns = [

	url(r'^recommend/$', RecommendView.as_view()),
	url(r'', include(router.urls)),
	
]