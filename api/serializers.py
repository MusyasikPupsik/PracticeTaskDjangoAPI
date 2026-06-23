from rest_framework import serializers
from django.contrib.auth.models import User
from .models import (
    Project, Hypothesis, Action, Data, Insight, AssistantFunction,
    RequestToAssistant, ChatWithAssistant, OpenAIHistory, Team,
    ProjectMembership, TeamMembership, Curator, HypothesisStatus,
    HypothesisMetric, HypothesisMetricValues, HypothesisContentVersion,
    ActionContentVersion, DataContentVersion, InsightContentVersion,
    UserActions, GlobalProperties, ProjectChangesSummary,
    HypothesisChangesSummary, ActionChanges, DataChanges,
    InsightChanges, MetricChanges, UserSettings
)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class HypothesisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hypothesis
        fields = '__all__'

class ActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Action
        fields = '__all__'

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = '__all__'

class InsightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insight
        fields = '__all__'

class AssistantFunctionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssistantFunction
        fields = '__all__'

class RequestToAssistantSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestToAssistant
        fields = '__all__'

class ChatWithAssistantSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatWithAssistant
        fields = '__all__'

class OpenAIHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = OpenAIHistory
        fields = '__all__'

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'

class ProjectMembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectMembership
        fields = '__all__'

class TeamMembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMembership
        fields = '__all__'

class CuratorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curator
        fields = '__all__'

class HypothesisStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = HypothesisStatus
        fields = '__all__'

class HypothesisMetricSerializer(serializers.ModelSerializer):
    class Meta:
        model = HypothesisMetric
        fields = '__all__'

class HypothesisMetricValuesSerializer(serializers.ModelSerializer):
    class Meta:
        model = HypothesisMetricValues
        fields = '__all__'

class HypothesisContentVersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = HypothesisContentVersion
        fields = '__all__'

class ActionContentVersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActionContentVersion
        fields = '__all__'

class DataContentVersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataContentVersion
        fields = '__all__'

class InsightContentVersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = InsightContentVersion
        fields = '__all__'

class UserActionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserActions
        fields = '__all__'

class GlobalPropertiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = GlobalProperties
        fields = '__all__'

class ProjectChangesSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectChangesSummary
        fields = '__all__'

class HypothesisChangesSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = HypothesisChangesSummary
        fields = '__all__'

class ActionChangesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActionChanges
        fields = '__all__'

class DataChangesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataChanges
        fields = '__all__'

class InsightChangesSerializer(serializers.ModelSerializer):
    class Meta:
        model = InsightChanges
        fields = '__all__'

class MetricChangesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetricChanges
        fields = '__all__'

class UserSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSettings
        fields = '__all__'
