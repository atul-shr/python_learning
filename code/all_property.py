import lusid
from lusid.utilities import ApiClientBuilder

api_client = ApiClientBuilder().build(r"D:\learning\lusid-repo\lusid-sdk-python-preview\sdk\tests\secrets.json")

property_definitions_api = lusid.PropertyDefinitionsApi(api_client)

scope_port = "filSource1"

result = property_definitions_api.delete_property_definition(domain="Portfolio", scope=scope_port, code="total_net_assets")

print(result)
