from django.contrib import admin
from django.db.models import Count

from api.categories.models import Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'total_notes')

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(
            total_notes=Count('notes', distinct=True),
        )
        return queryset

    def total_notes(self, obj):
        return obj.total_notes
    total_notes.admin_order_field = 'total_notes'


admin.site.register(Category, CategoryAdmin)
