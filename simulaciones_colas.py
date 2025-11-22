import queue
import time

# Ejemplo 1: Control de acceso en seguridad
class AccessRequest:
    def __init__(self, person, authorized):
        self.person = person
        self.authorized = authorized

    def __str__(self):
        return f"{self.person} - {'Autorizado' if self.authorized else 'Denegado'}"

def security_access_simulation():
    access_queue = queue.Queue()
    # Simulamos solicitudes de acceso
    requests = [
        AccessRequest("Ana", True),
        AccessRequest("Luis", False),
        AccessRequest("Marta", True),
        AccessRequest("Pedro", False),
    ]
    for req in requests:
        access_queue.put(req)
        print(f"Solicitud de acceso recibida: {req.person}")
        time.sleep(0.5)

    print("\nProcesando solicitudes de acceso:")
    while not access_queue.empty():
        req = access_queue.get()
        print(f"Procesando: {req}")
        time.sleep(0.5)

# Ejemplo 2: Línea de ensamblaje en fabricación
class Product:
    def __init__(self, id):
        self.id = id
        self.stages = []

    def __str__(self):
        return f"Producto {self.id} - Etapas: {', '.join(self.stages)}"

def assembly_line_simulation():
    assembly_queue = queue.Queue()
    # Simulamos productos entrando a la línea
    products = [Product(i) for i in range(1, 4)]
    for prod in products:
        assembly_queue.put(prod)
        print(f"Producto en cola: {prod.id}")
        time.sleep(0.5)

    # Simulamos estaciones de trabajo
    stages = ["Corte", "Soldadura", "Pintura"]
    print("\nProcesando línea de ensamblaje:")
    while not assembly_queue.empty():
        prod = assembly_queue.get()
        for stage in stages:
            prod.stages.append(stage)
            print(f"Producto {prod.id} en etapa: {stage}")
            time.sleep(0.5)
        print(f"{prod}\n")

# Ejemplo 3: Sistema de colas para inventario de partes de robots Skynet
class RobotPart:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} (Stock: {self.quantity})"

class InventoryQueue:
    def __init__(self):
        self.part_queues = {}

    def add_part(self, part_name, quantity):
        if part_name not in self.part_queues:
            self.part_queues[part_name] = queue.Queue()
        for _ in range(quantity):
            self.part_queues[part_name].put(RobotPart(part_name, 1))
        print(f"Agregadas {quantity} unidades de {part_name} al inventario.")

    def use_part(self, part_name, amount=1):
        if part_name not in self.part_queues or self.part_queues[part_name].qsize() < amount:
            print(f"No hay suficiente stock de {part_name}.")
            return False
        for _ in range(amount):
            self.part_queues[part_name].get()
        print(f"Usadas {amount} unidades de {part_name}.")
        return True

    def show_inventory(self):
        print("\nInventario actual de partes de robots Skynet:")
        for part, q in self.part_queues.items():
            print(f"- {part}: {q.qsize()} unidades")

def robot_parts_inventory_simulation():
    inventory = InventoryQueue()
    inventory.add_part("CPU", 5)
    inventory.add_part("Sensor óptico", 10)
    inventory.add_part("Actuador hidráulico", 7)
    inventory.show_inventory()
    time.sleep(0.5)
    inventory.use_part("CPU", 2)
    inventory.use_part("Sensor óptico", 4)
    inventory.use_part("Actuador hidráulico", 1)
    inventory.show_inventory()
    time.sleep(0.5)
    inventory.use_part("CPU", 4)  # Intento de usar más de lo disponible
    inventory.show_inventory()

if __name__ == "__main__":
    print("--- Simulación de Control de Acceso (Seguridad) ---")
    security_access_simulation()
    print("\n--- Simulación de Línea de Ensamblaje (Fabricación) ---")
    assembly_line_simulation()
    print("\n--- Simulación de Inventario de Partes de Robots Skynet ---")
    robot_parts_inventory_simulation()
