from django.urls import path
from home import views


urlpatterns = [
    path('', views.main, name='main'),
    path('note/<note_pk>/', views.view_note, name='view_note'),
    path('delete/<note_pk>', views.delete, name='delete'),
    path('settings/', views.settings, name='settings'),
    path('account/delete/', views.delete_account, name='delete_account'),
    path('search/', views.search_note, name='search_note'),
]