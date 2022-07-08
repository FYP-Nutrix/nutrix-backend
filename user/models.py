import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.
class AccountManager(BaseUserManager):
    def create_user(self, email, password, first_name, last_name, phone_number):

        if not email:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have a password")

        user = self.model(
            email=self.normalize_email(email),
            password=password,
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password, first_name, last_name, phone_number):

        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number
        )

        # admin power
        user.is_superuser = True
        user.is_staff = True

        # nutrionist power
        user.is_nutritionist = False

        # patient power
        user.is_patient = False
        
        user.is_active = True
        user.status = True

        user.save(using=self._db)
        return user

# class for data storage
# is patient : to identify the user is a patient
# is nutritionist : to identify the user is a nutrition
# is staff and is super user are admin and able to access django admin
class Account(AbstractBaseUser, PermissionsMixin):
    user_id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, null=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=11)
    email = models.EmailField(max_length=50, unique=True)
    profile_pic = models.ImageField(default="img/undraw_profile.svg", null=True, blank=True, upload_to="img/profile")
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(auto_now=True)
    is_staff = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=False)
    is_nutritionist = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password', 'first_name', 'last_name', 'phone_number']

    # class for creation
    objects = AccountManager()

class MealSetting(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, null=False)
    account = models.OneToOneField(Account, on_delete=models.CASCADE)
    daily_calories = models.DecimalField(max_digits=7, decimal_places=3, null=True)
