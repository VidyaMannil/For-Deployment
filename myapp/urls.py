
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', admin.site.urls),
    path('Welcome',views.MyWelcome,name='Welcome'),
]
