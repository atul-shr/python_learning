from datetime import datetime
import pytz
import threading
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

instruments = []
LUSID_INSTRUMENT_IDENTIFIER = "Instrument/default/LusidInstrumentId"

all_rec = pd.read_csv(r"D:\learning\lusid-repo\Source-files\instrument_source_data.csv",header=0,delimiter=",")
    
for idx, rows in all_rec.iterrows():    
    # print(rows['identifiers_value'])
    instruments.append({"ClientInternal":rows['identifiers_value'], "Name":rows['instrument_name']})

def build_transaction(trade_spec):
    return models.TransactionRequest(
        transaction_id=str(uuid.uuid4()),
        type="StockIn",
        instrument_identifiers={
            LUSID_INSTRUMENT_IDENTIFIER: trade_spec.id
        },
        transaction_date=trade_spec.trade_date,
        settlement_date=trade_spec.trade_date,
        units=100,
        transaction_price=models.TransactionPrice(
            price=trade_spec.price),
        total_consideration=models.CurrencyAndAmount(
            amount=100 * trade_spec.price, 
            currency="GBP"),
        source="Client"
    )

ids = instruments_api.get_instruments(
    identifier_type="ClientInternal", 
    request_body=[i["ClientInternal"] for i in instruments]
)

instrument_ids = [i.lusid_instrument_id for i in ids.values.values()]

# print(instrument_ids)

TransactionSpec = namedtuple('TradeSpec', 'id price trade_date')
trade_specs = [
    TransactionSpec(instrument_ids[0], 101, datetime(2018, 1, 1, tzinfo=pytz.utc)),
    TransactionSpec(instrument_ids[1], 102, datetime(2018, 1, 2, tzinfo=pytz.utc)),
    TransactionSpec(instrument_ids[2], 103, datetime(2018, 1, 3, tzinfo=pytz.utc))
]
trade_specs.sort(key=lambda ts: ts.id)

new_transactions = list(map(build_transaction, trade_specs))

print(new_transactions)