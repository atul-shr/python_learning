from datetime import datetime
import pytz
import threading
import uuid

import lusid
import lusid.models as models
from lusid.utilities import ApiClientBuilder

api_client = ApiClientBuilder().build(r"D:\learning\lusid-repo\lusid-sdk-python-preview\sdk\tests\secrets.json")

print(api_client)

instruments_api = lusid.InstrumentsApi(api_client)
property_definitions_api = lusid.PropertyDefinitionsApi(api_client)

response = instruments_api.upsert_instruments(request_body={

    "BBG000FD1111": models.InstrumentDefinition(
        name="Test poc lusid",
        identifiers={
            "Figi": models.InstrumentIdValue(value="BBG000FD1111"),
            "ClientInternal": models.InstrumentIdValue(value="internal_id_1")
        }
    )
})


print(response)