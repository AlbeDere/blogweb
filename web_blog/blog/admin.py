from django.contrib import admin
from blog.models import BlogPost, Comment, Category


class CategoryAdmin(admin.ModelAdmin):
    pass

class BlogPostAdmin(admin.ModelAdmin):
    pass

class CommentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Category, CategoryAdmin)
admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Comment, CommentAdmin)
