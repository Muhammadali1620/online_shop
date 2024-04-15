from django.contrib import admin
from apps.users.models import CustomUser

@admin.register(CustomUser) 
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'phone_number')
    readonly_fields = ('created_at',)
    list_display_linsk = ('email', 'first_name', 'last_name', 'phone_number')
    search_fields = ['email', 'first_name', 'last_name', 'phone_number']
    search_help_text = f'Serch from fields({search_fields})'

    def save_model(self, request, obj, form, change):
        if obj.password != form.inital.get('password'):
            obj.set_password(obj.password)
        obj.save()
