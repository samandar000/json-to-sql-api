from django.db import models

# Create your models here.
class SmartPhone(models.Model):
    price = models.CharField(max_length=20)
    img_url = models.CharField(max_length=255,default='image')
    color = models.CharField(max_length=20)
    ram = models.IntegerField()
    memory = models.IntegerField(blank=True)
    name = models.CharField(max_length=20)
    model = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.name
    

    def to_dict(self):
        returned = {
            'id':self.id,
            'price':self.price,
            'img_url':self.img_url,
            'color':self.color,
            'ram':self.ram,
            'memory':self.memory,
            'name':self.name,
            'model':self.model,
            }

        return returned
    