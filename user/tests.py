from django.test import TestCase
from rest_framework.test import APIClient
from model_bakery import baker
from datetime import (datetime, timedelta)


class UserTransactionEndpoint(TestCase):

    def setUp(self):
        self.user = baker.make(
            'user.User'
        )
        self.transaction1 = baker.make(
            'ledger.TacoLedger',
            amount=5,
            receiver='Tito',
            giver=self.user.unique_id,
            timestamp=datetime.now() - timedelta(days=1)
        )
        self.transaction2 = baker.make(
            'ledger.TacoLedger',
            amount=11,
            receiver='Tito',
            giver=self.user.unique_id,
            timestamp=datetime.now()
        )
        self.transaction3 = baker.make(
            'ledger.TacoLedger',
            amount=11,
            giver='Tito',
            receiver=self.user.unique_id,
            timestamp=datetime.now()
        )
        self.api_client = APIClient()
        self.api_client.force_authenticate(user=self.user)
    

    def test_transaction_endpoint(self):

        r = self.api_client.get(
            f'v1/user/{self.user.id}/transaction/',
            start_date=str(datetime.today().date() - timedelta(days=2)),
            end_date=str(datetime.today().date()) 
        )
        self.assertTrue(r.status_code in range(200, 300))

