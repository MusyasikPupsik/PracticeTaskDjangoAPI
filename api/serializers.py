from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Project, Hypothesis, Team

# Serializer for Users
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

# Serializer for Projects
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'content', 'deleted']

# Serializer for Hypotheses
class HypothesisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hypothesis
        fields = ['id', 'short_name', 'project', 'content', 'deleted', 'linked_to']

# Serializer for Teams
class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['id', 'name', 'description']
