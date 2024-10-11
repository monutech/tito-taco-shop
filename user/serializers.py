from rest_framework import serializers
from user.models import User
from ledger.models import TacoBank


class UserSerializer(serializers.ModelSerializer):

    taco_balance = serializers.SerializerMethodField()

    @classmethod
    def get_taco_balance(csl, user) -> int:
        return TacoBank.objects.get_or_create(user=user)[0].total_tacos if user.is_authenticated else 0

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'unique_id', 'taco_balance')


class UserTransactionSerializer(serializers.Serializer):
    start_date = serializers.CharField()
    end_date = serializers.CharField()


    def validate(self, data):
        start_date = data.get('start_date')
        end_date = data.get('end_date')
        if start_date > end_date:
            raise serializers.ValidationError('Start date needs to be earlier than end date.')
        return {'start_date': start_date, 'end_date': end_date}
