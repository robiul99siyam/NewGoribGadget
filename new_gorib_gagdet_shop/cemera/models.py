from django.db import models

class CameraCategory(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)

    def __str__(self):
        return f"Name: {self.name}, Slug: {self.slug}"

class CameraModel(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)

    def __str__(self):
        return f"Name: {self.name}, Slug: {self.slug}"

class CameraType(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)

    def __str__(self):
        return f"Name: {self.name}, Slug: {self.slug}"

class CameraWarranty(models.Model):
    name = models.CharField(max_length=250)
    duration = models.IntegerField()  

    def __str__(self):
        return f"Name: {self.name}, duration: {self.duration}"
    
    

STATUS_CHOICES = (
        ('In Stock', 'In Stock'),
        ('Out Of Stock', 'Out Of Stock')
)
class CameraProduct(models.Model):

    name = models.CharField(max_length=250)
    price = models.FloatField()
    discount = models.FloatField()
    status = models.CharField(choices=STATUS_CHOICES, max_length=40)
    image = models.ImageField(upload_to="cemera/media/image")
    created_on = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(
        CameraCategory,
        on_delete=models.CASCADE,
        related_name='products'
    )
    model = models.ForeignKey(
        CameraModel,
        on_delete=models.CASCADE,
        related_name='products'
    )
    camera_type = models.ForeignKey(
        CameraType,
        on_delete=models.CASCADE,
        related_name='products'
    )
    warranty = models.ForeignKey(
        CameraWarranty,
        on_delete=models.CASCADE,
        related_name='products'
    )
   
    class Meta:
        ordering = ['price']
