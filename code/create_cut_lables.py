from datetime import datetime
import pytz
import uuid
import pandas as pd
import lusid
import lusid.models as models
from lusid.utilities import ApiClientBuilder
import json
from collections import namedtuple

api_client = ApiClientBuilder().build(r"D:\learning\lusid-repo\lusid-sdk-python-preview\sdk\tests\secrets.json")

print(api_client)

instruments_api = lusid.InstrumentsApi(api_client)

transaction_portfolios_api = lusid.TransactionPortfoliosApi(api_client)

instruments = []
hold_src = []
LUSID_INSTRUMENT_IDENTIFIER = "Instrument/default/LusidInstrumentId"

# all_rec = pd.read_csv(r"D:\learning\lusid-repo\Source-files\holding_source.csv", header=0, delimiter=",")

# res = api_client.call_api('/api/systemconfiguration/cutlabels', 'GET')

# print(res)

sys_config_api = lusid.SystemConfigurationApi(api_client)


print(dir(sys_config_api))
