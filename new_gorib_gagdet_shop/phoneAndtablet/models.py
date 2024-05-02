from django.db import models

class PhoneCategory(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)

    def __str__(self):
        return f"Name: {self.name}, Slug: {self.slug}"



class PhoneStorage(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)

    def __str__(self):
        return f"Name: {self.name}, Slug: {self.slug}"


class PhoneType(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)

    def __str__(self):
        return f"Name: {self.name}, Slug: {self.slug}"

class PhoneSim(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)

    def __str__(self):
        return f"Name: {self.name}, Slug: {self.slug}"

class PhoneNetwork(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)

    def __str__(self):
        return f"Name: {self.name}, Slug: {self.slug}"

class PhoneColor(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)

    def __str__(self):
        return f"Name: {self.name}, Slug: {self.slug}"

class PhoneWarranty(models.Model):
    name = models.CharField(max_length=250)
    duration = models.IntegerField()  

    def __str__(self):
        return f"Name: {self.name}, Slug: {self.duration}"

class PhoneSpecification(models.Model):
    brand = models.ForeignKey(PhoneCategory,on_delete=models.CASCADE,blank=True,null=True)
    model = models.CharField(max_length=350)
    network = models.CharField(max_length=350)
    dimensions = models.CharField(max_length=350)
    weight = models.CharField(max_length=350)
    sim = models.CharField(max_length=350)
    display_type = models.CharField(max_length=350)
    display_size = models.CharField(max_length=350)
    display_resolution = models.CharField(max_length=350)
    os = models.CharField(max_length=350)
    chipset = models.CharField(max_length=350, blank=True, null=True)
    cpu = models.CharField(max_length=350, blank=True, null=True)
    memory = models.CharField(max_length=350)
    main_camera = models.CharField(max_length=350)
    selfie_camera = models.CharField(max_length=350)
    sound = models.CharField(max_length=350)
    battery_info = models.CharField(max_length=350)
    sensors = models.CharField(max_length=350)

    def __str__(self):
        return self.model

    class Meta:
        verbose_name = "Specification"
        verbose_name_plural = "Specifications"

class PhoneDescription(models.Model):
    image = models.ImageField(upload_to="phoneAndtablet/media/image", blank=True, null=True)
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




class PhoneTabletProduct(models.Model):
    name = models.CharField(max_length=250)
    price = models.FloatField()
    discount = models.FloatField()
    status = models.CharField(choices=STATUS, max_length=40)
    sim = models.ForeignKey(PhoneSim,on_delete=models.CASCADE, related_name='products')
    image = models.ImageField(upload_to="phoneAndtablet/media/image")
    created_on = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(PhoneCategory, on_delete=models.CASCADE, related_name='products')
    color = models.ManyToManyField(PhoneColor, related_name='products')
    warranty = models.ForeignKey(PhoneWarranty, on_delete=models.CASCADE, related_name='products')
    specification = models.ForeignKey(PhoneSpecification, on_delete=models.CASCADE, related_name='products')
    description = models.ForeignKey(PhoneDescription, on_delete=models.CASCADE, related_name='products')
    phone_type = models.ForeignKey(PhoneType, on_delete=models.CASCADE, related_name='products')
    phone_network = models.ForeignKey(PhoneNetwork, on_delete=models.CASCADE, related_name='products')

    class Meta:
        ordering = ['price']
