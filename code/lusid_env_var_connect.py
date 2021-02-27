import boto3
from botocore.exceptions import ClientError
from datetime import datetime
import pytz
import threading
import uuid
import pandas as pd
import lusid
import lusid.models as models
from lusid.utilities import ApiClientBuilder
import json
import os

with open("secrets.json") as f:
  data = json.load(f)

os.environ['FBN_LUSID_API_URL']=data["api"]["apiUrl"]
os.environ['FBN_TOKEN_URL']=data["api"]["tokenUrl"]
os.environ['FBN_CLIENT_ID']=data["api"]["clientId"]
os.environ['FBN_CLIENT_SECRET']=data["api"]["clientSecret"]
os.environ['FBN_USERNAME']=data["api"]["username"]
os.environ['FBN_PASSWORD']=data["api"]["password"]
os.environ['FBN_APP_NAME']=data["api"]["applicationName"]

print(os.environ['FBN_LUSID_API_URL'])
print(os.environ['FBN_TOKEN_URL'])
print(os.environ['FBN_CLIENT_ID'])
print(os.environ['FBN_CLIENT_SECRET'])
print(os.environ['FBN_USERNAME'])
print(os.environ['FBN_PASSWORD'])

session = boto3.session.Session()
client = session.client(service_name='secretsmanager')

api_client = ApiClientBuilder().build()

print(api_client)

instruments_api = lusid.InstrumentsApi(api_client)
property_definitions_api = lusid.PropertyDefinitionsApi(api_client)
portfolio_api = lusid.PortfoliosApi(api_client)
transaction_portfolios_api = lusid.TransactionPortfoliosApi(api_client)
page_size = 5

property_key = f"Instrument/filInsScope/Instrument_Country"
property_key1 = f"Instrument/filInsScope/exchange"
identifier_type = "LusidInstrumentId"
identifier = "LUID_L7YRVZYK"

# get the instrument with value
response = instruments_api.get_instrument(
    identifier_type=identifier_type,
    identifier=identifier,
    property_keys=[property_key,property_key1],
    as_at="2021-01-22T07:02:35.0000000+00:00"
)


print(response)
