from django.shortcuts import render
from login.models import Login
from django.http import HttpResponseRedirect
from user_reg.models import UserReg
from chat.models import Chat


def user_home(request):
    uid= request.session["uid"]
    obj=UserReg.objects.filter(user_id=uid)    #name

    objj = Chat.objects.filter(friend_id=uid)


    context={
        'chat':objj,
        'name':obj
    }
    return render(request, 'temp/user_home.html',context)

# Create your views here.
def admin_home(request):
    return render(request, 'temp/admin_home.html')

def login(request):
    if request.method == "POST":
        un = request.POST.get("email")
        ps = request.POST.get("pass")
        # print(ps)
        if Login.objects.filter(username=un, password=ps):
            obj = Login.objects.filter(username=un, password=ps)
            print(obj)
            tp = ""
            for l in obj:
                tp = l.type
                uid = l.user_id
                if tp == "admin":
                    request.session["uid"] = uid
                    return HttpResponseRedirect('/temp/admin_home/')
                elif tp == "user":
                    print("ii")
                    request.session["uid"] = uid
                    return HttpResponseRedirect('/temp/userhome/')
        else:
            obje = "Incorrect username or password!!!"
            context = {
                'inv': obje,
            }
            return render(request, 'temp/login_user.html', context)

    return render(request, 'temp/login_user.html')

