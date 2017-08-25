from django.db import models

from django.utils import timezone
#nfjkbdvjksvdjhjhd

# Create your models here.\
# this is how u make class in django. CLASS take variables
class Post(models.Model):
    author= models.ForeignKey('auth.user')
    title= models.CharField(max_length=9000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)
    text= models.TextField()
    created_date= models.DateTimeField(
        default=timezone.now)
    published_date= models.DateTimeField(
        blank=True, null=True)

    def publish(self):
#the spacing of publish into post thingy means specific to this class and can only be used for posts
#making a class is makig a template and every time use class, use template. if use self, use template of 1 thing itself, but not everything
        self.published_date= timezone.now()
        self.save()
    def __str__(self):
        #__str__ is a special python function
        return self.title
