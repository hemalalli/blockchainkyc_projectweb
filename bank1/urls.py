from django.urls import path
from . import views
from blockchainkyc import settings
from django.conf.urls.static import static

app_name = "bank1"
urlpatterns = [
    path('login', views.bank_user_login, name = 'login'),
    path('approval', views.bank_approval, name = 'approval'),
    path('sendtoblockchain/<slug:kid>/',views.send_blockchain, name= 'sendtoblockchain'),
    path('documentrejected/<slug:kid>/', views.document_rejected, name='documentrejected'),
]
