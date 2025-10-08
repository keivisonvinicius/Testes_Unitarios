# app.py

def calcular_desconto(valor_total, cliente_vip=False):
    
    if valor_total < 0:
        raise ValueError("Valor total não pode ser negativo")

    desconto = 0
    if cliente_vip:
        desconto += 0.10  

    if valor_total > 500:
        desconto += 0.05  

    valor_final = valor_total * (1 - desconto)
    return round(valor_final, 2)