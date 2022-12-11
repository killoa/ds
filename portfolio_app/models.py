from django.db import models
from datetime import date

# Create your models here.
class User(models.Model):
    Name=models.CharField(max_length=70,null=False, blank=False,default="")
    FamilyName=models.CharField(max_length=70,null=False, blank=False,default="")
    birthday=models.DateField(default=date)
    Email=models.EmailField(max_length=100,null=False, blank=False, default='my.mail@gmail.com')
    password=models.CharField(max_length=20,null=False,blank=False)
    phoneNumber=models.IntegerField(max_length=8,null=False)
    Photo=models.ImageField(upload_to='photo/user')
    class Meta:
        db_table="User"

class Biography(models.Model):
    email=models.EmailField(max_length=100,null=True, blank=True, default='my.mail@gmail.com')
    website=models.CharField(max_length=70,null=True, blank=True,default="")
    socialProfile=models.CharField(max_length=70,null=True, blank=True,default="")
    class Meta:
        db_table="Biography"

class ProfessionalAccomplishement(models.Model):
    ListOfAccomlishement=models.CharField(max_length=70,null=True, blank=True,default="")
    Example=models.CharField(max_length=70,null=True, blank=True,default="")
    photos=models.ImageField(upload_to='photo/ProfessionalAccomplishement')
    class Meta:
        db_table="ProfessionalAccomplishement"

class Awards(models.Model):
    title=models.CharField(max_length=70,null=True, blank=True,default="")
    date=models.DateField(default=date)
    photo=models.ImageField(upload_to='photo/awards')
    class Meta:
        db_table="Awards"

class licenses(models.Model):
    title=models.CharField(max_length=70,null=True, blank=True,default="")
    link=models.ImageField(upload_to='photo/licenses')
    class Meta:
        db_table="license"

class Volunteering(models.Model):
    title=models.CharField(max_length=70,null=True, blank=True,default="")
    description=models.CharField(max_length=100,null=True, blank=True,default="")
    class Meta:
        db_table="Volunteering"

class References(models.Model):
    name=models.CharField(max_length=70,null=True, blank=True,default="")
    job=models.CharField(max_length=70,null=True, blank=True,default="")
    Email=models.EmailField(max_length=100,null=True, blank=True, default='my.mail@gmail.com')
    phoneNumber=models.IntegerField(max_length=8,null=True)

    class Meta:
        db_table="references"


class Portfolio(models.Model):
    CareerSummary=models.CharField(max_length=70,null=True, blank=True,default="")
    PhilosophyStatement=models.CharField(max_length=70,null=True, blank=True,default="")
    biography=models.ForeignKey(Biography,max_length=70,on_delete=models.CASCADE)
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    accomplishement=models.ForeignKey(ProfessionalAccomplishement,null=True,blank=True,on_delete=models.CASCADE)
    awards=models.ForeignKey(Awards,null=True,blank=True,on_delete=models.CASCADE)
    license=models.ForeignKey(licenses,null=True,blank=True,on_delete=models.CASCADE)
    volunteering=models.ForeignKey(Volunteering,null=True,blank=True,on_delete=models.CASCADE)
    references=models.ManyToManyField(References)

    class Meta:
        db_table="Portfolio"



