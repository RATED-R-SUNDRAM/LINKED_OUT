from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth  import authenticate,  login, logout
from django.contrib import messages
from django.db.models import Q
from .models import Post,userDetails
# Create your views here.
def home(request):
    if request.user.is_authenticated:
        usr = userDetails.objects.all().filter(~Q(username=request.user))
        post=Post.objects.all()
        dic={'usr':usr,'post':post}
        
        return render(request,'home/index.html',dic)
    else:
        return render(request,'home.html')

def handleSignUp(request):
    if request.method=="POST":
        # Get the post parameters
        username=request.POST['username']
        email=request.POST['email']
        pass1=request.POST['password']
        fname=request.POST['fname']
        lname=request.POST['lname']
        try:
            user= User.objects.get(username=username)

            messages.error(request, "Username already exists")
            return redirect('home')
        except User.DoesNotExist:
            try:
                user= User.objects.get(email=email)

                messages.error(request, "email already exists")
                return redirect('home')
            except User.DoesNotExist:
                myuser = User.objects.create_user(username, email, pass1)

        myuser.first_name= fname
        myuser.last_name= lname
        myuser.save()
        return redirect('/')

    else:
        return HttpResponse("404 - Not found")

def handeLogin(request):
    if request.method=="POST":
        # Get the post parameters
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']

        user=authenticate(username= loginusername, password= loginpassword)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("/")

    return HttpResponse("404- Not found")


def handelLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('home')
def loginPage(request):
    return render(request, 'login.html') 

def myprofile(request):
    if request.user.is_authenticated:
        try:
            obj=userDetails.objects.get(username=request.user)
            dic={'user':obj}
        except userDetails.DoesNotExist:
            obj=User.objects.get(username=request.user)
            dic={'user':obj}   
        return render(request,'home/myprofile.html',dic)
    else:
        return redirect('/')          

def makepost(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            user=request.user
            content=request.POST['message']
            mypost=Post(user=user,content=content)
            mypost.save()
        
        return redirect('/')
    else:
        return render(request,'home.html')         

def update(request):
    if request.method=="POST":
        username=request.user
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.user.email
        institute=request.POST['insti']
        experience=request.POST['exp']
        location=request.POST['place'] 
        pPhoto=request.FILES['myfile'] 
        status=request.POST['check']
        phone=request.POST['pno']
        links=request.POST['link']
        slug=str(username)
        myuser=userDetails(username=username,fname=fname,lname=lname,email=email,institute=institute,experience=experience,location=location,pPhoto=pPhoto,status=status,phone=phone,links=links,slug=slug)
        try:
            user= userDetails.objects.get(username=request.user)
            user.delete()
            myuser.save()
        except userDetails.DoesNotExist:
            myuser.save()
    return redirect('/')    

def profile(request,username):
    if request.user.is_authenticated:
        obj=userDetails.objects.get(slug=username)
        
        dic={'user':obj}
        return render(request,'home/profile.html',dic)
    else:
        return redirect('/') 

