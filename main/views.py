from django.shortcuts import render,redirect,get_object_or_404
from .models import Post
from django.utils import timezone

# Create your views here.
def showmain(request):
    blogs = Post.objects.all()
    return render(request, 'main/mainpage.html',{'blogs':blogs})

# firstpage view 함수
def showfirst(request):
    return render(request, 'main/firstpage.html')

# secondpage view 함수
def showsecond(request):
    return render(request, 'main/secondpage.html')

# thirdpage view 함수
def showthird(request):
    return render(request, 'main/thirdpage.html')

# fourthpage view 함수
def showfourth(request):
    return render(request, 'main/fourthpage.html')

def detail(request,id):
    blog = get_object_or_404(Post, pk = id)
    return render(request,'main/detail.html',{'blog':blog})

def new(request):
    return render(request, 'main/new.html')

def create(request):
    new_blog = Post()
    new_blog.title = request.POST['title']
    new_blog.writer = request.POST['writer']
    new_blog.pub_date = timezone.now()
    new_blog.body = request.POST['body']
    new_blog.save()
    return redirect('detail',new_blog.id)