from rest_framework import serializers
from .models import patient_registration,billheader,billdetails,billreceipt

class patient_registrationSerializer(serializers.ModelSerializer):
    class Meta:
        model=patient_registration
        fields='__all__'

class billheaderSerializer(serializers.ModelSerializer):
    class Meta:
        model=billheader
        fields='__all__'

class billdetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=billdetails
        fields='__all__'

class billreceiptSerializer(serializers.ModelSerializer):
    class Meta:
        model=billreceipt
        fields='__all__'