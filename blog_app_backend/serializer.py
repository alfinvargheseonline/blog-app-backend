from rest_framework import serializers
from blog_app_backend.models import SignupModel,PostModel

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model=SignupModel
        fields=(
            'name',
            'image',
            'email',
            'password'
        )

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=PostModel
        fields=(
            'userid',
            'title',
            'message'
            
        )