from django.db import models
import uuid

class Product(models.Model):
    # Product = "3Thrift"
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    # mood_intensity = models.IntegerField()

    # @property
    # def is_mood_strong(self):
    #     return self.mood_intensity > 5

