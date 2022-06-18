import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.
USER_ROLE = (
    ('Nutritionist', 'Nutritionist'),
    ('Patient', 'Patient')
)

USER_STATUS = (
    ('Approved', 'Approved'),
    ('Declined', 'Declined'),
    ('Pending', 'Pending'),
)

class AccountManager(BaseUserManager):
    def create_user(self, email, password, role, first_name, last_name, phone_number):

        if not email:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have a password")

        user = self.model(
            email=self.normalize_email(email),
            password=password,
            role=role,
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password, role, first_name, last_name, phone_number):

        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            role=role,
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number
        )

        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.status = True

        user.save(using=self._db)
        return user

# class for data storage
class Account(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, null=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=11)
    email = models.EmailField(max_length=50, unique=True)
    role = models.CharField(choices=USER_ROLE, max_length=50)
    profile_pic = models.ImageField(default="undraw_profile.svg", null=True, blank=True, upload_to="img/profile")
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(auto_now=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password', 'role', 'first_name', 'last_name', 'phone_number']

    # class for creation
    objects = AccountManager()