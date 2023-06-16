class Car:
    def __init__(self, model, year):
        self.model = model
        self.year = year

class Bike:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

class Bus:
    def __init__(self, route, capacity):
        self.route = route
        self.capacity = capacity

class TransportVisitor:
    def visit_car(self, car):
        pass

    def visit_bike(self, bike):
        pass

    def visit_bus(self, bus):
        pass

class TransportCollection:
    def __init__(self, transports):
        self.transports = transports

    def accept(self, visitor):
        for transport in self.transports:
            if isinstance(transport, Car):
                visitor.visit_car(transport)
            elif isinstance(transport, Bike):
                visitor.visit_bike(transport)
            elif isinstance(transport, Bus):
                visitor.visit_bus(transport)

class InspectionVisitor(TransportVisitor):
    def visit_car(self, car):
        print(f"Проанализрованный car: {car.model} ({car.year})")

    def visit_bike(self, bike):
        print(f"Проанализрованный bike: {bike.brand} ({bike.color})")

    def visit_bus(self, bus):
        print(f"Проанализрованный bus: Маршрут {bus.route}, Стоимость {bus.capacity}")

transport_collection = TransportCollection([
    Car("Лада калина", 2002),
    Bike("Икарус", "Красно-белый"),
    Bus("967", 50)
])

inspection_visitor = InspectionVisitor()
transport_collection.accept(inspection_visitor)