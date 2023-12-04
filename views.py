import datetime
from turtledemo.chaos import h

import reg as reg
from dateutil.relativedelta import relativedelta
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.core.mail import send_mail
from django.db.models import Q
from django.http import HttpResponse, request
from django.shortcuts import render, redirect

# create your views here

from . import form
from .models import dprofile, uprofile, opday, optime, Admin, medHistory, appointment

import pandas as pd
import numpy as np
import random
import string

from disprediction.settings import EMAIL_HOST_USER


def index(request):
    print(type(datetime.datetime.now().date()))
    ddmin = str(datetime.datetime.now().date() - relativedelta(years=70))
    ddmax = str(datetime.datetime.now().date() - relativedelta(years=23))
    dexpmin = str(datetime.datetime.now().date() - relativedelta(years=46))
    dexpmax = str(datetime.datetime.now().date())
    pdmin = str(datetime.datetime.now().date() - relativedelta(years=105))
    pdmax = str(datetime.datetime.now().date())
    print(max)
    return render(request, 'index.html', {'ddmin': ddmin, 'ddmax': ddmax,'dexpmin':dexpmin,'dexpmax':dexpmax,'pdmin':pdmin,'pdmax':pdmax})


def index2(request):
    return render(request, 'index2.html')



def registration(request):
    if request.method=='POST' and request.FILES["bio"]:
        uploaded_file=request.FILES['bio']
        fs=FileSystemStorage()
        fname2=uploaded_file.name
        filename=fs.save(fname2,uploaded_file)
        uploaded_file_url=fs.url(filename)
        b = request.POST.get('lno')
        print("licence_no=",b)
        c = request.POST.get('fname')
        d = request.POST.get('lname')
        e = request.POST.get('gen')
        f = request.POST.get('DOB')
        g = request.POST.get('email')
        h = request.POST.get('ph')
        i = request.POST.get('qualifi')
        j = request.POST.get('spc')
        k = request.POST.get('exp')
        l = request.POST.get('hname')
        m = request.POST.get('cname')
        n = request.POST.get('district')
        o = request.POST.get('state')
        p = request.POST.get('country')
        q = request.POST.get('uname')
        r = request.POST.get('pwd')
        obj = dprofile.objects.all()
        for x in obj:
            if x.phone == h:
                return HttpResponse(" phone number already exists")
            elif x.email == g:
                return HttpResponse(" mail id already exists")
            elif x.uname == q:
                return HttpResponse(" user name already exists")
        print("FIRSTNAME",c)
        reg=dprofile(Lno=b,Fname=c,Lname=d,Gender=e,dob=f,email=g,phone=h,qualification=i,
                     furl=uploaded_file_url,certificates=request.POST.get('fname1'),spc=j,exp=k,hname=l,cname=m,district=n,state=o,country=p,uname=q,pwd=r)
        reg.save()

        days = request.POST.getlist('opdays')
        print('type of days=', type(days))
        d1 = d2 = d3 = d4 = d5 = d6 = d7 = 0
        if "sunday" in days:
            d1 = 1
        if "monday" in days:
            d2 = 1
        if "tuesday" in days:
            d3 = 1
        if "wednesday" in days:
            d4 = 1
        if "thursday" in days:
            d5 = 1
        if "friday" in days:
            d6 = 1
        if "saturday" in days:
            d7 = 1
        sttime=request.POST.get('stime')
        entime=request.POST.get('etime')
        docdata = dprofile.objects.get(Did=reg.Did)
        db1 = opday(Did=docdata, sun=d1, mon=d2, tue=d3, wed=d4, thu=d5, fri=d6, sat=d7)
        db2 = optime(Did=docdata,opfrom=sttime,opto=entime)
        db1.save()
        db2.save()
        return HttpResponse("registered successfully")




def user_registration(request):

    a = request.POST.get('fname')
    b = request.POST.get('lname')
    c = request.POST.get('gen')
    d = request.POST.get('DOB')
    e = request.POST.get('hname')
    f = request.POST.get('cname')
    g = request.POST.get('district')
    h = request.POST.get('state')
    i = request.POST.get('country')
    j = request.POST.get('mail')
    k = request.POST.get('ph')
    l = request.POST.get('uname')
    m = request.POST.get('pwd')
    n = request.POST.get('ename')
    o = request.POST.get('relation')
    p = request.POST.get('contact')
    obj = uprofile.objects.all()
    for x in obj:
        if x.phone == k:
            return HttpResponse("already exists")
        elif x.email ==j:
            return HttpResponse("already exists")
        elif x.uname == l:
            return HttpResponse("already exists")
    register=uprofile(Fname=a,Lname=b,Gender=c,dob=d,hname=e,cname=f,district=g,state=h,country=i,email=j,phone=k,uname=l,pwd=m,Ename=n,relation=o,contact=p)





    register.save()
    return HttpResponse("registered successfully")

