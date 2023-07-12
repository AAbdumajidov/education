from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe


def image_path(instance, filename):
    return f"{instance.user.username}/{filename}"


class Profile(models.Model):
    ROLE = {
        (0, 'Student'),
        (1, 'Teacher'),
    }
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=image_path)
    bio = models.TextField()
    role = models.IntegerField(choices=ROLE, default=1)

    def __str__(self):
        return self.user.username


    def image_tag(self):
        if self.image:
            return mark_safe(f'<a href="{self.image.url}"><img src="{self.image.url}" style="height:30px;"/></a>')
        else:
            return '-'

def user_post_save(instance, sender, created, *args, **kwargs):
    if created:
        Profile.objects.create(user_id=instance.id)


post_save.connect(user_post_save, sender=User)
