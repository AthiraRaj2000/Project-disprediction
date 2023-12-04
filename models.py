from django.db import models

# Create your models here.
class dprofile(models.Model):
    Did=models.AutoField(primary_key=True)
    Lno=models.CharField(max_length=100)
    Fname=models.CharField(max_length=100)
    Lname=models.CharField(max_length=100)
    Gender=models.CharField(max_length=10)
    dob=models.DateField()
    email=models.EmailField(max_length=100)
    phone=models.CharField(max_length=10)
    qualification=models.CharField(max_length=100)
    certificates=models.CharField(max_length=100)
    furl=models.CharField(max_length=100)
    spc=models.CharField(max_length=100)
    exp=models.DateField()
    hname=models.CharField(max_length=100)
    cname=models.CharField(max_length=100)
    district=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    country=models.CharField(max_length=100)
    uname=models.CharField(max_length=100)
    pwd=models.CharField(max_length=100)
    status=models.CharField(max_length=100,default='pending')

class uprofile(models.Model):
    Uid=models.AutoField(primary_key=True)
    Fname=models.CharField(max_length=100)
    Lname=models.CharField(max_length=100)
    Gender = models.CharField(max_length=10)
    dob = models.DateField()
    hname = models.CharField(max_length=100)
    cname = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=10)
    uname = models.CharField(max_length=100)
    pwd = models.CharField(max_length=100)
    Ename=models.CharField(max_length=100)
    relation=models.CharField(max_length=100)
    contact=models.CharField(max_length=10)
    Status=models.CharField(max_length=20,default="active")

class opday(models.Model):
    Did=models.ForeignKey(dprofile,unique=True,primary_key=True,on_delete=models.CASCADE)
    sun=models.IntegerField()
    mon=models.IntegerField()
    tue=models.IntegerField()
    wed=models.IntegerField()
    thu=models.IntegerField()
    fri=models.IntegerField()
    sat=models.IntegerField()

class optime(models.Model):
    Did=models.ForeignKey(dprofile,unique=True,primary_key=True,on_delete=models.CASCADE)
    opfrom=models.TimeField()
    opto=models.TimeField()


class Admin(models.Model):
    uname=models.CharField(max_length=100)
    pwd=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)


class medHistory(models.Model):
    uid=models.IntegerField()
    bg = models.CharField(max_length=10)
    height=models.IntegerField()
    weight=models.IntegerField()
    medication = models.CharField(max_length=10,default='no')
    medlist = models.CharField(max_length=200,default='nil')
    mallergy = models.CharField(max_length=10,default='no')
    allergylist = models.CharField(max_length=200,default='nil')
    tob = models.CharField(max_length=10)
    alco = models.CharField(max_length=10)

class appointment(models.Model):
    uid=models.IntegerField()
    Did=models.IntegerField()
    Date=models.DateField()
    token=models.IntegerField(default=0)
    dis=models.CharField(max_length=250,default='not consulted')
    med=models.CharField(max_length=250,default='not consulted')

