from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('recall/', views.RecallView.as_view(), name='recall'),
    path('sendcatalog/', views.SendCatalogView.as_view(), name='sendcatalog'),
    path('sendcatandprice/', views.SendCatandpriceView.as_view(), name='sendcatandprice'),
    path('quiz/', views.QuizView.as_view(), name='quiz'),
    path('subscribe/', views.SubscribeView.as_view(), name='subscribe'),
    path('agreement/', views.agreement, name='agreement'),
    path('privacy/', views.privacy, name='privacy'),
    path('thank-you/', views.thank_you, name='thank-you'),
]
