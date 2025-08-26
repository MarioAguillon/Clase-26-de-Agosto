print("*" * 143)
print("TIENDA DE ABARROTES DON LOLO")
print("NIT. 80154727")
print("============FACTURA No 001====================")# Factura con varios productos

# Lista de productos con nombre, precio y cantidad
productos = [
    {"nombre": "Arroz", "precio": 2500, "cantidad": 2},
    {"nombre": "Azúcar", "precio": 3000, "cantidad": 1},
    {"nombre": "Maíz", "precio": 1800, "cantidad": 3},
    {"nombre": "Papa", "precio": 2200, "cantidad": 5}
]

iva_porcentaje = 0.19  # 19% de IVA
subtotal_general = 0
iva_general = 0

print("\n========== FACTURA ==========")
print(f"{'Producto':<10} {'Cant.':<6} {'P.Unit':<10} {'Subtotal':<10} {'IVA':<10}")

# Calcular cada producto
for p in productos:
    subtotal = p["precio"]*p["cantidad"]
    iva = subtotal * iva_porcentaje
    subtotal_general += subtotal
    iva_general += iva
    
    print(f"{p['nombre']:<10} {p['cantidad']:<6} {p['precio']:<10,.2f} {subtotal:<10,.2f} {iva:<10,.2f}")

total = subtotal_general + iva_general

print("============================================")
print(f"{'Subtotal General:':<20} ${subtotal_general:,.2f}")
print(f"{'IVA Total (19%):':<20} ${iva_general:,.2f}")
print(f"{'TOTAL A PAGAR:':<20} ${total:,.2f}")
print("============================================")