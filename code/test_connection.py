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
portfolio_api = lusid.PortfoliosApi(api_client)
transaction_portfolios_api = lusid.TransactionPortfoliosApi(api_client)


# # details of the new portfolio to be created, created here with the minimum set of mandatory fields
# request = models.CreateTransactionPortfolioRequest(

#     # descriptive name for the portfolio
#     display_name="portfolio-filpoc-9999",

#     # unique portfolio code, portfolio codes must be unique across scopes
#     code="source1-filpoc-9999",
#     base_currency="GBP")

# # create the portfolio in LUSID in the specified scope
# result = transaction_portfolios_api.create_portfolio(
#     scope="cut1-filpoc-9999",
#     create_transaction_portfolio_request=request)

# figi = "INR1011"

# response = instruments_api.upsert_instruments(request_body={
#                                                             "fil_request_id_1": {
#                                                                 "name": "pocFilInsName1",
#                                                                 "identifiers": {
#                                                                 "ClientInternal": {
#                                                                     "value": "filInternalId001",
#                                                                     "effectiveAt": "0001-01-01T00:00:00.0000000+00:00"
#                                                                 },
#                                                                 "Sedol": {
#                                                                     "value": "ABCDEFG",
#                                                                     "effectiveAt": "0001-01-01T00:00:00.0000000+00:00"
#                                                                 }
#                                                                 }
#                                                             }
#                                                             }
# )

response = instruments_api.upsert_instruments(request_body={
    "fil_req_id_0000001": {
        "name": "pocFilInsName0000001",
        "identifiers": {
            "ClientInternal": {
                "value": "filInternalId0000001"
            }
        }
    }
})


# response = instruments_api.get_instrument_identifier_types()

page_size = 5

# list the instruments, restricting the number that are returned
# instruments = instruments_api.list_instruments(limit=page_size)

print(response)

# print(instruments) #limit=page_size

# portfolios = portfolio_api.list_portfolios()

# print(portfolios)
