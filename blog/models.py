from django.db import models

# Create your models here.
from django.contrib.auth.models import User



class Post(models.Model):
    """
    test Post for b blog app
    """
    title = models.CharField(max_length=63)
    slug = models.SlugField(null=True)
    text = models.TextField(null=True)
    pub_date = models.DateField(null=True)
    # create_by = models.ForeignKey()
    image = models.FileField(null=True)


    def __str__(self):
        return self.title



    def like_count(self):
        return 5

# class PostUser(User):
#     mobile_number