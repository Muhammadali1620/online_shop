from django.contrib import admin
from apps.comments.models import Comment

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('product', 'email', 'rating', 'created_at')
    readonly_fields = ('created_at','updated_at',) 

    list_display_linsk = ('product', 'email', 'rating', 'created_at')
    list_filter = ['rating']
    search_fields = ['product', 'email', 'rating', 'created_at']
    search_help_text = f'Serch from fields({search_fields})'
