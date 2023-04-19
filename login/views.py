from django.shortcuts import render
from login.models import Login
from user_reg.models import UserReg
from login.models import Login
from django.http import HttpResponseRedirect
from django.core.mail import send_mail

# Create your views here.

def login(request):
    if request.method == "POST":
        uname = request.POST.get("username")
        passw = request.POST.get("password")
        obj = Login.objects.filter(username=uname, password=passw)
        tp = ""
        for ob in obj:
            tp = ob.type
            uid = ob.user_id
            if tp == "admin":
                request.session["uid"] = uid
                return HttpResponseRedirect('/temp/admin_home/')
            elif tp == "user":
                request.session["uid"] = uid
                return HttpResponseRedirect('/temp/userhome/')
            objlist = "Username or Password incorrect... Please try again...!"
            context = {
                'msg': objlist,
            }
            return render(request, 'login/login.html', context)
    return render(request, 'login/login.html')

def forgot_password(request):
    em=request.POST.get('email')
    if request.method=="POST":
        if UserReg.objects.filter(email=em).exists():
            obj=UserReg.objects.get(email=em)
            obj.email=request.POST.get('email')
            obj.password=request.POST.get('conpass')
            obj.save()

            obb=Login.objects.get(username=em)
            obb.username=request.POST.get('email')
            obb.password=request.POST.get('conpass')
            obb.save()
            return HttpResponseRedirect('/temp/login/')
        else:
            msg="Invalid Username"
            context={
                'inv':msg
            }
            return render(request,'login/forgot_password.html',context)
    return render(request,'login/forgot_password.html')