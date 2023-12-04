"""disprediction URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from . import settings
from .app2 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('home/', views.index),
    path('index2/', views.index2),
    path('dprof/',views.registration),
    path('uprof/',views.user_registration),
    path('viewuprof/',views.viewuprofile),
    path('adminbase/',views.adminbase),
    path('doctorbase/',views.doctorbase),
    path('userbase/', views.userbase),
    path('login/',views.login),
    path('logout/',views.logout),
    path('viewdoctors/',views.viewdoctors),
    path('viewpatients/',views.viewpatients),
    path('viewuser/',views.viewuser),
    path('docManage/',views.manageDoc),
    path('viewblocked/',views.viewblockeddoctors),
    path('newdoctorreg/',views.newdoctorreg),
    path('docviewprofile/',views.doc_viewprofile),
    path('admviewmedhis/',views.admviewmedhis),
    path('dmailupdt/',views.dMail),
    path('dphnupdt/',views.dPhone),
    path('daddupdt/',views.dAdd),
    path('dqualupdt/',views.qualUpdate),
    path('dpwdupdt/',views.pwdUpdate),
    path('addupdt/',views.addUpdate),
    path('mailupdt/',views.mailUpdate),
    path('phoneupdt/',views.phoneUpdate),
    path('mailUpdate/', views.dMail),
    path('phoneUpdate/', views.dPhone),
    path('qualUpdate/', views.qualUpdate),
    path('addUpdate/', views.dAdd),
    path('daysUpdate/', views.daysUpdate),
    path('dpwdUpdate/', views.dPwd),
    path('uprofile/',views.myprofile),
    path('userPwdUpdate/',views.uPwd),
    path('userAddUpdate/',views.uAdd),
    path('userMailUpdate/',views.uMail),
    path('userPhoneUpdate/',views.uPhone),
    path('viewMedHistory/',views.viewMedHistory),
    path('addMedHistory/',views.addMedHistory),
    path('updateMedication/',views.updateMedication),
    path('updateallergy/',views.updateallergy),
    path('addMeddb/',views.addMeddb),
    path('usearch/',views.usearch),
    path('appointment/',views.userappointment),
    path('fixappointment/',views.fixappointment),
    path('myappointment_details/',views.myappointment_details),
    path('userviewappointment/',views.userviewappointment),
    path('docviewappointment/',views.docviewappointment),
    path('updatedisease/',views.updatedisease),
    path('predictionDisease/',views.disPredict),
    path('docviewmedhis/',views.docviewmedhis),
    path('adminviewapp/',views.adminviewapp),
    path('userhome/',views.userhome),
    path('forgot/',views.forgot)






]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
