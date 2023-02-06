from django.shortcuts import get_object_or_404,render,redirect
from django.views.generic import TemplateView
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from .models import  Uid, Address, ApprovedUids, CustomerCare, ImageFile, BasicInfo, LocationInfo, DetailedInfo, ContactInfo, FiveReview, Comment
from .forms import BasicForm, DetailedForm, ContactForm 
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def home(request):
    property = ApprovedUids.objects.all()
    uids = []
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

def address(request):
    return render(request, 'home/address.html')

def address_info(request, pk):
    address = get_object_or_404(Address, pk = pk)
    uids = []
    property = ApprovedUids.objects.filter(property__locationinfo__address = address)
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
    return render(request, 'home/addressinfo.html', {'uids': main, 'location':address})

def detail(request, uid):
    uid = Uid.objects.get(id=uid)
    comments = Comment.objects.filter(property=uid)
    property = ApprovedUids.objects.all().exclude(property=uid)
    others_uids = []
    for property in property:
        properties = Uid.objects.get(id=property.property.id)
        others_uids.append(properties)
    return render(request, 'property/single-property-2.html', {'uid': uid,'others':others_uids, 'comments':comments})


@login_required
def SubmitProperty(request):
    if request.user.is_staff:
        uid = Uid.objects.create()
        print(uid)
        return render(request, "property/submit-property.html",{'uid':uid})
    else:
        return redirect('/')

def delete_property_and_go_home(request, uid):
    uid = get_object_or_404(Uid, id=uid)
    uid.delete()
    return redirect('homepage')

def delete_property_and_add_another(request, uid):
    uid = get_object_or_404(Uid, id=uid)
    uid.delete()
    return redirect('submit')

def fivestarreview(request, uid):
    uid = get_object_or_404(Uid, id=uid)
    if request.method == "POST":
        service = request.POST.get('service')
        value_of_money = request.POST.get('value_of_money')
        location = request.POST.get('location')
        cleanliness = request.POST.get('cleanliness')
        
        FiveReview.objects.create(property=uid, service=service,value_of_money=value_of_money, location=location, cleanliness=cleanliness)
        return HttpResponse('')
    return JsonResponse({'post':'false'})

def approve_property_and_go_home (request, uid):
    uid = get_object_or_404(Uid, id=uid)
    property = ApprovedUids.objects.create(property=uid,approved=True)
    property.save()
    return redirect('homepage')


def approve_property_and_add_again(request, uid):
    uid = get_object_or_404(Uid, id=uid)
    property = ApprovedUids.objects.create(property=uid,approved=True)
    property.save()
    return redirect('submit')

def file_upload_view(request,uid):
    property = uid,
    uid = get_object_or_404(Uid, id=uid)
    print(request.FILES)
    if request.method == "POST":
        my_file = request.FILES.get('file')
        ImageFile.objects.create(property=uid,upload=my_file)
        uid.imageFile = True
        print( 'imageFile is ' +str(uid.imageFile))
        uid.save()
        return HttpResponse('')
    return JsonResponse({'post':'false'})


def SubmitBasicInfo(request,uid):
    uid = get_object_or_404(Uid, id=uid)
    property = uid
    if request.method == "POST":
        basic = BasicInfo.objects.create( property = uid, title = request.POST.get('title'), status = request.POST.get('status'), type = request.POST.get('type'), price = request.POST.get('price'), area = request.POST.get('area'), bedroom = request.POST.get('bedroom'), bathroom = request.POST.get('bathroom'))
        uid.basicInfo = True
        print( 'basicInfo is ' +str(uid.basicInfo))
        uid.save()
        data = {
            'property_uid' : property.id,
        }
        print(data)
        return JsonResponse(data)
    return JsonResponse({'post':'false'})

def SubmitLocationInfo(request,uid):
    uid = get_object_or_404(Uid, id=uid)
    value =  request.POST.get('address')
    address = get_object_or_404(Address, id=value)
    print(address)
    property = uid
    if request.method == "POST":
        basic = LocationInfo.objects.create(property = uid,address =address)
        uid.locationInfo = True
        print( 'locationInfo  is '+str(uid.locationInfo))
        uid.save()
        data = {
            'property_uid' : property.id,
        }
        print(data)
        return JsonResponse(data)
    return JsonResponse({'post':'false'})

def SubmitDetailedInfo(request,uid):
    uid = get_object_or_404(Uid, id=uid)
    property = uid
    if request.method == "POST":
        D_form = DetailedForm(request.POST)
        if D_form.is_valid():
            d_C = D_form.save(commit=False)
            d_C.property = property
            D_form.save()
        uid.detailedInfo = True
        print( 'detailedInfo  is '+str(uid.detailedInfo))
        uid.save()
        data = {
            'property_uid': property.id,
        }
        print(data)
        return JsonResponse(data)
    return JsonResponse({'post':'false'})

def SubmitContactInfo(request,uid):
    uid = get_object_or_404(Uid, id=uid)
    property = uid
    if request.method == "POST":
        C_form = ContactForm(request.POST)
        if C_form.is_valid():
            d_C = C_form.save(commit=False)
            d_C.property = property
            C_form.save()
        uid.contactInfo = True
        print( 'contactInfo is '+str(uid.contactInfo))
        uid.save()
        data = {
            'property_uid' : property.id,
        }
        print(data)
        return JsonResponse(data)
    return JsonResponse({'post':'false'})

def addcomment(request, uid):
    property = get_object_or_404(Uid, id=uid)
    if request.method == "POST":
        Comment.objects.create(
            property = property,
            name = request.POST.get('name'),
            email = request.POST.get('email'),
            message = request.POST.get('message')
        )
        data = {
            'property_uid' : property.id,
        }
        return JsonResponse(data)
    return JsonResponse({'post':'false'})

@login_required
def MessageCustomerCare(request, uid):
    property = get_object_or_404(Uid, id=uid)
    if request.method == "POST":
        CustomerCare.objects.create(
            property = property,
            user=request.user,
            email = request.POST.get('email'),
            phone = request.POST.get('phone'),
            description = request.POST.get('description')
        )
        data = {
            'property_uid' : property.id,
        }
        return JsonResponse(data)
    return JsonResponse({'post':'false'})
