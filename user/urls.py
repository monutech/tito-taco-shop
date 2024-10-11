from django.urls import path
from user.views import UserTransactionView


app_name = 'user'

urlpatterns = [
    path('<int:pk>/transaction/', UserTransactionView.as_view({'get': 'list'}), name='user-transaction')
]
