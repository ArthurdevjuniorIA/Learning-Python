pedido_usuario,quantidade = map(int,input().split())
possiveis_pedidos = {1: 4.00,2: 4.50, 3: 5.00, 4: 2.00, 5: 1.50}
total = possiveis_pedidos.get(pedido_usuario)*quantidade
print(f"TOTAL:R$ {total:.2f}")
