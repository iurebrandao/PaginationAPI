import os
import unittest

from src.models import db
from src.app import app

TEST_DB = 'wine.db'
project_dir = os.path.dirname(os.path.abspath(__file__))


class BasicTests(unittest.TestCase):

    # executed prior to each test
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///{}".format(os.path.join(project_dir, TEST_DB))
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        app.config['PAGE_SIZE'] = 10
        db.init_app(app)
        self.app = app.test_client()

        self.assertEqual(app.debug, False)

    # executed after each test
    def tearDown(self):
        pass

    def test_main_page(self):
        response = self.app.get('/wine?page=1', follow_redirects=True)
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
