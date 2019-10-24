from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView

from api.users.views import UserTokenObtainPairView, UserTokenRefreshView
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/users/token/', UserTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/users/token/refresh/', UserTokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/users/', include('api.users.urls')),
    path('api/v1/categories/', include('api.categories.urls')),
    path('api/v1/notes/', include('api.notes.urls')),
    path('templates/<slug:item>.html', views.AngularTemplateView.as_view()),
    path('note/<uuid:uuid>', views.NoteView.as_view(), name='note-view'),
]

urlpatterns += [
    re_path(r'', TemplateView.as_view(template_name='index.html'))
]
