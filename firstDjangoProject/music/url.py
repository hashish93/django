from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('<int:album_id>', views.detail, name='details'),
]
