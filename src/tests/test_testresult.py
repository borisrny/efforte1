from unittest import TestCase

from src.model import testresult_list, testresult_create, testresult_last_byuser
from src.util.conf import util_init_config


class Test(TestCase):

    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        util_init_config('./config/local_devel_config.yaml')
        self.userid = 101010
        self.doc1 = {'userid': self.userid, 'postuser': 1, 'fever': 100}
        self.doc2 = {'userid': 2, 'postuser': 1, 'funding1': 0.55}
        self.doc_last = {'funding1': 0.77, 'fever': 98}

    def test_testresult_core(self):
        init_cnt = testresult_list()
        testresult_create(self.userid, 1, self.doc1)['id']
        cnt_1 = testresult_list()
        self.assertEqual(len(init_cnt), len(cnt_1) - 1)
        testresult_create(1, 1, self.doc2)['id']
        cnt_1 = testresult_list()
        self.assertEqual(len(init_cnt), len(cnt_1) - 2)

    def test_testresult_user(self):
        rec = testresult_create(self.userid, 1, self.doc_last)
        doc = testresult_last_byuser(self.userid)
        self.assertDictEqual(Test._pgdict_2_dict(rec), Test._pgdict_2_dict(doc))

    # static
    def _pgdict_2_dict(doc: dict):
        return {k: v for k, v in doc.items()}
