from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from GisKend.views import EventoViewset

router = DefaultRouter()
router.register(r'GisKend', EventoViewset)

urlpatterns = router.urls

urlpatterns += [
    path('admin/', admin.site.urls),
]
