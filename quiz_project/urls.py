from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('super-admin/', admin.site.urls),
    path('quiz/', include('quiz.urls')),
]
