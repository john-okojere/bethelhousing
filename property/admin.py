from django.contrib import admin
from .models import Uid,Address, CustomerCare, FiveReview, Comment,ApprovedUids, ImageFile, BasicInfo, DetailedInfo, ContactInfo, LocationInfo


@admin.register(Address)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'city', 'state', 'country')


@admin.register(Uid)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'basicInfo', 'locationInfo', 'imageFile', 'detailedInfo', 'contactInfo', 'date_added')


@admin.register(ApprovedUids)
class UserAdmin(admin.ModelAdmin):
    list_display = ('property', 'approved')


admin.site.register(ImageFile)
admin.site.register(BasicInfo)
admin.site.register(LocationInfo)
admin.site.register(DetailedInfo)
admin.site.register(FiveReview)
admin.site.register(ContactInfo)
admin.site.register(Comment)
admin.site.register(CustomerCare)