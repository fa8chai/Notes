from django.urls import path
from users import views


urlpatterns = [
    path('login/', views.signin, name='login'),
    path('signup/',views.signup, name='signup'),
    path('logout/',views.signout, name='logout'),

]