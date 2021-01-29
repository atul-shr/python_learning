# Import system packages

# Import lusid specific packages
# These are the core lusid packages for interacting with the API via Python
from datetime import datetime
import pytz
import lusid
import lusid.models as models
from lusid.utilities import ApiClientFactory
# from lusidjam.refreshing_token import RefreshingToken
from lusidtools.cocoon.cocoon import load_from_data_frame
from lusidtools.cocoon.cocoon_printer import (
    format_instruments_response,
    format_portfolios_response,
    format_transactions_response,
    format_quotes_response,
    format_holdings_response
)
from lusidtools.pandas_utils.lusid_pandas import lusid_response_to_data_frame

import os
import pandas as pd

# Set pandas dataframe display formatting
pd.set_option('display.max_columns', None)
pd.options.display.float_format = '{:,.2f}'.format

# Authenticate our user and create our API client
secrets_path = r"D:\learning\lusid-repo\lusid-sdk-python-preview\sdk\tests\secrets.json"

# Initiate an API Factory which is the client side object for interacting with LUSID APIs
api_factory = lusid.utilities.ApiClientFactory(
    # token=RefreshingToken(),
    api_secrets_filename=secrets_path,
    app_name="fil-poc-df")

# ins_res = api_factory.build(lusid.api.InstrumentsApi).get_instrument(
#         identifier_type="ClientInternal",
#         identifier="filInternalId0000002")

# print(ins_res)

hold_df = \
    pd.read_csv(r"D:\learning\lusid-repo\Source-files\holding_source.csv", header=0, delimiter=",")

# print(hold_df.head())

# instrument_mapping = {
#     "identifier_mapping": {
#         "ClientInternal": "identifiers_value"
#     },
#     "required": {
#         "name": "instrument_name"
#     },
# }
#
# # Instruments can be loaded using a dataframe with file_type set to "instruments"
# result = load_from_data_frame(
#     api_factory=api_factory,
#     scope="filInsScope",
#     data_frame=instruments_df,
#     mapping_required=instrument_mapping["required"],
#     mapping_optional={},
#     file_type="instruments",
#     identifier_mapping=instrument_mapping["identifier_mapping"],
# )
#
# succ, failed, errors = format_instruments_response(result)
# print(pd.DataFrame(data=[{"success": len(succ), "failed": len(failed), "errors": len(errors)}]))

hold_df["effective_at"] = hold_df[["holding_date"]] + "NFIL_Cut1"
hold_df["currency"] = "GBP"
# print(hold_df.head())
hold_mapping = {
    "identifier_mapping": {
        "ClientInternal": "security_id"
    },
    "property_columns": ["data_cut", "holding_date", "holding_date"],
    "properties_scope": "filSource1",
    "required": {
        "code": "portfolio_id",
        "effective_at": "effective_at",
        "tax_lots.units": "units",
        "tax_lots.cost.amount": "cost",
        "tax_lots.cost.currency": "currency",
        "tax_lots.portfolioCost": "portfolio_cost",
        "tax_lots.price": "price",
        "tax_lots.purchaseDate": "purchase_date",
        "tax_lots.settlementDate": "settlement_date"
    }
}

result = load_from_data_frame(
    api_factory=api_factory,
    scope="filSource1",
    data_frame=hold_df,
    mapping_required=hold_mapping["required"],
    mapping_optional={},
    file_type="holdings",
    identifier_mapping=hold_mapping["identifier_mapping"],
    property_columns=hold_mapping["property_columns"],
    properties_scope=hold_mapping["properties_scope"]
)

succ, errors = format_holdings_response(result)
print(pd.DataFrame(data=[{"success": len(succ), "errors": len(errors)}]))
# print(result)
