from django.contrib import admin
from .models import Cat

# Register your models here.
@admin.register(Cat)
class CatAdminView(admin.ModelAdmin):

    model = Cat

    list_display = (
        'breed',
        'origin',
        'intro',
    )

    list_filter = (
        'breed',
        'body_type',
        'coat_type_and_length',
        'coat_pattern',
    )

    search_fields = (
        'breed',
        'origin',
        'occurrence',
        'body_type',
        'coat_type_and_length',
        'coat_pattern',
    )