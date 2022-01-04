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



