import json

response = """{
            "agreement" : [
            { "usageCD" : null,
              "relationshipID" : null,
              "account" : {
                "bookOfBusinessCD" : "RM03",
                "accountTypeCd" : "TFSA"              
              }
            
            }
            ],
            "streetAddressess" :[
              {
                "uniqueId":1,
                "address": {
                        "streetNum":"535",
                        "streetName": "THE EAST MALL"                  },
                "lastUpdate" : {
                    "userId" : "wcom_user"              }
              }
            ]
            }"""



res = json.loads(response)

for doc in res:
  print(doc)
  for inner in res[doc]:
    print(inner)
