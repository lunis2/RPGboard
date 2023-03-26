from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor_uploader.fields import RichTextUploadingField


class UserModel(AbstractUser):
    pass


class Postmodel(models.Model):
    CAT = (('tanks', 'Tanks'),
           ('healers', 'Heals'),
           ('dd', 'Damage Dealers'),
           ('vendors', 'Vendors'),
           ('guildmasters', 'Guildmasters'),
           ('quest_givers', 'Quest Givers'),
           ('blacksmiths', 'Blacksmiths'),
           ('leatherworkers', 'Leatherworkers'),
           ('potion_makers', 'Potion makers'),
           ('spell_masters', 'Spell masters'))

    user_id = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    category = models.CharField(max_length=20, choices=CAT, default='dd', verbose_name='Category')
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=128)
    content = RichTextUploadingField()

    def __str__(self):
        return f'{self.title.title()}'


class CommentModel(models.Model):
    user_id = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    post = models.ForeignKey(Postmodel, on_delete=models.CASCADE)
    is_confirmed = models.BooleanField(default=False)
