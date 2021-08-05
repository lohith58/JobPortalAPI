from rest_framework.serializers import ModelSerializer
from jobs.models import blorejobs
class BloreJobsSerializer(ModelSerializer):
    class Meta:
        model=blorejobs
        fields='__all__'
