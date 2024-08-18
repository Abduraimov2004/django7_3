from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.urls import reverse


# Create your models here.

class User(AbstractUser):
    phone = models.CharField(max_length=13, blank=True, unique=True, db_index=True, null=True)
    auth_code = models.CharField(max_length=6, blank=True)

    # def get_absolute_url(self):
    #     print(self)
    #     return reverse("main:account", kwargs={"id": self.id})

    def __str__(self) -> str:
        return f"{self.username}"


class Category(models.Model):
    category = models.CharField(max_length=100, null=True)


class Tag(models.Model):
    title = models.CharField(max_length=100, null=True)


class Course(models.Model):
    LANGUAGES = (
        ("uz", "O'zbekcha"),
        ("ru", "Ruscha"),
        ("en", "Inglizcha")
    )
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    category = models.ForeignKey(Category, max_length=100, blank=True, null=True, on_delete=models.PROTECT)
    description = models.TextField(blank=True, null=True)
    duration = models.DurationField(blank=True, null=True)
    created_at = models.DateTimeField(verbose_name="Bo'shlanish vaqti", blank=True, null=True)
    update_at = models.DateTimeField(auto_now=True, )
    rating = models.PositiveIntegerField(null=True, default=0)
    price = models.DateTimeField(null=True)
    language = models.CharField(max_length=100, blank=True, choices=LANGUAGES)
    image = models.ImageField(upload_to="images", blank=True)
    tags = models.ManyToManyField(Tag, verbose_name="tags")



class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.subject}'
