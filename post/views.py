from django.shortcuts import render,redirect,HttpResponse,get_object_or_404
from django.contrib.auth.models import User
from .models import post,Like,messageModel
from django.contrib.auth.decorators import login_required
from django.db.models import Q

def index(request):
    id = request.user.id
    usersobj = User.objects.get(pk=id)
    postobj = post.objects.all()
    if request.method == "POST":
        hastag = request.POST.get("hastag")
        content = request.POST.get("content")
        posttt = post(title = hastag,description=content)
        posttt.user = usersobj 
        posttt.save()
        return render(request,'index.html',{'posts':postobj,'users':usersobj,'id':id})

    return render(request,'index.html',{'posts':postobj,'users':usersobj,'id':id})

@login_required
def delete(request,id): 
    postobj = post.objects.get(id=id)
    if request.user == postobj.user :
         postobj.delete()
    return redirect('index')
    
@login_required
def edit(request,id):
    postobj = post.objects.get(id=id)
    if request.method == "POST" and request.user == postobj.user :
        postob = post.objects.get(id=id)
        hastag = request.POST.get("hastag")
        content = request.POST.get("content")
        postob.update(title=hastag,description=content)
    return redirect('index')

def liked(request,id):
    user = request.user
    if request.method == "POST":
        postob = post.objects.get(id=id)

        if user in postob.liked.all():
            postob.liked.remove(user)
        else:
            postob.liked.add(user)
        
        new_like,created=Like.objects.get_or_create(user=user,post_id=id)

        if not created:
            if Like.value == 'Like':
                Like.value == 'Unlike'
            else :
                Like.value == 'Like'
        new_like.save()

    return redirect('index')

def users(request):
    id = request.user.id
    usersobj = User.objects.exclude(pk=id)
    context = {'users':usersobj}
    return render(request, 'users.html',context)

def message(request,id):
    fromUserid = request.user.id
    fromUser = User.objects.get(id=fromUserid)
    toUser = User.objects.get(id=id)
    if request.method == "POST":
        messagee = request.POST.get('message')
        mesg = messageModel(message = messagee)
        mesg.userfrom = fromUser
        mesg.userto= toUser 
        mesg.save()

    mesgobj = messageModel.objects.filter((Q(userfrom=fromUser)&Q(userto=toUser))|(Q(userfrom=toUser)&Q(userto=fromUser)))
    context = {'from':fromUser,'to':toUser,'msg':mesgobj}
    return render(request,'message.html',context)