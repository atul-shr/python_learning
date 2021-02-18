from datetime import date, datetime
import pytz
import threading
import uuid
import pandas as pd
import lusid
import lusid.models as models
from lusid.utilities import ApiClientBuilder

api_client = ApiClientBuilder().build(r"D:\learning\lusid-repo\lusid-sdk-python-preview\sdk\tests\secrets.json")

print(api_client)

# instruments_api = lusid.InstrumentsApi(api_client)
# property_definitions_api = lusid.PropertyDefinitionsApi(api_client)
# portfolio_api = lusid.PortfoliosApi(api_client)
transaction_portfolios_api = lusid.TransactionPortfoliosApi(api_client)
reference_portfolios_api = lusid.ReferencePortfolioApi(api_client)


# port_df = pd.read_csv(r"D:\learning\lusid-repo\Source-files\portfolio_source_data.csv",header=0,delimiter=",")

# print(port_df)

scope_port = "filSource1"

print(datetime.now())

# create the portfolio

guid = str(uuid.uuid4())
effective_date = datetime(2018, 1, 1, tzinfo=pytz.utc)

request = models.CreateReferencePortfolioRequest(
    display_name="index_id_001",
    code="index_id_001",
    created=effective_date
)

result = reference_portfolios_api.create_reference_portfolio(
    scope=scope_port,
    create_reference_portfolio_request=request)

print(result)

