from django.contrib import admin
from .models import CustomUser
# Register your models here.

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if form.cleaned_data.get("password"):
            obj.set_password(form.cleaned_data["password"])
        return super().save_model(request, obj, form, change)