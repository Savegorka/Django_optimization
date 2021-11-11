from django.db import models
from django.contrib.auth.models import AbstractUser
<<<<<<< Updated upstream
=======
from django.utils.timezone import now
from django.dispatch import receiver
from django.db.models.signals import post_save
>>>>>>> Stashed changes


class ShopUser(AbstractUser):
    avatar = models.ImageField(upload_to='users_avatars', blank=True)
<<<<<<< Updated upstream
    age = models.PositiveIntegerField(verbose_name='возраст')
=======
    age = models.PositiveIntegerField(verbose_name='возраст', default=18)

    activation_key = models.CharField(max_length=128, blank=True)

    def is_activation_key_expired(self):
        return now() - self.date_joined > timedelta(hours=48)


class ShopUserProfile(models.Model):
    MALE = "M"
    FEMALE = "W"

    GENDER_CHOICES = (
        (MALE, 'M'),
        (FEMALE, 'Ж')
    )

    user = models.OneToOneField(
        ShopUser,
        unique=True,
        null=False,
        db_index=True,
        on_delete=models.CASCADE
    )

    tagline = models.CharField(verbose_name='тэги', max_length=128, blank=True)

    about_me = models.TextField(verbose_name='о себе', blank=True)

    gender = models.CharField(verbose_name='пол', max_length=1, choices=GENDER_CHOICES, blank=True)

    @receiver(post_save, sender=ShopUser)
    def save_user_profile(sender, instance, **kwargs):
        instance.shopuserprofile.save()

    @receiver(post_save, sender=ShopUser)
    def save_user_profile(sender, instance, created, **kwargs):
        if created:
            ShopUserProfile.objects.create(user=instance )
>>>>>>> Stashed changes
