from django.contrib import admin
from django.urls import path
from GisKend.views import crear_evento,  get_evento
from django.views.generic import RedirectView

app_name = 'evento'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/eventos/<id>/', get_evento, name="get"),
    path('v1/eventos/', crear_evento, name="post"),
    path('', RedirectView.as_view(url='v1/eventos/', permanent=True)),
]
