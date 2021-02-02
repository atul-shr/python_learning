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

quotes_df = \
    pd.read_csv(r"D:\learning\lusid-repo\Source-files\exchange_rate_source.csv", header=0, delimiter=",")

# print(quotes_df)

quotes_df["ins_id"] = quotes_df["from_currency"] + "/" + quotes_df["to_currency"]

# print(quotes_df.columns)
# print(quotes_df.head())
quotes_mapping = {
    "quote_id.quote_series_id.instrument_id_type": "$CurrencyPair",
    "quote_id.effective_at": "effective_date",
    "quote_id.quote_series_id.provider": "$Lusid",
    "quote_id.quote_series_id.priceSource": "source",
    "quote_id.quote_series_id.quote_type": "$Price",
    "quote_id.quote_series_id.instrument_id": "ins_id",
    "metric_value.unit": "$GBP",
    "metric_value.value": "rate",
    "quote_id.quote_series_id.field": "$mid"
}

result = load_from_data_frame(
    api_factory=api_factory,
    scope="filSource1",
    data_frame=quotes_df,
    mapping_required=quotes_mapping,
    mapping_optional={},
    file_type="quotes"
)

# succ, failed, errors = format_quotes_response(result)
# print(pd.DataFrame(data=[{"success": len(succ), "failed": len(failed), "errors": len(errors)}]))
print(result)
