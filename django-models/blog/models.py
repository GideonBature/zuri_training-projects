from datetime import datetime
from distutils.text_file import TextFile
from lib2to3.refactor import get_all_fix_names
from typing import Text
from django.db import models
from django.contrib.auth import get_user_model
import mmap

# Create your models here.
class Post(models.Model):
    Title: models.CharField(max_length=200)
    Text: models.TextField(max_length=500)
    Author: models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    Created_date: models.DateTimeField(default=datetime.today)
    Published_date: models.DateTimeField(default=datetime.today)