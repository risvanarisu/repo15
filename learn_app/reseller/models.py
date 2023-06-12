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
    user_id=models.IntegerField(null=True,db_column='login_id')
    password= models.TextField(max_length=50,db_column='pass_word')
    otp= models.TextField(max_length=50,db_column='company_otp')
    status=models.TextField(max_length=50,default="inactive",db_column='company_status')
    request_date=models.DateField(default=datetime.now,db_column='request_date')  


    class Meta:
        db_table='reseller'

class Add_product(models.Model):
    title=models.TextField(max_length=50,db_column='pro_title')
    pro_id=models.TextField(max_length=50,db_column='registerd_pro_id')
    discription=models.TextField(max_length=100,db_column='pro_discription')
    pro_picture=models.ImageField(upload_to='product_images/',db_column='pro_pictures')
    price=models.IntegerField(db_column='pro_price')
    quantity=models.IntegerField(db_column='pro_quantity')
    weight=models.IntegerField(db_column='pro_weight')
    weight_unit=models.TextField(max_length=50,db_column='pro_weight_unit')
    catagory=models.TextField(max_length=50,db_column='pro_catagory')
    sub_catagory=models.TextField(max_length=50,db_column='pro_sub_catagory')
    brand=models.TextField(max_length=50,db_column='pro_brand')
   # Status=models.TextField(max_length=50,null=True,db_column='pro_status')
    reseller=models.ForeignKey(Reseller,on_delete=models.CASCADE,null=True,db_column='reseller')

    class Meta:
        db_table='add_product'   