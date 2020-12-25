from django.urls import include, path
from . import views
app_name= 'book1'

urlpatterns = [
    path('empForm/',views.employee_form, name='employee_form'),
    path('empForm/<int:id>/',views.employee_form, name='employeeUpdate'),
    path('employee_list/',views.employee_list, name='employee_list'),
    path('employee_delete/<int:id>/',views.employee_delete, name='employee_delete'),
]
