class InvalidSeatingCapacityError(Exception):
    """Исключение, возникающее при неверном количестве посадочных мест."""
    pass


class TransportVehicle:
    """Базовый класс для всех транспортных средств."""

    def __init__(self, vin, max_speed, fuel_consumption, tank_capacity):
        self.vin = vin
        self.max_speed = max_speed
        self.fuel_consumption = fuel_consumption
        self.tank_capacity = tank_capacity

    def calculate_fuel_consumption(self, distance):
        return min((distance / 100) * self.fuel_consumption, self.tank_capacity)

    def calculate_speed(self, distance, time):
        return min(distance / time, self.max_speed)


class Car(TransportVehicle):
    def __init__(self, vin, model, color, seating_capacity, max_speed, fuel_consumption, tank_capacity):
        if seating_capacity > 9:
            raise InvalidSeatingCapacityError("Количество посадочных мест не может превышать 9.")
        super().__init__(vin, max_speed, fuel_consumption, tank_capacity)
        self.model = model
        self.color = color
        self.seating_capacity = seating_capacity

    def to_dict(self):
        return {
            'type': 'Car',
            'vin': self.vin,
            'model': self.model,
            'color': self.color,
            'seating_capacity': self.seating_capacity,
            'max_speed': self.max_speed,
            'fuel_consumption': self.fuel_consumption,
            'tank_capacity': self.tank_capacity
        }

class Truck(TransportVehicle):
    def __init__(self, vin, vehicle_type, load_capacity, max_speed, fuel_consumption, tank_capacity):
        super().__init__(vin, max_speed, fuel_consumption, tank_capacity)
        self.vehicle_type = vehicle_type
        self.load_capacity = load_capacity

    def to_dict(self):
        return {
            'type': 'Truck',
            'vin': self.vin,
            'vehicle_type': self.vehicle_type,
            'load_capacity': self.load_capacity,
            'max_speed': self.max_speed,
            'fuel_consumption': self.fuel_consumption,
            'tank_capacity': self.tank_capacity
        }