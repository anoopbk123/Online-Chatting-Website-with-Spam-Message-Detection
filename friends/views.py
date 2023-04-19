from django.shortcuts import render
from friends.models import Friends
from django.http import HttpResponseRedirect,HttpResponse
from user_reg.models import UserReg
from chat.models import Chat
from django.db import connection
from django.db.models import Q
from reported_comments.models import ReportedComments

# Create your views here.
def search_friends(request):
    uid = request.session["uid"]
    objj = UserReg.objects.filter(user_id=uid)   #name
    gm = Chat.objects.filter(friend_id=uid)
    context={
        'name':objj,
        'chat':gm
    }
    if request.method=="POST":
        search_friend=request.POST.get('search')
        request.session['name']=search_friend
        # return search_result(request)
        # return HttpResponseRedirect('/friends/search_result/')
        obj=UserReg.objects.filter(username__icontains=search_friend,status='approved')
        print(obj)
        searchf={
            'search':obj,
            'name':objj
        }
        return render(request,'friends/search_friends.html',searchf)
    return render(request,'friends/search_friends.html',context)

def search_send_request(request,df):
    fid=UserReg.objects.get(user_id=df)
    print(df)
    uid = request.session["uid"]
    objj = UserReg.objects.filter(user_id=uid)  # name
    context={
        'name':objj
    }
    if Friends.objects.filter(f_user_id=uid,user_id=fid.user_id).exists():
        pass
    else:
        ob=Friends()
        ob.user_id=uid
        ob.f_user_id=df
        ob.request_status="requested"
        ob.save()
        return HttpResponseRedirect('/friends/search_friends/')

    return render(request,'friends/search_friends.html',context)

def send_friend_request(request):
    uid = request.session["uid"]
    objj = UserReg.objects.filter(user_id=uid)  # name
    ff=Friends.objects.filter(f_user_id=uid).values_list('user_id',flat=True)
    rr=Friends.objects.filter(user_id=uid).values_list('f_user_id',flat=True)
    # fff=ff+str(uid)
    print(rr)
    print(ff)
    obj = UserReg.objects.filter(status='approved').exclude(user_id__in=ff).exclude(user_id=uid).exclude(user_id__in=rr)
    gm = Chat.objects.filter(friend_id=uid)
    request_friends = {
        'friends': obj,
        'name':objj,
        'chat':gm
    }

    return render(request,'friends/send_friend_request.html',request_friends)

def send_request(request,abc):
    uid = request.session["uid"]
    if Friends.objects.filter(user_id=uid,f_user_id=abc).exists():
        pass
    else:
        obj = Friends()
        obj.user_id = uid
        obj.f_user_id = abc
        obj.request_status = "requested"
        obj.save()
    return HttpResponseRedirect('/friends/send_friend_request/')

    # if Friends.objects.filter(Q(user_id=uid,f_user_id=abc) | Q(user_id=abc,f_user_id=uid)).exists():
    #     pass
    #     return HttpResponseRedirect('/friends/send_friend_request/')
    #
    # else:
    #     objj = UserReg.objects.filter(user_id=uid)  # name
    #     obj=Friends()
    #     obj.user_id=uid
    #     obj.f_user_id=abc
    #     obj.request_status="requested"
    #     obj.save()


def manage_friend_request(request):
    # obj = Friends.objects.all()
    uid = request.session["uid"]
    objj = UserReg.objects.filter(user_id=uid)  # name
    obj = Friends()
    gm = Chat.objects.filter(friend_id=uid)
    # obj.user_id = uid
    # obj.request_status = "requested"
    # obj.save()
    obj=Friends.objects.filter(request_status='requested',f_user_id=uid)
    manage_friend = {
        'friend': obj,
        'name':objj,
        'chat':gm
    }


    return render(request,'friends/manage_friend_request.html',manage_friend)

def accept_friend(request,abc):
    uid = request.session["uid"]
    obj=Friends.objects.get(friend_id=abc)
    obj.request_status="accepted"
    obj.save()

    ob=Friends()
    ob.f_user_id=obj.user_id
    ob.user_id=uid
    ob.request_status="accepted"
    ob.save()
    # return manage_friend_request(request)
    return HttpResponseRedirect('/friends/manage_friend_request/')
    # return render(request,'friends/manage_friend_request.html')


def reject_friend(request,cdf):
    obj=Friends.objects.get(friend_id=cdf)
    obj.request_status="rejected"
    obj.save()

    return manage_friend_request(request)


