# test_app.py
import pytest
from app import calcular_desconto

def test_valor_negativo():
    with pytest.raises(ValueError):
        calcular_desconto(-100)

def test_sem_desconto():
    assert calcular_desconto(100) == 100

def test_vip_recebe_desconto():
    assert calcular_desconto(100, cliente_vip=True) == 90

def test_valor_alto_recebe_desconto():
    assert calcular_desconto(600) == 570

def test_vip_valor_alto_recebe_desconto_dobrado():
    # 10% + 5% = 15%
    assert calcular_desconto(600, cliente_vip=True) == 510
