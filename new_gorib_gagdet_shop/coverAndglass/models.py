from django.db import models

class coverAndglassCategroy(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)

    def __str__(self):
        return f"Name : {self.name}  slug : {self.slug}"

class ProductModel(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)

    def __str__(self):
        return f"Name: {self.name}, Slug: {self.slug}"

class Cover_Color(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)

    def __str__(self):
        return f"Name: {self.name}, Slug: {self.slug}"

class ProductSize(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)

    def __str__(self):
        return f"Name: {self.name}, Slug: {self.slug}"

class Warranty(models.Model):
    name = models.CharField(max_length=250)
    duration = models.IntegerField()  

    def __str__(self):
         return f"Name: {self.name}, duration: {self.duration}"


STATUS = (
     ('In Stock',"In Stock"),
     ("Out Of Stock ", "Out Of Stock ")
 )  

class CoverAndGlassProduct(models.Model):
    name = models.CharField(max_length=250)
    price = models.FloatField()
    discount = models.FloatField()
    status = models.CharField(choices=STATUS, max_length=40)
    image = models.ImageField(upload_to="coverAndglass/media/image")
    created_on = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(
        coverAndglassCategroy,
        on_delete=models.CASCADE,
        related_name='products'
    )
    product_model = models.ForeignKey(
        ProductModel,
        on_delete=models.CASCADE,
        related_name='products'
    )
    product_size = models.ForeignKey(
        ProductSize,
        on_delete=models.CASCADE,
        related_name='products'
    )
    Cover_Color = models.ManyToManyField(
        Cover_Color,
        related_name='products'
    )
    warranty = models.ForeignKey(
        Warranty,
        on_delete=models.CASCADE,
        related_name='products'
    )
   
    class Meta:
        ordering = ['price']