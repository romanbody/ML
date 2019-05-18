#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri May 17 15:56:07 2019

@author: romanbody
"""

# Imports the Google Cloud client library
from google.cloud import storage

# Instantiates a client
storage_client = storage.Client()

# The name for the new bucket
bucket_name = 'my-new-bucket'

# Creates the new bucket
bucket = storage_client.create_bucket(bucket_name)

print('Bucket {} created.'.format(bucket.name))