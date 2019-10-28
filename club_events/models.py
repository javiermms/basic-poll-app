from django.db import models

# myclub_project\events\models.py

class Ticket(models.Model):
    price = models.IntegerField(default=50)
    
class Person(models.Model):
    name = models.CharField('First & Last Name: ', max_length=200)
    phone_number = models.CharField('Phone Number: ', max_length=30)

class Event(models.Model):
    name = models.CharField('Event Name', max_length=120)
    event_date = models.DateTimeField('Event Date')
    venue = models.CharField(max_length=120)
    manager = models.CharField(max_length = 60)
    description = models.TextField(blank=True)
    tickets = models.ManyToManyField(Ticket)
    guest_list = models.ManyToManyField(Person)
    
    def __str__(self):
        return self.name
   
    # by date to find an upcoming event_date
    # by location/ venune to see proximixy 
    # by desciption to see if the event is intresting 
    # guest_list --> to see what events a specifc user is attending


