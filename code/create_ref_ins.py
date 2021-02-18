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

instruments = []

all_rec = pd.read_csv(r"D:\learning\lusid-repo\Source-files\instrument_ref_data.csv", header=0, delimiter=",")

for idx, rows in all_rec.iterrows():
    print(rows['identifiers_value'])
    instruments.append({"ClientInternal": rows['identifiers_value'], "Name": rows['instrument_name']})

# print(instruments)


ClientInternal_to_create = {
    i["ClientInternal"]: models.InstrumentDefinition(
        name=i["Name"],
        identifiers={"ClientInternal": models.InstrumentIdValue(
            value=i["ClientInternal"])},
        look_through_portfolio_id=models.ResourceId(scope="filSource1", code="index_id_001")
    ) for i in instruments
}

print(ClientInternal_to_create)

print(datetime.now())
response = instruments_api.upsert_instruments(request_body=ClientInternal_to_create)
print(len(response.values))
print(datetime.now())
