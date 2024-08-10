from django.urls import path
from . import views
from .views import blog_list
from .views import contact_view, success_view


urlpatterns = [
    path('', views.home, name='home'),
    path('vr/', views.vr, name='vr'),
    path('development/', views.underdevelopment, name='development'),
    path('ecot/', views.eco_t, name='eco_t'),
    path('topten/', views.topten, name='topten'),
    path('blog/', blog_list, name='blog_list'),
    path('contact/', contact_view, name='contact'),
    path('success/', success_view, name='success'),
    
]
