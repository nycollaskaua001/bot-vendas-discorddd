import json
import os
from datetime import datetime
from config import TRANSACTIONS_FILE, DATA_DIR

def save_transaction(product_name, price, buyer_id, buyer_name, payment_method='PIX'):
    """Salva uma transação realizada"""
    os.makedirs(DATA_DIR, exist_ok=True)
    
    transactions = []
    if os.path.exists(TRANSACTIONS_FILE):
        with open(TRANSACTIONS_FILE, 'r', encoding='utf-8') as f:
            transactions = json.load(f)
    
    transaction = {
        'timestamp': datetime.now().isoformat(),
        'product': product_name,
        'price': price,
        'buyer_id': buyer_id,
        'buyer_name': buyer_name,
        'payment_method': payment_method,
        'status': 'pending'
    }
    
    transactions.append(transaction)
    
    with open(TRANSACTIONS_FILE, 'w', encoding='utf-8') as f:
        json.dump(transactions, f, ensure_ascii=False, indent=2)
    
    return transaction

def get_sales_stats():
    """Retorna estatísticas de vendas"""
    if not os.path.exists(TRANSACTIONS_FILE):
        return {'total': 0, 'revenue': 0.0, 'transactions': []}
    
    with open(TRANSACTIONS_FILE, 'r', encoding='utf-8') as f:
        transactions = json.load(f)
    
    total_sales = len(transactions)
    total_revenue = sum(t['price'] for t in transactions)
    
    return {
        'total': total_sales,
        'revenue': total_revenue,
        'transactions': transactions
    }
