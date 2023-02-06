from django.shortcuts import render
from property.models import ApprovedUids, Uid

def home(request):
    property = ApprovedUids.objects.all()
    uids = []
    for property in property:
        properties = Uid.objects.get(id=property.property.id)
        uids.append(properties)
    print(uids)
    return render(request, 'home/index.html', {'uids': uids})

def about(request):
    return render(request, 'home/about-us.html')

def contact(request):
    return render(request, 'home/contact.html')

def faq(request):
    return render(request, 'home/faq.html')