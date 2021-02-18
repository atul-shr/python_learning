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
transaction_portfolios_api = lusid.TransactionPortfoliosApi(api_client)

portfolios_api = lusid.PortfoliosApi(api_client)

limit_counter = 0

request_dict = {}

val_list = []

property_init = "Portfolio/filSource1/"

all_rec = pd.read_csv(r"D:\learning\lusid-repo\Source-files\valuation_source.csv", header=0, delimiter=",")

for idx, rows in all_rec.iterrows():
    val_list.append({
        "val_date": rows['val_date'],
        "cut": rows['cut'],
        "portfolio_id": rows['portfolio_id'],
        "source": rows['source'],
        "base_currency": rows['base_currency'],
        "class_level": rows['class_level'],
        "total_net_assets": rows['total_net_assets'],
        "nav_per_share": rows['nav_per_share'],
        "shares_outstanding": rows['shares_outstanding'],
        "market_value_assets": rows['market_value_assets']
    }
    )

# print(val_list)

val_to_create = {
    property_init + "cut": models.ModelProperty(
        key=property_init + "cut",
        value=models.PropertyValue(label_value='FIL_Cut5'),
        effective_from=datetime(year=2021, month=1, day=17, tzinfo=pytz.utc)
    )
}

print(val_to_create)

print(datetime.now())
# response = portfolios_api.upsert_portfolio_properties(scope='source', code='portfolio_id_201_TF',
#                                                       request_body=val_to_create)
# print(response)
# print(datetime.now())
response = portfolios_api.get_portfolio_properties(scope='source', code='portfolio_id_201_TF',
                                                   effective_at=datetime(year=2021, month=1, day=20,
                                                                         tzinfo=pytz.utc)
                                                   )

# response = portfolios_api.delete_portfolio_properties(scope='source', code='portfolio_id_301_10',
#                                                       property_keys=[property_init + "val_date",
#                                                                      property_init + "cut",
#                                                                      property_init + "class_level",
#                                                                      property_init + "nav_per_share",
#                                                                      property_init + "shares_outstanding",
#                                                                      property_init + "market_value_assets",
#                                                                      property_init + "total_net_assets"]
#                                                       )
print(response)
