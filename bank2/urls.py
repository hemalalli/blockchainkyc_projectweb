from django.urls import path
from . import views
from blockchainkyc import settings
from django.conf.urls.static import static

app_name = "bank2"
urlpatterns = [
    path('login', views.bank_user_login, name = 'login'),
    path('search', views.usersearch, name = 'search'),
]
