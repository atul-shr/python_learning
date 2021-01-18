from datetime import datetime
import pytz
import threading
import uuid
import pandas as pd
import lusid
import lusid.models as models
from lusid.utilities import ApiClientBuilder
import json 

api_client = ApiClientBuilder().build(r"D:\learning\lusid-repo\lusid-sdk-python-preview\sdk\tests\secrets.json")

print(api_client)

instruments_api = lusid.InstrumentsApi(api_client)

limit_counter = 0

request_dict = {}

for chunks in pd.read_csv(r"D:\learning\lusid-repo\Source-files\instrument_source_data.csv",header=0,delimiter=",",chunksize=2000):
    # print(chunks.head())
    for inner_chunks in chunks.iterrows():
        # print(inner_chunks[1]['request_id'])
        # break
        request_dict[inner_chunks[1]['request_id']] = {}
        request_dict[inner_chunks[1]['request_id']]["name"] = {}
        request_dict[inner_chunks[1]['request_id']]["name"] = inner_chunks[1]["instrument_name"]
        request_dict[inner_chunks[1]['request_id']]["identifiers"] = {}
        request_dict[inner_chunks[1]['request_id']]["identifiers"][inner_chunks[1]['identifiers_name']] = {}
        request_dict[inner_chunks[1]['request_id']]["identifiers"][inner_chunks[1]['identifiers_name']]["value"] = {}
        request_dict[inner_chunks[1]['request_id']]["identifiers"][inner_chunks[1]['identifiers_name']]["value"] = inner_chunks[1]["identifiers_value"]
    with open(r"D:\learning\lusid-repo\Source-files\instrument_req.json", 'w') as fp:
        json.dump(request_dict, fp)        
    response = instruments_api.upsert_instruments(request_body=json.dumps(request_dict))
    print(len(response.values))
    request_dict = {}


