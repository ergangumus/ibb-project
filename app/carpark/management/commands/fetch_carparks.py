from django.core.management.base import BaseCommand
from carpark.models import CarPark
from django.contrib.gis.geos import Point
import requests

class CarParkFetcher:
    """API'den verileri çeken ve döndüren sınıf."""

    API_URL = 'https://data.ibb.gov.tr/api/3/action/datastore_search'

    def __init__(self, resource_id, limit=1000):
        self.resource_id = resource_id
        self.limit = limit
        self.offset = 0

    def fetch_data(self):
        """API'den verileri çeker."""
        all_data = []
        while True:
            params = {
                'resource_id': self.resource_id,
                'limit': self.limit,
                'offset': self.offset
            }
            response = requests.get(self.API_URL, params=params)
            data = response.json()

            if 'result' in data and 'records' in data['result']:
                all_data.extend(data['result']['records'])

                if len(data['result']['records']) == self.limit:
                    self.offset += self.limit
                else:
                    break
            else:
                break
        return all_data

class CarParkService:
    """CarPark modeline verileri kaydetme işlemini yöneten sınıf."""
    
    def save_carparks(self, carpark_data):
        """Verilen verileri kullanarak CarPark modeline kaydeder."""
        for record in carpark_data:
            try:
                # Enlem ve boylamı Point objesi ile geometrik formata çevirme
                longitude = float(record.get('LONGITUDE'))
                latitude = float(record.get('LATITUDE'))
                location = Point(longitude, latitude, srid=4326)  # SRID 4326, coğrafi koordinatlar için standart

                # CarPark kaydını oluştur veya var olanı al
                carpark, created = CarPark.objects.get_or_create(
                    park_name=record.get('PARK_NAME'),
                    location_name=record.get('LOCATION_NAME'),
                    park_type_id=record.get('PARK_TYPE_ID'),
                    park_type_desc=record.get('PARK_TYPE_DESC'),
                    capacity_of_park=record.get('CAPACITY_OF_PARK'),
                    working_time=record.get('WORKING_TIME'),
                    county_name=record.get('COUNTY_NAME'),
                    location=location
                )
                if created:
                    print(f"Created car park: {carpark.park_name}")
                else:
                    print(f"Car park {carpark.park_name} already exists")

            except (TypeError, ValueError) as e:
                print(f"Invalid data for {record.get('PARK_NAME')}: {e}")

class Command(BaseCommand):
    """Fetch car park data from API and save to the database"""
    help = 'Fetch car park data from API and save to the database'

    def handle(self, *args, **kwargs):
        resource_id = 'f4f56e58-5210-4f17-b852-effe356a890c'
        limit = 709

        # Veri çekme sınıfını kullanarak verileri al
        fetcher = CarParkFetcher(resource_id, limit)
        carpark_data = fetcher.fetch_data()

        print(f"Toplam çekilen veri sayısı: {len(carpark_data)}")

        # Veri kaydetme sınıfını kullanarak verileri kaydet
        service = CarParkService()
        service.save_carparks(carpark_data)
