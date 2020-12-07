from rest_framework import routers
from .api import patient_registrationViewSet,billheaderViewSet,billdetailsViewSet,billreceiptViewSet

router = routers.DefaultRouter()
router.register('patient_registration',patient_registrationViewSet,'patient_registration')
router.register('billheader',billheaderViewSet,'billheader')
router.register('billdetails',billdetailsViewSet,'billdetails')
router.register('billreceipt',billreceiptViewSet,'billreceipt')
urlpatterns=router.urls