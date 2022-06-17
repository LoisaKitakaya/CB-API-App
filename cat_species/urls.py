from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cats.urls')),
]

admin.site.site_header = 'Cat Breeds API App Admin Panel'
admin.site.site_title = 'Cat Breeds API App Backend'