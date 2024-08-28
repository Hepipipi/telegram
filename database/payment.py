
from yookassa import Payment
from yookassa.domain.request import PaymentRequest
import uuid
import asyncio


# from yookassa import Configuration

# Configuration.configure('<Идентификатор магазина>', '<Секретный ключ>')
async def create_payment(amount,description,currency='RUB'):
    id_key = str(uuid.uuid4())
    payment = Payment.create(
        {
            'amount': {
                'value': str(amount),
                'currency': currency
            },
            
            'confirmation': {
                'type': 'redirect',
                'return_url': 'https://webhook.site/2cf3d36d-894b-4b37-968b-1a11ff841943'
            },
            "capture": True,
                "description": description,
                "metadata": {
                'order_id': str(uuid.uuid4())
        },
        })
    
    return payment

async def get_payment(payment_id):
    payment = await Payment.find_one(payment_id)
    return payment.status





















