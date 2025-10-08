# app.py

def calcular_desconto(valor_total, cliente_vip=False):
    """Calcula desconto conforme o tipo de cliente e valor da compra."""
    if valor_total < 0:
        raise ValueError("Valor total não pode ser negativo")

    desconto = 0
    if cliente_vip:
        desconto += 0.10  # 10% de desconto para clientes VIP

    if valor_total > 500:
        desconto += 0.05  # +5% se o valor for maior que 500

    valor_final = valor_total * (1 - desconto)
    return round(valor_final, 2)