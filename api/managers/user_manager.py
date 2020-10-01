from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    def _create_user(self, email, username, password, **extra_details):
        """
        Creates and saves a User with the given email and password
        """

        if not email:
            raise ValueError('The given email must be set')

        if username is None:
            raise ValueError('Name cannot be empty')

        email = self.normalize_email(email)
        user  = self.model(email=email, username=username, **extra_details)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, username, password=None, **extra_details):
        """
        Creates and saves a user with the given email, password
        """

        extra_details.setdefault('is_superuser', False)
        return self._create_user(email, username, password, **extra_details)

    def create_superuser(self, email, username, password, **extra_details):
        """
        Creates and saves a user with the given email, password
        """

        extra_details.setdefault('is_superuser', True)

        if extra_details.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')

        return self._create_user(email, username, password, **extra_details)
