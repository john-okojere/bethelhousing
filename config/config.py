from users.models import CustomUser
from property.models import Address
from django.db.models import Count

def usersProfile(request):
    address = Address.objects.annotate(
        property=Count('location_property'))    
    
    if request.user.is_staff:
        chatusers = CustomUser.objects.all().exclude(username=request.user.username )
    else:
        chatusers = CustomUser.objects.filter(is_staff=True).exclude(username=request.user.username )
    return {
        'chatusers': chatusers,
        'location_address' : address,
        }