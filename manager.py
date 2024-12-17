import json
from transport import TransportVehicle


class VehicleRepository:
    """Интерфейс для работы с хранилищем транспортных средств."""

    def add(self, vehicle):
        pass

    def remove(self, vin):
        pass

    def get_all(self):
        pass


class JsonVehicleRepository(VehicleRepository):
    def __init__(self, file_path):
        self.file_path = file_path
        self.vehicles = self.load_from_json()

    def load_from_json(self):
        try:
            with open(self.file_path) as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Ошибка загрузки данных: {e}")
            return []  # Возвращаем пустой список при ошибке

    def save_to_json(self):
        with open(self.file_path, 'w') as file:
            json.dump(self.vehicles, file, indent=4)

    def add(self, vehicle):
        if isinstance(vehicle, TransportVehicle):
            self.vehicles.append(vehicle.to_dict())
            self.save_to_json()
        else:
            raise TypeError("Неверный тип транспортного средства.")

    def remove(self, vin):
        self.vehicles = [v for v in self.vehicles if v['vin'] != vin]
        self.save_to_json()

    def get_all(self):
        return self.vehicles


class TransportManager:
    def __init__(self, repository):
        self.repository = repository

    def add_vehicle(self, vehicle):
        self.repository.add(vehicle)

    def remove_vehicle(self, vin):
        self.repository.remove(vin)

    def display_vehicles(self):
        vehicles = self.repository.get_all()
        for vehicle in vehicles:
            print(vehicle)

    def sort_vehicles(self, criteria, ascending=True):
        vehicles = self.repository.get_all()
        if criteria not in ["vin", "model", "color", "seating_capacity", "max_speed", "fuel_consumption", "tank_capacity"]:
            print("Неверный критерий сортировки.")
            return

        vehicles.sort(key=lambda x: x[criteria], reverse=not ascending)
        for vehicle in vehicles:
            print(vehicle)