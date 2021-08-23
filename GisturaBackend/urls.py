from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from GisKend.views import ChelaViewset

router = DefaultRouter()
router.register(r'GisKend', ChelaViewset)

urlpatterns = router.urls

urlpatterns += [
    path('admin/', admin.site.urls),
]
