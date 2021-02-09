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

val_df = \
    pd.read_csv(r"D:\learning\lusid-repo\Source-files\valuation_source.csv", header=0, delimiter=",")

val_df["port_code"] = val_df["portfolio_id"] + "_" + val_df["class_level"]

val_mapping = {
    "property_columns": ["cut", "class_level", "total_net_assets", "nav_per_share", "shares_outstanding", "market_value_assets"],
    "properties_scope": "filSource1",
    "portfolio_scope": "source",
    "required": {
        "code": "port_code",
        "display_name": "port_code",
        "base_currency": "base_currency",
    }
}

result = load_from_data_frame(
    api_factory=api_factory,
    scope=val_mapping["portfolio_scope"],
    data_frame=val_df,
    mapping_required=val_mapping["required"],
    mapping_optional={},
    file_type="portfolios",
    # identifier_mapping=val_mapping["identifier_mapping"],
    property_columns=val_mapping["property_columns"],
    properties_scope=val_mapping["properties_scope"]
)

succ, errors = format_portfolios_response(result)
print(pd.DataFrame(data=[{"success": len(succ), "errors": len(errors)}]))
# print(result)
