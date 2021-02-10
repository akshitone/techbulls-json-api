import json
import os
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CustomerSerializer
from .models import Customer


@api_view(['GET'])
def home(request):
    list = {"api links": {"View:'api/customers/'", "Create:api/customer-create/"}}
    return Response(list)


@api_view(['GET'])
def customer_list(request):
    customers = Customer.objects.all()
    customer_serializer = CustomerSerializer(customers, many=True)
    return Response(customer_serializer.data)


@api_view(['GET', 'POST'])
def customer_create(request):
    for file in os.listdir('./assets/json'):
        if file.endswith(".json"):
            json_file = open('./assets/json/'+file, 'r')
            json_data = json_file.read()
            customer_data = json.loads(json_data)
            for customer in customer_data['customers']:
                print(customer)
                customer_serializer = CustomerSerializer(data=customer)
                if customer_serializer.is_valid():
                    customer_serializer.save()
    return Response({"Successfully created!"})
