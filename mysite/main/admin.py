from django.contrib import admin
from.models import Tutorial
from tinymce.widgets import TinyMCE
from django.db import models

class TutorialAdmin(admin.ModelAdmin):

    fieldsets=[
        ("Title/date",{"fields":["tutorial_title","tutorial_pulished"]}),
        ("Content",{"fields":["tutorial_content"]})
    ]
    formfield_overrides= {
            models.TextField:{'widget':TinyMCE()}
        }

admin.site.register(Tutorial,TutorialAdmin)

# Register your models here.
'''
class Tutorial(admin.ModelAdmin):
    fields=[
        "tutorial_title",
        "tutorial_pulished",
        "tutorial_content"
    ]
'''