from django.test import TestCase, Client
from advenchore_backend.models import *
from rest_framework.test import APIRequestFactory

class BasicTest(TestCase):
    # Using the standard RequestFactory API to create a form POST request
    def setUp(self):
        self.family = Family(name="jones")
        self.family.save()
    
    def test_details(self):
        factory = Client()
        response = factory.get('/get/family/')
        # self.assertEqual(response.status_code, 200)
        # self.assertEqual(response.content, [{"id": 1, "name": "jones"}])
        response2 = factory.put("/post/family/1/", {{"id": 1, "name": "smith"}, "application/json", accept = "application/json")
        self.assertEqual(response2.content,200)
        
        response = factory.get('/get/family/1/')
        self.assertEqual(response.content, {"id": 1, "name": "max"})