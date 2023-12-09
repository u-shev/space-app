from django.db import models
from space_app.users.models import User


'''Standart post model, connected to author, file can be added'''


class Post(models.Model):
    name = models.CharField(max_length=150, blank=False,
                            verbose_name='Name')
    description = models.TextField(blank=True,
                                   verbose_name='Description')
    author = models.ForeignKey(User, on_delete=models.PROTECT,
                               blank=False, related_name='authors',
                               verbose_name='Author')
    date_created = models.DateTimeField(auto_now_add=True,
                                        verbose_name='Creation date')
    picture = models.FileField(upload_to='upload/pictures/',
                               verbose_name='Upload picture')
    view_count = models.IntegerField(verbose_name="View Count", default=0)

    def __str__(self):
        return '"%s" by %s' % (self.title, self.author)

    def delete(self, *args, **kwargs):
        self.picture.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
