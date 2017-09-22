from django.db import models
from smartcity.choices import *
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.urlresolvers import reverse

class Users(models.Model):
    username = models.CharField(max_length= 20)
    password = models.CharField(max_length= 20)
    firstname = models.CharField(max_length= 20)
    middlename = models.CharField(max_length= 20)
    lastname = models.CharField(max_length= 20)
    email = models.CharField(max_length= 50)
    phoneNumber = models.CharField(max_length= 15)
    gender = models.IntegerField(choices= gender_Choices)
    dob = models.DateField(max_length= 8)
    unit = models.CharField(max_length= 20)
    street = models.CharField(max_length= 50)
    suburb = models.CharField(max_length= 50)
    state = models.IntegerField(choices= state_Choices)
    postcode = models.IntegerField(validators=[MaxValueValidator(9999), MinValueValidator(1)])
    userType = models.IntegerField(choices= usertype_Choices)
    #userIcon = models.CharField(max_length= 500)

    def get_absolut_url(self):
        return reverse('smartcity:register', kwargs={'pk: self.pk'})

    def __str__(self):
         return self.username + ' - ' + self.password + ' - ' + self.firstname + ' - ' + self.middlename + ' - ' + self.lastname \
            + ' - ' + self.email + ' - ' + self.phoneNumber + ' - ' + str(self.gender) + ' - ' + str(self.dob) + ' - ' + self.unit \
            + ' - ' + self.street + ' - ' + self.suburb + ' - ' + str(self.state) + ' - ' + str(self.postcode) + ' - ' + str(self.userType)