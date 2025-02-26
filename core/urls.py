from django.urls import include, path, re_path
from rest_framework import routers

from .views import ClientView, EmployeeView, FileUploadView, SalesView

app_name = 'core'


router = routers.DefaultRouter()
router.register(r'sales', viewset=SalesView, basename='sales')
router.register(r'clients', viewset=ClientView, basename='clients')
router.register(r'employees', viewset=EmployeeView, basename='employees')

urlpatterns = [
    path('', include(router.urls)),
    path('upload/', FileUploadView.as_view(), name="file-upload"),  # Remove regex
]