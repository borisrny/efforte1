from datetime import datetime
from unittest import TestCase

from src.model import user_create, user_list, user_delete
from src.model.registration import registration_post
from src.util.conf import util_init_config


class Test(TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        util_init_config('./config/local_devel_config.yaml')

    def test_user_basic(self):
        r0 = self._register_user(1)
        r1 = self._register_user(2)
        user_delete(r0)
        user_delete(r1)

        users_1 = user_list({})
        u = self._add_user()
        users_2 = user_list({})
        user_delete(u['id'])
        users_3 = user_list({})
        self.assertEqual(len(users_1), len(users_3))
        self.assertEqual(len(users_1), len(users_2) - 1)

    def _add_user(self):
        doc = {
            'first_name': 'Boris',
            'last_name': 'Khanales',
            'dob': datetime.now().date(),
            'phone_number': '2017803283',
            'email': 'khanlesb@yahoo.com'
        }
        return user_create(doc)

    def _register_user(self, id):
        doc = {
            'username': 'testUserName_{}'.format(id),
            'email': 'khanlesb@yahoo.com',
            'password': 'pwd123'
        }
        return registration_post(doc)
