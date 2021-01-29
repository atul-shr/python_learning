# Import system packages

# Import lusid specific packages
# These are the core lusid packages for interacting with the API via Python

import lusid
import lusid.models as models
from lusid.utilities import ApiClientBuilder

import pandas as pd

# Set pandas dataframe display formatting
pd.set_option('display.max_columns', None)
pd.options.display.float_format = '{:,.2f}'.format

# Authenticate our user and create our API client
secrets_path = r"D:\learning\lusid-repo\lusid-sdk-python-preview\sdk\tests\secrets.json"

api_client = ApiClientBuilder().build(secrets_path)

print(api_client)

instruments_api = lusid.InstrumentsApi(api_client)
property_definitions_api = lusid.PropertyDefinitionsApi(api_client)
transaction_portfolios_api = lusid.TransactionPortfoliosApi(api_client)

cut_label_api = lusid.CutLabelDefinitionsApi(api_client)

response = cut_label_api.create_cut_label_definition(create_cut_label_definition_request=models.CutLabelDefinition(
        code="FIL_Cut1",
        display_name="FIL Cut 1",
        description="FIL Cut 1",
        cut_local_time=models.CutLocalTime(
            hours=17,
            minutes=0
        ),
        time_zone="GB"
    ))

print(response)
