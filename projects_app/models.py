from django.db import models


class project(models.Model):
    title = models.CharField(max_length=25)
    description = models.CharField(max_length=40)
    image = models.ImageField(upload_to="projects_app/projects")
    link = models.TextField(max_length=60, null=True)

    def __str__(self):
        return f"{self.title}"
