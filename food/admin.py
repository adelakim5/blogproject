from django.contrib import admin
from .models import Food
from .models import Comment

# Register your models here.
admin.site.register(Food)
admin.site.register(Comment)