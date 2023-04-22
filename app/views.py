from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.models import *


def Topic_insert(request):
    if request.method=="POST":
        a=request.POST['topic']
        TO=Topic.objects.get_or_create(Topic_name=a)[0]
        TO.save()
        return HttpResponse('Date Inserted Suceesfully')
    return render(request,"Topic_insert.html")


def webpage_insert(request):
    T=Topic.objects.all()
    d={'TO':T}
    if request.method=='POST':
        a=request.POST['a']
        b=request.POST['b']
        c=request.POST['c']
        d=request.POST['d']
        TO=Topic.objects.get(Topic_name=a)
        TO.save()
        WO=Webpage.objects.get_or_create(Topic_name=TO,Name=b,Url=c,Email=d)[0]
        WO.save()
        return HttpResponse("Data Inserted successfully")
    return render(request,"webpage_insert.html",d)


def Access_insert(request):
    WO=Webpage.objects.all()
    d={'AR':WO}
    if request.method=="POST":
        a=request.POST['a']
        b=request.POST['b']
        c=request.POST['c']
        AA=Webpage.objects.get(Name=a)
        AA.save()
        ARR=AccessRecords.objects.get_or_create(Name=AA,Autho=b,Date=c)[0]
        ARR.save()
        return HttpResponse('Data Insertd succeefully')
    return render(request,'Access_insert.html',d)



def Webpage_retrieve(request):
    W=Topic.objects.all()
    d={'R':W}
    if request.method=="POST":
        aa=request.POST.getlist('a')
        wq=Webpage.objects.none()
        for i in aa:
            wq=wq|Webpage.objects.filter(Topic_name=i)
            d1={'dd':wq}
            return render(request,'Display_webpage.html',d1)
    return render(request,'Webpage_retrieve.html',d)
            

def checkbox(request):
    D=Topic.objects.all()
    d={'c':D}
    return render(request,'Checkbox.html',d)

def Radio(request):
    D=Topic.objects.all()
    d={'c':D}
    return render(request,'Radio.html',d)


def access_display(request):
    WO=Webpage.objects.all()
    d={'ARR':WO}
    if request.method=='POST':
        AA=request.POST.getlist('a')
        AR=AccessRecords.objects.none()
        for i in AA:
            AR=AR|AccessRecords.objects.filter(Name=i)
            d1={'AR':AR}
            return render(request,'access_display.html',d1)
    return render(request,'acess_retrive.html',d)


































# def update_Topic(request):
#     TO=Topic.objects.all()
#     d={'topics':TO}
#     if request.method=='POST':
#         tn=request.POST.getlist('topic')
#         new=request.POST['new']
#         for i in tn:
#             Topic.objects.filter(Topic_name=i).update(Topic_name=new)
#             d1={'DD':Topic.objects.all()}
#             return render(request,'update.html',d1)
#     return render(request,'Display_topic.html',d)