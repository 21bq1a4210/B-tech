# myapp/urls.py
from django.urls import path
from .views import image_upload, image_list

urlpatterns = [
    path('upload/', image_upload, name='image_upload'),
    path('list/', image_list, name='image_list'),
]

# myproject/urls.py
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
