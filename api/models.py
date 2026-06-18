from django.db import models
from django.contrib.auth.models import User

# Create your models here.
        
class Project(models.Model):
    title = models.CharField(max_length = 64)
    description = models.CharField(max_length = 512, default='')
    content = models.TextField(default = '')
    deleted = models.BooleanField(default = False)

    def __str__(self):
        return f'{self.title}'

class Hypothesis(models.Model):

    short_name = models.CharField(max_length = 128, verbose_name = 'Название')
    project = models.ForeignKey('Project', on_delete = models.CASCADE, verbose_name='Проект')
    content = models.TextField(default = '', verbose_name='Формулировка гипотезы')
    deleted = models.BooleanField(default = False, verbose_name='Удалена?')
    linked_to = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, default = None, verbose_name = 'Связана с')

    def __str__(self):
        return f'{self.short_name} ({self.project.title})'

class Action(models.Model):
    hypothesis = models.ForeignKey('Hypothesis', on_delete = models.CASCADE)
    content = models.TextField(default = '')
    deleted = models.BooleanField(default = False)
    def __str__(self):
        return f'{self.content[:16]} ({self.hypothesis.short_name})'
    
class Data(models.Model):
    hypothesis = models.ForeignKey('Hypothesis', on_delete = models.CASCADE)
    content = models.TextField(default = '')
    deleted = models.BooleanField(default = False)
    def __str__(self):
        return f'{self.content[:16]} ({self.hypothesis.short_name})'

class Insight(models.Model):
    hypothesis = models.ForeignKey('Hypothesis', on_delete = models.CASCADE)
    content = models.TextField(default = '')
    deleted = models.BooleanField(default = False)
    def __str__(self):
        return f'{self.content[:16]} ({self.hypothesis.short_name})'

class AssistantFunction(models.Model):
    name = models.CharField(max_length = 32)
    user_prompt = models.TextField(default = '')
    system_prompt = models.TextField()
    send_context = models.BooleanField(default = True)
    send_to_llm_instantly = models.BooleanField(default = True)
    description = models.CharField(max_length = 128, blank = True, null = True)
    author = models.ForeignKey(User, on_delete = models.CASCADE, null = True, blank = True)
    is_public = models.BooleanField(default = False)
    deleted = models.BooleanField(default = False)
    last_updated = models.DateTimeField(null = True, blank = True)
    send_project_info = models.BooleanField(default = False)
    def __str__(self):
        return self.name

class RequestToAssistant(models.Model):
    MESSAGE_TYPES = [
        ('context', 'Контекст'),
        ('instruction', 'Инструкция'),
        ('user', 'Сообщение пользователя'),
        ('devprompt', 'Сообщение с форматом ответа')
    ]
    chat = models.ForeignKey("ChatWithAssistant", on_delete = models.CASCADE)
    role = models.CharField(max_length = 16)
    message = models.TextField()
    recieved_at = models.DateTimeField()
    message_type = models.CharField(max_length = 12, choices = MESSAGE_TYPES, null = True, blank = True)
    def __str__(self):
        return f'{self.chat.chat_name} ({self.role}): {self.message[:30]}'

class ChatWithAssistant(models.Model):
    chat_name = models.CharField(max_length = 32, default = 'Новый чат')
    function = models.ForeignKey("AssistantFunction", on_delete = models.CASCADE, null = True, blank = True)
    hypothesis = models.ForeignKey('Hypothesis', on_delete = models.CASCADE)
    context_length = models.IntegerField(default = 0)
    closed = models.BooleanField(default = False)
    created_at = models.DateTimeField(null = True, blank = True)
    def __str__(self):
        return self.chat_name

class OpenAIHistory(models.Model):
    recieved_at = models.DateTimeField()
    input = models.TextField()
    result = models.TextField(null = True, blank = True)

#Пользователи
class Team(models.Model):
    name = models.CharField(max_length = 64)
    description = models.TextField()
    
    def __str__(self):
        return self.name

class ProjectMembership(models.Model):
    ROLE_CHOICES = [
        ('viewer', 'Viewer'),
        ('editor', 'Editor'),
        ('owner', 'Owner')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="project_memberships")
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="memberships")
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.user.username} - {self.project.title} ({self.get_role_display()})"
    
