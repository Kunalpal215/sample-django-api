from django.urls import path
from . import views
urlpatterns = [
    path('',views.homePage,name="jsdfk"),
    path('json/',views.nextPage,name="jsonPage"),
]