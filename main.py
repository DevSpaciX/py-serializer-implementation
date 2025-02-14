from rest_framework.renderers import JSONRenderer
from car.models import Car
from car.serializers import CarSerializer
import io
from rest_framework.parsers import JSONParser
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "car_service.settings")
django.setup()


def serialize_car_object(car: Car) -> bytes:
    serializer = CarSerializer(car)
    content = JSONRenderer().render(serializer.data)
    return content


def deserialize_car_object(json: bytes) -> Car:
    stream = io.BytesIO(json)
    data = JSONParser().parse(stream)
    serializer = CarSerializer(data=data)
    serializer.is_valid()
    return serializer.save()
