from django.forms import widgets
from rest_framework import serializers
from advenchore_backend.models import *

class FamilySerializer(serializers.ModelSerializer):
    child_set = serializers.PrimaryKeyRelatedField(many=True)
    
    class Meta:
        model = Family
        fields = ('id','name', 'child_set')

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id','child','startDate','dueDate','pointValue','status','description','response','picture')

class RewardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reward
        fields = ('id', 'child', 'cost', 'status', 'quantity')

class ChildSerializer(serializers.ModelSerializer):
    task_set = serializers.PrimaryKeyRelatedField(many=True)
    reward_set = serializers.PrimaryKeyRelatedField(many=True)

    class Meta:
        model = Child
        fields = ('id','family','points','task_set','reward_set','level','points','toNextLevel','type','type_flavor')