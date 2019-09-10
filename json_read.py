import json

res = json.loads(response)

for doc in res:
  print(doc)
  for inner in res[doc]:
    print(inner)
