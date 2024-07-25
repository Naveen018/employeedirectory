from . import views
from django.urls import path


urlpatterns = [
    path("",views.display, name="home_url"),
    path("<int:id>/",views.employee_details,name="employee_url"),
]
