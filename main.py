from models import *

print("--- REGISTRO MANUAL DE INVENTARIO (10 OBJETOS) ---")

p1 = Producto(1, "Palomitas Grandes", 85.0, "Snacks")
p2 = Producto(2, "Refresco Mediano", 45.0, "Bebidas")
p3 = Producto(3, "Hot Dog", 60.0, "Comida")
p4 = Producto(4, "Nachos con Queso", 70.0, "Snacks")
p5 = Producto(5, "Chocolate Crunch", 35.0, "Dulces")
p6 = Producto(6, "Agua Ciel 600ml", 30.0, "Bebidas")
p7 = Producto(7, "Combo Pareja", 210.0, "Combos")
p8 = Producto(8, "Entrada 2D Adulto", 80.0, "Boletos")
p9 = Producto(9, "Entrada 3D Niño", 65.0, "Boletos")
p10 = Producto(10, "Cubeta Promocional", 150.0, "Promos")

print(p1.mostrar_detalle())
print(p2.mostrar_detalle())
print(p3.mostrar_detalle())
print(p4.mostrar_detalle())
print(p5.mostrar_detalle())
print(p6.mostrar_detalle())
print(p7.mostrar_detalle())
print(p8.mostrar_detalle())
print(p9.mostrar_detalle())
print(p10.mostrar_detalle())

print("\n-VALIDACION DE DATOS FINALIZADA-")
print("Sistema de Cine")

peliculas = [
    Pelicula("Avengers", 120, "B", "Accion"),
    Pelicula("Toy Story", 95, "A", "Animacion"),
    Pelicula("Joker", 122, "C", "Drama"),
    Pelicula("Batman", 130, "B", "Accion"),
    Pelicula("Titanic", 180, "B", "Romance"),
    Pelicula("Frozen", 102, "A", "Infantil"),
    Pelicula("Matrix", 136, "C", "Ciencia Ficcion"),
    Pelicula("Shrek", 90, "A", "Comedia"),
    Pelicula("Spiderman", 140, "B", "Accion"),
    Pelicula("Coco", 105, "A", "Animacion")
]

for p in peliculas:
    p.obtener_detalles()


salas = [
    Sala(1, "Sala 1", "Piso 1", "2D", 20),
    Sala(2, "Sala 2", "Piso 1", "3D", 15),
    Sala(3, "Sala 3", "Piso 2", "IMAX", 10),
    Sala(4, "Sala 4", "Piso 2", "2D", 25),
    Sala(5, "Sala 5", "Piso 3", "3D", 18),
    Sala(6, "Sala 6", "Piso 3", "2D", 12),
    Sala(7, "Sala 7", "Piso 4", "IMAX", 8),
    Sala(8, "Sala 8", "Piso 4", "2D", 30),
    Sala(9, "Sala 9", "Piso 5", "3D", 22),
    Sala(10, "Sala 10", "Piso 5", "2D", 16)
]

for s in salas:
    s.calcular_asientos_libres()


funciones = []

for i in range(10):
    funcion = Funcion(i+1, peliculas[i], salas[i], "18:00", 80)
    funciones.append(funcion)

for f in funciones:
    f.obtener_detalles_funcion()


usuarios = [
    Usuario(1, "Carlos", "carlos@mail.com", "111"),
    Usuario(2, "Ana", "ana@mail.com", "222"),
    Usuario(3, "Luis", "luis@mail.com", "333"),
    Usuario(4, "Marta", "marta@mail.com", "444"),
    Usuario(5, "Pedro", "pedro@mail.com", "555"),
    Usuario(6, "Sofia", "sofia@mail.com", "666"),
    Usuario(7, "Diego", "diego@mail.com", "777"),
    Usuario(8, "Elena", "elena@mail.com", "888"),
    Usuario(9, "Jorge", "jorge@mail.com", "999"),
    Usuario(10, "Lucia", "lucia@mail.com", "000")
]

for u in usuarios:
    u.login()


empleados = [
    Empleado(11, "Admin1", "admin1@mail.com", "101", "EMP01", "ADMIN"),
    Empleado(12, "Taquilla1", "taquilla@mail.com", "102", "EMP02", "TAQUILLERO"),
    Empleado(13, "Limpieza1", "clean@mail.com", "103", "EMP03", "LIMPIEZA")
]

for e in empleados:
    e.marcar_entrada()
    e.gestionar_funciones()


promociones = [
    Promocion("DESC10", "10% descuento", 0.10),
    Promocion("DESC20", "20% descuento", 0.20),
    Promocion("DESC5", "5% descuento", 0.05),
    Promocion("DESC15", "15% descuento", 0.15),
    Promocion("DESC25", "25% descuento", 0.25)
]


reserva1 = Reserva(1, usuarios[0], funciones[0], ["A1", "A2", "A3"])
reserva1.calcular_total()
reserva1.monto_total = promociones[0].aplicar_descuento(reserva1.monto_total)
reserva1.confirmar_pago()

reserva2 = Reserva(2, usuarios[1], funciones[0], ["A1"])
reserva2.calcular_total()
reserva2.confirmar_pago()

reserva3 = Reserva(3, usuarios[2], funciones[1], ["B1", "B2"])
reserva3.calcular_total()
reserva3.confirmar_pago()

salas[0].calcular_asientos_libres()
salas[1].calcular_asientos_libres()