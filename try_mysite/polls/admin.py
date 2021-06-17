from django.contrib import admin
from django.db import models
from django.db.models import fields
from .models import Question

# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    fields=['pub_date','question_test']


admin.site.register(Question,QuestionAdmin)



