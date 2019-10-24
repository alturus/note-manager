from django.contrib import admin

from api.filters import RelatedDropdownFilter, DropdownFilter
from api.notes.models import Note


class NoteAdmin(admin.ModelAdmin):
    list_display = (
        'uuid',
        'title',
        'created',
        'is_favorited',
        'is_published',
        'owner',
    )

    list_filter = (
        ('category', RelatedDropdownFilter),
        ('owner', RelatedDropdownFilter),
        ('is_favorited', DropdownFilter),
        ('is_published', DropdownFilter),
    )


admin.site.register(Note, NoteAdmin)
