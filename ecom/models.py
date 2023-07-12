from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class SubsubCategory(models.Model):
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to="upload/",blank=True, null=True)
    def __str__(self):
        return f"{self.name}"
class SubCategory(models.Model):
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to="upload/",blank=True, null=True)
    subcategory = models.ManyToManyField(SubsubCategory)
    def __str__(self):
        return f"{self.name}"
class Category(models.Model):
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to="upload/",blank=True, null=True)
    subcategory = models.ManyToManyField(SubCategory)
    def __str__(self):
        return f"{self.name}"
class Images(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    filename = models.CharField(max_length=300)
    image = models.ImageField(upload_to="upload/")
    @property
    def image_url(self):
        if self.image:
            return self.image.url
        return None
    def __str__(self):
        return f"{self.filename}"
class Color(models.Model):
    name = models.CharField(max_length=20)
    code = models.CharField(max_length=10)
    def __str__(self):
        return f"{self.name}"
class Unit(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.name}"
class Brand(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to="upload/")
    def __str__(self):
        return f"{self.name}"
class Size(models.Model):
    name = models.CharField(max_length=50)
    unit = models.ForeignKey(Unit,on_delete=models.CASCADE,null=True,blank=True)
    value = models.CharField(max_length=10)
    def __str__(self):
        return f"{self.name}"
class Product(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=200)
    OPTION_a = 'New Arrival'
    OPTION_b = 'Feature Product'
    OPTION_c = 'Hot Product'
    CHOICES2 = (
        (OPTION_a, 'New Arrival'),
        (OPTION_b, 'Feature Product'),
        (OPTION_c, 'Hot Product'), 
        
    )
    type = models.CharField(max_length=50, choices=CHOICES2,blank=True,null=True)
    category = models.ManyToManyField(Category)
    sub_category = models.ManyToManyField(SubCategory)
    sub_Sub_category = models.ManyToManyField(SubsubCategory)
    brand = models.ManyToManyField(Brand,null=True,blank=True)
    color = models.ManyToManyField(Color,null=True,blank=True)
    size = models. ManyToManyField(Size,null=True,blank=True)
    short_descriptions = models.TextField()
    long_description = models.TextField()
    image = models.ManyToManyField(Images)
    videos = models.URLField(null=True,blank=True)
    price = models.FloatField()
    offer_price = models.FloatField()
    quantity = models.IntegerField()
    in_stock = models.BooleanField()
    def __str__(self):
        return f"{self.name}"
class ProductReviews(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE,unique=True)
    text = models.TextField(max_length=1000)
    def __str__(self):
        return f"{self.user}"

class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE,unique=True,null=True,blank=True)
    color = models.ForeignKey(Color,on_delete=models.CASCADE,null=True,blank=True)
    size = models.ForeignKey(Size,on_delete=models.CASCADE,null=True,blank=True)
    quantity = models.IntegerField()
    vendor = models.CharField(max_length=15,null=True,blank=True)
    def __str__(self):
        return f"{self.user}"
class Wishlist(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE,unique=True)
    color = models.ForeignKey(Color,on_delete=models.CASCADE)
    size = models.ForeignKey(Size,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    vendor = models.CharField(max_length=15,null=True,blank=True)
    def __str__(self):
        return f"{self.user}"
class OrderedProduct(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE,unique=True)
    color = models.ForeignKey(Color,on_delete=models.CASCADE)
    size = models.ForeignKey(Size,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    vendor = models.CharField(max_length=15,null=True,blank=True)
    def __str__(self):
        return f"{self.user}"
class Cuopone(models.Model):
    title = models.CharField(max_length=50)
    code = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField
    Free_shipping = models.BooleanField()
    OPTIONl = 'Fixed'
    OPTIONm = 'Percentage'
    CHOICES6 = (
        
        (OPTIONl, 'Fixed'),
        (OPTIONm, 'Percentage'), 
        
    )
    discount_type = models.CharField(max_length=50, choices=CHOICES6)
    amount = models.FloatField()
    category = models.ManyToManyField(Category)
    spent_limit = models.IntegerField()

class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.TextField()
    phone_number = models.CharField(max_length=20)
    ordered_product = models.ManyToManyField(OrderedProduct)
    amount = models.FloatField()
    OPTIONa = 'Hold'
    OPTIONb = 'Shipment'
    OPTIONc = 'Delivered'
    OPTIONd = 'Canceled'
    CHOICES3 = (
        (OPTIONa, 'Hold'),
        (OPTIONb, 'Shipment'),
        (OPTIONc, 'Delivered'), 
        (OPTIONd, 'Canceled'), 
        
    )

    OPTIONe = 'Cash on Delivery'
    OPTIONf = 'Bkash'
    OPTIONg = 'Rocket'
    OPTIONh = 'Nagad'
    CHOICES4 = (
        (OPTIONe, 'Cash on Delivery'),
        (OPTIONf, 'Bkash'),
        (OPTIONg, 'Rocket'), 
        (OPTIONh, 'Nagad'), 
        
    )
    
    OPTIONi = 'Pending'
    OPTIONj = 'Successful'
    OPTIONk = 'Canceled'
    CHOICES5 = (
        
        (OPTIONi, 'Pending'),
        (OPTIONj, 'Successful'), 
        (OPTIONk, 'Canceled'), 
        
    )
    order_status = models.CharField(max_length=50, choices=CHOICES3,blank=True,null=True)
    payment_method = models.CharField(max_length=50, choices=CHOICES4,blank=True,null=True)
    payment_number = models.CharField(max_length=20,blank=True,null=True)
    transaction_id = models.CharField(max_length=20,blank=True,null=True)
    payment_status = models.CharField(max_length=50, choices=CHOICES5,blank=True,null=True)
    date = models.DateField(null=True,blank=True)
    used_cuopone = models.ManyToManyField(Cuopone,null=True,blank=True)
    def __str__(self):
        return f"{self.user}"

 
class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)