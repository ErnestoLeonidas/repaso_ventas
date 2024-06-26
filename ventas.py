import random
import globales

def precargar_ventas():
    todas_las_ventas = globales.leer_archivo_json('ventas.json')
    todos_los_empleados = globales.leer_archivo_json('empleados.json')
    todos_los_productos = ["Polera", "Pelota", "Camiseta", "Zapatillas", "Pantalon"]

    for i in range(10):
        id_venta = i+1 # es ir a buscar el ultimo id
        nombre_empleado = random.choice(todos_los_empleados)['nombre']
        nombre_producto = random.choice(todos_los_productos)
        # generar un random con valores aproximados a la centena
        # entre el rango 40000 a 80000       
        valor = random.randint(400, 800) * 100

        nueva_venta = {
            "id_venta": id_venta,
            "nombre_empleado": nombre_empleado,
            "nombre_producto": nombre_producto,
            "valor": valor
        }

        todas_las_ventas.append(nueva_venta)

    globales.guardar_archivo_json('ventas.json', todas_las_ventas)
    print("Ventas registradas")
