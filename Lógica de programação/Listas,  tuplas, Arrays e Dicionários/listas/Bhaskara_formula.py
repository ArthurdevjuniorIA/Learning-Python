A, B, C = map(float, input().split())
delta = (B**2 - (4*A*C))
if A == 0 or delta<0:
    print("Impossivel calcular")
else:
    raiz_delta = delta**0.5
    bhaskara_formule_positive = (-B+raiz_delta)/ (2*A)
    bhaskara_formule_negative = (-B-raiz_delta)/ (2*A)
    print(f"R1 = {bhaskara_formule_positive:.5f}")
    print(f"R2 = {bhaskara_formule_negative:.5f}")



