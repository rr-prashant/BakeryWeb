from django.db import models
from django.core.exceptions import ValidationError
from PIL import Image
from bakery_app.make_slug import unique_slug_generator
from django.db.models.signals import pre_save
from django.contrib.auth.models import User
# Create your models here.

    
    
class phone(models.Model):
    user = models.ForeignKey(User,editable=False ,on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True, null=True)



#Validating image size in the model - start
def validate_image_dimensions(image):
    max_width = 1920  # Maximum allowed width
    max_height = 930  # Maximum allowed height

    img = Image.open(image)
    width, height = img.size

    if width > max_width or height > max_height:
        raise ValidationError(f"Maximum allowed dimensions are {max_width}px width and {max_height}px height.")
#Validating image size in the model - end


class IntroSlider(models.Model):
    main_title = models.CharField(max_length=100, null=False, blank=False)
    sub_title = models.CharField(max_length=100, null=False, blank=False)
    photo = models.ImageField(upload_to='slider_images/', null=False, blank=False, validators=[validate_image_dimensions])
    
    def __str__(self):
        return self.main_title
    
    
    
#Validating image size in the model - start
def validate_banner_image(image):
    max_width = 1200  # Maximum allowed width
    max_height = 810  # Maximum allowed height

    img = Image.open(image)
    width, height = img.size

    if width > max_width or height > max_height:
        raise ValidationError(f"Maximum allowed dimensions are {max_width}px width and {max_height}px height.")
#Validating image size in the model - end


class Banner(models.Model):
    banner_title = models.CharField(max_length=100, null=False, blank=False)
    banner_sub_title = models.CharField(max_length=100, null=False, blank=False)
    banner_photo = models.ImageField(upload_to='banner_images/', null=False, blank=False, validators=[validate_banner_image])
    banner_link = models.CharField(max_length=100, null=False, blank=False)
    
    def __str__(self):
        return self.banner_title

    
    
#Validating image size in the model - start
def validate_cake_image_dimensions(image):
    max_width = 1100  # Maximum allowed width
    max_height = 1300  # Maximum allowed height

    img = Image.open(image)
    width, height = img.size

    if width > max_width or height > max_height:
        raise ValidationError(f"Maximum allowed dimensions are {max_width}px width and {max_height}px height.")
#Validating image size in the model - end

class accessories(models.Model):
    title =  models.CharField(max_length=100, null=False, blank=False)
    accessory_price = models.FloatField(max_length=100, null=False, blank=False)
    about_accessory = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(max_length=500, null=False, blank=False)
    accessory_Dimension = models.CharField(max_length=100, null=False, blank=False)
    color = models.CharField(max_length=100, null=False, blank=False)
    accessory_image1 = models.ImageField(upload_to='accessories_images/', null=False, blank=False, validators=[validate_cake_image_dimensions])
    accessory_image2 = models.ImageField(upload_to='accessories_images/', null=False, blank=False, validators=[validate_cake_image_dimensions])
    accessory_image3 = models.ImageField(upload_to='accessories_images/', null=False, blank=False, validators=[validate_cake_image_dimensions])
    slug = models.SlugField(unique=True, null=True, blank=True, editable=True)
    
    def __str__(self):
        return self.title
    
def pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
    
pre_save.connect(pre_save_receiver, sender=accessories )


class cakes(models.Model):
    title =  models.CharField(max_length=100, null=False, blank=False)
    cake_price = models.FloatField(max_length=100, null=False, blank=False)
    about_cake = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    cake_weight = models.CharField(max_length=100, null=False, blank=False)
    cake_toppings = models.CharField(max_length=100, null=False, blank=False)
    cake_extras = models.CharField(max_length=100, null=False, blank=False)
    cake_image1 = models.ImageField(upload_to='cake_images/', null=False, blank=False, validators=[validate_cake_image_dimensions])
    cake_image2 = models.ImageField(upload_to='cake_images/', null=False, blank=False, validators=[validate_cake_image_dimensions])
    cake_image3 = models.ImageField(upload_to='cake_images/', null=False, blank=False, validators=[validate_cake_image_dimensions])
    is_featured = models.BooleanField(default=False)
    slug = models.SlugField(unique=True, null=True, blank=True, editable=True)
    
    
    def __str__(self):
        return self.title
    
def pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
    
pre_save.connect(pre_save_receiver, sender=cakes )


class cakeOnSale(models.Model):
    title =  models.CharField(max_length=100, null=False, blank=False)
    cake_actual_price = models.FloatField(max_length=100, null=False, blank=False)
    cake_sale_price = models.FloatField(max_length=100, null=False, blank=False)
    about_cake = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(max_length=500, null=False, blank=False)
    cake_weight = models.CharField(max_length=100, null=False, blank=False)
    cake_toppings = models.CharField(max_length=100, null=False, blank=False)
    cake_extras = models.CharField(max_length=100, null=False, blank=False)
    cake_image1 = models.ImageField(upload_to='cakeonsale_images/', null=False, blank=False, validators=[validate_cake_image_dimensions])
    cake_image2 = models.ImageField(upload_to='cakeonsale_images/', null=False, blank=False, validators=[validate_cake_image_dimensions])
    cake_image3 = models.ImageField(upload_to='cakeonsale_images/', null=False, blank=False, validators=[validate_cake_image_dimensions])
    slug = models.SlugField(unique=True, null=True, blank=True, editable=True)
    
    def __str__(self):
        return self.title
    
def pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
    
pre_save.connect(pre_save_receiver, sender=cakeOnSale )

class about(models.Model):
    our_story = models.TextField(null=False, blank=False)
    image1 = models.ImageField(upload_to='aboutus_images/', null=False, blank=False, validators=[validate_cake_image_dimensions])
    our_mission = models.TextField(null=False, blank=False)
    image2 = models.ImageField(upload_to='aboutus_images/', null=False, blank=False, validators=[validate_cake_image_dimensions])
    quote = models.CharField(max_length=500,null=True, blank=True)
    quote_author = models.CharField(max_length=100, null=True, blank=True)
    
    class meta:
        verbose_name_plural = 'abouts'
    
    def __str__(self):
        return "About us"


class contact_info(models.Model):
    address = models.CharField(max_length=100, null=False, blank=False)
    contact_number = models.CharField(max_length=15, null=False, blank=False)
    company_email = models.CharField(max_length=100, null=False, blank=False)
    
    def __str__(self):
        return "Contact us"

class contact_us(models.Model):
    client_email = models.CharField(max_length=100, null=False, blank=False)
    client_message = models.TextField(null=False, blank=False)
    
    def __str__(self):
        return self.client_email
    