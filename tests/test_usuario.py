"""
Test usuario endpoints
"""
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_criar_usuario():
    """Test create user endpoint"""
    user_data = {
        "nome": "João Silva",
        "email": "joao@example.com",
        "cpf": "12345678901",
        "telefone": "11987654321",
        "senha": "senha123",
    }

    response = client.post("/api/v1/usuario", json=user_data)
    assert response.status_code == 201
    data = response.json()
    assert data["nome"] == user_data["nome"]
    assert data["email"] == user_data["email"]
    assert "id" in data
