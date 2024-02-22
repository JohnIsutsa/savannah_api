from django.db import models

from authentication.models import User

# Create your models here.
class Order(models.Model):
    
    MEDICINES = [
        ('Paracetamol', 'Paracetamol'),
        ('Aspirin', 'Aspirin'),
        ('Ibuprofen', 'Ibuprofen'),
        ('Naproxen', 'Naproxen'),
        ('Diclofenac', 'Diclofenac'),
        ('Celecoxib', 'Celecoxib'),
        ('Acetaminophen', 'Acetaminophen'),
        ('Meloxicam', 'Meloxicam'),
        ('Piroxicam', 'Piroxicam'),
        ('Ketorolac', 'Ketorolac'),
    ]
    
    item = models.CharField(max_length=100, choices=MEDICINES)
    amount = models.IntegerField()
    owner = models.ForeignKey(to=User, related_name='orders', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    
    class Meta: 
        ordering = ['-date']

    def __str__(self):
        return str(self.owner) + 's order'