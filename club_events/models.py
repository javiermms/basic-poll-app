from django.db import models

# myclub_project\events\models.py

class Ticket(models.Model):
    price = models.IntegerField(default=50)
    
class Person(models.Model):
    name = models.CharField('First & Last Name: ', max_length=200)
    phone_number = models.CharField('Phone Number: ', max_length=30)
    person = models.ManyToManyField(Ticket)

class Event(models.Model):
    name = models.CharField('Event Name', max_length=120)
    event_date = models.DateTimeField('Event Date')
    venue = models.CharField(max_length=120)
    manager = models.CharField(max_length = 60)
    description = models.TextField(blank=True)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, default=0)
    guest_list = models.ManyToManyField(Person)
    
    def __str__(self):
        return self.name


'''
Model Associations

Person:
-one person can have many tickets
-one person can go to many events


Ticket:
-one ticket can have access to many event
-one ticket can also just have accesss to one event

Event:
- one person can go to many events


'''


