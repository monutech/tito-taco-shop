from django.test import TestCase
from ledger.tasks import record_transaction
from ledger.models import TacoLedger
from user.models import User
from model_bakery import baker


class LedgerTests(TestCase):

    def setUp(self):
        self.giver = baker.make(
            User,
            unique_id='ABC123'
        )
        self.receiver = baker.make(
            User,
            unique_id='123ABC'
        )
    

    def test_record_transaction(self):
        good_data = {
            'giver_id': self.giver.unique_id,
            'receiver_id': self.receiver.unique_id,
            'tacos': 2
        }
        not_enough_tacos = {
            'giver_id': self.giver,
            'receiver_id': self.receiver,
            'tacos': 7
        }
        good_result = record_transaction(good_data)
        self.assertTrue(good_result[0])

        bad_result = record_transaction(not_enough_tacos)
        self.assertFalse(bad_result[0])
    

    def tearDown(self):
        TacoLedger.objects.filter(giver=self.giver.unique_id).delete()

