from django.shortcuts import render
from django.db.models import Q
from property.models import  Uid, ApprovedUids, CustomerCare, ImageFile, BasicInfo, LocationInfo, DetailedInfo, ContactInfo, FiveReview, Comment
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def property_search(request):
    types = request.POST.get("type")
    name = request.POST.get("name")
    print(types)
    print(name)
    uids = []
    property = ApprovedUids.objects.filter(
        Q(property__basicinfo__status__icontains ="" if types is None else types) &
    
        Q(property__locationinfo__address__id__icontains = "" if name is None else name) 
    )
    for property in property:
        properties = Uid.objects.get(id=property.property.id)
        uids.append(properties)
    page = request.GET.get('page', 1)
    listj = Paginator(uids, 6)
    try:
        main = listj.page(page)
    except PageNotAnInteger:
        main = listj.page(1)
    except EmptyPage:
        main = listj.page(listj.num_pages)
    return render(request, 'property/index.html', {'uids': main})   


def home_property_search(request):
    address = request.POST.get("name")
    minPrice = request.POST.get("minPrice")
    maxPrice = request.POST.get("maxPrice")
    types = request.POST.get("type")
    bedroom = request.POST.get("bedrooms")
    status = request.POST.get("status")
    
    uids = []
    property = ApprovedUids.objects.filter(
        Q(property__basicinfo__status__icontains ="" if status is None else status) &
        Q(property__basicinfo__bedroom__icontains ="" if bedroom is None else bedroom) |
        Q(property__basicinfo__type__icontains ="" if types is None else types) |
        Q(property__locationinfo__address__id__icontains = "" if address is None else address) 
    )
    for property in property:
        properties = Uid.objects.get(id=property.property.id)
        uids.append(properties)
    page = request.GET.get('page', 1)
    listj = Paginator(uids, 6)
    try:
        main = listj.page(page)
    except PageNotAnInteger:
        main = listj.page(1)
    except EmptyPage:
        main = listj.page(listj.num_pages)
    return render(request, 'property/index.html', {'uids': main})   