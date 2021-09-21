from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import project, contact
# Create your views here.
def index(request):
    project_data = project.objects.all()
    return render(request,'port/index.html',{'project':project_data})

def project_view(request, id):
    project_data = project.objects.filter(id=id)
    return render(request,'port/projects.html',{'project_data':project_data})

def contact_us(request):
    check = 'abcdefghijklmnopqrstuvwxyz'
    condition = True
    if request.method =='POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        query = request.POST['query']
        project_data = project.objects.all()
        for i in phone:
            if i in check:
                condition = False
        
        if len(name)<15 and len(email)<30 and len(phone)<12 and condition==True :
            contact_data = contact(name=name, email=email, phone=int(phone), address=address, query=query)
            contact_data.save()
            correct = True
            return render(request,'port/index.html',{'correct':correct,'project':project_data})
        else:
            incorrect = True
            return render(request,'port/index.html',{'incorrect':incorrect,'project':project_data})
    