def viewuprofile(request):
    obj=uprofile.objects.all()
    return render(request,'admin/user.html',{'data':obj})

def adminbase(request):
    return render(request,'admin/adminbase.html')


def doctorbase(request):
    return render(request,'doctor/doctorbase.html')

def userbase(request):
    return render(request,'user/userbase.html')

def login(request):
    utype=request.POST.get('utype')
    uname=request.POST.get('username')
    pwd=request.POST.get('password')
    print('utype=',utype)
    print('uname=',uname)
    print('password=',pwd)
    if utype=='Admin':
        try:
            print('hai')
            obj1=Admin.objects.all()
            for x in obj1:
                print(x.uname)
            ad=Admin.objects.get(uname=uname)
            if pwd==ad.pwd:
                request.session['sid']=ad.uname
                return render(request,'admin/adminHome.html',{'username':ad})
            else:
                return HttpResponse('incorrect password')
        except:
            return HttpResponse("username doesn't exist")
    elif utype == 'Doctor':


         if dprofile.objects.get(uname=uname) is not None:
             print("not nont")
             doc=dprofile.objects.get(uname=uname)
             if pwd == doc.pwd:
                 request.session["sid"]=doc.uname
                 st=doc.status
                 print("status=",st)

                 return render(request,"doctor/doctorHome.html",{'doc':doc})
             else:
                return HttpResponse('incorrect password')
         else:
            return HttpResponse("username doesn't exist")
    else:

         if uprofile.objects.get(uname=uname) is not None:
             print("not nont")
             patient1=uprofile.objects.get(uname=uname)
             if pwd==patient1.pwd:
                 print("correct password")
                 request.session['sid']=patient1.uname
                 print('session set' )
                 return render(request,'user/userHome.html',{'obj':patient1,'symlist':s2})
             else:
                 return HttpResponse("incorrect password")
         else:

             return HttpResponse("username doesn't exist")

def logout(request):
    try:
        request.session['sid'].delete()
        return render(request,'index.html')
    except:
        print("exception")
        return render(request,"index.html")

def viewdoctors(request):
    obj=dprofile.objects.all()
    return render(request,'admin/ViewDoctors.html',{'data':obj})

def viewblockeddoctors(request):
    obj=dprofile.objects.filter(status='deactivated')
    return render(request,'admin/ViewDoctors.html',{'data':obj})

def newdoctorreg(request):
    obj=dprofile.objects.filter(status='pending')
    return render(request,'admin/ViewDoctors.html',{'data':obj})



def viewpatients(request):
    obj=uprofile.objects.all()
    return render(request,'admin/ViewPatients.html',{'data':obj})

def viewuser(request):
    obj=uprofile.objects.get(uname=request.session['sid'])
    return render(request,'user/uprofile.html',{'data':obj})

def manageDoc(request):
    id=request.POST.get('did')
    doc=dprofile.objects.get(Did=id)
    print(doc.Did)
    print(id)
    if 'approve' in request.POST:
        doc.status = "active"
        doc.save()
        return viewdoctors(request)
    elif 'reject' in request.POST:
        doc.status = "rejected"
        doc.save()
        return viewdoctors(request)
    elif 'deactivate' in request.POST and doc.status== "active":
        doc.status = "deactivated"
        doc.save()
        return viewdoctors(request)

def getDid(request):
    obj=dprofile.objects.get(uname=request.session['sid'])
    did=obj.Did
    return did

def doc_viewprofile(request):
    dp=form.Abc(request.POST,request.FILES)
    doc=dprofile.objects.get(uname=request.session['sid'])
    print("uname=",doc.uname)
    st=doc.status
    con=optime.objects.get(Did=getDid(request))

    days=opday.objects.get(Did=doc)
    print(days.Did_id)
    print(days.mon)
    print("from",con.opfrom)


    return render(request, 'doctor/doctorprofile.html',{'doc':doc,'con':con,'days':days,'status':st})

def dMail(request):
    us=dprofile.objects.get(uname=request.session['sid'])
    return mailUpdate (request,us)



def dPhone(request):
    us=dprofile.objects.get(uname=request.session['sid'])
    return phoneUpdate (request,us)



def dPwd(request):

    us=dprofile.objects.get(uname=request.session['sid'])
    return pwdUpdate(request,us)



def dAdd(request):
    us=dprofile.objects.get(uname=request.session['sid'])
    return addUpdate (request,us)


def qualUpdate(request):
    if request.method=='POST' and request.FILES['cert']:
        print('yes')
        certificate=request.FILES['cert']
        fs=FileSystemStorage()
        fname=certificate.name
        fsize=certificate.size
        print(fname)
        print(fsize)
        filename=fs.save(fname,certificate)
        certificate_url=fs.url(filename)

    doc=dprofile.objects.get(uname=request.session['sid'])
    x=doc.qualification
    doc.qualification=request.POST.get('qual'),x
    doc.furl=certificate_url
    doc.save()
    return doc_viewprofile(request)

