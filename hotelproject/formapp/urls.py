from . import views
from django.urls import path

urlpatterns = [



    path('signin',views.signin,name='signin'),
    path('register',views.register,name='register'),
    path('logout',views.logout,name='logout'),
]
