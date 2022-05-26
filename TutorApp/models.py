from pyexpat import model
from MySQLdb import Timestamp
from django.db import models
from django.forms import CharField, IntegerField

# Create your models here.

# Gigs Model 


class AdminModel(models.Model):
    email=models.CharField(max_length=400)
    password=models.CharField(max_length=400)
    fullname=models.CharField(max_length=400)
    CNIC=models.CharField(max_length=15)

class Teachers(models.Model):
    email=models.CharField(max_length=400)
    password=models.CharField(max_length=400)
    fullname=models.CharField(max_length=400)
    CNIC=models.CharField(max_length=15)
    DOB=models.DateField()
    badge=models.BooleanField(default=False)

class Subjects(models.Model):
    name=models.CharField(max_length=400)
    ranking=models.CharField(max_length=400)
    type=models.CharField(max_length=400)



class Students(models.Model):
    email=models.CharField(max_length=400)
    password=models.CharField(max_length=400)
    fullname=models.CharField(max_length=400)
    CNIC=models.CharField(max_length=15)
    DOB=models.DateField()

class Packages(models.Model):
    name=models.CharField(max_length=200)
    services=models.TextField()
    type=models.CharField(max_length=200)
    price=models.IntegerField()




class Requests(models.Model):
    status=models.CharField(max_length=450)
    description=models.TextField()
    file= models.BinaryField (blank = True, null = True, editable = True)
    teacher = models.ForeignKey(Teachers, on_delete=models.CASCADE)
    student = models.ForeignKey(Students, on_delete=models.CASCADE)

class Orders(models.Model):
    status=models.CharField(max_length=200)
    ord_start_time=models.DateTimeField(auto_now_add=True)
    ord_end_time=models.DateTimeField(auto_now_add=True)
    desc=models.TextField()
    Orderprice=models.IntegerField()
    teacher = models.ForeignKey(Teachers, on_delete=models.CASCADE)
    student = models.ForeignKey(Students, on_delete=models.CASCADE)


class Tuition(models.Model):
    name=models.CharField(max_length=200)
    quiz=models.BinaryField (blank = True, null = True, editable = True)
    assesment=models.BinaryField (blank = True, null = True, editable = True)
    lecture=models.BinaryField (blank = True, null = True, editable = True)
    teacher = models.ForeignKey(Teachers, on_delete=models.CASCADE)
    student = models.ForeignKey(Students, on_delete=models.CASCADE)
    order=models.ForeignKey(Orders, on_delete=models.CASCADE,default=1)

class CodeEditor(models.Model):
    language=models.CharField(max_length=200)
    timestamp=models.DateTimeField(auto_now_add=True)
    teacher = models.ForeignKey(Teachers, on_delete=models.CASCADE)
    student = models.ForeignKey(Students, on_delete=models.CASCADE)

class DemoTests(models.Model):
    name=models.CharField(max_length=400)
    file=models.BinaryField(blank = True, null = True, editable = True)

class  Results(models.Model):
    teacher = models.ForeignKey(Teachers, on_delete=models.CASCADE)
    test = models.ForeignKey(DemoTests, on_delete=models.CASCADE)
    result=models.IntegerField()


class Payment(models.Model):
    stripe_id=models.CharField(max_length=300)

class Gigs(models.Model):
    gig_id=models.IntegerField(default=2)
    name=models.CharField(max_length=400)
    desc=models.TextField()
    image=models.BinaryField (blank = True, null = True, editable = True)
    Startingprice=models.IntegerField(default=300)
    teacher = models.ForeignKey(Teachers, on_delete=models.CASCADE,default=1)
    subject=models.ForeignKey(Subjects, on_delete=models.CASCADE,default=1)
    # review=models.ManyToManyField(Reviews)
    
class Reviews(models.Model):
    rating=models.IntegerField()
    text=models.TextField()
    gig = models.ForeignKey(Gigs, on_delete=models.CASCADE,default=1)


class GigRating(models.Model):
    gig = models.ForeignKey(Gigs, on_delete=models.CASCADE)
    rating=models.IntegerField()


class GigPackages(models.Model):
    gig=models.ManyToManyField(Gigs)
    package=models.ForeignKey(Packages,on_delete=models.CASCADE,default=1)

    # def __bytes__  (self):
    #     return self.image
class demo(models.Model):
    image=models.BinaryField (blank = True, null = True, editable = True)
    name=models.CharField(max_length=300)
    price=models.IntegerField()

    def __str__(self):
        return self.name