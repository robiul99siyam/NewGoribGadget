from django.db import models


class smartWatchCategroy(models.Model):
   
    name = models.CharField(max_length=200,null=True,blank=True)
    slug = models.SlugField(max_length=200,null=True,blank = True)

    def __str__(self):
        return self.name
    

   


class smartWatchType(models.Model):
  

    name = models.CharField(max_length=200,null=True,blank=True)
    slug = models.SlugField(max_length=200,null=True,blank = True)

    def __str__(self):
        return self.name
    



class smartWatchSize(models.Model):
   

    name = models.CharField(max_length=200,null=True,blank=True)
    slug = models.SlugField(max_length=200,null=True,blank = True)

    def __str__(self):
        return self.name
    






class SmartWatchDescription(models.Model):
    image = models.ImageField(upload_to="smartWatch/media/image",blank=True,null=True)
    description = models.TextField()

    def __str__(self):
        return self.description


class SmartWatchWarranty (models.Model):
    name = models.CharField(max_length=200,null=True,blank=True)
    slug = models.SlugField(max_length=200,null=True,blank = True)

    def __str__(self):
        return self.name



class SmartWatchStrap (models.Model):
    name = models.CharField(max_length=200,null=True,blank=True)
    slug = models.SlugField(max_length=200,null=True,blank = True)

    def __str__(self):
        return self.name




class SmartWatchNetwork (models.Model):
    name = models.CharField(max_length=200,null=True,blank=True)
    slug = models.SlugField(max_length=200,null=True,blank = True)

    def __str__(self):
        return self.name




class SmartWatchEdition (models.Model):
    name = models.CharField(max_length=200,null=True,blank=True)
    slug = models.SlugField(max_length=200,null=True,blank = True)

    def __str__(self):
        return self.name



class color (models.Model):
    name = models.CharField(max_length=200,null=True,blank=True)
    slug = models.SlugField(max_length=200,null=True,blank = True)

    def __str__(self):
        return self.name


    


class SmartWatchSpecificaion(models.Model):

    categroy = models.ForeignKey(smartWatchCategroy,on_delete=models.CASCADE,blank=True,null=True)
    Model = models.CharField(max_length=350)
    DisplaySize = models.CharField(max_length=350)
    Compatiblewith  = models.CharField(max_length=350)
    OtherFeaturesInfo = models.CharField(max_length=350)
    CallingFeatures = models.CharField(max_length=350)
    Batterycapacity = models.CharField(max_length=350)
    Material = models.CharField(max_length=350)
    Chargingtime = models.CharField(max_length=350)
    OS = models.CharField(max_length=350)
    Display = models.CharField(max_length=350)
    SweatWaterResistance = models.CharField(max_length=350)
    Chipset = models.CharField(max_length=350)
    Memory = models.CharField(max_length=350)
    BatteryLife = models.CharField(max_length=350)
    OtherFeaturesnfo = models.CharField(max_length=350)
    
    
    def __str__(self) -> str:
        return self.model


    
STATUS = (
    ("In Stock ", "In Stock"),
    ("Out of Stock","Out of Stock"),
)




class smartWatchProduct(models.Model):
    name = models.CharField(max_length=250)
    price = models.FloatField()
    discount = models.FloatField()
    status = models.CharField(choices=STATUS, max_length=40)
    image = models.ImageField(upload_to="smartWatch/media/image")
    created_on = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(smartWatchCategroy, on_delete=models.CASCADE, related_name='products')
    color = models.ManyToManyField(color, related_name='products')
    specification = models.ForeignKey(SmartWatchSpecificaion, on_delete=models.CASCADE, related_name='products', blank=True, null=True)
    description = models.ForeignKey(SmartWatchDescription, on_delete=models.CASCADE, related_name='products', blank=True, null=True)

    description = models.ForeignKey(SmartWatchDescription, on_delete=models.CASCADE, related_name='products', blank=True, null=True)
    smartWatchType = models.ForeignKey(smartWatchType, on_delete=models.CASCADE, related_name='products', blank=True, null=True)
    smartWatchSize = models.ForeignKey(smartWatchSize, on_delete=models.CASCADE, related_name='products', blank=True, null=True)
    SmartWatchWarranty = models.ForeignKey(SmartWatchWarranty, on_delete=models.CASCADE, related_name='products', blank=True, null=True)
    SmartWatchStrap = models.ForeignKey(SmartWatchStrap, on_delete=models.CASCADE, related_name='products', blank=True, null=True)
    SmartWatchNetwork = models.ForeignKey(SmartWatchNetwork, on_delete=models.CASCADE, related_name='products', blank=True, null=True)
    SmartWatchEdition = models.ForeignKey(SmartWatchEdition, on_delete=models.CASCADE, related_name='products', blank=True, null=True)
    
    class Meta:
        ordering = ['price']
