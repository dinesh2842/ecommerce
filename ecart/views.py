from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.contrib import messages
from ecart.forms import CustomUserCreation
from django.contrib.auth import authenticate,login as auth_login,logout

#This functions returns the home page
def home(request):
    return render(request,'ecart/index.html')

#This function returns the collections page
def collections(request):
    category = Category.objects.filter(status=0)
    context={'category':category}
    return render(request,'ecart/collections.html',context)

#this function returns all the collections in our database
def collectionsview(request,slug):
    if(Category.objects.filter(slug=slug ,status=0)):
        products = Product.objects.filter(category__slug=slug)
        category= Category.objects.filter(slug=slug).first()
        context = {'products':products,'category':category}
        return render(request,'ecart/products/index.html',context)
    else:
        messages.warning(request,"No Such Category Was found")
        return redirect('collections')

#this function returns the details of the particular product
def productview(request,cate_slug,prod_slug):
    if(Category.objects.filter(slug=cate_slug,status=0)):
        if(Product.objects.filter(slug=prod_slug,status=0)):
            products = Product.objects.filter(slug=prod_slug,status=0).first
            context= {'products': products}
        else:
            messages.error(request,"No Such Product Found ")
            return redirect('collections')
    else:
        messages.error(request,"No Such Category Found")
        return redirect('collections')
    return render(request,'ecart/products/view.html',context)
            
#This function is used to register a new user
def register(request):
    form = CustomUserCreation()
    if request.method == 'POST':
        form = CustomUserCreation(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Registered Successfully! please Login to Continue")
            return redirect('login')
    context= {'form':form}
    return render(request,'ecart/auth/register.html',context)

#This function is used to login the user who has registered in our shoping page
def user_login(request):
    if request.user.is_authenticated:
        messages.warning(request,'you are already logged in ')
        return redirect('home')
    else:
        if request.method == 'POST':
            name = request.POST['username']
            passw = request.POST['password']
            user = authenticate(request,username=name,password=passw)
            if user is not None:
                auth_login(request,user)
                messages.success(request,"Logged in Successfully")
                return redirect('collections')
            else:
                messages.error(request,"Invalid Username or Password")
                return redirect('login')
            
        return render(request,'ecart/auth/login.html')
    
#This function is used to logout
def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"logged out successfully")
    return redirect('home')