def daysUpdate(request):
    days=request.POST.getlist('condays')
    print('type of days=',type(days))
    d1=d2=d3=d4=d5=d6=d7=0

    if "sunday" in days:
        d1=1

    if "monday" in days:
        d2=1

    if "tuesday" in days:
        d3=1

    if "wednesday" in days:
        d4=1

    if "thursday" in days:
        d5=1

    if "friday" in days:
        d6=1

    if "saturday" in days:
        d7=1

    docdata=dprofile.objects.get(uname=request.session['sid'])
    db1=opday(Did=docdata,sun=d1,mon=d2,tue=d3,wed=d4,thu=d5,fri=d6,sat=d7)
    db1.save()

    return doc_viewprofile(request)

def myprofile(request):
    user1=uprofile.objects.get(uname=request.session['sid'])
    return render(request,'user/uProfile.html',{'data':user1,"med":checkMeddata(request)})

def getUid(request):
    obj=uprofile.objects.get(uname=request.session['sid'])
    uid=obj.uid
    return uid

def checkMeddata(request):
    try:
        if medHistory.objects.get(uid=getUid(request)):
            med="yes"
    except:
        med="no"
    return med




def pwdUpdate(request,obj):
    print("pwd",obj.pwd)
    print("pwd1",request.POST.get('pwd1'))
    if obj.pwd==request.POST.get('pwd1'):
        obj.pwd=request.POST.get('pwd2')

    else:
        return HttpResponse("current password is incorrect")

    obj.save()
    try:
        if obj.Did:
            return doc_viewprofile(request)
    except:
        return myprofile(request)



def addUpdate(request,obj):
    obj.hname=request.POST.get('hname')
    obj.cname = request.POST.get('cname')
    obj.district = request.POST.get('district')
    obj.state = request.POST.get('state')
    obj.country = request.POST.get('country')
    obj.save()

    try:
        if obj.Did:
            return doc_viewprofile(request)
    except:
        return myprofile(request)


def mailUpdate(request,objt):
    try:
        if objt.Did:
            doc1=dprofile.objects.all()

    except:
        doc1=uprofile.objects.all()
    for x in doc1:
        if x.email==request.POST.get('email') and x.uname!=request.session['sid']:
            return HttpResponse ('mail id already exsist')
    print('mail=',request.POST.get('email'))
    objt.email=request.POST.get('email')
    objt.save()
    try:
        if objt.Did:
            return doc_viewprofile(request)

    except:
        return myprofile(request)

def phoneUpdate(request,obj):
    try:
        if obj.Did:
            doc1 = dprofile.objects.all()

    except:
        doc1 = uprofile.objects.all()
    for x in doc1:
        if x.phone == request.POST.get('phone') and x.uname != request.session['uname']:
            return HttpResponse('phone no already exsist')

    obj.phone = request.POST.get('phone')
    obj.save()
    try:
        if obj.Did:
            return doc_viewprofile(request)

    except:
        return myprofile(request)

def uPhone(request):
    us=uprofile.objects.get(uname=request.session['sid'])
    return phoneUpdate(request,us)

def uMail(request):
    us = uprofile.objects.get(uname=request.session['sid'])
    return mailUpdate(request, us)


def uPwd(request):
    us = uprofile.objects.get(uname=request.session['sid'])
    return pwdUpdate(request, us)


def uAdd(request):
    us = uprofile.objects.get(uname=request.session['sid'])
    return addUpdate(request, us)

def viewMedHistory(request):
    user1=uprofile.objects.get(uname=request.session['sid'])
    try:
        medobj=medHistory.objects.get(uid=user1.Uid)
        return render(request,'user/viewMedHistory.html',{'user1':medobj,'userview':user1})
    except:
        medobj="no"
        return render(request,'user/viewMedHistory.html',{'user1':medobj,'userview':user1})

def addMedHistory(request):
    user1=uprofile.objects.get(uname=request.session['sid'])
    return render(request,'user/addMedHistory.html',{ 'userview': user1, "med": checkMeddata(request)})


def updateMedication(request):
    user1 = uprofile.objects.get(uname=request.session['sid'])
    medobj = medHistory.objects.get(uid=user1.Uid)
    medobj.medlist=request.POST.get('medlist')
    medobj.save()
    return render(request,'user/addMedHistory.html',{'userview': user1,'user1':medobj,"med": checkMeddata(request)})

def updateallergy(request):
    user1 = uprofile.objects.get(uname=request.session['sid'])
    medobj = medHistory.objects.get(uid=user1.Uid)
    medobj.allergylist=request.POST.get('allergylist')
    medobj.save()
    return render(request,'user/addMedHistory.html',{'userview': user1,'user1':medobj,"med": checkMeddata(request)})