class TeamMembership(models.Model):
    ROLE_CHOICES = [
        ('manager', 'Manager'),
        ('supervisor', 'Supervisor'),
        ('inactive', 'Inactive')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="team_memberships")
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="memberships")
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.user.username} - {self.team.name} ({self.get_role_display()})"
    
class Curator(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="curator")

    def __str__(self):
        return str(self.user)
    

class HypothesisStatus(models.Model):
    STATUS_CHOICES = [
        ('changed', 'Изменена'),
        ('declined', 'Отклонена'),
        ('accepted', 'Принята'),
        ('inprogress', 'В работе'),
        ('deffered', 'Отложена'),
    ]

    hypothesis = models.ForeignKey('Hypothesis', on_delete = models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    changing_time = models.DateTimeField()
    changing_to = models.ForeignKey('Hypothesis', on_delete = models.CASCADE, blank = True, null = True, related_name = 'new_hypothesis')
    deffered_to = models.DateTimeField(default = None, blank = True, null = True)
    comment = models.TextField(blank = True, null = True, default = '')
    author = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True)

class HypothesisMetric(models.Model):
    TYPE_CHOICES = [
        ('boolean', 'Чекбокс'),
        ('integer', 'Целое число'),
        ('float', 'Дробное число'),
    ]

    name = models.CharField(max_length=64)
    hypothesis = models.ForeignKey('Hypothesis', on_delete = models.CASCADE)
    metric_type = models.CharField(max_length = 7, choices = TYPE_CHOICES)
    deleted = models.BooleanField(default = False)
    target_value = models.FloatField(default = 0)
    description = models.CharField(max_length = 128, default = '')

    def __str__(self):
        return str(self.hypothesis) + '-' + str(self.metric_type)

class HypothesisMetricValues(models.Model):
    metric = models.ForeignKey('HypothesisMetric', on_delete = models.CASCADE)
    value = models.FloatField(default = 0)
    updated_at = models.DateTimeField()
    deleted = models.BooleanField(default = False)

    def __str__(self):
        return str(self.metric) + '-' + str(self.value)
    
class HypothesisContentVersion(models.Model):
    object = models.ForeignKey('Hypothesis', on_delete = models.CASCADE)
    content = models.TextField()
    updated = models.DateTimeField()

class ActionContentVersion(models.Model):
    object = models.ForeignKey('Action', on_delete = models.CASCADE)
    content = models.TextField()
    updated = models.DateTimeField()

class DataContentVersion(models.Model):
    object = models.ForeignKey('Data', on_delete = models.CASCADE)
    content = models.TextField()
    updated = models.DateTimeField()

class InsightContentVersion(models.Model):
    object = models.ForeignKey('Insight', on_delete = models.CASCADE)
    content = models.TextField()
    updated = models.DateTimeField()

class UserActions(models.Model):
    ACTION_TYPE_CHOICES = [
        ('create', 'Создание'),
        ('delete', 'Удаление'),
        ('update', 'Изменение'),
    ]

    user = models.ForeignKey(User, on_delete = models.CASCADE)
    updated = models.DateTimeField()
    project = models.ForeignKey('Project', on_delete = models.CASCADE, null = True, blank = True)
    hypothesis = models.ForeignKey('Hypothesis', on_delete = models.CASCADE, null = True, blank = True)
    metric = models.ForeignKey('HypothesisMetric', on_delete = models.CASCADE, null = True, blank = True)
    action_type = models.CharField(max_length=20, choices = ACTION_TYPE_CHOICES)

class GlobalProperties(models.Model):
    PROPERTY_TYPES = [
        ('format_prompt', 'Строка формата (text)'),
        ('max_context_size', 'Максимальная величина контекста (int)'),
        ('gpt_type', 'Тип использующейся модели GPT'),
        ('openai_key', 'API ключ OpenAI'),
        ('yandex_catalog_id', 'ID каталога Yandex Cloud'),
        ('yandex_api_key', 'API ключ Yandex Cloud'),
    ]

    property_type = models.CharField(max_length = 30, choices = PROPERTY_TYPES)
    property_value_text = models.TextField(null = True, blank = True)
    property_value_int = models.IntegerField(null = True, blank = True)
    property_value_bool = models.IntegerField(default = False)
    updated_at = models.DateTimeField()


