from database import init_db, SessionLocal
from models import Buyer, Car
from repository.sqlalchemy_repository import SQLAlchemyRepository

# Инициализация базы данных
init_db()

# Создание сессии
session = SessionLocal()

# Репозитории
buyer_repo = SQLAlchemyRepository(session, Buyer)
car_repo = SQLAlchemyRepository(session, Car)

# Добавление покупателя
new_buyer = Buyer(name="John Doe", budget=20000)
buyer_repo.add(new_buyer)

# Добавление автомобиля
new_car = Car(model="Toyota Corolla", price=18000, vin="123456789ABCDEFG")
car_repo.add(new_car)

# Получение всех автомобилей
cars = car_repo.get_all()
print("All cars:", cars)

# Проверка покупателя
buyer = buyer_repo.get_by_id(1)
print("Buyer:", buyer.name, "Budget:", buyer.budget)
