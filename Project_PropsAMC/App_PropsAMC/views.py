
from django.shortcuts import render, redirect
from App_PropsAMC.models import UploadFilesDB
import pandas as pd
import requests
import json

# Create your views here.

def upload_file(request):
    if request.method == "POST":
        titlename = request.POST['filetitle']
        filename = request.FILES['fileupload']
        qs = UploadFilesDB(title=titlename,file_name=filename)
        csv_sheet = qs.file_name
        print("Uploaded Sheet Name: ",csv_sheet)
        df = pd.read_csv(csv_sheet)
        print(df)
        for i,row in df.iterrows():
            apiaddress = str(df.at[i,'address'])
            parameters = {
                "key": "ZjEGjfS3BvC26R7nzG1bK5ybM8qVMcZR",
                "location": apiaddress
            }
            response = requests.get("http://www.mapquestapi.com/geocoding/v1/address", params=parameters)
            # print("status_code: ", response.status_code)
            # print(response.text)
            # print(type(response.text)) # <class 'str'>
            data = json.loads(response.text)['results']
            # print(type(data)) # <class 'dict'>
            # print(data)

            # working on json(filter required data)
            lat = data[0]['locations'][0]['latLng']['lat']
            lng = data[0]['locations'][0]['latLng']['lng']
            # print(lat, lng)
            df.at[i, 'latitude'] = lat
            df.at[i, 'longitude'] = lng
            print(lat, lng)

        # Save to new csv
        df.to_csv(r"App_PropsAMC\static\addresswithlatlng.csv") # we can remove index if required(keep FALSE)
        qs.save() # commit to DB
        print("File Saved Successfully..")
        qs = UploadFilesDB.objects.all()
        return render(request, 'upload_form.html', {"filedata": qs})
    qs = UploadFilesDB.objects.all()
    return render(request,'upload_form.html', {"filedata": qs})