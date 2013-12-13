from django.db import models
import datetime

class Family(models.Model):
    name = models.CharField(max_length=70)
    
class Task(models.Model):
    name = models.CharField(max_length=150)
    child = models.ForeignKey('Child')
    startDate = models.DateTimeField(default=datetime.datetime.now(), blank=True)
    dueDate = models.DateTimeField(default=datetime.datetime.now(), blank=True)
    pointValue = models.IntegerField()
    # 0 incomplete
    # 1 pending parent approval
    # 2 parent sent back incomplete
    # 3 completed task
    status = models.IntegerField(default=0, blank=True)
    description = models.TextField(blank=True)
    response = models.TextField(blank=True)
    picture = models.BooleanField(default=False)
    pictureURL = models.TextField(blank=True)
    
    def toJson(self):
        return {
            'id' : self.id,
            'child' : self.child,
            'startDate': self.startDate,
            'dueDate' : self.dueDate,
            'pointValue' : self.pointValue,
            'status' : self.status,
            'description' : self.description,
            'response' : self.response,
            'picture' : self.picture,
        }

class Reward(models.Model):
    name = models.CharField(max_length=150)
    child = models.ForeignKey('Child')
    cost = models.IntegerField(blank=True)
    status = models.IntegerField(default=0)
    quantity = models.IntegerField(blank=True)
    rewardURL = models.TextField(blank=True)
    
    def toJson(self):
        return {
            'id' : self.id,
            'child' : self.child,
            'cost' : self.cost,
            'status' : self.status,
            'quantity' : self.quantity,
        }
    
class Child(models.Model):
    name = models.CharField(max_length=50)
    family = models.ForeignKey('Family')
    points = models.IntegerField(default=0)
    level = models.IntegerField(default=1)
    toNextLevel = models.IntegerField()
    type = models.CharField(max_length=70)
    type_flavor = models.CharField(max_length=70)