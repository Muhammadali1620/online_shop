from django.contrib import admin
from apps.contacts.models import Contact

 
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('email', 'title', 'message')
    readonly_fields = ('created_at',)

    list_display_linsk = ('email', 'title', 'message')
    search_fields = ('email', 'title', 'message')
    search_help_text = f'Serch from fields({search_fields})'