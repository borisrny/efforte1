from unittest import TestCase

from src.model import business_list, business_create, business_update, business_get, business_delete
from src.util.conf import util_init_config


class Test(TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        util_init_config('./config/local_devel_config.yaml')
        self.bObj = {
            'facilitytype': 'client',
            'name': 'bussiness 1',
            'description': '',
            'phone_number': '',
            'email': '',
            'street1': '',
            'street2': '',
            'city': '',
            'county': '',
            'state': '',
            'postal': '',
            'country': ''
        }
        self.list_fltr = {'businessType': 'client'}

    def test_all(self):
        init_cnt = business_list(self.list_fltr)
        recid = business_create(self.bObj)['id']
        cnt_1 = business_list(self.list_fltr)
        self.assertEqual(len(init_cnt), len(cnt_1) - 1)
        business_update(recid, {'name': 'bussiness 2'})
        doc = business_get(recid)
        self.assertEqual(doc['name'], 'bussiness 2')
        business_delete(recid)
        cnt_1 = business_list(self.list_fltr)
        self.assertEqual(len(init_cnt), len(cnt_1))
