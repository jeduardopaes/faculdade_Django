
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^cliente/', include('cliente.urls')),
    url(r'^admin/', admin.site.urls),
]
