from django.contrib import admin
from app.models import *
# Register your models here.


admin.site.register(BlogPostComment)


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    class Media:
        js= ('js/admin_blog.js',)

    
admin.site.register(New)