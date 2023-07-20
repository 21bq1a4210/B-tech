from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls import include


urlpatterns =[
    path('hello/',views.say_hello),
    path('hello/next/',views.upload_file,name='next'),
]
if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path(r'^__debug__/', include(debug_toolbar.urls)),
    ]