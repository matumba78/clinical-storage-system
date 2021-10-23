from rest_framework.response import Response
from rest_framework import generics, permissions
# Create your views here.
from rest_framework.views import APIView

from apis.models import PatientMedicalDetail, Designation
from apis.serializers import PatientMedicalDetailSerializer

class UserIsDoctor(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.designation == Designation.DOCTOR:
            return True
        return False


class PatientMedicalDetailView(generics.ListCreateAPIView):
    serializer_class = PatientMedicalDetailSerializer
    permission_classes = (
        permissions.IsAuthenticated,
        UserIsDoctor,
    )

    def get_queryset(self):
        aadhaar_number = self.request.query_params.get("aadhaar_number", None)
        queryset = PatientMedicalDetail.objects.filter(aadhaar_number=aadhaar_number)
        return queryset


class AuditAPI(generics.ListAPIView):
    queryset = PatientMedicalDetail.objects.all()
    serializer_class = PatientMedicalDetailSerializer
    permission_classes =[
        permissions.IsAuthenticated
    ]
