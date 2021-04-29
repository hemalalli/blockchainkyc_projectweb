from django.urls import path
from . import views
from blockchainkyc import settings
from django.conf.urls.static import static

app_name = "fileupload"
urlpatterns = [
    path('login', views.user_login, name = 'login'),
    path('upload/<slug:user>', views.upload, name= 'upload'),
    path('updatenotification/<slug:action>/<slug:kid>', views.updatenotification, name= 'updatenotification')
]
