AUTH0_DOMAIN = 'fsnd-capstone-project.auth0.com'
ALGORITHMS = ['RS256']
API_AUDIENCE = 'Agency'

self.token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InAyTkRUM2pfUXB6UzY3QWh5czNtWiJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtY2Fwc3RvbmUtcHJvamVjdC5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWVkMTE5ZDFmZTE5NjIwYzFiNDVhZTJmIiwiYXVkIjoiQWdlbmN5IiwiaWF0IjoxNTkwOTEwMTc4LCJleHAiOjE1OTA5MTczNzgsImF6cCI6ImhuNmZYTWN5eEtBY1BOYUxQYnVSR3JNbExGZ1R3TVVDIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyJdfQ.cVCCJBKrBw5B4pPJknPxfLhZAqzILIip9fUxQPiwJYqKTP5cXnyoYVIgSIBWiGO7nvkgpfuxnlLNFY0RK5zsG7hUyYo0xf0rZScKNbaArPhuvzkPkdbVnqkobopO4q6rMOQVm172NQzm8kYvc0xeJkEKTbpuUlew3CwnYOtqBJQAVJzsE2taEFJrDQPQ9bJOIy-CZyA75ahQqGPNFU0s1fH3pH4sOkTlXAEOGopPEeRsaAiZGS1nnp0gEtVnYOanh6r3gAO_NLepIH6hhAfX3VpUrc6dIoLYKxIXqmacUida-zJQxV8mqBWktY2eaYA_MzQOwTEminZlXwv2p_wAtw"

database_name = "capstone"
database_path = "postgres://{}@{}/{}".format('postgres:123', 'localhost:5432', database_name)