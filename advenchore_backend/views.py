from advenchore_backend.models import *
from advenchore_backend.modelSerializers import *
from rest_framework import generics


class FamilyList(generics.ListCreateAPIView):
    queryset = Family.objects.all()
    serializer_class = FamilySerializer

    def pre_save(self, obj):
        obj.child_set = []
    
class FamilyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Family.objects.all()
    serializer_class = FamilySerializer
    
class TaskList(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    
class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    
class ChildDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Child.objects.all()
    serializer_class = ChildSerializer

class ChildList(generics.ListCreateAPIView):
    queryset = Child.objects.all()
    serializer_class = ChildSerializer

class RewardList(generics.ListCreateAPIView):
    queryset = Reward.objects.all()
    serializer_class = RewardSerializer
    
class RewardDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reward.objects.all()
    serializer_class = RewardSerializer