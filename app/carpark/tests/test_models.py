"""
Tests for CarPark model.
"""
from django.test import TestCase
from django.contrib.gis.geos import Point
from carpark.models import CarPark
from django.db.utils import IntegrityError

class CarParkModelTests(TestCase):
    """Test the CarPark model."""

    def setUp(self):
        """Set up the common test data."""
        self.park_name = 'Kalamış Parkı Yol Üstü 2'
        self.location_name = 'Kalamış Parkı Yol Üst'
        self.park_type_id = 'YOL ÜSTÜ'
        self.park_type_desc = 'YOL ÜSTÜ'
        self.capacity_of_park = 25
        self.working_time = '09:00-19:00'
        self.county_name = 'KADIKÖY'
        self.location = Point(29.0364496713435, 40.9692532913464)

    def test_create_car_park_successful(self):
        """Test creating a car park is successful."""
        car_park = CarPark.objects.create(
            park_name=self.park_name,
            location_name=self.location_name,
            park_type_id=self.park_type_id,
            park_type_desc=self.park_type_desc,
            capacity_of_park=self.capacity_of_park,
            working_time=self.working_time,
            county_name=self.county_name,
            location=self.location,
        )

        self.assertEqual(car_park.park_name, self.park_name)
        self.assertEqual(car_park.location_name, self.location_name)
        self.assertEqual(car_park.park_type_id, self.park_type_id)
        self.assertEqual(car_park.park_type_desc, self.park_type_desc)
        self.assertEqual(car_park.capacity_of_park, self.capacity_of_park)
        self.assertEqual(car_park.working_time, self.working_time)
        self.assertEqual(car_park.county_name, self.county_name)
        self.assertEqual(car_park.location, self.location)

    def test_car_park_str(self):
        """Test the CarPark string representation."""
        car_park = CarPark.objects.create(
            park_name=self.park_name,
            location_name=self.location_name,
            park_type_id=self.park_type_id,
            park_type_desc=self.park_type_desc,
            capacity_of_park=self.capacity_of_park,
            working_time=self.working_time,
            county_name=self.county_name,
            location=self.location,
        )

        self.assertEqual(str(car_park), self.park_name)

    def test_create_car_park_with_negative_capacity(self):
        """Test creating a car park with negative capacity raises an error."""
        with self.assertRaises(IntegrityError):
            CarPark.objects.create(
                park_name=self.park_name,
                location_name=self.location_name,
                park_type_id=self.park_type_id,
                park_type_desc=self.park_type_desc,
                capacity_of_park=-10,  #
                working_time=self.working_time,
                county_name=self.county_name,
                location=self.location,
            )
