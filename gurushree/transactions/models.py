from django.db import models
import datetime

class patient_registration(models.Model):
    reg_type=models.CharField(max_length=32, null=True)
    title=models.CharField(max_length=32, null=True)
    gender=models.CharField(max_length=32, null=True)
    p_name=models.CharField(max_length=32, null=True)
    year=models.IntegerField(null=True)
    month=models.IntegerField(null=True)
    day=models.IntegerField(null=True)
    mobile_number=models.CharField(max_length=32, null=True)
    address=models.CharField(max_length=32, null=True)
    email_id=models.CharField(max_length=32, null=True)
    address2=models.CharField(max_length=32, null=True)
    location=models.CharField(max_length=32, null=True)
    pincode=models.CharField(max_length=32, null=True)
    alternateContact=models.CharField(max_length=32, null=True)
    marital=models.CharField(max_length=32, null=True)
    occupation=models.CharField(max_length=32, null=True)
    religion=models.CharField(max_length=32, null=True)
    father_name=models.CharField(max_length=32, null=True)
    blood_group=models.CharField(max_length=32, null=True)
    nationality=models.CharField(max_length=32, null=True)
    id_type=models.CharField(max_length=32, null=True)
    id_number=models.CharField(max_length=32, null=True)
    p_photo = models.FileField(max_length=355, null=True)
    a_photo = models.FileField(max_length=355, null=True)
    isActive=models.BooleanField(default=True)
    AddedBY =models.CharField(max_length=32, null=True)
    Addeddate = models.DateTimeField(auto_now_add=True)
    editedby =models.CharField(max_length=32, null=True)
    editeddate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.p_name


def generet_billNO():
    text = 'MRB'
    date = datetime.date.today()
    year = date.year
    last_bill = billheader.objects.all().count()
    return text + str(year) + str(last_bill + 1)

def str_date():
    date = datetime.date.today()
    return '{0}/{1}/{2}'.format(date.day, date.month, date.year)


def str_time():
    now = datetime.datetime.now()
    time = datetime.datetime.strftime(now, '%H:%M')
    return time

class billheader(models.Model):
    BillNo=models.CharField(max_length=32, null=True, default=generet_billNO)
    BillDateTime= models.DateTimeField(auto_now_add=True)
    BillDate=models.CharField(max_length=32, null=True, default=str_date)
    BillTime=models.CharField(max_length=32, null=True, default=str_time)
    RegNo=models.CharField(max_length=32, null=True)
    RegType=models.CharField(max_length=32, null=True)
    PayType=models.CharField(max_length=32, null=True)
    DiscountBy=models.CharField(max_length=32, null=True)
    DiscType=models.CharField(max_length=32, null=True)
    DiscPerc=models.DecimalField(max_digits=18, decimal_places=2, null=True)
    DiscNote=models.CharField(max_length=32, null=True)
    TotalAmount=models.DecimalField(max_digits=18, decimal_places=2, null=True)
    DrDiscount=models.DecimalField(max_digits=18, decimal_places=2, null=True)
    ReferDiscount=models.DecimalField(max_digits=18, decimal_places=2, null=True)
    HospDiscount=models.DecimalField(max_digits=5, decimal_places=2, null=True)
    TotalDiscount=models.DecimalField(max_digits=5, decimal_places=2, null=True)
    NetAmount=models.DecimalField(max_digits=5, decimal_places=2, null=True)
    Payable=models.DecimalField(max_digits=5, decimal_places=2, null=True)
    Balance=models.DecimalField(max_digits=5, decimal_places=2, null=True)
    TPAName=models.CharField(max_length=32, null=True)
    TPABalance=models.DecimalField(max_digits=5, decimal_places=2, null=True)
    PaidAmount=models.DecimalField(max_digits=5, decimal_places=2, null=True)
    Advance=models.DecimalField(max_digits=5, decimal_places=2, null=True)
    TobeRefund=models.DecimalField(max_digits=5, decimal_places=2, null=True)
    Refunded=models.DecimalField(max_digits=5, decimal_places=2, null=True)
    Status=models.CharField(max_length=32, null=True)
    CancelDate= models.DateTimeField(auto_now_add=True)
    CancelUser=models.CharField(max_length=32, null=True)
    CancelReason=models.CharField(max_length=32, null=True)
    FY=models.CharField(max_length=32, null=True)
    PatientName=models.CharField(max_length=32, null=True)
    Age=models.CharField(max_length=32, null=True)
    Year=models.IntegerField(null=True)
    Month=models.IntegerField(null=True)
    Days=models.IntegerField(null=True)
    Address1=models.CharField(max_length=32, null=True)
    IsActive=models.BooleanField(default=True)
    AddedBy=models.CharField(max_length=32, null=True)
    AddedOn	= models.DateTimeField(auto_now_add=True)
    EditedBy=models.CharField(max_length=32, null=True)
    EditedOn= models.DateTimeField(auto_now_add=True)





