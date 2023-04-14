from django.db import models
from datetime import datetime
# Create your models here.
class Reseller(models.Model):
    company_name=models.TextField(max_length=50,db_column='reseller_company_name')
    reg_id=models.TextField(max_length=50,db_column='company_reg_id')
    account_number=models.TextField(max_length=50,db_column='bank_account_number')
    ifsc_code=models.TextField(max_length=50,db_column='bank_ifsc_code')
    branch_bank=models.TextField(max_length=50,db_column='bank_branch_name')
    address=models.TextField(max_length=50,db_column='company_address')
    country=models.TextField(max_length=50,db_column='company_country')
    mobile=models.TextField(max_length=50,db_column='mobile_number')
    email=models.TextField(max_length=50,db_column='company_email')
    password= models.TextField(max_length=50,db_column='pass_word')
    otp= models.TextField(max_length=50,db_column='company_otp')
    status=models.TextField(max_length=50,default="inactive",db_column='company_status')
    request_date=models.DateField(default=datetime.now,db_column='request_date')  


    class Meta:
        db_table='reseller'