from django.test import TestCase
from csv_processor_core.models import Farms


class FarmModelTest(TestCase):


    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Farms.objects.create(
            location="Test farm", 
            date_time="2019-01-01T06:09:47.373Z",
            sensor_type = "pH",
            values = 7,
            )

    # Check existing labels
    # Check location label
    def test_location_label(self):
        farm = Farms.objects.get(id=1)
        field_label = farm._meta.get_field("location").verbose_name
        self.assertEqual(field_label, "location")

    # Check date_time label
    def test_date_time_label(self):
        farm = Farms.objects.get(id=1)
        field_label = farm._meta.get_field("date_time").verbose_name
        self.assertEqual(field_label, "date time")

    # Check sensor_type label
    def test_sensor_type_label(self):
        farm = Farms.objects.get(id=1)
        field_label = farm._meta.get_field("sensor_type").verbose_name
        self.assertEqual(field_label, "sensor type")

    # Check values label
    def test_values_label(self):
        farm = Farms.objects.get(id=1)
        field_label = farm._meta.get_field('values').verbose_name
        self.assertEqual(field_label, 'values')

    # Check maximum length of location and sensor_type labels
    # Check maximum length of location label
    def test_location_max_length(self):
        farm = Farms.objects.get(id=1)
        max_length = farm._meta.get_field('location').max_length
        self.assertEqual(max_length, 150)

    # Check maximum length of sensor_type label
    def test_sensor_type_max_length(self):
        farm = Farms.objects.get(id=1)
        max_length = farm._meta.get_field('sensor_type').max_length
        self.assertEqual(max_length, 50)

    # Check location lable with created data
    def test_farm_location_object_with_data(self):
        farm = Farms.objects.get(id=1)
        expected_farm_value = f'{farm.location}'
        self.assertEqual(str(farm), expected_farm_value)