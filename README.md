#  Sistema de Descontos — Testes Unitários com Pytest

##  Descrição

Este projeto faz parte da atividade prática da disciplina, na **Opção A: Projeto Aberto (Tema Livre)**.  
O objetivo foi desenvolver uma pequena aplicação com regras de negócio bem definidas e criar **testes unitários automatizados** que garantam a validação dessas regras com **alta cobertura de código**.

A aplicação foi desenvolvida em **Python**, utilizando as ferramentas **Pytest** e **Pytest-Cov**.

---

##  Regras de Negócio Testadas

1. O valor total da compra **não pode ser negativo** (gera erro).  
2. **Clientes VIP** recebem **10% de desconto** no valor total da compra.  
3. Compras **acima de R$ 500,00** recebem um **desconto adicional de 5%**.  
4. Os descontos **são cumulativos** — um cliente VIP com compra acima de R$ 500,00 recebe **15% de desconto total**.  
5. O valor final deve ser **arredondado para duas casas decimais**.

Essas regras foram validadas pelos testes unitários no arquivo `test_app.py`.

---

##  Tecnologias Utilizadas

- **Python 3.11**
- **Pytest**
- **Pytest-Cov**

---

## Exemplo de Saída:
<img width="779" height="198" alt="image" src="https://github.com/user-attachments/assets/23e6c872-9b31-4389-8142-71d4350da0f6" />

