from rest_framework import serializers

from apis.models import PatientMedicalDetail


class PatientMedicalDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = PatientMedicalDetail
        fields = "__all__"
