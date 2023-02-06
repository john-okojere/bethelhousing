from django.db import models
import uuid
from users.models import CustomUser

class Address(models.Model):
    image = models.ImageField(upload_to='location/%y/%m/%d/' , null=True)
    name = models.CharField(max_length=255)   
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    def __str__(self):
        return str(self.name+' '+self.city+ " " + self.state + ", "+ self.country)

class Uid(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    basicInfo = models.BooleanField(default=False)
    locationInfo = models.BooleanField(default=False)
    imageFile = models.BooleanField(default=False)
    detailedInfo = models.BooleanField(default=False)
    contactInfo = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.id)

class ApprovedUids(models.Model):
    property = models.OneToOneField(Uid, on_delete = models.CASCADE)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return str(self.property.id)

class BasicInfo(models.Model):
    property = models.OneToOneField(Uid, on_delete = models.CASCADE, related_name="basicinfo")
    title = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    price = models.IntegerField()
    area = models.IntegerField()
    bedroom = models.IntegerField()
    bathroom = models.IntegerField()
    def __str__(self):
        return str(self.property.id)

class LocationInfo(models.Model):
    property = models.OneToOneField(Uid, on_delete = models.CASCADE, related_name="locationinfo")
    address = models.ForeignKey(Address, on_delete = models.CASCADE, related_name='location_property')
    

    def __str__(self):
        return str(self.property.id)

class ImageFile(models.Model):
    property = models.ForeignKey(Uid, on_delete = models.CASCADE, related_name="imageinfo")
    upload = models.ImageField(upload_to='property/%y/%m/%d/')

    def __str__(self):
        return str(self.property.id)


class DetailedInfo(models.Model):
    property = models.OneToOneField(Uid, on_delete = models.CASCADE, related_name="detailinfo")
    description =  models.TextField()
    age =  models.CharField(max_length=25)
    garage =  models.IntegerField()
    Room =  models.IntegerField()
    airCondition =  models.BooleanField(default=False)
    Bedding =  models.BooleanField(default=False)
    Heating =  models.BooleanField(default=False)
    Internet =  models.BooleanField(default=False)
    Microwave =  models.BooleanField(default=False)
    SmokingAllow =  models.BooleanField(default=False)
    Terrace =  models.BooleanField(default=False)
    Balcony =  models.BooleanField(default=False)
    Icon =  models.BooleanField(default=False)
    Wi_Fi =  models.BooleanField(default=False)
    Beach =  models.BooleanField(default=False)
    Parking =  models.BooleanField(default=False)

    def __str__(self):
        return str(self.property.id)

class ContactInfo(models.Model):
    property = models.OneToOneField(Uid, on_delete = models.CASCADE, related_name="contactinfo")
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    gdpr = models.BooleanField(default=False)

    def __str__(self):
        return str(self.property.id)


class FiveReview(models.Model):
    property = models.OneToOneField(Uid, on_delete = models.CASCADE, related_name="fivereview")
    service = models.FloatField()
    value_of_money = models.FloatField()
    location = models.FloatField()
    cleanliness = models.FloatField()

    def total_review(self):
        sum = self.service + self.value_of_money + self.location + self.cleanliness
        total = sum/5 
        return total

    def __str__(self):
        return str(self.property)

class Comment(models.Model):
    property = models.ForeignKey(Uid, on_delete = models.CASCADE, related_name="comment")
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField( null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.property)

class CustomerCare(models.Model):
    property = models.ForeignKey(Uid, on_delete = models.CASCADE, related_name="customercare")
    user = models.ForeignKey(CustomUser, on_delete= models.CASCADE)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    description = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.property)
