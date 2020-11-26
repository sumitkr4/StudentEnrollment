from django.shortcuts import render
from enrollment.models import Classroom,Student
from django.contrib.auth.models import User,auth
from django.core.mail import send_mail
from django.conf import settings

def index(request):
    classess = Classroom.objects.all()
    mydict={'classes':classess}
    return render(request,'enrollment/home.html',mydict)

def registration(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        # import pdb
        # pdb.set_trace()
        # classes=request.POST.get('class')
        password=request.POST.get('password')
        user= User.objects.create_user(username=name,password=password,email=email)
        user.save()
        s=Student.objects.create(user=user)
        s.classroom.add(request.POST.get('detail_id'))
        send_mail(
            'Successful Registration mail',
            'Hi you have successfully registered for class',
            settings.EMAIL_HOST_USER,
            [email,],
            fail_silently=False,
        )
        return render(request,'enrollment/enrolledclass.html',context={'enrolled_class':s.classroom.all()})
    else:
        # print(request.GET['detail_id'])
        return render(request,'enrollment/register.html',{'detail_id':request.GET['detail_id']})

def classRoomDetail(request,pk):
    detail=Classroom.objects.get(id=pk)
    return render(request,'enrollment/details.html',{'detail':detail})