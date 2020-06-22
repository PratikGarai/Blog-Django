from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('MainApp.urls'), name = "MainApp"),
    path('blog/', include('BlogApp.urls'), name = "BlogApp"),
]
