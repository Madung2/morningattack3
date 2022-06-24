from rest_framework import serializers
from .models import Company as CompanyModel
from .models import BusinessArea
from .models import JobPost as JobPostModel
from .models import JobType
from .models import SkillSet
from .models import JobPostSkillSet

class BusinessAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessArea
        fields = ['area', ]


class CompanySerializer(serializers.ModelSerializer):
    business_area = BusinessAreaSerializer(many=True, source="review_set", read_only=True)

    class Meta:
        model = CompanyModel
        fields = ['company_name', 'business_area', ]

class JobTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobType
        fields = ['job_type', ]
        
        
class JobPostSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = JobPostModel
        fields = ['job_type', 'company', 'job_description', 'salary', 'created_at', ]



class SkillSetSerializer(serializers.ModelSerializer):
    job_posts = JobPostSerializer(many=True, source="review_set", read_only=True)
    
    class Meta:
        model = SkillSet
        fields = ['name', 'job_posts']
        

        