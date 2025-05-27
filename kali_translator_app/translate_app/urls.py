from django.urls import path
from . import views
from .views import translate_view

urlpatterns = [
    path('', translate_view, name='home'),
]
