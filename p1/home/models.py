from django.db import models

# Create your models here.

class Fruits(models.Model):
	fruit_name = models.CharField(max_length=100)
	price = models.IntegerField()
	manufacturing_date = models.DateField()
	fruit_description = models.TextField(null=False, blank=True)
	is_fresh = models.BooleanField(default=True)


	def __str__(self) -> str:
		return self.fruit_name +'  Expiry:'+str(self.manufacturing_date)


	class Meta:
		db_table = 'home_fruits'
		verbose_name = 'home_fruits'
		ordering = ['-fruit_name']
		unique_together = [['fruit_name','price']]