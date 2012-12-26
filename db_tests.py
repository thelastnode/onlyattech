import unittest

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import db

class ValidateSchemaTestCase(unittest.TestCase):
    def testSchema(self):
        self.engine = create_engine('sqlite:///:memory:')

        db.Base.metadata.create_all(self.engine)

        del self.engine

class AuthenticatedUserTestCase(unittest.TestCase):
    def testPasswordHashing(self):
        u = db.AuthenticatedUser('test', 'pw', 'test@example.com', 'Test User')
        assert u.password != 'pw', 'Password is stored in plain-text'
        assert not u.verify_password('wrong pw'), \
            'Incorrect passwords validate'
        assert u.verify_password('pw'), 'Correct passwords do not validate'


class PostTestCase(unittest.TestCase):
    def testUpdatePost(self):
        orig_text = 'the original text'
        new_text = 'new text'

        p = db.Post(orig_text, 'Test', None)
        p.updatePost(new_text)

        assert p.text == new_text, "Didn't correctly update text"
        assert p.original_text == orig_text, 'Original text was not retained'

if __name__ == '__main__':
    unittest.main()
