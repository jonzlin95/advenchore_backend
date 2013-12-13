from advenchore_backend.models import *
from advenchore_backend.modelSerializers import *
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class FamilyList(generics.ListAPIView):
    queryset = Family.objects.all()
    serializer_class = FamilySerializer

class FamilyListPOST(generics.CreateAPIView):
    queryset = Family.objects.all()
    serializer_class = FamilySerializerPOST
    
class FamilyDetail(generics.RetrieveDestroyAPIView):
    queryset = Family.objects.all()
    serializer_class = FamilySerializer

class FamilyDetailPOST(generics.UpdateAPIView):
    queryset = Family.objects.all()
    serializer_class = FamilySerializerPOST
    
class TaskList(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    
class TaskListPOST(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializerPOST
  
class TaskDetail(generics.RetrieveDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskDetailPOST(generics.UpdateAPIView):
    queryset =  Task.objects.all()
    serializer_class = TaskSerializerPOST
    
class ChildDetail(generics.RetrieveDestroyAPIView):
    queryset = Child.objects.all()
    serializer_class = ChildSerializer
    
class ChildDetailPOST(generics.UpdateAPIView):
    queryset = Child.objects.all()
    serializer_class = ChildSerializerPOST

class ChildList(generics.ListAPIView):
    queryset = Child.objects.all()
    serializer_class = ChildSerializer

class ChildListPOST(generics.CreateAPIView):
    queryset = Child.objects.all()
    serializer_class = ChildSerializerPOST
    
class RewardList(generics.ListCreateAPIView):
    queryset = Reward.objects.all()
    serializer_class = RewardSerializer
    
class RewardListPOST(generics.CreateAPIView):
    queryset = Reward.objects.all()
    serializer_class = RewardSerializerPOST
    
class RewardDetail(generics.RetrieveDestroyAPIView):
    queryset = Reward.objects.all()
    serializer_class = RewardSerializer
    
class RewardDetailPOST(generics.UpdateAPIView):
    queryset = Reward.objects.all()
    serializer_class = RewardSerializerPOST
    
# Custom views

class TasksOfChild(APIView):
    """
    List all tasks owned by Child
    """
    def get(self, request, pk, format=None):
        try:
            task = Task.objects.get(child__exact=pk, status__lte = 2)
            serializer = TaskSerializer(task, many=True)
            return Response(serializer.data)
        except Task.DoesNotExist:
            return Response()

class TasksOfParent(APIView):            
    
    # List all tasks owned by a Parent
    def get(self,request,pk, format=None):
        try:
            children = Child.objects.get(parent__exact=pk)
            for child in children:
                task = Task.objets.get(child__exact = child__id, status__lte = 2)
                serializer = TaskSerializer(task, many=True)
            return Response(serializer.data)
        except Task.DoesNotExist:
            return Response()
        except Child.DoesNotExist:
            return Response()
            
class RewardsOfChild(APIView):
    """
    List all Rewards owned by Child
    """
    def get(self, request, pk, format=None):
        try:
            reward = Reward.objects.get(child__exact=pk)
            serializer = RewardSerializer(reward, many=True)
            return Response(serializer.data)
        except Task.DoesNotExist:
            return Response()

class RewardsOfParent(APIView):            
    
    # List all tasks owned by a Parent
    def get(self,request,pk, format=None):
        try:
            children = Child.objects.get(parent__exact=pk)
            for child in children:
                reward = Reward.objets.get(child__exact = child__id)
                serializer = RewardSerializer(task, many=True)
            return Response(serializer.data)
        except Task.DoesNotExist:
            return Response()
        except Child.DoesNotExist:
            return Response()
            