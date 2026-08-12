from django.urls import path
from .views import * 

urlpatterns = [
    path("",employee_list,name='employee_list'),
    path('add/', add_employee, name='add_employee'),
    path('edit/<int:id>/', edit_employee, name='edit_employee'),
    path('delete/<int:id>/',delete_employee, name='delete_employee'),
    path("employees/import/",import_employees, name="import_employees"),
    path("download-sample/",download_sample,name="download_sample"),
    path("export/pdf/",export_pdf,name="export_pdf"),
]