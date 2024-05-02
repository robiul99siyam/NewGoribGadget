from django.db import models

class SoundCategory(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)

    def __str__(self):
        return f"Name: {self.name}, Slug: {self.slug}"



class SoundType(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)

    def __str__(self):
        return f"Name: {self.name}, Slug: {self.slug}"



class SoundPlug(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)

    def __str__(self):
        return f"Name: {self.name}, Slug: {self.slug}"



class Soundcolor(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)

    def __str__(self):
        return f"Name: {self.name}, Slug: {self.slug}"






class SoundWarranty(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)


    def __str__(self):
        return f"Name: {self.name}, Slug: {self.slug}"


class soundSpecificaion(models.Model):
  
    brand = models.ForeignKey(SoundCategory,on_delete=models.CASCADE,blank=True,null=True)
    ChargingInterface = models.CharField(max_length=350)
    Bluetooth  = models.CharField(max_length=350)
    StorageCapacity = models.CharField(max_length=350)
    StorageType = models.CharField(max_length=350)
    GraphicsModel = models.CharField(max_length=350)
    Model = models.CharField(max_length=350)
    Batterycapacity = models.CharField(max_length=350)
    ANCStatus = models.CharField(max_length=350)
    MicStatus = models.CharField(max_length=350)
    DriverSize = models.CharField(max_length=350,blank=True,null=True)
    SweatWaterResistance = models.CharField(max_length=350,blank=True,null=True)
    WirelessCharging = models.CharField(max_length=350)
    Playtime = models.CharField(max_length=350)
    OtherFeaturesInfo = models.CharField(max_length=350)



class SoundDescription(models.Model):
    image = models.ImageField(upload_to="soundAndequipment/media/image", blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = "Description"
        verbose_name_plural = "Descriptions"






STATUS = (
    ("In Stock ", "In Stock"),
    ("Out of Stock","Out of Stock"),
)


class SoundAndequipmentProduct(models.Model):
    name = models.CharField(max_length=250)
    price = models.FloatField()
    discount = models.FloatField()
    status = models.CharField(choices =STATUS,blank=True,null=True,max_length=40)
    image = models.ImageField(upload_to="soundAndequipment/media/image")
    created_on = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(SoundCategory, on_delete=models.CASCADE, related_name='products')
    warranty = models.ForeignKey(SoundWarranty, on_delete=models.CASCADE, related_name='products')
    specification = models.ForeignKey(soundSpecificaion, on_delete=models.CASCADE, related_name='products')
    description = models.ForeignKey(SoundDescription, on_delete=models.CASCADE, related_name='products')

    class Meta:
        ordering = ['price']
