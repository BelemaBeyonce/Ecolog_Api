from django.contrib import admin
from .models import Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):  
    list_display = ('name', 'description')
    search_fields = ('name',)
    list_filter = ('name',)



# Register your models here.
