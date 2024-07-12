from django.contrib import admin
from .models import Post, Comment, Category

# Remove this line:
# admin.site.register(User)
list_display = ("name",)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Category)
