#!/usr/bin/env python3.4
# -*- coding: utf-8 -*-
"""
Created on Thu May 16 09:10:08 2019

@author: romanbody
"""
import os
from googleapiclient import discovery
from oauth2client.client import GoogleCredentials


os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/Users/romanbody/git/ML/RboProject-3d694a700687.json"

credentials = GoogleCredentials.get_application_default()
service = discovery.build('storage', 'v1', credentials=credentials)

filename = '/Users/romanbody/git/ML/demo/sample.csv'
bucket = 'clear-adapter-232311'

body = {'name': 'dest_file_name.csv'}
req = service.objects().insert(bucket=bucket, body=body, media_body=filename)
resp = req.execute()