from django import http
from django.http import response
from django.http.response import HttpResponse
from django.shortcuts import render,HttpResponse,redirect
from blogs.models import Post,Blogcomments

def bloghome(request):
   allposts=Post.objects.all()
   #print(allposts)
   context={'allposts':allposts}
   # return HttpResponse("this is Blog home .We will keep all the blogs here ")
   return render(request,'blog/bloghome.html',context)
# Create your views here.
def blogPost(request,slug):
   post=Post.objects.filter(slug=slug).first()
   comments=Blogcomments.objects.filter(post=post)
   context={'post':post ,'comments':comments}
   return render(request,'blog/blogpost.html',context)


def createblog(request):
   if request.method=="POST":
        title=request.POST['title']
        author=request.POST['name']
        content=request.POST['content']
        slug=title[0:len(title)]
        Posti=Post(title=title,author=author,content=content,slug=slug)
        #print(name_value,email,phone,content)
        Posti.save()
   return render(request,'blog/createblog.html')
   #return HttpResponse("Here you can create your blogs")

def userblogs(request):
   if request.user.is_authenticated:
      username = request.user.username
   post=Post.objects.filter(author=username).all()
   context={'allposts':post}
   return render(request,'blog/userblogs.html',context)
   #return HttpResponse('We! Will display your blogs here')


def postcomment(request):
   if request.method=="POST":
      comment=request.POST.get("comment")
      user=request.user
      postSno=request.POST.get("postSno")
      post=Post.objects.get(sno=postSno)
      comment=Blogcomments(comment=comment,user=user,post=post)
      comment.save()
   return redirect(f"/blog/{post.slug}")