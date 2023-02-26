from django.test import TestCase
from restaurant.models import Menu
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient 
from restaurant.serializers import MenuSerializer

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(menu_id=10, title="IceCream", price=80, inventory=100)
        self.assertEqual(str(item), "IceCream : 80")
        
class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        Menu.objects.create(menu_id=1, title="Cheeseburger", price=8.99, inventory=10)
        Menu.objects.create(menu_id=2, title="Fries", price=3.99, inventory=20)
        Menu.objects.create(menu_id=3, title="Soda", price=1.99, inventory=30)

    def test_getall(self):
        response = self.client.get('/menu/')
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)