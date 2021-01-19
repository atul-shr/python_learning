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

port_df = pd.read_csv(r"D:\learning\lusid-repo\Source-files\portfolio_source_data.csv",header=0,delimiter=",")

# print(port_df)

scope_port = "cut1-filpoc-9999"

print(datetime.now())

# for index,row in port_df.iterrows():
#     # print(row['display_name'],row['code'],row['base_currency'])
#     # print(all_port[0],all_port[1],all_port[2],all_port[3])

#     # details of the new portfolio to be created, created here with the minimum set of mandatory fields
#     request = models.CreateTransactionPortfolioRequest(
#         # descriptive name for the portfolio
#         display_name=row['display_name'],
#         # unique portfolio code, portfolio codes must be unique across scopes
#         code=row['code'],
#         base_currency=row['base_currency'])

#     # create the portfolio in LUSID in the specified scope
#     result = transaction_portfolios_api.create_portfolio(
#         scope=scope_port,
#         create_transaction_portfolio_request=request)

print(datetime.now())


# create the portfolio
# scope = "finbourne"
guid = str(uuid.uuid4())
effective_date = datetime(2018, 1, 1, tzinfo=pytz.utc)

request = models.CreateTransactionPortfolioRequest(
    display_name="portfolio-filpoc-X001",
    code="source1-filpoc-X001",
    base_currency="GBP",
    created=effective_date
)

result = transaction_portfolios_api.create_portfolio(
    scope=scope_port, 
    create_transaction_portfolio_request=request)

portfolio_id = result.id.code

print(portfolio_id)

