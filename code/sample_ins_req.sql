# create instruments
instruments = [
    {"Figi": "BBG000C6K6G9", "Name": "VODAFONE GROUP PLC"},
    {"Figi": "BBG000C04D57", "Name": "BARCLAYS PLC"},
    {"Figi": "BBG000FV67Q4", "Name": "NATIONAL GRID PLC"},
    {"Figi": "BBG000BF0KW3", "Name": "SAINSBURY (J) PLC"},
    {"Figi": "BBG000BF4KL1", "Name": "TAYLOR WIMPEY PLC"}
]

figis_to_create = {
    i["Figi"]:models.InstrumentDefinition(
        name=i["Name"], 
        identifiers={"Figi": models.InstrumentIdValue(
            value=i["Figi"])}
    ) for i in instruments 
}

upsert_response = api_factory.build(lusid.api.InstrumentsApi).upsert_instruments(request_body=figis_to_create)

if len(upsert_response.failed) != 0:
    raise Exception(upsert_response.failed)

ids = api_factory.build(lusid.api.InstrumentsApi).get_instruments(
    identifier_type="Figi", 
    request_body=[i["Figi"] for i in instruments]
)

instrument_ids = [i.lusid_instrument_id for i in ids.values.values()]