from django.contrib import admin
from .models import Teams
from markdownx.admin import MarkdownxModelAdmin

# Register your models here.
@admin.register(Teams)
class TeamsAdmin(MarkdownxModelAdmin):
    fields = ('teamname', 'email', 'points')
    list_display = ('teamname', 'email', 'points')

