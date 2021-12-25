from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db.models import Q
from .models import Post, UserDetails


def home(request):
    """Displays home page for user

    Context
        `UserDetails`
            An instance of :model:`home.UserDetails`


    Templates
        For authenticated users: :template:`home/index.html`
        For anonymous users: :template:`home.html`
    """
    if request.user.is_authenticated:
        usr = UserDetails.objects.all().filter(~Q(username=request.user))
        post = Post.objects.all()
        dic = {"usr": usr, "post": post}

        return render(request, "home/index.html", dic)
    else:
        return render(request, "home.html")


def handleSignUp(request):
    """Handles user signup.

    Args:
        request: Contains username, email, password,
        fname(first name), lname(last name)

    Redirects to `/home` if email or username already exists and
    `/` for unique username and email
    """
    if request.method == "POST":
        # Get the post parameters
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        try:
            user = User.objects.get(username=username)

            messages.error(request, "Username already exists")
            return redirect("home")
        except User.DoesNotExist:
            try:
                user = User.objects.get(email=email)

                messages.error(request, "email already exists")
                return redirect("home")
            except User.DoesNotExist:
                myuser = User.objects.create_user(username, email, password)

        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        return redirect("/")

    else:
        return HttpResponse("404 - Not found")


def handeLogin(request):
    """Handles login for users.

    Args:
        request: Contains loginusername and loginpassword

    Redirects to `/` for valid username and password else
    returns HTTPResponse(404)
    """
    if request.method == "POST":
        # Get the post parameters
        loginusername = request.POST["loginusername"]
        loginpassword = request.POST["loginpassword"]

        user = authenticate(username=loginusername, password=loginpassword)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("/")

    return HttpResponse("404- Not found")


def handelLogout(request):
    """Handles logout for user. Redirects to `/home`"""
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect("home")


def loginPage(request):
    """Shows login page

    Templates:
        :template:`login.html`
    """
    return render(request, "login.html")


def myprofile(request):
    """Shows user profile for authenticated user else
    redirects `/` for anonymous user
    """
    if request.user.is_authenticated:
        try:
            obj = UserDetails.objects.get(username=request.user)
            dic = {"user": obj}
        except UserDetails.DoesNotExist:
            obj = User.objects.get(username=request.user)
            dic = {"user": obj}
        return render(request, "home/myprofile.html", dic)
    else:
        return redirect("/")


def makepost(request):
    """Inserts user post to DB

    Args:
        request: Contains post content and it's author(user)

    For authenticated user: redirects to `/`
    For anonymous user: redirects to `/home`
    """
    if request.user.is_authenticated:
        if request.method == "POST":
            user = request.user
            content = request.POST["message"]
            mypost = Post(user=user, content=content)
            mypost.save()

        return redirect("/")
    else:
        return render(request, "home.html")


def update(request):
    """Updates user profile

    Args:
        request: Contains user's first name, last name,
        email, institute, experience, location, photo, status,
        status, phone, links, slug(username)

    Redirects to `/`
    """
    if request.method == "POST":
        username = request.user
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        email = request.user.email
        institute = request.POST["insti"]
        experience = request.POST["exp"]
        location = request.POST["place"]
        pPhoto = request.FILES["myfile"]
        status = request.POST["check"]
        phone = request.POST["pno"]
        links = request.POST["link"]
        slug = str(username)
        myuser = UserDetails(
            username=username,
            fname=fname,
            lname=lname,
            email=email,
            institute=institute,
            experience=experience,
            location=location,
            pPhoto=pPhoto,
            status=status,
            phone=phone,
            links=links,
            slug=slug,
        )
        try:
            user = UserDetails.objects.get(username=request.user)
            user.delete()
            myuser.save()
        except UserDetails.DoesNotExist:
            myuser.save()
    return redirect("/")


def profile(request, username):
    """Shows profile page for autneticated users

    Args:
        request: Contains username

    For authenticated user: Redirects to /profile
    For anonymous user: Redirects to /
    """
    if request.user.is_authenticated:
        obj = UserDetails.objects.get(slug=username)

        dic = {"user": obj}
        return render(request, "home/profile.html", dic)
    else:
        return redirect("/")
