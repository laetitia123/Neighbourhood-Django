from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.dispatch import receiver
from django.db.models.signals import post_save

class Neighbour(models.Model):
    name = models.CharField(max_length =60)
    location = models.CharField(max_length =60)
    caption= HTMLField()
    profile = models.ForeignKey(User,on_delete=models.CASCADE)
    count=models.CharField(default=0,blank=True)
    image = models.ImageField(upload_to = 'images/')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='images')
    

    def create_neighbourhood(self):
        
        self.save()

    
    def delete_neighbourhood(self):
       
        self.delete()
    @classmethod
    def find_by_id(cls,id):
        hoods=cls.objects.filter(id=id)
        return hoods

    

 

    


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', null=True)
    Name = models.TextField(default="Any")
    profile_picture = models.ImageField(
        upload_to='users/', default='users/user.png')
    bio = models.TextField(default="Welcome !")
    neighbour=models.ForeignKey(Neighbour,null=True)
    

    @classmethod
    def search(cls,username):
        profiles=cls.objects.filter(user__username__icontains=username)
        return profiles

class Comment(models.Model):
    comment= models.TextField()
    photo = models.ForeignKey(Neighbour, on_delete=models.CASCADE,null=True)
    posted_by=models.ForeignKey(Profile,on_delete=models.CASCADE,null=True)

#     def __str__(self):
#         return self.posted_by
    

#     def get_comment(self,id):
#         comments=Comment.objects.filter(image_id=id)
#         return comments

# class Business(models.Model):
#     own= models.CharField(max_length =60)
#     bussiness= models.CharField(max_length =60)
#     email= models.CharField(max_length =60)
#     description = models.CharField(max_length =60)
#     date_post= models.DateTimeField(max_length =60)
#     location = models.CharField(max_length =60)
    
#     def create_business(self):
#         self.save()

#     def delete_business(self):
#         self.delete()

#     @classmethod
#     def get_location_business(cls,location):
#         business=Business.objects.filter(location_pk=location)
#         return business

   

# class Post(models.Model):
#     title = models.CharField(max_length=40)
#     post_description = HTMLField()
#     posted_by = models.ForeignKey(User,on_delete=models.CASCADE)
#     post_hood = models.ForeignKey('Neighbour',on_delete=models.CASCADE)
#     posted_on = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f'{self.title},{self.post_hood.neighborhood_name}'

# class Contact(models.Model):
#     name = models.CharField(max_length=30)
#     contacts = models.CharField(max_length=20)
#     email = models.EmailField()
#     neighborhood_contact = models.ForeignKey('Neighbour',on_delete=models.CASCADE)

#     # def __str__(self):
#         # return f'{self.name},{self.email}'
