from os import link
from django.shortcuts import render, redirect
from .models import School, Link
import uuid 


# Create your views here.
#function for School
# def index(request):
#     if request.method == 'POST':
#         school_name = request.POST['school']
#         school = School.objects.get(name=school_name)
#         return render(request, 'index.html', {'school': school})  

#     return render(request, 'index.html')  

#function for Link Shortener
def index(request):
    if request.method == 'POST':
        url = request.POST['link']
        unique_id = str(uuid.uuid4())[:5]

        new_url = Link(link=url, uuid=unique_id)
        new_url.save()
        return render(request, 'index.html', {'unique_id': unique_id})
    return render(request, 'index.html')

def return_url(request, pk):
    link_details = Link.objects.get(uuid=pk)
    link_url = link_details.url
    
    return redirect('https://'+link_url)