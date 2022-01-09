from django.test import SimpleTestCase
from django.urls import reverse, resolve
from csv_processor_core.views import csv_file_upload, db_data_show_table, db_data_show_statistics, index_main_page


class TestUrls(SimpleTestCase):

    # Test case for csv_file_upload URL
    # for detecting it can be resolved or not
    def test_csv_file_upload_url_is_resolved(self):
        url = reverse('csv_file_upload')
        self.assertEquals(resolve(url).func, csv_file_upload)

    # Test case for db_data_show_table URL
    # for detecting it can be resolved or not
    def test_db_data_show_table_url_is_resolved(self):
        url = reverse('db_data_show_table')
        self.assertEquals(resolve(url).func, db_data_show_table)

    # Test case for db_data_show_statistics URL
    # for detecting it can be resolved or not
    def test_db_data_show_statistics_url_is_resolved(self):
        url = reverse('db_data_show_statistics')
        self.assertEquals(resolve(url).func, db_data_show_statistics)

    # Test case for index_main_page URL
    # for detecting it can be resolved or not
    def test_index_main_page_url_is_resolved(self):
        url = reverse('index_main_page')
        self.assertEquals(resolve(url).func, index_main_page)


