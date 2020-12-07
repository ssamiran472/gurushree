from rest_framework import viewsets,permissions
from .serializers import patient_registrationSerializer,billheaderSerializer,billdetailsSerializer,billreceiptSerializer
from .models import patient_registration,billheader,billdetails,billreceipt

class patient_registrationViewSet(viewsets.ModelViewSet):
    queryset = patient_registration.objects.all()
    permissions = [
        permissions.AllowAny
    ]
    serializer_class = patient_registrationSerializer


class billheaderViewSet(viewsets.ModelViewSet):
    queryset = billheader.objects.all()
    permissions = [
        permissions.AllowAny
    ]
    serializer_class = billheaderSerializer


class billdetailsViewSet(viewsets.ModelViewSet):
    queryset = billdetails.objects.all()
    permissions = [
        permissions.AllowAny
    ]
    serializer_class = billdetailsSerializer

class billreceiptViewSet(viewsets.ModelViewSet):
    queryset = billreceipt.objects.all()
    permissions = [
        permissions.AllowAny
    ]
    serializer_class = billreceiptSerializer