def addMeddb(request):
    b = request.POST.get('bg')
    c = request.POST.get('hg')
    d = request.POST.get('wg')
    e = request.POST.get('medication')
    f = request.POST.get('mlist')
    g = request.POST.get('mallergy')
    h =request.POST.get('alist')
    i = request.POST.get('tobaco')
    j = request.POST.get('alco')
    obj = uprofile.objects.all()
    reg=medHistory(uid=request.POST.get('uid'),bg=b,height=c,weight=d,medication=e,medlist=f,mallergy=g,allergylist=h,tob=i,alco=j)
    reg.save()
    return render(request,'user/addMedHistory.html',{'obj':obj})

def departs(request):
    dep=dprofile.objects.values("spec").distinct()
    list1=[]
    for x in dep:
            list1.append(x['spec'])
    return list1

global l1

l1 = ['back_pain', 'constipation', 'abdominal_pain', 'diarrhoea', 'mild_fever', 'yellow_urine',
          'yellowing_of_eyes', 'acute_liver_failure', 'fluid_overload', 'swelling_of_stomach',
          'swelled_lymph_nodes', 'malaise', 'blurred_and_distorted_vision', 'phlegm', 'throat_irritation',
          'redness_of_eyes', 'sinus_pressure', 'runny_nose', 'congestion', 'chest_pain', 'weakness_in_limbs',
          'fast_heart_rate', 'pain_during_bowel_movements', 'pain_in_anal_region', 'bloody_stool',
          'irritation_in_anus', 'neck_pain', 'dizziness', 'cramps', 'bruising', 'obesity', 'swollen_legs',
          'swollen_blood_vessels', 'puffy_face_and_eyes', 'enlarged_thyroid', 'brittle_nails',
          'swollen_extremeties', 'excessive_hunger', 'extra_marital_contacts', 'drying_and_tingling_lips',
          'slurred_speech', 'knee_pain', 'hip_joint_pain', 'muscle_weakness', 'stiff_neck', 'swelling_joints',
          'movement_stiffness', 'spinning_movements', 'loss_of_balance', 'unsteadiness',
          'weakness_of_one_body_side', 'loss_of_smell', 'bladder_discomfort', 'foul_smell_of urine',
          'continuous_feel_of_urine', 'passage_of_gases', 'internal_itching', 'toxic_look_(typhos)',
          'depression', 'irritability', 'muscle_pain', 'altered_sensorium', 'red_spots_over_body', 'belly_pain',
          'abnormal_menstruation', 'dischromic _patches', 'watering_from_eyes', 'increased_appetite', 'polyuria',
          'family_history', 'mucoid_sputum',
          'rusty_sputum', 'lack_of_concentration', 'visual_disturbances', 'receiving_blood_transfusion',
          'receiving_unsterile_injections', 'coma', 'stomach_bleeding', 'distention_of_abdomen',
          'history_of_alcohol_consumption', 'fluid_overload', 'blood_in_sputum', 'prominent_veins_on_calf',
          'palpitations', 'painful_walking', 'pus_filled_pimples', 'blackheads', 'scurring', 'skin_peeling',
          'silver_like_dusting', 'small_dents_in_nails', 'inflammatory_nails', 'blister', 'red_sore_around_nose',
          'yellow_crust_ooze']
s2=[]
slist=l1
print(slist)
for sl in slist:
    s2.append(sl.replace("_","  ").upper())





def userHome(request):
    obj=uprofile.objects.get(uname=request.session['sid'])
    list=departs(request)

    try:
        if medHistory.objects.get(uid=obj.Uid):
            return  render(request,'user/userHome.html',{"udata":obj,"med":"yes","dep":list,"symlist":s2})
    except:
        return render(request,'user/userHome.html',{"udata":obj,"med":"yes","dep":list,"symlist":s2})


def getuid(request):
    obj=uprofile.objects.get(uname=request.session['sid]'])
    uid=obj.Uid
    return uid

def userappointment(request):
    obj=dprofile.objects.get(Did=request.POST.get('did'))
    obj1=opday.objects.get(Did=obj)
    obj2=optime.objects.get(Did=obj)
    obj3=datetime.datetime.now().date()

    return render(request,'user/appointment.html', {'obj': obj,'obj1':obj1,'obj2':obj2, 'obj3':obj3})

