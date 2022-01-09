from django.test import TestCase, Client
from django.urls import reverse


# Class for holding test cases of views 
class TestViews(TestCase):


    # Create client object for using get and post requests
    client = Client()

    # I create test for GET request of index_main_page view
    def test_index_main_page_GET(self):
    
        response = self.client.get(reverse('index_main_page'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        

    # I create test for GET request of db_data_show_table view
    def test_db_data_show_table_GET(self):
    
        response = self.client.get(reverse('db_data_show_table'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'table_csv.html')

    # I create test for GET request of csv_file_upload view
    def test_csv_file_upload_GET(self):
    
        response = self.client.get(reverse('csv_file_upload'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'upload_csv.html')


    