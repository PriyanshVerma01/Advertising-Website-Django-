from django.shortcuts import render
from django.http import HttpResponse
from wdapp.models import ContactInfo
from django.contrib import messages
from django.core.mail import send_mail
def LandingPage(request):
    s="<h1> Hello Welcom To Web Devlopment & Graphic Design</h1>"
    return HttpResponse(s)
'''def ContactInformation(request):
    l="<p>Vipin 96958622</p>"
    l+="<p>Priyansh 4641212313</p>"
    return HttpResponse(l)'''
def EwbDevlopment(request):
    res=render(request,'WdHome.html',{'link1':'typography', 'HomePage':'wd','link3':'contact'})
    return res
def Typography(request):
    res=render(request,'typography.html',{'link2':'post-single'})
    return res
def PostSingle(request):
    res=render(request,'post-single.html')
    return res
def Contact(request):
    if request.method=="POST":
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        content = request.POST['content']
        print(name,phone,email,content)

        #sending mail by Django server
        send_mail(
            name,
            content,
            email,
            ['priyanshverma9@gmail.com'],
            fail_silently=False,
        )

        if len(name)<2 or len(phone)<10 or len(email)<3 or len(content)<4:
            messages.error(request,"Please fill the Form Correctly")

        else:
            contact = ContactInfo(name=name, phone=phone, email=email, content=content)
            contact.save()
            messages.success(request,"Your message has been successfully sent")

    res=render(request,'contact.html',{'HomePage':'wd'})
    return res
# Create your views here.
