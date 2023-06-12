from django.shortcuts import render , redirect
from course_app.models import Course
# Create your views here.
def home(request):
    courses=Course.objects.all()
 
    return render(request, 'main_app/home.html',{'courses':courses})

def about(request):
   return render(request,'core/about.html')
def course(request):
    #Add
    if request.method=='GET':
     return render(request,'main_app/course.html')
    else:
       title=request.POST['title']
       desc=request.POST['desc']
       price=request.POST['price']
       duration=request.POST['duration']

          #course=Course(title=title,description=desc,price=price,duration=duration)
          #course.save()
#creating an object 
       Course.objects.create(title=title,description=desc,price=price,duration=duration)
       return redirect('home')
    

def delete(request,id):
   c=Course.objects.get(id=id)
   c.delete()
   return redirect('home')

def delete_all(request):
   c=Course.objects.all()
   c.delete()
   return redirect('home')  

def edit(request,id):
   course=Course.objects.get(id=id)
   if request.method=='GET':
    return render(request,'main_app/edit.html',{'course':course}) 
   
   else:
     
      course.title=request.POST['title']
      course.description=request.POST['desc']
      course.price=request.POST['price']
      course.duration=request.POST['duration']

      course.save()

      return redirect('home')


