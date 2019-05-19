#!/usr/bin/env python3.4
# -*- coding: utf-8 -*-
"""
Created on Thu May 16 09:10:08 2019

@author: romanbody
"""
import os
from googleapiclient import discovery
from oauth2client.client import GoogleCredentials

"""
Set envirinment atribute with google json credentials
 
fot more details:
 https://cloud.google.com/docs/authentication/production#auth-cloud-implicit-python
 https://cloud.google.com/storage/docs/reference/libraries
"""
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/Users/romanbody/git/config/google/RboProject-45348ace0c53.json"

credentials = GoogleCredentials.get_application_default()
service = discovery.build('storage', 'v1', credentials=credentials)

filename = '/Users/romanbody/git/ML/demo/sample.csv'
bucket = 'clear-adapter-232311'

body = {'name': 'dest_file_name5.csv'}
req = service.objects().insert(bucket=bucket, body=body, media_body=filename)
resp = req.execute()