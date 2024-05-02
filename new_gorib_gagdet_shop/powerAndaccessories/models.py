from django.db import models

class PowerCategory(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)

    def __str__(self):
        return f"Name: {self.name}, Slug: {self.slug}"

class PowerModel(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)

    def __str__(self):
        return f"Name: {self.name}, Slug: {self.slug}"

class PowerType(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)

    def __str__(self):
        return f"Name: {self.name}, Slug: {self.slug}"

class PowerSize(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)


    def __str__(self):
        return f"Name: {self.name}, Slug: {self.slug}"



class PowerCapcity(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)

    def __str__(self):
        return f"Name: {self.name}, Slug: {self.slug}"

class PowerPlug(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)

    def __str__(self):
        return f"Name: {self.name}, Slug: {self.slug}"

class PowerColor(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)

    def __str__(self):
        return f"Name: {self.name}, Slug: {self.slug}"

class PowerWatt(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)


    def __str__(self):
        return f"Name: {self.name}, Slug: {self.slug}"

class PowerLength(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)

    def __str__(self):
        return f"Name: {self.name}, Slug: {self.slug}"


     

    
class PowerSpecification(models.Model):
    brand = models.ForeignKey(PowerCategory, on_delete=models.CASCADE, blank=True, null=True)
    power_output = models.CharField(max_length=350)
    model = models.CharField(max_length=350)
    battery_capacity = models.CharField(max_length=350)
    input_interface = models.CharField(max_length=350)
    color = models.CharField(max_length=350)
    other_features_info = models.CharField(max_length=350)

    def __str__(self) -> str:
        return self.model

class PowerDescription(models.Model):
    image = models.ImageField(upload_to="powerAndaccessories/media/image", blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = "Description"
        verbose_name_plural = "Descriptions"

STATUS = (
    ('In Stock', "In Stock"),
    ('Out Of Stock', "Out Of Stock")
)

class PowerTabletProduct(models.Model):
    name = models.CharField(max_length=250)
    price = models.FloatField()
    discount = models.FloatField()
    status = models.CharField(choices=STATUS, max_length=40)
    image = models.ImageField(upload_to="powerAndaccessories/media/image")
    created_on = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(PowerCategory, on_delete=models.CASCADE, related_name='products')
    color = models.ManyToManyField(PowerColor, related_name='products')
    specification = models.ForeignKey(PowerSpecification, on_delete=models.CASCADE, related_name='products', blank=True, null=True)
    description = models.ForeignKey(PowerDescription, on_delete=models.CASCADE, related_name='products', blank=True, null=True)
    plug = models.ForeignKey(PowerPlug, on_delete=models.CASCADE, related_name='products', blank=True, null=True)
    watt = models.ForeignKey(PowerWatt, on_delete=models.CASCADE, related_name='products', blank=True, null=True)
    length = models.ForeignKey(PowerLength, on_delete=models.CASCADE, related_name='products', blank=True, null=True)

    class Meta:
        ordering = ['price']
