import json



client='{"id":"25","nom":"Ndiaye","prenom":"lamine","date_naissance":"1998-10-24 14:07:23","created":"2021-05-23 16:33:58","numero_compte":"7890086","solde_compte":"999196","intitule_compte":"individuel","description":"ce compte est un compte individuel"}'
dicoclient=json.loads(client)
print(dicoclient['id'])

jsonclient=json.dumps(dicoclient)

print(type( jsonclient))