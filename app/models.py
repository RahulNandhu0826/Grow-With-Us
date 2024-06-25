

from django.db import models
from django.contrib.auth.models import User
from datetime import datetime,date


# Create your models here

class users_reg(models.Model):
    userr=models.ForeignKey(User,on_delete=models.CASCADE)
    user_name=models.CharField(max_length=30,null=True)
    child_name=models.CharField(max_length=30,null=True)
    parent_name=models.CharField(max_length=30,null=True)
    address=models.CharField(max_length=30,null=True)
    birth_date=models.DateField(max_length=30,null=True)
    image=models.ImageField(upload_to="uploadedimages",null=True)
    email=models.EmailField(null=True)
    users_approve=models.CharField(max_length=30,null=True)

    contact_number=models.IntegerField(null=True)
    password=models.CharField(max_length=50,null=True)

    def __str__(self):
        return self.user_name
    

    def age(self):
        today = date.today()
        delta_in_years = today.year - self.birth_date.year
        if today.month < self.birth_date.month or \
            (today.month == self.birth_date.month and today.day < self.birth_date.day):
            delta_in_years -= 1
        return delta_in_years
    


class Dietition(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    diet_Username=models.CharField(max_length=30,null=True)
    diet_Name=models.CharField(max_length=30,null=True)
    diet_Date_of_Birth=models.DateField(null=True)
    diet_Qualifications=models.CharField(max_length=30,null=True)
    diet_Experience=models.CharField(max_length=30,null=True)
    diet_Mobile_no=models.IntegerField(null=True)
    email=models.EmailField(null=True)
    diet_password=models.CharField(max_length=50,null=True)
    diet_Image=models.ImageField(upload_to="uploadedimages",null=True)
    diet_approvement=models.CharField(max_length=30,null=True)
    # replay=models.CharField(max_length=30,default="waiting")
    rating=models.CharField(max_length=30,null=True)
    # is_active=models.BooleanField(null=True)
    def __str__(self):
        return self.diet_Name
    
      
class add_plans(models.Model):
    user=models.ForeignKey(Dietition,on_delete=models.CASCADE)
    std_three_month=models.IntegerField(null=True)
    std_six_month=models.IntegerField(null=True)
    std_one_yr=models.IntegerField(null=True)
    
class plan(models.Model):
    user=models.ForeignKey(Dietition,on_delete=models.CASCADE)
    ex_three_month=models.IntegerField(null=True)
    ex_six_month=models.IntegerField(null=True)
    ex_one_yr=models.IntegerField(null=True)
    
    
class user_appointment(models.Model):
    userr_appointment=models.ForeignKey(Dietition,on_delete=models.CASCADE)
    userr=models.ForeignKey(users_reg,on_delete=models.CASCADE)
    name=models.CharField(max_length=30,null=True)
    mobile_number=models.IntegerField(null=True)
    email_address=models.EmailField(null=True)
    name_of_dietition=models.CharField(max_length=30,null=True)
    choose_a_plan=models.CharField(max_length=30,null=True)
    duration_of_plan=models.CharField(max_length=30,null=True)
    payment_amount=models.IntegerField(null=True)
    chat_code=models.CharField(max_length=30,null=True)
    payment_done=models.CharField(max_length=30,null=True,default="no")

    


class payments(models.Model):
    
    name=models.CharField(max_length=30,null=True)
    amount=models.IntegerField(null=True)
    
class user_feedback(models.Model):
    userr_feedback=models.ForeignKey(users_reg,on_delete=models.CASCADE)
    name_of_user=models.CharField(max_length=30,null=True)
    Name_of_dietition=models.CharField(max_length=30,null=True)
    feedback=models.CharField(max_length=30,null=True)
    rating=models.CharField(max_length=30,null=True)

class paid_details(models.Model):
    card_name=models.CharField(max_length=30,null=True)
    card_number=models.IntegerField(null=True)
    expiry_date=models.CharField(max_length=30,null=True)
    security_code=models.IntegerField(null=True)
    postal_code=models.IntegerField(null=True)

class user_complaint(models.Model):
    user=models.ForeignKey(users_reg,on_delete=models.CASCADE)
    name=models.CharField(max_length=30,null=True)
    diet_name=models.CharField(max_length=30,null=True)
    admin_reply=models.CharField(max_length=500,default='waiting for admin reply')
    issues=models.CharField(max_length=30,null=True)
    


class add_healthy_tips(models.Model):
    tips=models.CharField(max_length=30,null=True)
    tip=models.CharField(max_length=30,null=True)

class admin_reply(models.Model):
    reply=models.CharField(max_length=30,null=True)

class diet_chart(models.Model):
    # charts=models.ForeignKey(users_reg,on_delete=models.CASCADE)
    diets=models.ForeignKey(Dietition,on_delete=models.CASCADE)
    diet_name=models.CharField(max_length=30,null=True)
    chart_heading=models.CharField(max_length=5000,null=True)
    explanation=models.CharField(max_length=5000,null=True)

#chat
class Room(models.Model):
    name=models.CharField(max_length=1000)

class Messages(models.Model):
    value=models.CharField(max_length=1000000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=1000000)
    room = models.CharField(max_length=1000000)



class videos(models.Model):
    age=models.IntegerField(null=True)
    videos=models.FileField(upload_to="videos",null=True)
    video_name=models.CharField(max_length=1000,null=True)

class images(models.Model):
    age=models.IntegerField(null=True)
    images=models.ImageField(upload_to="videos",null=True)
    image_name=models.CharField(max_length=1000,null=True)

class stories(models.Model):
    age=models.IntegerField(null=True)
    story=models.FileField(upload_to="videos",null=True)
    story_name=models.CharField(max_length=1000,null=True)

class lullaby(models.Model):
    age=models.IntegerField(null=True)
    lullaby=models.FileField(upload_to="videos",null=True)
    lullaby_name=models.CharField(max_length=1000,null=True)

class vaccine_notification(models.Model):
    v_age=models.CharField(max_length=50,null=True)
    vaccine_name=models.CharField(max_length=50,null=True)
    v_dose=models.CharField(max_length=50,null=True)

# class notification(models.Model):


# vaccinenotification
# from django.db import models
# from datetime import date

# class Person(models.Model):
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     birthdate = models.DateField()

#     @property
#     def age(self):
#         today = date.today()
#         years_diff = today.year - self.birthdate.year
#         if today.month < self.birthdate.month or (today.month == self.birthdate.month and today.day < self.birthdate.day):
#             years_diff -= 1
#         return years_diff
