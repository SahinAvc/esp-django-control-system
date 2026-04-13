from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.kontrol_panel,name="kontrol"),
    path('<str:komut>/', views.komut_gonder)
]