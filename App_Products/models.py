from django.db import models

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Categories"



class Sub_Category(models.Model):
    title = models.CharField(max_length=20)
    categorys = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='categorys')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Sub_Categories"



class Color(models.Model):
    name=models.CharField(max_length=30)

    def __str__(self):
        return self.name



class Size(models.Model):
    name=models.CharField(max_length=30)

    def __str__(self):
        return self.name
   


class Product(models.Model):
    mainimage = models.ImageField(upload_to='Products')
    name = models.CharField(max_length=264)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    sub_category = models.ForeignKey(Sub_Category, on_delete=models.CASCADE, null=True,blank=True, related_name='sub_category')
    preview_text = models.TextField(max_length=200, verbose_name='Preview Text')
    detail_text = models.TextField(max_length=1000, verbose_name='Description')
    additional_info=models.TextField(max_length=1000, verbose_name='Additional Info')
    sku=models.CharField(max_length=30)
    price = models.FloatField()
    old_price = models.FloatField(default=0.00)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created',]

class Product_Color(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,related_name='color_variants')
    color = models.ForeignKey(Color, on_delete=models.CASCADE,related_name='product_color')

    def __str__(self):
        return f"{self.product.name} - {self.color.name}"
    
class Product_Size(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='size_variants')
    size = models.ForeignKey(Size, on_delete=models.CASCADE,related_name='product_size')

    def __str__(self):
        return f"{self.product.name} - {self.size.name}"
    
class Product_Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='image_variants')
    image = models.ImageField(upload_to='Products')

    def __str__(self):
        return f"{self.product.name}"