# Epic Title: Personalized Dashboard

from backend.repositories.dashboard.dashboard_repository import DashboardRepository
from backend.models.dashboard.dashboard_model import Account, Transaction

class DashboardService:
    @staticmethod
    def get_user_dashboard(user_id: int) -> dict:
        accounts = DashboardRepository.get_user_accounts(user_id)
        dashboard_data = {'accounts': []}

        for account in accounts:
            transactions = DashboardRepository.get_account_transactions(account.id)
            account_data = {
                'account_number': account.account_number,
                'balance': account.balance,
                'transactions': [{'amount': t.amount, 'transaction_type': t.transaction_type, 'timestamp': t.timestamp} for t in transactions]
            }
            dashboard_data['accounts'].append(account_data)

        return dashboard_data

# File 4: Dashboard Controller in controllers/dashboard/dashboard_controller.py