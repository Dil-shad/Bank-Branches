from django.test import TestCase
import requests
# Create your tests here.


url = 'http://127.0.0.1:8005/bank/'

data = {
    'ifsc': "ABHY0065003"
}

response = requests.post(url, data)

print(response.json())
