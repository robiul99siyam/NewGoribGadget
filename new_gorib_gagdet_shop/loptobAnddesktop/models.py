from django.db import models

class LaptopCategory(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)

    def __str__(self):
        return f"Name: {self.name}, Slug: {self.slug}"

class LaptopSpecification(models.Model):
    brand = models.ForeignKey(LaptopCategory,on_delete=models.CASCADE,blank=True,null=True)
    dimension = models.CharField(max_length=350)
    keyboard_type = models.CharField(max_length=350)
    storage_capacity = models.CharField(max_length=350)
    storage_type = models.CharField(max_length=350)
    graphics_model = models.CharField(max_length=350)
    model = models.CharField(max_length=350)
    graphics = models.CharField(max_length=350)
    interface_port = models.CharField(max_length=350)
    weight = models.CharField(max_length=350)
    display_type = models.CharField(max_length=350, blank=True, null=True)
    display_resolution = models.CharField(max_length=350, blank=True, null=True)
    display_size = models.CharField(max_length=350)
    adapter_type = models.CharField(max_length=350)
    os = models.CharField(max_length=350)
    chipset = models.CharField(max_length=350)
    memory = models.CharField(max_length=350)
    audio = models.CharField(max_length=350)
    battery_info = models.CharField(max_length=250)

    def __str__(self):
        return self.model

    class Meta:
        verbose_name = "Specification"
        verbose_name_plural = "Specifications"




class LaptobStorage(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)

    def __str__(self):
        return f"Name: {self.name}, Slug: {self.slug}"

class LaptobRim(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)

    def __str__(self):
        return f"Name: {self.name}, Slug: {self.slug}"

class LaptobWarranty(models.Model):
    name = models.CharField(max_length=250)
    duration = models.IntegerField()  

    def __str__(self):
        return f"Name: {self.name}, Slug: {self.duration}"

class LaptobDescription(models.Model):
    image = models.ImageField(upload_to="loptobAnddesktop/media/image", blank=True, null=True)
    description = models.TextField()


    def __str__(self):
        return self.description

    class Meta:
        verbose_name = "Description"
        verbose_name_plural = "Descriptions"






STATUS = (
        ('In Stock',"In Stock"),
        ("Out Of Stock ", "Out Of Stock ")
    )  


KEYBOARD = (
        ("Arabic","Arabic"),
        ("Regular","Regular")
    )

class laptobAnddesktopProduct(models.Model):


    name = models.CharField(max_length=250)
    price = models.FloatField()
    discount = models.FloatField()
    status = models.CharField(choices=STATUS, max_length=40)
    keyboard = models.CharField(choices=KEYBOARD, max_length=40)
    image = models.ImageField(upload_to="loptobAnddesktop/media/image")
    created_on = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(LaptopCategory, on_delete=models.CASCADE, related_name='products')
    warranty = models.ForeignKey(LaptobWarranty, on_delete=models.CASCADE, related_name='products')
    specification = models.ForeignKey(LaptopSpecification, on_delete=models.CASCADE, related_name='products')
    description = models.ForeignKey(LaptobDescription, on_delete=models.CASCADE, related_name='products')
    storage = models.ForeignKey(LaptobStorage, on_delete=models.CASCADE, related_name='products')
    Ram = models.ForeignKey(LaptobRim, on_delete=models.CASCADE, related_name='products')

    class Meta:
        ordering = ['price']
