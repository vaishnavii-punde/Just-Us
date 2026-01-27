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
    description = models.TextField(blank=True)
    is_recurring = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['date']
    
    def days_until(self):
        delta = self.date - date.today()
        return delta.days
    
    def __str__(self):
        return self.title


class LoveNote(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_notes')
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Note from {self.sender.username} at {self.created_at}"


class LoveLetter(models.Model):
    """Special love letters that show on hover"""
    title = models.CharField(max_length=200)
    content = models.TextField()
    emoji = models.CharField(max_length=10, default='💌')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title