from django.contrib import admin
from Posts.models import Post, Comment
# Register your models here.

class CommentAdminInline(admin.TabularInline):
    model=Comment
    fields = ['text']
    extra=0
 


class PostAdmin(admin.ModelAdmin):
    list_display =['id','title',]
    inlines = [CommentAdminInline,]


# class CommentAdmin(admin.ModelAdmin):
#     list_display = [ 'post', 'text']

# admin.site.register(Comment,CommentAdmin)
admin.site.register(Post, PostAdmin)


