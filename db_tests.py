import unittest

import db

class UserTestCase(unittest.TestCase):
    def testPasswordHashing(self):
        u = db.User('test', 'pw', 'test@example.com', 'Test User')
        assert u.password != 'pw', 'Password is stored in plain-text'
        assert not u.verify_password('wrong pw'), \
            'Incorrect passwords validate'
        assert u.verify_password('pw'), 'Correct passwords do not validate'

if __name__ == '__main__':
    unittest.main()
