from django.urls import path
from django.contrib.auth import views as vs
from . import views

urlpatterns=[
    path('',views.register_page,name='register'),
    path('login/',views.login_page,name='login'),
    path('home/',views.home,name='home'),
    path('logout/',views.logoutuser,name='logout'),
    path('pwdreset/',vs.PasswordResetView.as_view(),name='password_reset'),
    path('pwdresetdone/',vs.PasswordChangeDoneView.as_view(),name='password_reset_done'),
    path('pwdresetcnfrm/<uidb64>/<token>',vs.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('pwdresetcmpt/',vs.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
]