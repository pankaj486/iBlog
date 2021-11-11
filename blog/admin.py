from django.contrib import admin
from .models import Post, Category, PostComment


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'url',)
    search_fields = ('title',)
    list_filter = ('cat',)

    class Media:
        js = ('https://cdn.tiny.cloud/1/no-api-key/tinymce/5/tinymce.min.js', 'js/script.js',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('image_tag', 'title', 'add_date', 'url',)
    search_fields = ('title',)


class PostCommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'posted_at', 'user')


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(PostComment, PostCommentAdmin)
