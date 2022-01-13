# Farm Exercise for Solita Dev Academy 2022
# Şahin Yusifli

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/shahinyusifli/solita_dev_academy.git
$ cd solita_dev_academy
```


Then install the dependencies:

```sh
pip install -r requirements.txt
```

Once `pip` has finished downloading the dependencies:
```sh
python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`.

To test the functionalities of web app such as CSV file upload, showing data in table and showing statistics about data which manual testing can happen in following way. 

## Main page

Before you interact with the application, you must visit the main page with this URL `http://127.0.0.1:8000/`. You can menu which you can be directed to other pages such as CSV file upload, showing data in table and showing statistics about data. 

### CSV file upload

You can access this functionality with "Upload" in the menu which this menu is on the main page. You can upload CSV files. If someone tries to upload another type of file, an error message will be seen. Also, this uploaded CSV file will be stored in a database after some transformations which can be seen in the Solita Dev Academy task.


### Show data in tables

All data in the database can be seen in this functionality. Also, if data is over 100 rows, it will be paginated. This functionality can be accessed by a "Table" section of the menu which is seen on the main page.


### Showing statistics about data

Statistics about data can be seen in this functionality. Statistics are about minimum, maximum, and average of months of years by values. Statistics about data are shown in tables and these tables can be collapsed by clicking their headers which can be returned in the same way too. 

### Admin panel
Admin panel reads metadata from Farms model to provide a quick, model-centric interface where trusted users can manage content on site. It can be accessed by `http://127.0.0.1:8000/admin/'. Also, the username is sahinyusifli and password is Adminsahin123


### Notes

All transformations with data are done by the panda library which is highly used in data science. Also, it can make faster file upload and file storage to the database. Also, I return data in JSON format to some pages with pandas transformations and it allows us to use some JavaScript frameworks without using RESTfull methods. If I need to inform about data transformations which I have seen many concepts of data engineering in this task, I have used ETL instead of ELT process for avoiding making busy to the database. The database is serving data to users, it will be used for authenticating users, etc. If I use ELT principles, I can say my database is working under pressure. Therefore, I have used ETL principles in my exporting, transformation, and importing steps of data. Also, I have used pandas, csv, io, and json libraries of the Python programming language. According to my previous data engineering and data science experience, I think I could make the right decisions in data processing steps. 


## Tests

To run the tests, `cd` into the directory where `manage.py` is. And run this:
```
python manage.py test
