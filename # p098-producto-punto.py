# p098-producto-punto.py
# Cálculo del producto punto de dos vectores (listas)

print('\033[H\033[J')
print("--- Cálculo del Producto Punto ---\n")

# Vectores representados como listas
vector_a = [1, 3, -5]
vector_b = [4, -2, -1]

print(f"Vector A: {vector_a}")
print(f"Vector B: {vector_b}\n")

if len(vector_a) == len(vector_b):
    producto_punto = 0
    for i in range(len(vector_a)):
        producto = vector_a[i] * vector_b[i]
        producto_punto += producto
    print(f"El producto punto de los vectores es: {producto_punto}")
    # Ejemplo: (1*4) + (3*-2) + (-5*-1) = 4 - 6 + 5 = 3
else:
    print("Error: Los vectores deben tener la misma longitud para calcular el producto punto.")
