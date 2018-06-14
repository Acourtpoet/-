from django.contrib import admin
from .models import Post, Works, Tags, Enjoy

# Register your models here.
admin.site.register(Post)
admin.site.register(Works)
admin.site.register(Tags)
admin.site.register(Enjoy)