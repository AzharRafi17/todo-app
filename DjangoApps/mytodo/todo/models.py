from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=300)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    completed = models.BooleanField(default=False)
    due_date = models.DateField(null=True, blank=True)  # Due date field
    priority = models.IntegerField(default=1)  # Priority level

    def __str__(self):
        return self.title
