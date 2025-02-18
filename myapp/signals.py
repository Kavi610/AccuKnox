from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Mymodel

@receiver(post_save, sender=Mymodel)
def my_signal_handler(sender, instance, **kwargs):
    print ("Signal received for:", instance.name)
# Creating an instance of MyModel
obj = Mymodel.objects.create(name="Test")
print("Object created") # This will be printed after
