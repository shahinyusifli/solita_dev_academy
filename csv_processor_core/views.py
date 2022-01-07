import csv, io, json
from django.shortcuts import render
from django.contrib import messages
from pandas.io.parsers import read_csv
from .models import Farms
import pandas as pd
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def csv_file_upload(request):

    # declaring template
    template = "upload_csv.html"
    data = Farms.objects.all()

    # prompt is a context variable that can have different values depending on their context
    prompt = {
        'order': 'Order of the CSV should be location, datetime, sensorType, value',
        'farm': data    
              }
    

    # HANDLE USER REQUEST STEP
    # GET request returns the value of the data with the specified key.
    if request.method == "GET":
        return render(request, template, prompt)


    # Let's check if it is a csv file
    csv_file = request.FILES['file']
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')
    
    # Reading data which
    # directed to view by html form 
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)

    # Creating pandas DataFrame
    df = pd.read_csv(io_string, header=None)
    df.columns = ['location', 'datetime', 'sensorType', 'value']
    
   
   # TRANSFORMATION STEP
    newdf = df[
        (
            (df["sensorType"] == "pH") &
            (
                (df["value"] < 14) & (df["value"] > 0)
            ) 
        )|
        

        (
            (df["sensorType"] == "temperature") &
            (
                (df["value"] < 100) & (df["value"] > -50) 
            )      
        ) | 

        (
            (df["sensorType"] == "rainFall") &
            (
                (df["value"] < 50) & (df["value"] > 0) 
            )
        )
        ]

    
   # LOAD STEP 
    model_instances = [Farms(
        location=row[1],
        date_time = row[2],
        sensor_type=row[3],
        values=row[4]
        ) for row in newdf.itertuples()]

    Farms.objects.bulk_create(model_instances)

    context = {}
    return render(request, template, context)



def db_data_show_table(request):

    # Select all data from Farms table in database.  
    farm_pure_db_data = Farms.objects.all()
    context = {
        "farms_pure": farm_pure_db_data
    }

    # Create pandas DataFrame from data
    # which came from project database.
    df_assets = pd.DataFrame(
        list(
            farm_pure_db_data.values()
            )
        )

    # Parsing the DataFrame in json format. 
    json_records = df_assets.reset_index().to_json(orient ='records') 
    csv_data = [] 
    csv_data = json.loads(json_records) 
    
    # Create pagination
    page = request.GET.get('page', 1)
    paginator = Paginator(csv_data, 100)
    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)

    # Render table to table.html
    return render(request, 'table_csv.html', { 'farms': data })

def db_data_show_statistics(request):
    
    # Create lists for storing json data
    # to be used in fornt-end
    json_avg_monthly = []
    json_min_monthly = [] 
    json_max_monthly = [] 


     # Select all data from Farms table in database.  
    farm_pure_db_data = Farms.objects.all()
    context = {
        "farms_pure": farm_pure_db_data
    }


    # Create pandas DataFrame from data
    # which came from project database.
    df_assets = pd.DataFrame(
        list(
            farm_pure_db_data.values()
            )
        )
    

    # Find average by monthly 
    df_avg_month = df_assets.groupby(
        pd.PeriodIndex
            (
            df_assets['date_time'], freq="M"
            )
    )['values'].mean().to_frame(name='mean').reset_index()
    #Define columns
    df_avg_month.columns = ['date', 'values']


    # Find minumum by monthly
    df_min_month = df_assets.groupby(
        pd.PeriodIndex
            (
            df_assets['date_time'], freq="M"
            )
    )['values'].min().to_frame(name='mean').reset_index()
    #Define columns
    df_min_month.columns = ['date', 'values']


    # Find maximum by monthly
    df_max_month = df_assets.groupby(
        pd.PeriodIndex
            (
            df_assets['date_time'], freq="M"
            )
    )['values'].max().to_frame(name='mean').reset_index()
    #Define columns
    df_max_month.columns = ['date', 'values']

        
    # Convert pandas DateFrames to json format

    # Convert df_max_month to json format
    json_records_avg_monthly = df_avg_month.reset_index().to_json(orient ='records')  
    json_avg_monthly = json.loads(json_records_avg_monthly)

    # Convert df_max_month to json format
    json_records_min_monthly = df_min_month.reset_index().to_json(orient ='records')  
    json_min_monthly = json.loads(json_records_min_monthly)

    # Convert df_max_month to json format
    json_records_max_monthly = df_max_month.reset_index().to_json(orient ='records')  
    json_max_monthly = json.loads(json_records_max_monthly)


    # Create context for using in template 
    context = {
        'json_avg_monthly' : json_avg_monthly,
        'json_min_monthly' : json_min_monthly,
        'json_max_monthly' : json_max_monthly,
    }


    return render(request, 'statistics_csv.html', context)

    