from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.validators import RegexValidator
from .manager import CustomUserManager

ACCOUNT_TYPE=(
    ('As a Customer','As a Customer'),
    ('As a Agent','As a Agent'),
    ('As a Agency','As a Agency'),
    ('As a Staff','As a Staff'),
)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator()
    username = models.CharField(
        verbose_name='username',
        max_length=150,
        unique=True,
        help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.',
        validators=[username_validator],
        error_messages={
            'unique': "A user with that username already exists.",
        },
    )
    fullName = models.CharField(max_length=255)
    phone_regex = RegexValidator(regex=r'^\+\d{8,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone = models.CharField(
        validators=[phone_regex],
        max_length=16,
        unique=True,
        help_text="Phone number must be entered in the format: '+999999999'.",
        error_messages={
            'unique': "This Phone has been used already",
        },
        ) # validators should be a list
    email = models.EmailField(verbose_name='email address', unique=True,
        error_messages={
            'unique': "This email has been used already",
        },
    )
    accountType = models.CharField(max_length= 20, choices=ACCOUNT_TYPE)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_customer = models.BooleanField(default=False)
    is_agent = models.BooleanField(default=False)
    is_agency = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    update_fields = models.DateTimeField(auto_now=True)

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['phone','email']


    objects = CustomUserManager()
    
    
    def save(self,force_insert=True,using='dataset'):
        super().save(force_insert)

    def save(self, *args, **kwargs):
        if self.accountType == "As a Customer":
            self.is_customer = True
        elif self.accountType == "As a Agent":
            self.is_agent = True
        elif self.accountType == "As a Agency":
            self.is_agency = True
        elif self.is_staff == True:
            self.accountType = "As a Staff"
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.username


class Account(models.Model):
    profile = models.OneToOneField(CustomUser, on_delete=models.CASCADE, verbose_name='profile')
    yourTitle = models.CharField(max_length=255)
    address = models.TextField()
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=244)
    zipcode = models.CharField(max_length=20)
    about = models.TextField()
    #Socials
    facebook = models.TextField()
    twitter = models.TextField()
    googlePlus = models.TextField()
    linkedIn = models.TextField()

    def __str__(self):
        return self.profile.username