from datetime import datetime
import pytz
import threading
import uuid

import lusid
import lusid.models as models
from lusid.utilities import ApiClientBuilder
from lusid.exceptions import ApiException

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

# response = instruments_api.upsert_instruments_properties(upsert_instrument_property_request={
#     "identifierType": "LusidInstrumentId",
#     "identifier": "LUID_L7YRVZYK",
#     "properties": [
#         {
#             "key": "Instrument/filInsScope/Instrument_Country",
#             "value": {
#                 "labelValue": "UK"
#             },
#             "effectiveFrom": "2018-03-05T12:00:00.0000000+00:00"
#         }
#     ]
# })

# try:
#     property_definitions_api.get_property_definition(
#         domain="Instrument",
#         scope="filInsScope",
#         code="Instrument_Country"
#     )
# except ApiException as e:
#     # property definition doesn't exist (returns 404), so create one
#     property_definition = models.CreatePropertyDefinitionRequest(
#         domain="Instrument",
#         scope="filInsScope",
#         life_time="Perpetual",
#         code="Instrument_Country",
#         display_name="Instrument_Country",
#         value_required=False,
#         data_type_id=models.ResourceId("system", "string"),
#         constraint_style=None, property_description=None
#     )
#
#     # create the property
#     property_definitions_api.create_property_definition(create_property_definition_request=property_definition)
#
# property_value = models.PropertyValue(label_value="UK")
# property_key = f"Instrument/filInsScope/Instrument_Country"
# identifier_type = "LusidInstrumentId"
# identifier = "LUID_L7YRVZYK"
#
# # update the instrument
# response = instruments_api.upsert_instruments_properties(upsert_instrument_property_request=[
#     models.UpsertInstrumentPropertyRequest(
#         identifier_type=identifier_type,
#         identifier=identifier,
#         properties=[models.ModelProperty(key=property_key, value=property_value)]
#     )
# ])

# # get the instrument with value
# instrument = self.instruments_api.get_instrument(
#     identifier_type=identifier_type,
#     identifier=identifier,
#     property_keys=[property_key]
# )

# response = instruments_api.get_instrument_identifier_types()

page_size = 5

# list the instruments, restricting the number that are returned
# instruments = instruments_api.list_instruments(limit=page_size)

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


# print(instruments) #limit=page_size

# portfolios = portfolio_api.list_portfolios()

# print(portfolios)