def fixappointment(request):
    us1=uprofile.objects.get(uname=request.session['sid'])
    docid=request.POST.get('Did')
    docobj=dprofile.objects.get(Did=docid)
    print(type(docid))
    adate=request.POST.get('date')
    ld1=request.POST.get('date').split('-')
    today =datetime.datetime(int(ld1[0]),int(ld1[1]),int(ld1[2]))
    day=today.strftime("%A")
    print("day=",day)

    opdays=opday.objects.get(Did=docobj)
    l2="yes"
    if day=="sunday":
        if opdays.sun!=1:
            l2="no"
    elif day=="monday":
        if opdays.mon!=1:
            l2="no"
    elif day=="tuesday":
        if opdays.tue!=1:
            l2="no"
    elif day=="wednesday":
        if opdays.wed!=1:
            l2="no"
    elif day=="thursday":
        if opdays.thu!=1:
            l2="no"
    elif day=="friday":
        if opdays.fri!=1:
            l2="no"
    elif day=="saturday":
        if opdays.sat!=1:
            l2="no"



    print("L2=",l2)


    if l2=="no":
        return HttpResponse("<html> <head> </head> <body bgcolor='pink'> <br> <br> <br> <br>  <center> Doctor is not available for consultations on this day. Try another day <br> <a href='/searchDoc/'  > Back </center> </body> </html>")

    if appointment.objects.filter(Did=request.POST.get('Did'),Date=request.POST.get('date'),uid=us1.Uid):
        return HttpResponse("<html> <head> </head> <body> <br> <br> <br> <center> You already took appointment for this date. Try another day <br> <a href='/searchDoc/'  > Back </centre> </body> </html>")

    if not appointment.objects.filter(Q(Did=request.POST.get('Did')),Q(Date=request.POST.get('date'))):
           tok=1

    else:
        tok=appointment.objects.filter(Q(Did=request.POST.get('Did')),Q(Date=request.POST.get('date'))).order_by('-token').first().token+1

    if tok > 2:
        return HttpResponse("<html> <head> </head> <br> <br> <br> <center> TOKEN for this day is closed. Try another day <br> <a href='/usearch/'   > Back </center> </body> </html>")

    else :
        db=appointment(uid=us1.Uid,Did=request.POST.get('Did'),Date=request.POST.get('date'),token=tok)
        db.save()
        messages.success(request,f"YOUR APPOINTMENT IS FIXED WITH: {docobj.Fname} {docobj.Lname} on:{adate}.\n TOKEN N0:{tok} ")
        return redirect('/userviewappointment/')

def myappointment_details(request):
    obj=dprofile.objects.filter(Did=request.POST.get('did'))
    return render(request,'doctor/appointment.html', {'obj': obj})


def userviewappointment(request):
    obj=dprofile.objects.all()
    obj1=optime.objects.all()
    obj3=uprofile.objects.get(uname=request.session['sid'])
    obj2=appointment.objects.filter(uid=obj3.Uid)
    return render(request,'user/viewappointments.html', {'apobj': obj2,'dobj':obj,'optime':obj1})


def docviewappointment(request):
    obj3 = uprofile.objects.all()
    obj4 = dprofile.objects.get(uname=request.session['sid'])
    obj2 = appointment.objects.filter(Did=obj4.Did)
    for x in obj2:
        for y in obj3:
            print(x.uid,'=',y.Uid)
    return render(request,'doctor/docviewappointments.html', {'apobj': obj2,'uobj':obj3})

def updatedisease(request):
    obj =  appointment.objects.get(id=request.POST.get('aid'))
    obj.med=request.POST.get('medicine')
    obj.dis=request.POST.get('disease')
    obj.save()
    return docviewappointment(request)




