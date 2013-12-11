from django.db import models


class Family(models.Model):
    name = models.CharField(max_length=70)

class Task(models.Model):
    child = models.ForeignKey('Child')
    startDate = models.DateTimeField()
    dueDate = models.DateTimeField()
    pointValue = models.IntegerField()
    # 0 incomplete
    # 1 pending parent approval
    # 2 parent sent back incomplete
    # 3 completed task
    status = models.IntegerField()
    description = models.TextField()
    response = models.TextField()
    picture = models.BooleanField(default=False)

    
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
    child = models.ForeignKey('Child')
    cost = models.IntegerField()
    status = models.IntegerField()
    quantity = models.IntegerField()
    
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
    points = models.IntegerField()
    level = models.IntegerField()
    toNextLevel = models.IntegerField()
    type = models.CharField(max_length=70)
    type_flavor = models.CharField(max_length=70)