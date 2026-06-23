from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import *

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'hypotheses', HypothesisViewSet)
router.register(r'actions', ActionViewSet)
router.register(r'data', DataViewSet)
router.register(r'insights', InsightViewSet)
router.register(r'assistant-functions', AssistantFunctionViewSet)
router.register(r'requests-to-assistant', RequestToAssistantViewSet)
router.register(r'chats-with-assistant', ChatWithAssistantViewSet)
router.register(r'openai-history', OpenAIHistoryViewSet)
router.register(r'teams', TeamViewSet)
router.register(r'project-memberships', ProjectMembershipViewSet)
router.register(r'team-memberships', TeamMembershipViewSet)
router.register(r'curators', CuratorViewSet)
router.register(r'hypothesis-statuses', HypothesisStatusViewSet)
router.register(r'hypothesis-metrics', HypothesisMetricViewSet)
router.register(r'hypothesis-metric-values', HypothesisMetricValuesViewSet)
router.register(r'hypothesis-content-versions', HypothesisContentVersionViewSet)
router.register(r'action-content-versions', ActionContentVersionViewSet)
router.register(r'data-content-versions', DataContentVersionViewSet)
router.register(r'insight-content-versions', InsightContentVersionViewSet)
router.register(r'user-actions', UserActionsViewSet)
router.register(r'global-properties', GlobalPropertiesViewSet)
router.register(r'project-changes-summaries', ProjectChangesSummaryViewSet)
router.register(r'hypothesis-changes-summaries', HypothesisChangesSummaryViewSet)
router.register(r'action-changes', ActionChangesViewSet)
router.register(r'data-changes', DataChangesViewSet)
router.register(r'insight-changes', InsightChangesViewSet)
router.register(r'metric-changes', MetricChangesViewSet)
router.register(r'user-settings', UserSettingsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
