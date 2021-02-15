from django.urls import path
from . import views


app_name = 'dash'
urlpatterns = [
    path("dash/",views.index, name="dash"),
    
]