def view_friends_list(request):
    # obj = Friends.objects.all()
    uid = request.session["uid"]
    print(uid)
    objj = UserReg.objects.filter(user_id=uid)  # name

    cd=UserReg.objects.filter(status='cyberbullying detected').values_list('user_id',flat=True)
    print(cd)

    obj=Friends.objects.filter(user_id=uid,request_status='accepted').exclude(f_user_id__in=cd)
    print(obj)

    gm = Chat.objects.filter(friend_id=uid)

    # objlist = connection.cursor()
    # objlist.execute("SELECT * FROM user_reg,friends WHERE user_reg.user_id=friends.user_id AND user_reg.status='approved' AND friends.user_id=%s",[uid])

    friends = {
        'friend': obj,
        'name':objj,
        'chat':gm,
        # 'images': o
        # bjlist.fetchall()

    }


    return render(request,'friends/view_friends_list.html',friends)



def chat_with_friends(request):
    return render(request,'friends/chat_with_friends.html')



def search_result(request):
    uid = request.session["uid"]
    objj = UserReg.objects.filter(user_id=uid)  # name
    # gm = Chat.objects.filter(user_id=uid).exclude(friend_id=uid)
    ff=request.session['name']
    al=Friends.objects.filter(f_user_id=uid).values_list('user_id',flat=True)
    print(al)
    # ff=Friends.objects.filter(f_user_id=uid).values_list('user_id',flat=True)
    context={
        'name':objj,

    }
    if UserReg.objects.filter(username__icontains=ff,status='approved').exclude(user_id=uid).exclude(user_id__in=al):

        obj=UserReg.objects.filter(username__icontains=ff,status='approved').exclude(user_id=uid).exclude(user_id__in=al)
        print(obj)
        gm = Chat.objects.filter(friend_id=uid)
        searchf={
            'search':obj,
            'name':objj,
            'chat':gm
        }
    # return render(request,'friends/search_friends.html',searchf)
        return render(request,'friends/search_result.html',searchf)
    return render(request,'friends/search_result.html',context)

def already_friend(request):


      return render(request,'friends/already_friend.html')

def view_blocked_friends(request):
    uid = request.session["uid"]
    objj = UserReg.objects.filter(user_id=uid)  # name
    print(objj)
    # obj = UserReg.objects.filter(status="approved")

    objlist = connection.cursor()
    # objlist.execute( "SELECT * FROM user_reg,reported_comments WHERE user_reg.user_id=%s AND reported_comments.user_id=user_reg.user_id",[uid])
    objlist.execute("SELECT user_reg.*,reported_comments.*,friends.* FROM friends INNER JOIN reported_comments on friends.f_user_id=reported_comments.user_id INNER JOIN user_reg on user_reg.user_id=reported_comments.user_id WHERE friends.request_status='accepted' and friends.user_id=%s",[uid])
    gm = Chat.objects.filter(friend_id=uid)

    fr=Friends.objects.filter(user_id=uid).values_list('f_user_id',flat=True)
    print(fr)

    ob = UserReg.objects.filter(user_id__in=fr,status='blocked').values_list('user_id',flat=True)
    print(ob)
    # obj = ReportedComments.objects.all()

    blocked = {
        # 'block': obj,
         'bl':ob,
        'name':objj,
        'images': objlist.fetchall(),
        'chat':gm
    }
    return render(request,'friends/view_blocked_friends.html',blocked)


# def block_your_friends(request):
#     # obj = Friends.objects.all()
#     uid = request.session["uid"]
#     # print(uid)
#     objj = UserReg.objects.filter(user_id=uid)  # name
#
#     bfr = UserReg.objects.filter(status='blocked').values_list('user_id', flat=True)
#     print(bfr)
#     obj = Friends.objects.filter(
#         Q(request_status='accepted', user_id=uid) | Q(request_status='accepted', friend_id=uid)).exclude(
#         f_user_id__in=bfr)
#     print(obj)
#     gm = Chat.objects.filter(user_id=uid).exclude(friend_id=uid)
#
#     # objlist = connection.cursor()
#     # objlist.execute("SELECT * FROM user_reg,friends WHERE user_reg.user_id=friends.user_id AND user_reg.status='approved' AND friends.user_id=%s",[uid])
#
#     friends = {
#         'friend': obj,
#         'name': objj,
#         'chat': gm,
#         # 'images': objlist.fetchall()
#
#     }
#
#     return render(request, 'friends/block_your_friends.html', friends)
#
#
#
# def view_block_your_friends(request):
#     uid = request.session["uid"]
#     objj = UserReg.objects.filter(user_id=uid)  # name








