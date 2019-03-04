from django.db import models
import datetime as dt

# Create your models here.


class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return self.first_name

    class Meta:
        ordering = ['first_name']

    def save_user(self):
        self.save()


class tags(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Location(models.Model):
    nairobi = models.CharField(max_length=30)
    thika = models.CharField(max_length=30)
    mombasa = models.CharField(max_length=30)
    nakuru = models.CharField(max_length=30)
    naivasha = models.CharField(max_length=30)


class Category(models.Model):
    food = models.CharField(max_length=30)
    travel = models.CharField(max_length=30)
    party = models.CharField(max_length=30)
    memes = models.CharField(max_length=30)
    architecture = models.CharField(max_length=30)


class Pics(models.Model):
    title = models.CharField(max_length=60)
    post = models.TextField()
    location = models.ForeignKey(Location)
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(tags)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    @classmethod
    def todays_pics(cls):
        today = dt.date.today()
        pics = cls.objects.filter(pub_date__date = today)
        return pics

    @classmethod
    def days_pics(cls,date):
        pics = cls.objects.filter(pub_date__date = date)
        return pics
