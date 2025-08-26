print("*" * 143)
print("TIENDA DE ABARROTES DON LOLO")
print("NIT. 80154727")
print("============FACTURA No 001====================")

#Factura con productos de la canasta familiar
#productos connombre precio y cantidad

productos=[
    {"nombre":"Arroz","precio":2500,"cantidad":2},
    {"nombre":"Azúcar","precio":3000,"cantidad":1},
    {"nombre":"Maíz","precio":1800,"cantidad":3},
    {"nombre":"Papa","precio":2200,"cantidad":5}
]
Iva_porcentaje=0.19 #19% de iva
Subtotal_general=0
iva_general=0

print("\n===========FACTURA No 001==========")
print(f"{'producto':<10}{'Cant.':<6}{'P.Unitario':<10} {'Subtotal':<10}{'Iva':<10}")

#calcular cada producto
for p in productos:
    subtotal = p["precio"]*p["cantidad"]
    iva = subtotal*Iva_porcentaje
    subtotal_general +=subtotal
    iva_general +=iva

    print(f"{p['nombre']:<10} {p['cantidad']:<6}{p['precio']:<10,.2f}{subtotal:<10,.2f}{iva:<10,.2f}")

total=subtotal_general+iva_general

print("=" * 143)
print(f"{'Subtotal General:':<20'}$(subtotal_general:,.2f)")
print(f"{'IVA Total(19):':<20} ${iva_general:,2f}")
print(f"{'TOTAL A PAGAR:':<20} ${total:,2f}")
print("=" * 143)
