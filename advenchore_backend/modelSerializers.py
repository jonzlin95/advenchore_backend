from django.forms import widgets
from rest_framework import serializers
from advenchore_backend.models import *

# GET Serializers

class FamilySerializer(serializers.ModelSerializer):
    child_set = serializers.PrimaryKeyRelatedField(many=True)
    
    class Meta:
        model = Family
        fields = ('id','name', 'child_set')

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'name', 'child','startDate','dueDate','pointValue','status','description','response','picture', 'pictureURL')

class RewardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reward
        fields = ('id', 'name', 'child', 'cost', 'status', 'quantity', 'rewardURL')

class ChildSerializer(serializers.ModelSerializer):
    task_set = serializers.PrimaryKeyRelatedField(many=True)
    reward_set = serializers.PrimaryKeyRelatedField(many=True)

    class Meta:
        model = Child
        fields = ('id', 'name', 'family','points','task_set','reward_set','level','points','toNextLevel','type','type_flavor')
        
# POST Serializers

class FamilySerializerPOST(serializers.ModelSerializer):
    
    class Meta:
        model = Family
        fields = ('id','name')

class TaskSerializerPOST(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'name', 'child','startDate','dueDate','pointValue','status','description','response','picture', 'pictureURL')

class RewardSerializerPOST(serializers.ModelSerializer):
    class Meta:
        model = Reward
        fields = ('id', 'name', 'child', 'cost', 'status', 'quantity', 'rewardURL')

class ChildSerializerPOST(serializers.ModelSerializer):

    class Meta:
        model = Child
        fields = ('id', 'name', 'family','points', 'level','points','toNextLevel','type','type_flavor')