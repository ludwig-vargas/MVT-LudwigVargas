from django.db import models

# Create your models here.
class Familiar (models.Model):
    name = models.CharField(max_length = 40)
    last_name = models.CharField(max_length = 40)
    numberphone = models.IntegerField()
    birthday = models.DateField()
    
    def __str__(self):
        return f'Nombre Completo: {self.name} {self.last_name} | Telefono: {self.numberphone} | Cumpleños: {self.birthday}'