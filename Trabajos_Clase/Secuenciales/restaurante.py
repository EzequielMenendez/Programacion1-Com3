monto = float(input("Ingrese el monto de la cuenta: "))
propina_diez = monto * 0.1
propina_quince = monto * 0.15
total_diez = monto + propina_diez
total_quince = monto + propina_quince

print(f'Propina sugerida (10%): {propina_diez}')
print(f'Total a pagar (10%): {total_diez}')
print(f'Propina sugerida (15%): {propina_quince}')
print(f'Total a pagar (15%): {total_quince}')