from rest_framework import viewsets, permissions
from django.contrib.auth.models import User
from .models import *
from .serializers import *
from .permissions import IsProjectMemberOrCurator, IsTeamMemberOrCurator

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser] 

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsProjectMemberOrCurator]

class HypothesisViewSet(viewsets.ModelViewSet):
    queryset = Hypothesis.objects.all()
    serializer_class = HypothesisSerializer
    permission_classes = [IsProjectMemberOrCurator]

class ActionViewSet(viewsets.ModelViewSet):
    queryset = Action.objects.all()
    serializer_class = ActionSerializer
    permission_classes = [IsProjectMemberOrCurator]

class DataViewSet(viewsets.ModelViewSet):
    queryset = Data.objects.all()
    serializer_class = DataSerializer
    permission_classes = [IsProjectMemberOrCurator]

class InsightViewSet(viewsets.ModelViewSet):
    queryset = Insight.objects.all()
    serializer_class = InsightSerializer
    permission_classes = [IsProjectMemberOrCurator]

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [IsTeamMemberOrCurator]

class ProjectMembershipViewSet(viewsets.ModelViewSet):
    queryset = ProjectMembership.objects.all()
    serializer_class = ProjectMembershipSerializer
    permission_classes = [permissions.IsAuthenticated]

class TeamMembershipViewSet(viewsets.ModelViewSet):
    queryset = TeamMembership.objects.all()
    serializer_class = TeamMembershipSerializer
    permission_classes = [permissions.IsAuthenticated]

class CuratorViewSet(viewsets.ModelViewSet):
    queryset = Curator.objects.all()
    serializer_class = CuratorSerializer
    permission_classes = [permissions.IsAdminUser]

class AssistantFunctionViewSet(viewsets.ModelViewSet):
    queryset = AssistantFunction.objects.all()
    serializer_class = AssistantFunctionSerializer
    permission_classes = [permissions.IsAuthenticated]

class RequestToAssistantViewSet(viewsets.ModelViewSet):
    queryset = RequestToAssistant.objects.all()
    serializer_class = RequestToAssistantSerializer
    permission_classes = [permissions.IsAuthenticated]

class ChatWithAssistantViewSet(viewsets.ModelViewSet):
    queryset = ChatWithAssistant.objects.all()
    serializer_class = ChatWithAssistantSerializer
    permission_classes = [permissions.IsAuthenticated]

class OpenAIHistoryViewSet(viewsets.ModelViewSet):
    queryset = OpenAIHistory.objects.all()
    serializer_class = OpenAIHistorySerializer
    permission_classes = [permissions.IsAuthenticated]

class HypothesisStatusViewSet(viewsets.ModelViewSet):
    queryset = HypothesisStatus.objects.all()
    serializer_class = HypothesisStatusSerializer
    permission_classes = [permissions.IsAuthenticated]

class HypothesisMetricViewSet(viewsets.ModelViewSet):
    queryset = HypothesisMetric.objects.all()
    serializer_class = HypothesisMetricSerializer
    permission_classes = [permissions.IsAuthenticated]

class HypothesisMetricValuesViewSet(viewsets.ModelViewSet):
    queryset = HypothesisMetricValues.objects.all()
    serializer_class = HypothesisMetricValuesSerializer
    permission_classes = [permissions.IsAuthenticated]

class HypothesisContentVersionViewSet(viewsets.ModelViewSet):
    queryset = HypothesisContentVersion.objects.all()
    serializer_class = HypothesisContentVersionSerializer
    permission_classes = [permissions.IsAuthenticated]

class ActionContentVersionViewSet(viewsets.ModelViewSet):
    queryset = ActionContentVersion.objects.all()
    serializer_class = ActionContentVersionSerializer
    permission_classes = [permissions.IsAuthenticated]

class DataContentVersionViewSet(viewsets.ModelViewSet):
    queryset = DataContentVersion.objects.all()
    serializer_class = DataContentVersionSerializer
    permission_classes = [permissions.IsAuthenticated]

class InsightContentVersionViewSet(viewsets.ModelViewSet):
    queryset = InsightContentVersion.objects.all()
    serializer_class = InsightContentVersionSerializer
    permission_classes = [permissions.IsAuthenticated]

class UserActionsViewSet(viewsets.ModelViewSet):
    queryset = UserActions.objects.all()
    serializer_class = UserActionsSerializer
    permission_classes = [permissions.IsAuthenticated]

class GlobalPropertiesViewSet(viewsets.ModelViewSet):
    queryset = GlobalProperties.objects.all()
    serializer_class = GlobalPropertiesSerializer
    permission_classes = [permissions.IsAuthenticated]

class ProjectChangesSummaryViewSet(viewsets.ModelViewSet):
    queryset = ProjectChangesSummary.objects.all()
    serializer_class = ProjectChangesSummarySerializer
    permission_classes = [permissions.IsAuthenticated]

class HypothesisChangesSummaryViewSet(viewsets.ModelViewSet):
    queryset = HypothesisChangesSummary.objects.all()
    serializer_class = HypothesisChangesSummarySerializer
    permission_classes = [permissions.IsAuthenticated]

class ActionChangesViewSet(viewsets.ModelViewSet):
    queryset = ActionChanges.objects.all()
    serializer_class = ActionChangesSerializer
    permission_classes = [permissions.IsAuthenticated]

class DataChangesViewSet(viewsets.ModelViewSet):
    queryset = DataChanges.objects.all()
    serializer_class = DataChangesSerializer
    permission_classes = [permissions.IsAuthenticated]

class InsightChangesViewSet(viewsets.ModelViewSet):
    queryset = InsightChanges.objects.all()
    serializer_class = InsightChangesSerializer
    permission_classes = [permissions.IsAuthenticated]

class MetricChangesViewSet(viewsets.ModelViewSet):
    queryset = MetricChanges.objects.all()
    serializer_class = MetricChangesSerializer
    permission_classes = [permissions.IsAuthenticated]

class UserSettingsViewSet(viewsets.ModelViewSet):
    queryset = UserSettings.objects.all()
    serializer_class = UserSettingsSerializer
    permission_classes = [permissions.IsAuthenticated]