class ProjectChangesSummary(models.Model):
    STATUSES = [
        ('inprogress', 'Формируется'),
        ('ready', 'Сформирован')
    ]
    status = models.CharField(max_length = 12, choices=STATUSES)
    date_from = models.DateField()
    date_to = models.DateField()
    project = models.ForeignKey('Project', on_delete = models.CASCADE)
    summary_date = models.DateTimeField()
    use_general_summary = models.BooleanField(default = False)
    use_content_summary = models.BooleanField(default = False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    changes = models.IntegerField(default = 0)

class HypothesisChangesSummary(models.Model):
    STATUSES = [
        ('inprogress', 'Формируется'),
        ('ready', 'Сформирован')
    ]

    status = models.CharField(max_length = 12, choices=STATUSES)
    date_from = models.DateField()
    date_to = models.DateField()
    hypothesis = models.ForeignKey('Hypothesis', on_delete=models.CASCADE)
    summary_date = models.DateTimeField()
    use_general_summary = models.BooleanField(default = False)
    use_content_summary = models.BooleanField(default = False)
    hypothesis_content_before = models.TextField(null = True, blank = True)
    hypothesis_content_after = models.TextField(null = True, blank = True)
    summary_hypothesis = models.TextField(null = True, blank = True)
    summary_actions = models.TextField(null = True, blank = True)
    summary_data = models.TextField(null = True, blank = True)
    summary_insights = models.TextField(null = True, blank = True)
    summary_metrics = models.TextField(null = True, blank = True)
    summary_general = models.TextField(null = True, blank = True)
    points_hypothesis = models.IntegerField(null = True, blank = True, default = 0)
    points_actions = models.IntegerField(null = True, blank = True, default = 0)
    points_data = models.IntegerField(null = True, blank = True, default = 0)
    points_insights = models.IntegerField(null = True, blank = True, default = 0)
    points_metrics = models.IntegerField(null = True, blank = True, default = 0)
    points_general = models.IntegerField(null = True, blank = True, default = 0)
    changes = models.IntegerField(default = 0)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    is_subordinate = models.BooleanField(default = False)
    subordinate_of = models.ForeignKey('ProjectChangesSummary', on_delete = models.CASCADE, null = True, blank = True)

class ActionChanges(models.Model):
    summary = models.ForeignKey('HypothesisChangesSummary', on_delete=models.CASCADE)
    action = models.ForeignKey('Action', on_delete=models.CASCADE)
    content_before = models.TextField(null = True, blank = True)
    content_after = models.TextField(null = True, blank = True)

class DataChanges(models.Model):
    summary = models.ForeignKey('HypothesisChangesSummary', on_delete=models.CASCADE)
    data = models.ForeignKey('Data', on_delete=models.CASCADE)
    content_before = models.TextField(null = True, blank = True)
    content_after = models.TextField(null = True, blank = True)

class InsightChanges(models.Model):
    summary = models.ForeignKey('HypothesisChangesSummary', on_delete=models.CASCADE)
    insight = models.ForeignKey('Insight', on_delete=models.CASCADE)
    content_before = models.TextField(null = True, blank = True)
    content_after = models.TextField(null = True, blank = True)

class MetricChanges(models.Model):
    summary = models.ForeignKey('HypothesisChangesSummary', on_delete=models.CASCADE)
    metric = models.ForeignKey('HypothesisMetric', on_delete=models.CASCADE)
    value_before = models.FloatField(null = True, blank = True)
    value_after = models.FloatField(null = True, blank = True)

class UserSettings(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, help_text="Пользователь, к которому относится настройка.")
    setting = models.CharField(max_length=32, help_text="Название настройки.")
    value = models.CharField(max_length=32, help_text="Значение настройки.")

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'setting'], name='unique_user_setting')
        ]
        verbose_name = "Настройка пользователя"
        verbose_name_plural = "Настройки пользователей"

    def __str__(self):
        return f"{self.user.username} — {self.setting} = {self.value}"