class billdetails(models.Model):
    BillCode=models.IntegerField(null=True)
    LineNo=models.IntegerField(null=True)
    SerDept=models.IntegerField(null=True)
    SerCode=models.IntegerField(null=True)
    SubSerCode=models.IntegerField(null=True)
    Qty=models.IntegerField(null=True)
    Amount=models.DecimalField(max_digits=5, decimal_places=2, null=True)
    TotalAmount=models.DecimalField(max_digits=5, decimal_places=2, null=True)
    DrCode=models.IntegerField(null=True)
    DrShare=models.DecimalField(max_digits=5, decimal_places=2, null=True)
    DrDisc=models.DecimalField(max_digits=5, decimal_places=2, null=True)
    ReferCode=models.IntegerField(null=True)
    ReferShare=models.DecimalField(max_digits=5, decimal_places=2, null=True)
    ReferDisc=models.DecimalField(max_digits=5, decimal_places=2, null=True)
    HospShare=models.DecimalField(max_digits=5, decimal_places=2, null=True)
    HospDisc=models.DecimalField(max_digits=5, decimal_places=2, null=True)
    NetAmount=models.DecimalField(max_digits=5, decimal_places=2, null=True)
    PaidAmount=models.DecimalField(max_digits=5, decimal_places=2, null=True)
    Balance=models.DecimalField(max_digits=5, decimal_places=2, null=True)
    VisitType=models.CharField(max_length=32, null=True)
    TPAApplicable=models.BooleanField(default=True)
    IsActive=models.BooleanField(default=True)





class billreceipt(models.Model):
    BillCode=models.IntegerField(null=True)
    RecNo=models.CharField(max_length=32, null=True)
    RecDateTime= models.DateTimeField(auto_now_add=True)
    RecDate=models.CharField(max_length=32, null=True)
    RecTime=models.CharField(max_length=32, null=True)
    RecAmount=models.DecimalField(max_digits=5, decimal_places=2, null=True)
    Cash=models.DecimalField(max_digits=5, decimal_places=2, null=True)
    CardType=models.CharField(max_length=32, null=True)
    CardBank=models.IntegerField(null=True)
    CardNo=models.CharField(max_length=32, null=True)
    Card=models.DecimalField(max_digits=5, decimal_places=2, null=True)
    Transfee=models.DecimalField(max_digits=5, decimal_places=2, null=True)
    CardTotal=models.DecimalField(max_digits=5, decimal_places=2, null=True)
    OtherPayType=models.CharField(max_length=32, null=True)
    OtherPayNo=models.CharField(max_length=32, null=True)
    OtherBank=models.IntegerField(null=True)
    OtherPaid=models.DecimalField(max_digits=5, decimal_places=2, null=True)
    OtherDate= models.DateTimeField(auto_now_add=True)
    RecMode=models.CharField(max_length=32, null=True)
    AddedBy=models.CharField(max_length=32, null=True)
    AddedDate= models.DateTimeField(auto_now_add=True)
    EditedBy=models.CharField(max_length=32, null=True)
    EditedDate= models.DateTimeField(auto_now_add=True)
    CancelBy=models.CharField(max_length=32, null=True)
    CancelDate= models.DateTimeField(auto_now_add=True)



