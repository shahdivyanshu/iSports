from django.db.models import query
from django.http.response import HttpResponse
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from home.models  import Contact
from django.contrib.auth import authenticate,login,logout
from blogs.models import Post


def home(request):
    #return HttpResponse('This is the home page')
    posts=Post.objects.filter(title="Cricket Rules").all()
    context={'allposts':posts}
    return render(request,'home/home.html',context)

def contacts(request):
    #return HttpResponse('This is the contacts page')
    if request.method=="POST":
        name_value=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        content=request.POST['content']
        print(name_value,email,phone,content)
        Cont=Contact(name=name_value,phone=phone,email=email,content=content)
        Cont.save()
        #print("We are using post request")
    return render(request,'home/contacts.html')

def about(request):
    #return HttpResponse('This is the about page')
    return render(request,'home/about.html')

# Create your views here.
def Handlesignup(request):
    if request.method=="POST":
        #get parameters
        Username=request.POST['Username']
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        Email=request.POST['email']
        Password1=request.POST['pass']
        exampleInputPassword=request.POST['confirmpass']
        #verify for user
        #create a user
        myuser=User.objects.create_user(Username,Email,Password1)
        myuser.first_name=firstname
        myuser.last_name=lastname
        myuser.save()
        user=authenticate(username=Username, password=Password1)
        login(request,user)
        return redirect("/")
        #return HttpResponse("Congrats Account created")

    else:
        return HttpResponse("User Not found")

def Handlelogin(request):
        logiusername=request.POST['logiusername']
        loginpassword=request.POST['loginpassword']
        user=authenticate(username=logiusername,password=loginpassword)
        if user is not None:
            login(request,user)
            return redirect('/')
           # return HttpResponse("Succesfully logged in")
            
        else:
            return HttpResponse("Try Again wrong password ")
    
def Handlelogout(request):
        logout(request)
        return redirect('/')
        #return HttpResponse("you have successfully logged out")


def search(request):
    search=request.GET['search']
    allposts=Post.objects.filter(title__icontains=search)
    param={'allposts':allposts}
    return render (request,'home/search.html',param)
   # return HttpResponse('this is search')
