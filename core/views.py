import os

from django.conf import settings
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.views import View

from api.notes.models import Note


class NoteView(View):
    def get(self, request, uuid):
        note = get_object_or_404(Note, pk=uuid, is_published=True)
        context = {
            'note': note,
        }
        return render(request, 'note.html', context=context)


class AngularTemplateView(View):
    def get(self, request, item=None, *args, **kwargs):
        template_dir_path = settings.TEMPLATES[0]['DIRS'][0]
        final_path = os.path.join(template_dir_path, item + '.html')
        try:
            html = open(final_path)
            return HttpResponse(html)
        except:
            raise Http404