def disPredict(request):

    l1 = ['back_pain', 'constipation', 'abdominal_pain', 'diarrhoea', 'mild_fever', 'yellow_urine',
          'yellowing_of_eyes', 'acute_liver_failure', 'fluid_overload', 'swelling_of_stomach',
          'swelled_lymph_nodes', 'malaise', 'blurred_and_distorted_vision', 'phlegm', 'throat_irritation',
          'redness_of_eyes', 'sinus_pressure', 'runny_nose', 'congestion', 'chest_pain', 'weakness_in_limbs',
          'fast_heart_rate', 'pain_during_bowel_movements', 'pain_in_anal_region', 'bloody_stool',
          'irritation_in_anus', 'neck_pain', 'dizziness', 'cramps', 'bruising', 'obesity', 'swollen_legs',
          'swollen_blood_vessels', 'puffy_face_and_eyes', 'enlarged_thyroid', 'brittle_nails',
          'swollen_extremeties', 'excessive_hunger', 'extra_marital_contacts', 'drying_and_tingling_lips',
          'slurred_speech', 'knee_pain', 'hip_joint_pain', 'muscle_weakness', 'stiff_neck', 'swelling_joints',
          'movement_stiffness', 'spinning_movements', 'loss_of_balance', 'unsteadiness',
          'weakness_of_one_body_side', 'loss_of_smell', 'bladder_discomfort', 'foul_smell_of urine',
          'continuous_feel_of_urine', 'passage_of_gases', 'internal_itching', 'toxic_look_(typhos)',
          'depression', 'irritability', 'muscle_pain', 'altered_sensorium', 'red_spots_over_body', 'belly_pain',
          'abnormal_menstruation', 'dischromic _patches', 'watering_from_eyes', 'increased_appetite', 'polyuria',
          'family_history', 'mucoid_sputum',
          'rusty_sputum', 'lack_of_concentration', 'visual_disturbances', 'receiving_blood_transfusion',
          'receiving_unsterile_injections', 'coma', 'stomach_bleeding', 'distention_of_abdomen',
          'history_of_alcohol_consumption', 'fluid_overload', 'blood_in_sputum', 'prominent_veins_on_calf',
          'palpitations', 'painful_walking', 'pus_filled_pimples', 'blackheads', 'scurring', 'skin_peeling',
          'silver_like_dusting', 'small_dents_in_nails', 'inflammatory_nails', 'blister', 'red_sore_around_nose',
          'yellow_crust_ooze']
    # print("\ncount of L1==",len(l1))
    # List of Diseases is listed in list disease.

    disease = ['Fungal infection', 'Allergy', 'GERD', 'Chronic cholestasis', 
               'Peptic ulcer disease', 'Diabetes', 'Gastroenteritis', 'Bronchial Asthma', 'Hypertension',
               ' Migraine', 'Cervical spondylosis',
               'Paralysis (brain hemorrhage)', 'Jaundice', 'Malaria', 'Chicken pox', 'Dengue', 'Typhoid', 'hepatitis A',
               'Hepatitis B', 'Hepatitis C', 'Hepatitis D', 'Hepatitis E', 'Alcoholic hepatitis', 'Tuberculosis',
               'Common Cold', 'Pneumonia', 'Dimorphic hemmorhoids(piles)',
               'Heartattack', 'Varicoseveins', 'Hypothyroidism', 'Hyperthyroidism', 'Hypoglycemia', 'Osteoarthristis',
               'Arthritis', '(vertigo) Paroymsal  Positional Vertigo', 'Acne', 'Urinary tract infection', 'Psoriasis',
               'Impetigo']

    l2 = []
    for i in range(0, len(l1)):
        l2.append(0)
    # print("L2 are==\n", l2, "end of l2\n")

    # Reading the training .csv file
    df = pd.read_csv("media/training.csv")
    # Replace the values in the imported file by pandas by the inbuilt function replace in pandas.
    df.replace(
        {'prognosis': {'Fungal infection': 0, 'Allergy': 1, 'GERD': 2, 'Chronic cholestasis': 3, 'Drug Reaction': 4,
                       'Peptic ulcer diseae': 5, 'AIDS': 6, 'Diabetes ': 7, 'Gastroenteritis': 8, 'Bronchial Asthma': 9,
                       'Hypertension ': 10,
                       'Migraine': 11, 'Cervical spondylosis': 12,
                       'Paralysis (brain hemorrhage)': 13, 'Jaundice': 14, 'Malaria': 15, 'Chicken pox': 16,
                       'Dengue': 17, 'Typhoid': 18, 'hepatitis A': 19,
                       'Hepatitis B': 20, 'Hepatitis C': 21, 'Hepatitis D': 22, 'Hepatitis E': 23,
                       'Alcoholic hepatitis': 24, 'Tuberculosis': 25,
                       'Common Cold': 26, 'Pneumonia': 27, 'Dimorphic hemmorhoids(piles)': 28, 'Heart attack': 29,
                       'Varicose veins': 30, 'Hypothyroidism': 31,
                       'Hyperthyroidism': 32, 'Hypoglycemia': 33, 'Osteoarthristis': 34, 'Arthritis': 35,
                       '(vertigo) Paroymsal  Positional Vertigo': 36, 'Acne': 37, 'Urinary tract infection': 38,
                       'Psoriasis': 39,
                       'Impetigo': 40}}, inplace=True)

    # printing the top 5 rows of the training dataset
    df.head()
    X = df[l1]
    y = df[["prognosis"]]
    np.ravel(y)
    # print("\n X==\n", X, "\nend of x\n")
    # print("\nY==\n", y, "\nend of y\n")

    # Reading the  testing.csv file
    tr = pd.read_csv("media/testing.csv")

    # Using inbuilt function replace in pandas for replacing the values
    tr.replace(
        {'prognosis': {'Fungal infection': 0, 'Allergy': 1, 'GERD': 2, 'Chronic cholestasis': 3, 'Drug Reaction': 4,
                       'Peptic ulcer diseae': 5, 'AIDS': 6, 'Diabetes ': 7, 'Gastroenteritis': 8, 'Bronchial Asthma': 9,
                       'Hypertension ': 10,
                       'Migraine': 11, 'Cervical spondylosis': 12,
                       'Paralysis (brain hemorrhage)': 13, 'Jaundice': 14, 'Malaria': 15, 'Chicken pox': 16,
                       'Dengue': 17, 'Typhoid': 18, 'hepatitis A': 19,
                       'Hepatitis B': 20, 'Hepatitis C': 21, 'Hepatitis D': 22, 'Hepatitis E': 23,
                       'Alcoholic hepatitis': 24, 'Tuberculosis': 25,
                       'Common Cold': 26, 'Pneumonia': 27, 'Dimorphic hemmorhoids(piles)': 28, 'Heart attack': 29,
                       'Varicose veins': 30, 'Hypothyroidism': 31,
                       'Hyperthyroidism': 32, 'Hypoglycemia': 33, 'Osteoarthristis': 34, 'Arthritis': 35,
                       '(vertigo) Paroymsal  Positional Vertigo': 36, 'Acne': 37, 'Urinary tract infection': 38,
                       'Psoriasis': 39,
                       'Impetigo': 40}}, inplace=True)

    # printing the top 5 rows of the testing data
    tr.head()
    X_test = tr[l1]
    y_test = tr[["prognosis"]]
    np.ravel(y_test)
    # print("\n X_TEST==",X_test)
    # print("\n Y_TEST==",y_test,"\n ")
    global pred4
    print("Out knn,request.POST.get('sym1')=", request.POST.get('sym1'))

    def KNN():
        print("Entered to knn algorithm")

        if ((request.POST.get('sym1') == "Select Here") or (request.POST.get('sym2') == "Select Here")):
            return  HttpResponse( "Kindly Fill atleast first two Symptoms")
        #    if sym:
        #        KNN()
        else:

            from sklearn.neighbors import KNeighborsClassifier
            knn = KNeighborsClassifier(n_neighbors=5, metric='minkowski', p=2)
            knn = knn.fit(X, np.ravel(y))

            from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
            y_pred = knn.predict(X_test)
            print("KNN")
            print("Accuracy")
            print(accuracy_score(y_test, y_pred))
            print(accuracy_score(y_test, y_pred, normalize=False))
            print("Confusion matrix")
            conf_matrix = confusion_matrix(y_test, y_pred)
            print(conf_matrix)
            print("\n ###'Y_PRED===", y_pred, "\n endof y_pred\n")

            print("in knn,request.POST.get('sym1')=" ,request.POST.get('sym1'))


            print("sym1=" ,request.POST.get('sym1'))
            print("sym2=", request.POST.get('sym2'))
            print("sy3=", request.POST.get('sym3'))
            print("sym4=", request.POST.get('sym4'))
            print("sym5=", request.POST.get('sym5'))

            def replaceValue(s1):
                for a in l1:
                    avalue =a
                    if avalue.replace("_", " ").upper() == s1:
                        return avalue

            Symptom1 = replaceValue(request.POST.get('sym1'))
            Symptom2 = replaceValue(request.POST.get('sym2'))
            Symptom3 = replaceValue(request.POST.get('sym3'))
            Symptom4 = replaceValue(request.POST.get('sym4'))
            Symptom5 = replaceValue(request.POST.get('sym5'))


            print("symtom1=" ,Symptom1)
            print("symtom2=" ,Symptom2)
            print("symtom3=" ,Symptom3)
            print("symtom4=" ,Symptom4)
            print("symtom5=" ,Symptom5)

            # psymptoms = [request.POST.get('sym1'), request.POST.get('sym2'), request.POST.get('sym3'), request.POST.get('sym4'), request.POST.get('sym5')]
            # print("psymptoms=",psymptoms)
            # psymptoms = ["PUS FILLED PIMPLES", 'BLACKHEADS', 'SCURRING','Select Here', 'Select Here']
            psymptoms =[Symptom1 ,Symptom2 ,Symptom3 ,Symptom4 ,Symptom5]

            for k in range(0, len(l1)):
                for z in psymptoms:
                    if (z == l1[k]):
                        l2[k] = 1

            inputtest = [l2]
            predict = knn.predict(inputtest)
            predicted = predict[0]

            result = 'no'
            for a in range(0, len(disease)):
                if (predicted == a):
                    result = 'yes'
                    break

            if (result == 'yes'):

                pred4 =disease[a]
                print("pred4==", pred4)

            else:

                pred4 ="Not Found"
                print("pred4==", pred4)

        print("predicted result=" ,pred4)



        dict ={'Fungal infection': "Dermatology", 'Allergy': "General Medicine", 'GERD': "Gastrology",
              'Chronic cholestasis': "Gastrology", 'Drug Reaction': "General Medicine",
              'Peptic ulcer diseae': "Gastrology", 'AIDS': "General Medicine", 'Diabetes ': "General Medicine",
              'Gastroenteritis': "General Medicine", 'Bronchial Asthma': "General Medicine",
              'Hypertension ':  "General Medicine" ,'Migraine':  "General Medicine", 'Cervical spondylosis': "Orthopedic",
              'Paralysis (brain hemorrhage)' :"Neurology", 'Jaundice': "General Medicine", 'Malaria': "General Medicine",
              'Chicken pox': "General Medicine" ,'Dengue': "General Medicine", 'Typhoid': "General Medicine",
              'hepatitis A': "General Medicine" ,'Hepatitis B': "General Medicine", 'Hepatitis C': "General Medicine",
              'Hepatitis D': "General Medicine", 'Hepatitis E': "General Medicine",
              'Alcoholic hepatitis': "General Medicine", 'Tuberculosis': "General Medicine",
              'Common Cold': "General Medicine", 'Pneumonia': "General Medicine", 'Dimorphic hemmorhoids(piles)': "Gastrology",
              'Heart attack': "Cardiology" ,'Varicose veins': "Neurology", 'Hypothyroidism': "ENT",
              'Hyperthyroidism': "ENT", 'Hypoglycemia': "General Medicine", 'Osteoarthristis': "Orthopedic",
              'Arthritis': "Orthopedic" ,'(vertigo) Paroymsal  Positional Vertigo': "General Medicine",
              'Acne': "Dermatology", 'Urinary tract infection': "Urology",
              'Psoriasis': "Dermatology", 'Impetigo': "Dermatology"}

        print("department2=" ,dict.get(pred4))
        return searchDocX(request ,pred4 ,dict.get(pred4))



    pred4 =" "
    return KNN()
    print("final pred4=" ,pred4)
    return HttpResponse("predicted=" ,pred4)
    # return render(request,'predict.html',{'res':pred4 })









