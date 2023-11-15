from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('identifier',)}

#admin.site.register(Post)
#admin.site.register(Comment)
