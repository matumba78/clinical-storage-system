from django.contrib import admin

# Register your models here.
from apis.models import PatientMedicalDetail, Hospital, User

admin.site.register(Hospital)
admin.site.register(PatientMedicalDetail)
admin.site.register(User)
