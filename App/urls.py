from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('detail/<int:pk>', views.DetailView.as_view(), name='detail'),
    path('delete/<str:username>', views.DeleteView.as_view(), name='delete'),
    path('update/<int:pk>', views.UpdataView.as_view(), name='update'),
    path('signup/', views.SignUp.as_view(), name='SignUp'),
    path('login/', views.LoginView.as_view(), name='login')
]