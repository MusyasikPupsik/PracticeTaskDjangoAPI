from rest_framework import permissions
from .models import ProjectMembership, TeamMembership, Curator, Hypothesis

class IsProjectMemberOrCurator(permissions.BasePermission):
    """
    Custom permission to restrict project access based on ProjectMembership roles and Curators.
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        user = request.user
        
        if Curator.objects.filter(user=user).exists():
            return True
        project = obj if hasattr(obj, 'title') and not hasattr(obj, 'project') else getattr(obj, 'project', None)
        
        if not project:
            return False
        membership = ProjectMembership.objects.filter(user=user, project=project).first()
        if not membership:
            return False

        if request.method in permissions.SAFE_METHODS:  # GET, HEAD, OPTIONS
            return membership.role in ['viewer', 'editor', 'owner']
        
        return membership.role in ['editor', 'owner']


class IsTeamMemberOrCurator(permissions.BasePermission):
    """
    Custom permission to restrict data access based on TeamMembership roles.
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        user = request.user
        
        if Curator.objects.filter(user=user).exists():
            return True

        team = getattr(obj, 'team', None)
        if not team:
            return True 

        membership = TeamMembership.objects.filter(user=user, team=team).first()
        if not membership:
            return False

        if request.method in permissions.SAFE_METHODS:
            return membership.role in ['manager', 'supervisor', 'inactive']
            
        return membership.role in ['manager', 'supervisor']
