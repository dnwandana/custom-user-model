from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)


class UserManager(BaseUserManager):
    def create_user(
        self, email, username, first_name, last_name, password=None
    ):
        """
        Creates and saves a User with the given email, username,
        first name, last name and password.
        """
        if not email:
            raise ValueError(_('User must have an email address!'))
        if not username:
            raise ValueError(_('User must have an username!'))
        if not first_name:
            raise ValueError(_('User must have a first name!'))
        if not last_name:
            raise ValueError(_('User must have a last name!'))

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(
        self, email, username, first_name, last_name, password
    ):
        """
        Creates and saves a superuser with the given email, username,
        first name, last name and password.
        """
        user = self.create_user(
            email,
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        _('email address'),
        max_length=60,
        unique=True
    )

    username = models.CharField(
        _('username'),
        max_length=20,
        unique=True,
        null=False
    )

    # password field supplied by AbstractBaseUser
    # last_login field supplied by AbstractBaseUser

    first_name = models.CharField(
        _('first name'),
        max_length=30,
        null=False
    )

    last_name = models.CharField(
        _('last name'),
        max_length=30,
        null=False
    )

    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )

    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_(
            'Designates whether the user can log into this admin site.'
        ),
    )

    # is_superuser field provided by PermissionsMixin
    # groups field provided by PermissionsMixin
    # user_permissions field provided by PermissionsMixin

    date_joined = models.DateTimeField(
        _('date joined'),
        auto_now_add=True
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def get_full_name(self):
        """
        Return the first_name and the last_name.
        """
        return '{} {}'.format(self.first_name, self.last_name)

    def __str__(self):
        return '{} <{}>'.format(self.get_full_name(), self.email)

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
