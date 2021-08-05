from rest_framework import viewsets
from jobs.models import blorejobs
from jobs.api.serializers import BloreJobsSerializer
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated
class BloreJobsCRUDCBV(viewsets.ModelViewSet):
    serializer_class=BloreJobsSerializer
    queryset=blorejobs.objects.all()
    authentication_classes=[JSONWebTokenAuthentication,]
    permission_classes=[IsAuthenticated,]
