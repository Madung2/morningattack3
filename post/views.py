from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions, status
from .models import (   JobPostSkillSet,JobType,JobPost,Company)
from django.db.models.query_utils import Q
from .serializers import JobPostSerializer


class SkillView(APIView):

    permission_classes = [permissions.AllowAny]

    def get(self, request):
        skills = self.request.query_params.getlist('skills', '')
        print("skills = ", end=""), print(skills)

        return Response(status=status.HTTP_200_OK)


class JobView(APIView):
    def get(self, request):
        job_post = JobPost.objects.all()
        jobpost_serializer = JobPostSerializer(job_post, many=True)
        return Response(jobpost_serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        # job_type = int( request.data.get("job_type", None) )
        # company_name = request.data.get("company_name", None)
        jobpost_serializer = JobPostSerializer(data=request.data)

        if jobpost_serializer.is_valid():
            jobpost_serializer.save()
            return Response(jobpost_serializer.data, status=status.HTTP_200_OK)

