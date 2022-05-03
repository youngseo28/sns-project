from django.shortcuts import render

# Create your views here.
def showmain(request):
    return render(request, 'main/mainpage.html')

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