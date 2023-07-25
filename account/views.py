from django.shortcuts import render
from django.http import HttpResponse
from . models import Person
# Create your views here.

def regis(request):
    
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        city = request.POST.get('city')
        country = request.POST.get('country')
        password = request.POST.get('password')

        # Save the form data to the database
        user = Person.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            gender=gender,
            city=city,
            country=country,
            password=password
        )
        return HttpResponse('success')
            
    return render(request, 'account/register.html')

