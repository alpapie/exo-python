import json
# 1) convertit des données JSON en objet Python ;
client='{"id":"25","nom":"Ndiaye","prenom":"lamine","date_naissance":"1998-10-24 14:07:23","created":"2021-05-23 16:33:58","numero_compte":"7890086","solde_compte":"9999999196","intitule_compte":"individuel","description":"ce compte est un compte individuel"}'
dict_client=json.loads(client)
print(type(dict_client))
print(dict_client['nom'],dict_client['prenom'],dict_client['numero_compte'])
# 2) convertit un objet Python en données JSON.
client_json=json.dumps(dict_client,indent=4)
print(type(client_json))
print(client_json)