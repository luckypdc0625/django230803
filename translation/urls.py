from django.urls import path

from .views import base_views

app_name = 'translation'

urlpatterns = [
    path('translation/', base_views.index, name='translation_index'),
]