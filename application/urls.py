from django.contrib import admin
from django.urls import path
import hector.views as views

urlpatterns = [
    path('', views.index, name="home"),
    path('admin/', admin.site.urls),
    path('oignon_clicked', views.oignon),
    path('carotte_clicked', views.carotte),
    path('salade_clicked', views.salade),
    path('reset_clicked', views.reset),
    path('start_clicked', views.start_mission),
]
