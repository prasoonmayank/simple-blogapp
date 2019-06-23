
from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('post/<int:id>/', views.post, name='post'),
    path('add_article/', views.add_article, name='add_article'),
    path('post_article/', views.post_article, name='post_article'),
    path('contact_now/', views.contact_form, name='contact_now')
]
