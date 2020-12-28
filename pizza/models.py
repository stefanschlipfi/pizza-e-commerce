from django.db import models

class Products(models.Model):
    name = models.CharField(max_length=20)
    _ingredients =  models.CharField(max_length=100,name='ingredients',blank=True)
    price = models.FloatField()
    lage_image = models.ImageField(default='product-images/lage/lage_default.png', upload_to='product-images/lage',blank=True)
    small_image = models.ImageField(default='product-images/small/small_default.png', upload_to='product-images/small',blank=True)


    CATEGORIES = (
        ('Pizza', 'Pizza'),
        ('Pasta', 'Pasta'),
        ('Salte', 'Salate'),
    )
    category = models.CharField(max_length=10,choices=CATEGORIES)

    class Meta:
        managed = True
        db_table = 'products'

    def __str__(self):
        return self.name

    @property
    def ingredients(self):
        return self._ingredients.split(';')
    
    @ingredients.setter
    def ingredients(self,value):
        if isinstance(value,list):
            value = ';'.join(value)
        self._ingredients = value