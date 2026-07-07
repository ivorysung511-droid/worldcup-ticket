from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Event(models.Model):
    STAGE_CHOICES = [
        ('GROUP', 'Group Stage'),
        ('ROUND_32', 'Round of 32'),
        ('ROUND_16', 'Round of 16'),
        ('QUARTER', 'Quarter Final'),
        ('SEMI', 'Semi Final'),
        ('THIRD', 'Third Place'),
        ('FINAL', 'Final'),
    ]
    
    event_id = models.CharField(max_length=100, unique=True)
    title = models.CharField(max_length=200)
    stage = models.CharField(max_length=20, choices=STAGE_CHOICES, default='GROUP')
    date = models.DateTimeField()
    venue = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100, default='United States')
    team1 = models.CharField(max_length=100, blank=True, null=True)
    team2 = models.CharField(max_length=100, blank=True, null=True)
    team1_logo = models.URLField(blank=True, null=True)
    team2_logo = models.URLField(blank=True, null=True)
    min_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    max_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    avg_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    tickets_available = models.IntegerField(default=0)
    image_url = models.URLField(blank=True, null=True)
    last_updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['date']
    
    def __str__(self):
        return f"{self.title} - {self.date.strftime('%b %d, %Y')}"

class Venue(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100, default='United States')
    capacity = models.IntegerField(null=True, blank=True)
    address = models.TextField(blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.name}, {self.city}"
