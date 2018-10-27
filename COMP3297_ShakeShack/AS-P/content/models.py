from django.db import models
import mpu #Install via "pip install mpu --user"

# Create your models here.

class user(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    clinic = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    email_ID = models.CharField(max_length=200)
    token code = models.CharField(max_length=200)

    def __str__(self):
        return self.username

class cart(models.Model):
    username = models.ForeignKey(user, on_delete=modes.CASCADE)
    item_id = models.ForeignKey(inventory, on_delete=modes.CASCADE)
    quantity = models.DecimalField(max_digits=5)
    
    def __str__(self):
        return f'{self.username} ({self.item})

class content(models.Model):
    username = models.ForeignKey(user, on_delete=modes.CASCADE)
    item_id = models.ForeignKey(inventory, on_delete=modes.CASCADE)
    quantity = models.DecimalField(max_digits=5)
    orderID = models.ForeignKey(orders, on_delete=modes.CASCADE)
    
    def __str__(self):
        return f'{self.username} ({self.item})'

class Location(models.Model):
	name = models.CharField(max_length=200)
	latitude = models.FloatField
	longitude = models.FloatField
	altitude = models.IntegerField
	
	def _str_(self):
		return self.name

class Distance(models.Model):
	placeA = models.ForeignKey(Location, on_delete=models.CASCADE)
	placeB = models.ForeignKey(Location, on_delete=models.CASCADE)
	distance = models.FloatField(default = 0.0)
	
	def save(self, *args, **kwargs):
		self.distance = self.calculate()
		super(Distance, self).save(*args, **kwargs)
	
	def calculate(self):
		return mpu.haversine_distance((placeA.latitude, placeA.longitude), (placeB.latitude, placeB.longitude))

class orders(models.Model):
	orderID=models.DecimalField(max_digit=10)
	content=models.CharField(max_length=200)
	username=models.ForeignKey(user,on_delete=models.CASCADE)
	status=models.CharField(max_length=200)
	priority=models.CharField(max_length=200)
	
	def __str__(self):
		return self.orderID
		
