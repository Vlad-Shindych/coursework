from manager import TransportManager, JsonVehicleRepository
from transport import Car, Truck, InvalidSeatingCapacityError

def main():
    repository = JsonVehicleRepository('vehicles.json')
    manager = TransportManager(repository)

    while True:
        print("\nДобро пожаловать в систему управления транспортными средствами!")
        print("Введите команду:")
        print("1. Добавить транспортное средство")
        print("2. Удалить транспортное средство")
        print("3. Отобразить все транспортные средства")
        print("4. Сортировать транспортные средства")
        print("5. Выход")

        choice = input("Ваш выбор: ")

        if choice == '1':
            vehicle_type = input("Введите тип транспортного средства (Легковой или Грузовик): ")
            vin = input("Введите VIN-код: ")
            if vehicle_type.lower() == 'легковой':
                model = input("Модель: ")
                color = input("Цвет: ")
                seating_capacity = int(input("Количество мест: "))
                max_speed = int(input("Макс. скорость: "))
                fuel_consumption = float(input("Расход топлива: "))
                tank_capacity = int(input("Ёмкость бака: "))
                try:
                    car = Car(vin, model, color, seating_capacity, max_speed, fuel_consumption, tank_capacity)
                    manager.add_vehicle(car)
                except InvalidSeatingCapacityError as e:
                    print(e)

            elif vehicle_type.lower() == 'грузовик':
                vehicle_type = input("Тип грузовика: ")
                load_capacity = float(input("Грузоподъемность: "))
                max_speed = int(input("Макс. скорость: "))
                fuel_consumption = float(input("Расход топлива: "))
                tank_capacity = int(input("Ёмкость бака: "))
                truck = Truck(vin, vehicle_type, load_capacity, max_speed, fuel_consumption, tank_capacity)
                manager.add_vehicle(truck)
            else:
                print("Неизвестный тип транспортного средства.")

        elif choice == '2':
            vin = input("Введите VIN-код транспортного средства для удаления: ")
            manager.remove_vehicle(vin)

        elif choice == '3':
            manager.display_vehicles()

        elif choice == '4':
            criteria = input("Введите критерий сортировки (vin, модель, цвет, количество мест, макс. скорость, расход топлива, ёмкость бака): ")
            ascending = input("Сортировать по возрастанию? (да/нет): ").lower() == 'да'
            manager.sort_vehicles(criteria, ascending)

        elif choice == '5':
            print("Выход из программы.")
            break

if __name__ == "__main__":
    main()