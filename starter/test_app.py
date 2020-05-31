import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db, Actors, Movies


class CastingTestCase(unittest.TestCase):
    """This class represents the casting test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InAyTkRUM2pfUXB6UzY3QWh5czNtWiJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtY2Fwc3RvbmUtcHJvamVjdC5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWVkMTE5ZDFmZTE5NjIwYzFiNDVhZTJmIiwiYXVkIjoiQWdlbmN5IiwiaWF0IjoxNTkwOTEwMTc4LCJleHAiOjE1OTA5MTczNzgsImF6cCI6ImhuNmZYTWN5eEtBY1BOYUxQYnVSR3JNbExGZ1R3TVVDIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyJdfQ.cVCCJBKrBw5B4pPJknPxfLhZAqzILIip9fUxQPiwJYqKTP5cXnyoYVIgSIBWiGO7nvkgpfuxnlLNFY0RK5zsG7hUyYo0xf0rZScKNbaArPhuvzkPkdbVnqkobopO4q6rMOQVm172NQzm8kYvc0xeJkEKTbpuUlew3CwnYOtqBJQAVJzsE2taEFJrDQPQ9bJOIy-CZyA75ahQqGPNFU0s1fH3pH4sOkTlXAEOGopPEeRsaAiZGS1nnp0gEtVnYOanh6r3gAO_NLepIH6hhAfX3VpUrc6dIoLYKxIXqmacUida-zJQxV8mqBWktY2eaYA_MzQOwTEminZlXwv2p_wAtw"
        self.database_name = "capstone"
        self.database_path = "postgres://{}@{}/{}".format('postgres:123', 'localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass

    # TODO: Write at least one test for each test for successful \
    # operation and for expected errors. -- DONE
    def test_get_actors(self):
        res = self.client().get('/actors', headers={'Authorization': 'Bearer '+self.token})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actors'])

    def test_get_movies(self):
        res = self.client().get('/movies', headers={'Authorization': 'Bearer '+self.token})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_delete_actor(self):
        res = self.client().delete('actors/1', headers={'Authorization': 'Bearer '+self.token})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['Deleted'])

    def test_delete_actor_invalid(self):
        res = self.client().delete('actors/99', headers={'Authorization': 'Bearer '+self.token})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_delete_movie(self):
        res = self.client().delete('movies/1', headers={'Authorization': 'Bearer '+self.token})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['Deleted'])

    def test_delete_movie_invalid(self):
        res = self.client().delete('movies/99', headers={'Authorization': 'Bearer '+self.token})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_post_actor(self):
        new_actor = {
            "name": "john malkovich",
            "age": 65,
            "gender": "Male"
        }
        res = self.client().post('/actors', headers={'Authorization': 'Bearer '+self.token}, json = new_actor)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_post_actor_invalid(self):
        res = self.client().post('/actors', headers={'Authorization': 'Bearer '+self.token})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_post_movie(self):
        new_movie = {
            "title": "being john malkovich",
            "release_date": "1999-11-02"
        }
        res = self.client().post('/movies', headers={'Authorization': 'Bearer '+self.token}, json = new_movie)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_post_movie_invalid(self):
        res = self.client().post('/movies', headers={'Authorization': 'Bearer '+self.token})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_patch_actor(self):
        new_actor = {
            "name": "john malkovich",
        }
        res = self.client().patch('/actors/4', headers={'Authorization': 'Bearer '+self.token}, json = new_actor)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_patch_actor_invalid(self):
        res = self.client().patch('/actors/99', headers={'Authorization': 'Bearer '+self.token})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_patch_movie(self):
        new_movie = {
            "title": "finding nemo",
        }
        res = self.client().patch('/movies/3', headers={'Authorization': 'Bearer '+self.token}), json = new_movie)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_patch_movie_invalid(self):
        res = self.client().patch('/movies/99', headers = {'Authorization': 'Bearer '+self.token})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()