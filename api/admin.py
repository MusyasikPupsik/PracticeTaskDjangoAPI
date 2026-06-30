from django.contrib import admin
from .models import Project, ProjectMembership, Team, TeamMembership, Curator, Hypothesis

admin.site.register(Project)
admin.site.register(ProjectMembership)
admin.site.register(Team)
admin.site.register(TeamMembership)
admin.site.register(Curator)
admin.site.register(Hypothesis)
