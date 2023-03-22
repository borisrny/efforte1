from unittest import TestCase
from src.model import notification_list, notification_create, notification_update, notification_get, notification_delete
from src.util.conf import util_init_config


class Test(TestCase):
    def test_all(self):
        util_init_config('./config/local_devel_config.yaml')
        init_cnt = notification_list()
        obj = {'text': 'text 1'}
        recid = notification_create(obj)['id']
        cnt_1 = notification_list()
        self.assertEqual(len(init_cnt), len(cnt_1) - 1)
        notification_update(recid, {'text': 'text 2'})
        doc = notification_get(recid)
        self.assertEqual(doc['text'], 'text 2')
        notification_delete(recid)
        cnt_1 = notification_list()
        self.assertEqual(len(init_cnt), len(cnt_1))
