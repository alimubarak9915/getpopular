from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('user.urls', namespace='user')),
    path('', include('smm.urls', namespace='smm')),
]

admin.site.site_header = "GET POPULAR.COM"
admin.site.site_title = "GET POPULAR"
admin.site.index_title = "WELCOME TO GET POPULAR"
