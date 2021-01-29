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
property_definitions_api = lusid.PropertyDefinitionsApi(api_client)
transaction_portfolios_api = lusid.TransactionPortfoliosApi(api_client)

instruments = []
hold_src = []
LUSID_INSTRUMENT_IDENTIFIER = "Instrument/default/LusidInstrumentId"

all_rec = pd.read_csv(r"D:\learning\lusid-repo\Source-files\holding_source.csv", header=0, delimiter=",")

for idx, rows in all_rec.iterrows():
    # print(rows['identifiers_value'])
    hold_src.append({"portfolio_id": rows['portfolio_id'],
                     "security_id": rows['security_id'],
                     "holding_date": rows['holding_date'],
                     "holding_source": rows['holding_source'],
                     "data_cut": rows['data_cut'],
                     "units": rows['units'],
                     "cost": rows['cost'],
                     "portfolio_cost": rows['portfolio_cost'],
                     "price": rows['price'],
                     "purchase_date": rows['purchase_date'],
                     "settlement_date": rows['settlement_date'],
                     })


# ids = instruments_api.get_instruments(
#     identifier_type="ClientInternal",
#     request_body=[i["security_id"] for i in hold_src]
# )

# print(ids)

# dict_ids = [i.identifiers for i in ids.values.values()]
#
# print(dict_ids)


def get_ins_luid(identifier_type, identifier_val):
    ids = instruments_api.get_instruments(
        identifier_type=identifier_type,
        request_body=[identifier_val]
    )
    return [i.lusid_instrument_id for i in ids.values.values()]


# print(get_ins_luid("ClientInternal", "filInternalId0000001"))

data_cut_property_key = f"Holding/filSource1/data_cut"
holding_source_property_key = f"Holding/filSource1/holding_source"
holding_date_property_key = f"Holding/filSource1/holding_date"

hold_req = [
    models.AdjustHoldingRequest(
        instrument_identifiers={
            LUSID_INSTRUMENT_IDENTIFIER: get_ins_luid("ClientInternal", i["security_id"])[0]
        },
        properties={
            data_cut_property_key: models.PerpetualProperty(key=data_cut_property_key, value=models.PropertyValue(label_value=i["data_cut"])),
            holding_source_property_key: models.PerpetualProperty(key=holding_source_property_key, value=models.PropertyValue(label_value=i["holding_source"])),
            holding_date_property_key: models.PerpetualProperty(key=holding_date_property_key, value=models.PropertyValue(label_value=datetime.strptime(i["holding_date"], '%d-%m-%Y')))
        },
        tax_lots=[
            models.TargetTaxLotRequest(units=i["units"],
                                       price=i["price"],
                                       cost=models.CurrencyAndAmount(amount=i["cost"], currency="GBP"),
                                       portfolio_cost=i["portfolio_cost"],
                                       purchase_date=datetime(int(i["purchase_date"][6:]), int(i["purchase_date"][3:5]), int(i["purchase_date"][:2]), tzinfo=pytz.utc),
                                       settlement_date=datetime(int(i["settlement_date"][6:]), int(i["settlement_date"][3:5]), int(i["settlement_date"][:2]), tzinfo=pytz.utc)
                                       )
        ]) for i in hold_src
]

# print(hold_req[:3])

req_code = "portfolio_id_1"

req_scope = "filSource2"

# res_prop = property_definitions_api.get_property_definition(
#     domain="Holding",
#     scope="filSource1",
#     code="data_cut"
# )
#
#
# print(res_prop)

# day1 = datetime(2021, 1, 22, tzinfo=pytz.utc)

# yyyy-MM-ddTHH:mm:ss.FFFFFFFK

day1 = "2021-01-22NFIL_Cut1"

# set the initial holdings on day 1
response = transaction_portfolios_api.set_holdings(scope=req_scope,
                                                   code=req_code,
                                                   adjust_holding_request=hold_req,
                                                   effective_at=day1)

# print(response)
