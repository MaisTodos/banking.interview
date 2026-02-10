from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_handle_payment_pix():

    response = client.post("/payment", json={
        "transaction_type": "pix",
        "payload": {
            "pix_key": "test@test.com",
            "amount": 100.50,
            "description": "Test PIX payment"
        }
    })
    assert response.status_code == 200
    assert response.json() == {
        "status": "ok",
        "receiver": {
            "pix_key": "test@test.com",
            "amount": 100.50,
            "description": "Test PIX payment"
        }
    }

def test_handle_payment_ted():
    response = client.post("/payment", json={
        "transaction_type": "ted",
        "payload": {
            "bank_code": "001",
            "agency": "1234",
            "account_number": "56789-0",
            "amount": 250.75
        }
    })
    assert response.status_code == 200
    assert response.json() == {
        "status": 200,
        "tipo": "ted",
        "recebedor": {
            "conta": "001-1234/56789-0",
            "valor": 250.75
        }
    }

def test_handle_payment_boleto():
    response = client.post("/payment", json={
        "transaction_type": "boleto",
        "payload": {
            "payer_name": "John Doe",
            "amount": 500.00
        }
    })
    assert response.status_code == 200
    assert response.json() == {
        "status": "issued",
        "provider": "BoletoGateway",
        "destinatorio": {
            "nome": "John Doe",
            "valor": 500.00
        }
    }
