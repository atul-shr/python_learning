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
reference_portfolios_api = lusid.ReferencePortfolioApi(api_client)

print(api_client)

instruments_api = lusid.InstrumentsApi(api_client)

limit_counter = 0

request_dict = {}

cons = []

all_rec = pd.read_csv(r"D:\learning\lusid-repo\Source-files\constituents_weight.csv", header=0, delimiter=",")

# print(all_rec)

for idx, rows in all_rec.iterrows():
    cons.append({"ClientInternal": rows["identifiers_value"],
                 "effective_date": rows["effective_date"],
                 "weight_type": rows["weight_type"],
                 "period_type": rows["period_type"],
                 "period_count": rows["period_count"],
                 "weight": rows["weight"],
                 "currency": rows["currency"]
                 })

# print(cons)


# ClientInternal_to_create = [
#     models.UpsertReferencePortfolioConstituentsRequest(
#         effective_from=i["effective_date"],
#         weight_type=i["weight_type"],
#         period_type=i["period_type"],
# period_count=1
#         constituents=[
#             models.ReferencePortfolioConstituentRequest(
#                 instrument_identifiers={
#                     "instrument/filSource1/ClientInternal": i["ClientInternal"]
#                 },
#                 weight=i["weight"],
#                 currency=i["currency"]
#             )
#         ]
#     ) for i in cons
# ]

# print(str(ClientInternal_to_create)[1:-1])

# add_cons = models.UpsertReferencePortfolioConstituentsRequest(
#     effective_from="2021-02-15",
#     weight_type="Periodical",
#     period_type="Daily",
#     period_count=1,
#     constituents=[
#         models.ReferencePortfolioConstituentRequest(
#             instrument_identifiers={
#                 "Instrument/default/ClientInternal": "filInternalIdRef0001"
#             },
#             weight=0.6,
#             currency="GBP"
#         )
#     ]
# )

# print(add_cons)
#
# print(datetime.now())
# response = reference_portfolios_api.upsert_reference_portfolio_constituents(scope="filSource1",
#                                                                             code="index_id_001",
#                                                                             upsert_reference_portfolio_constituents_request=add_cons)
# print(response)
# print(datetime.now())

for items in cons:
    # print(items)

    each_request = models.UpsertReferencePortfolioConstituentsRequest(
        effective_from=items["effective_date"],
        weight_type=items["weight_type"],
        period_type=items["period_type"],
        period_count=items["period_count"],
        constituents=[
            models.ReferencePortfolioConstituentRequest(
                instrument_identifiers={
                    "Instrument/default/ClientInternal": items["ClientInternal"]
                },
                weight=items["weight"],
                currency=items["currency"]
            )
        ]
    )

    # print(each_request)
    print(datetime.now())
    response = reference_portfolios_api.upsert_reference_portfolio_constituents(scope="filSource1",
                                                                                code="index_id_001",
                                                                                upsert_reference_portfolio_constituents_request=each_request)
    print(datetime.now())
