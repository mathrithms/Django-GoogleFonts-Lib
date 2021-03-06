from django.contrib import admin
from .models import font
# Register your models here.
@admin.register(font)

class fontName(admin.ModelAdmin):
	list_display = ["category", "kind", "family", "version", "lastModified"]
