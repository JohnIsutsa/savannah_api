from django.db import models

from authentication.models import User

# Create your models here.
class Order(models.Model):
    
    MEDICINES = [
        ('1', 'Paracetamol'),
        ('2', 'Aspirin'),
        ('3', 'Ibuprofen'),
        ('4', 'Naproxen'),
        ('5', 'Diclofenac'),
        ('6', 'Celecoxib'),
        ('7', 'Acetaminophen'),
        ('8', 'Meloxicam'),
        ('9', 'Piroxicam'),
        ('10', 'Ketorolac'),
    ]
    
    item = models.CharField(max_length=100, choices=MEDICINES)
    amount = models.IntegerField()
    owner = models.ForeignKey(to=User, related_name='orders', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    
    class Meta: 
        ordering = ['-date']

    def __str__(self):
        return str(self.owner) + 's order'