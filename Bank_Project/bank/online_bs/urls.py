from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("login", views.user_login, name="login"),
    path("register", views.user_registration, name="user_registration"),
    path("withdraw", views.withdrawal, name="withdrawal"),
    path("report", views.report, name="report"),
    path("deposit", views.deposit, name="deposit"),
    path("request", views.request_exd_money, name="request_exd_money"),
    path("monthly_inc", views.set_limit, name="monthly_inc"),
    path('download-report', views.download_report, name='download_report'),
    path('req_withdraw', views.req_withdrawal, name='req_withdrawal'),

]