from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_field):
        if not email:
            raise ValueError('iltimos email manzilingizni kiriting')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_field)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('superuser da is_staff True bo`lishi kerak')

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('superuser da is_superuser True qiymati bo`lishi kerak')

        return self._create_user(email, password, **extra_fields)
