from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import MyModel
import threading
import time
@receiver(post_save, sender=MyModel, dispatch_uid="my_signal_handler")
def my_signal_handler(sender, instance, **kwargs):
    print("Signal received for:", instance.name)
time.sleep(2) # simulate a delay of 2 sec in task execution
print("Signal handler finished")
# Creating an instance of MyModel
obj = MyModel.objects.create(name="Test")
print("Object created")
# Printing the current thread’s ID
print("Current thread ID:", threading.get_ident())