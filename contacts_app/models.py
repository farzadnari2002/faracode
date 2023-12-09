from django.db import models


class Contact(models.Model):
    post_address = models.TextField(max_length=150)
    city = models.CharField(max_length=30)
    number = models.CharField(max_length=20)
    email = models.EmailField(null=True, blank=True)
    instagram = models.CharField(max_length=200)
    telegram = models.CharField(max_length=200)
    whatsapp = models.CharField(max_length=200)

    def __str__(self):
        return "Contacts"


class Massage(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    subject = models.CharField(max_length=60)
    body = models.TextField(max_length=300)

    def __str__(self):
        return f"{self.name} - {self.subject}"
