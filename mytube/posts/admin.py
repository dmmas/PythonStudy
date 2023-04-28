from django.contrib import admin

# Register your models here.
# из файла models импортируем модель Post
from .models import Post

admin.site.register(Post)