def searchDocX(request,dis,dept):
    dep1 = dprofile.objects.values("spc").distinct()
    list = []
    for x in dep1:
        list.append(x['spc'])


    dept=dept
    doc=dprofile.objects.filter(spc=dept,status='active')
    us=uprofile.objects.get(uname=request.session['sid'])
    op=optime.objects.all()
    days=opday.objects.all()
    return render(request,'user/usearch.html',{'data':doc,"disease":dis,'dept':dept,"med":checkMeddata(request),'uprofile':us,'optime':op,'days':days,'deprtlist':list })

def usearch(request):
    if request.method=='POST':

        a=request.POST.get('spc')   #get data from html form field
        obj=dprofile.objects.filter(spc=a,status='active') #filter from dprofile table where spc (table field)=a(value from html field)
        return render(request, 'user/usearch.html', {'data': obj})

    return render(request, 'user/usearch.html')


def docviewmedhis(request):
    obj1=uprofile.objects.get(Uid=request.POST.get('uid'))
    try:
        obj = medHistory.objects.get(uid=obj1.Uid)

    except:
        obj=None

    return render(request,'doctor/docviewmedhis.html',{'user1':obj})


def admviewmedhis(request):
    obj1=uprofile.objects.get(Uid=request.POST.get('uid'))
    try:
        obj = medHistory.objects.get(uid=obj1.Uid)

    except:
        obj=None

    return render(request,'admin/admviewmedhis.html',{'user1':obj})

