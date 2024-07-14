from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create_note/', views.create_note, name='create_note'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path("note/<note_id>/", views.note, name="note"),
]
