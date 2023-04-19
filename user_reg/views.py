from django.shortcuts import render
from user_reg.models import UserReg
from login.models import Login
from chat.models import Chat
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse,HttpResponseRedirect

# from user_reg.models import UserRegCreate your views here.
def user_reg(request):
    if request.method == "POST":
        obj=UserReg()
        obj.username=request.POST.get('username')
        obj.gender = request.POST.get('gender')
        obj.dob = request.POST.get('dob')
        obj.phno = request.POST.get('phno')
        obj.email = request.POST.get('email')
        obj.password = request.POST.get('password')
        obj.status="pending"

        myfile = request.FILES["photo"]
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        obj.profile_photo = myfile.name


        obj.save()

        ob =Login()
        ob.username=request.POST.get('email')
        ob.password=request.POST.get('password')
        ob.type="user pending"
        ob.user_id=obj.user_id
        ob.save()



    return render(request,'user_reg/user_reg.html')

def manage_user(request):
    ob=UserReg.objects.filter(status='pending')
    context={
        'objval':ob,
    }
    return render(request,"user_reg/manage_user.html",context)
def view_blocked_user(request):
    obj=UserReg.objects.filter(status='approved')
    context={
        'objval':obj,
    }
    return render(request,"user_reg/view_blocked_user.html",context)

def blckuser(request,idd):
    obj=UserReg.objects.get(user_id=idd)
    obj.status='blocked'
    obj.save()

    objj = Login.objects.get(user_id=idd)
    objj.type = 'user pending'
    objj.save()


    return view_blocked_user(request)


def admin_view_user(request):
    obj=UserReg.objects.filter(status='approved')
    user_details = {
        'user': obj
    }


    return render(request,'user_reg/admin_view_user.html',user_details)



def approve_user(request,abc):
    obj=UserReg.objects.get(user_id=abc)
    obj.status="approved"
    obj.save()

    ob=Login.objects.get(user_id=abc, type = 'user pending')
    ob.type="user"
    ob.save()
    # return render(request,'user_reg/manage_user.html')
    # return HttpResponse("yesss")
    return HttpResponseRedirect("/user_reg/manage_user/")
def reject_user(request,cdf):
    obj = UserReg.objects.get(user_id=cdf)
    obj.status = "rejected"
    obj.save()
    return render(request,'user_reg/manage_user.html')

def edit_profile(request):
    uid = request.session["uid"]
    objj = UserReg.objects.filter(user_id=uid) #name
    gm = Chat.objects.filter(friend_id=uid)

    context = {
        'name': objj,
        'chat': gm
    }
    if request.method == "POST":
        obj = UserReg.objects.get(user_id=uid)
        myfile = request.FILES["profile"]
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        obj.profile_photo = myfile.name

        # obj.profile_photo = request.POST.get('profile_photo')
        obj.save()

        ob = Login.objects.get(type="user", user_id=uid)
        ob= request.POST.get('user_id')
        # ob.save()
    return render(request,'user_reg/edit_profile.html',context)


def edit_username(request):
    uid = request.session["uid"]
    objj = UserReg.objects.filter(user_id=uid)  # name
    gm = Chat.objects.filter(friend_id=uid)
    context = {
        'name': objj,
        'chat':gm
    }
    if request.method == "POST":
        obj = UserReg.objects.get(user_id=uid)
        obj.username= request.POST.get('username')
        obj.save()

        # ob = Login.objects.get(type="user", user_id=uid)
        # ob.user_id = request.POST.get('user_id')
        # ob.save()
    return render(request,'user_reg/edit_username.html',context)
def edit_email(request):
    uid = request.session["uid"]
    objj = UserReg.objects.filter(user_id=uid)  # name
    gm = Chat.objects.filter(friend_id=uid)
    context = {
        'name': objj,
        'chat':gm
    }
    if request.method == "POST":
        obj = UserReg.objects.get(user_id=uid)
        obj.email = request.POST.get('email')
        obj.save()

        ob = Login.objects.get(type="user", user_id=uid)
        ob.username = request.POST.get('email')
        ob.save()
    return render(request,'user_reg/edit_email.html',context)

def edit_password(request):
    uid=request.session["uid"]
    objj = UserReg.objects.filter(user_id=uid)  # name
    gm = Chat.objects.filter(friend_id=uid)
    context = {
        'name': objj,
        'chat':gm
    }
    if request.method == "POST":
        obj=UserReg.objects.get(user_id=uid)
        obj.password=request.POST.get('password')
        obj.save()

        ob=Login.objects.get(type="user",user_id=uid)
        ob.password=request.POST.get('password')
        ob.save()
    return render(request,'user_reg/edit_password.html',context)
def edit_phno(request):
    uid=request.session["uid"]
    objj = UserReg.objects.filter(user_id=uid)  # name
    gm = Chat.objects.filter(friend_id=uid)
    context = {
        'name': objj,
        'chat':gm
    }
    if request.method == "POST":
        obj=UserReg.objects.get(user_id=uid)
        obj.phno=request.POST.get('phno')
        obj.save()

        # ob=Login.objects.get(type="user",user_id=uid)
        # ob.=request.POST.get('password')
        # ob.save()
    return render(request,'user_reg/edit_phno.html',context)

def admin_view_blocked_users(request):
    uid = request.session["uid"]
    objj = UserReg.objects.filter(user_id=uid)  # name

    obj = UserReg.objects.filter(status='blocked')

    blk = {
        'bl': obj,
        'name': objj,
    }


    return render(request, 'user_reg/admin_view_blocked_users.html',blk)


def unblock(request,aa):
    # uid = request.session["uid"]
    # objj = UserReg.objects.filter(user_id=uid)  # name

    obj = UserReg.objects.get(user_id=aa)
    obj.status = 'approved'
    obj.save()

    objj = Login.objects.get(user_id=aa)
    objj.type = 'user'
    objj.save()



    # unbl={
    #     'name':objj
    # }

    # return render(request,'user_reg/admin_view_blocked_users.html',unbl)


    return admin_view_blocked_users(request)








