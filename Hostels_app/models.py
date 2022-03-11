import email
from statistics import mode
from django.db import models
from Users_app.models import CustomUser

class Hostel(models.Model):
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    category = models.CharField(choices=(('boys', 'Boys'), ('girls', 'Girls'), ('C', 'CoEd')), max_length=5)
    type = models.CharField(choices=(('RB', 'I am a registered business'), ('PB', 'I am a private seller')), max_length=2, default="RB")
    state = models.CharField(max_length=100)
    city =models.CharField(max_length=100)
    pin_code = models.IntegerField()
    street_address = models.CharField(max_length=500)
    one_seater_room = models.IntegerField(null=True)
    one_seater_price = models.IntegerField(null=True)
    two_seater_room = models.IntegerField(null=True)
    two_seater_price = models.IntegerField(null=True)
    three_seater_room = models.IntegerField(null=True)
    three_seater_price = models.IntegerField(null=True)
    
    attached_bathrooms = models.BooleanField(default=False)
    parking = models.BooleanField(default=False)
    wifi = models.BooleanField(default=False)
    gym = models.BooleanField(default=False)
    laundry  = models.BooleanField(default=False)
    pets_friendly = models.BooleanField(default=False)
    tv = models.BooleanField(default=False)
    air_conditioning = models.BooleanField(default=False)
    balcony = models.BooleanField(default=False)
    water_heating = models.BooleanField(default=False)
    linens = models.BooleanField(default=False)
    iron = models.BooleanField(default=False)
    kitchen = models.BooleanField(default=False)
    watercooler = models.BooleanField(default=False)
    security_cameras = models.BooleanField(default=False)
    mess = models.BooleanField(default=False)
    description = models.TextField()
    total_area = models.IntegerField()
    vacant = models.BooleanField(default=False)
    verified = models.BooleanField(default=False)

    sentiment = models.FloatField(null=True)
    lat = models.FloatField(null=True) 
    log = models.FloatField(null=True) 

    def __str__(self):
        return self.title
    
class Hostel_images(models.Model):
    hostel = models.ForeignKey(Hostel, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='Hostel_images')

class HostelReview(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    hostel = models.ForeignKey(Hostel, on_delete=models.CASCADE)
    comment = models.TextField(null=True)
    locality_rate = models.IntegerField(null=True, choices=((1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),(9,9),(10,10)))
    food_rate = models.IntegerField(null=True, choices=((1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),(9,9),(10,10)))
    hostel_rate = models.IntegerField(null=True, choices=((1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),(9,9),(10,10)))
    timestamp = models.DateTimeField(auto_now_add=True, null=True)


class Wishlist(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    hostels = models.ManyToManyField(Hostel)
