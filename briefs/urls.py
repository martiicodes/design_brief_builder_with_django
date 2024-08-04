from django.urls import path
from . import views

app_name = 'briefs'

urlpatterns = [
    path('create/', views.create_brief, name='create_brief'),
    path('success/', views.success, name='success'),
]