def adminviewapp(request):
    obj=appointment.objects.all()
    obj1=uprofile.objects.all()
    obj2=dprofile.objects.all()
    return render(request,'admin/adminviewapp.html',{'apobj':obj,'uobj':obj1,'dobj':obj2})


def userhome(request):
    patient1 = uprofile.objects.get(uname=request.session['sid'])
    return render(request, 'user/userHome.html', {'obj': patient1, 'symlist': s2})

def forgot(request):
    if request.method=="POST":
        mail=request.POST.get('email')
        uname1=request.POST.get('uname')
        print("Method POST")

        try:
            if request.POST.get('utype') == "Admin":

                obj=Admin.objects.get(uname=uname1,email=mail)
                ustype="Admin"
            elif request.POST.get('utype') == "Dietitian":
                obj =dprofile.objects.get(uname=uname1, email=mail)
                ustype = "Dietitian"
            else:
                obj = uprofile.objects.get(uname=uname1, email=mail)
                ustype = "User"
                print('ustype=',ustype)
        except:
            return render(request, 'index.html', {'msg1': 2})


        if 'otpsend' in  request.POST:
            try:
                n = 4
                res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=n))
                subject = 'OTP to change Password'
                message = 'Your OTP is' + res
                recepient = str(mail)
                print("RECEPIENT", recepient)
                send_mail(subject,message,EMAIL_HOST_USER,[recepient],fail_silently=False,)
                print("Successfull")
                return render(request, 'forgot.html',{'otp': res, 'uname': uname1, 'mail': mail, 'utype': ustype, 'form': 2})
            except:
                return render(request, 'forgot.html',{'utype': ustype, 'uname': uname1, 'mail': mail, 'form': 1,
                                                       'msg': "OTP sending Unsuccessfull"})

        elif "confirmOTP" in request.POST:
            print("Confirm function")
            otp=request.POST.get('otp')
            print("OTP===",request.POST.get('otp'))
            if request.POST.get('uotp') == request.POST.get('otp'):
                return render(request,'forgot.html',{'otp':otp,'utype':ustype,'uname':uname1,'mail':mail,'form':3})
            else:
                return render(request,'forgot.html',{'otp':otp,'utype':ustype,'uname':uname1,'mail':mail,'form':2,'msg':"OTP Not Matched"})


        elif 'updatePWD' in request.POST:
            print("Update")
            obj.pwd=request.POST.get('newpwd')
            obj.save()
            return render(request,'index.html',{'msg1':1})

    return render(request,'forgot.html',{'form':1})





