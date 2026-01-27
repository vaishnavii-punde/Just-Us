from django.db import models
from django.contrib.auth.models import User
from datetime import date


class Memory(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    image = models.ImageField(upload_to='memories/', blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-date']
        verbose_name_plural = 'Memories'
    
    def __str__(self):
        return self.title


class ImportantDate(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    is_recurring = models.BooleanField(default=False)
    
    def days_until(self):
        delta = self.date - date.today()
        return delta.days
    
    def __str__(self):
        return self.title