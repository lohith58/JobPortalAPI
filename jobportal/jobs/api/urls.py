from django.urls import path,include
from rest_framework import routers
from jobs.api.views import BloreJobsCRUDCBV
router=routers.DefaultRouter()
router.register('blorejobsinfo',BloreJobsCRUDCBV)
urlpatterns = [
  path('', include(router.urls)),
]
