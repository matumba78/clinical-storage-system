from django.urls import path
from apis.views import *

urlpatterns = [
    path('details/', PatientMedicalDetailView.as_view(), name="patient_details"),
    path('audit/', AuditAPI.as_view(), name="audit_api"),
    ]