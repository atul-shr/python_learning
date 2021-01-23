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

try:
    property_definitions_api.get_property_definition(
        domain="Holding",
        scope="filSource1",
        code="data_cut"
    )
except ApiException as e:
    # property definition doesn't exist (returns 404), so create one
    property_definition = models.CreatePropertyDefinitionRequest(
        domain="Holding",
        scope="filSource1",
        life_time="Perpetual",
        code="data_cut",
        display_name="data_cut",
        value_required=False,
        data_type_id=models.ResourceId("system", "string"),
        constraint_style=None, property_description=None
    )

    # create the property
    property_definitions_api.create_property_definition(create_property_definition_request=property_definition)
