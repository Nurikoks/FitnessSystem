# FitnessSystem

Приложение на Django REST Framework для управления тренерами, залами, расписанием и записями на тренировки с JWT-авторизацией.

---

##  Возможности

- Регистрация новых пользователей (по email и паролю)
- Авторизация пользователей через JWT-токены (SimpleJWT)
- CRUD для:
  - Тренеров
  - Залов
  - Расписания
  - Записей (Booking) — только для авторизованных
- Админ-панель доступна по `/api/v1/admin/`

---

## Быстрый старт

1. **Клонировать проект**  
   ```bash
   git clone https://github.com/Nurikoks/FitnessSystem.git
   cd FitnessSystem
2. Создайте и активируйте виртуальное окружение:

python -m venv venv
venv\Scripts\activate   # для Windows
source venv/bin/activate  # для Linux/Mac


3. Установите зависимости:

pip install -r requirements.txt


4. Примените миграции:

python manage.py migrate


5. Запустите сервер:

python manage.py runserver

---

## API эндпоинты

-Аутентификация
Регистрация:
POST /api/v1/register/
Тело запроса:
json:
{
  "email": "test@example.com",
  "username": "testuser",
  "password": "your_password",
  "password2": "your_password"
}

-Вход (получение токена):
POST /api/v1/login/
Тело запроса:
json:
{
  "email": "test@example.com",
  "password": "your_password"
}

-Обновление токена:
POST /api/v1/login/refresh/
Тело запроса:
json:
{
  "refresh": "your_refresh_token"
}

---

## Фитнес-модуль

Список тренеров: GET /api/v1/fitness/trainers/
Список занятий: GET /api/v1/fitness/schedule/

Пример использования (PowerShell):
Powershell:
"$headers = @{
  "Authorization" = "Bearer <your_access_token>"
}
Invoke-WebRequest -Uri "http://127.0.0.1:8000/api/v1/fitness/trainers/" -Method GET -Headers $headers"

---

## Модели и связи

👤 User (Пользователь)
Наследуется от AbstractUser
Дополнительно:
birthday — дата рождения
Может входить в разные группы/роли (например, Админ, Клиент, Тренер)
Может иметь много записей (Booking)
🔗 Связи:
OneToOne с Trainer (если пользователь является тренером)
OneToMany с Booking (пользователь может делать несколько записей)

🏆 Trainer (Тренер)
Связан с User (один к одному)
Поля:
experience — стаж (в годах)
bio — краткая биография
achievements — спортивные достижения
🔗 Связи:
OneToOne → User
ManyToMany → Gym (через промежуточную модель TrainersGym)
OneToMany → Schedule (через TrainersGym)

🏟️ Gym (Зал)
Поля:
name — название зала
address — адрес
🔗 Связи:
ManyToMany → Trainer (через TrainersGym)
OneToMany → Schedule (через TrainersGym)

🤝 TrainersGym (Связка Тренер–Зал)
Промежуточная таблица для связи многие ко многим между Trainer и Gym.
Используется для того, чтобы один тренер мог работать в нескольких залах, а один зал мог иметь много тренеров.
🔗 Связи:
ManyToOne → Trainer
ManyToOne → Gym
OneToMany → Schedule

📅 Schedule (Расписание)
Поля:
day_of_week — день недели
start_time — время начала
end_time — время окончания
Привязано к конкретному тренеру и залу через TrainersGym.
🔗 Связи:
ManyToOne → TrainersGym
OneToMany → Booking

📌 Booking (Запись)
Поля:
booking_date — дата и время записи
duration_hours — длительность (в часах)
Привязана к конкретному пользователю и конкретному занятию (Schedule).
🔗 Связи:
ManyToOne → User
ManyToOne → Schedule

---

## URL
Все маршруты начинаются с `/api/v1/`.

- **POST** `/register/` — регистрация нового пользователя.  
- **POST** `/login/` — авторизация, получение JWT-токенов.  
- **POST** `/login/refresh/` — обновление access-токена.  
- **GET** `/fitness/trainers/` — список всех тренеров.  
- **POST** `/fitness/trainers/` — добавить нового тренера.  
- **GET** `/fitness/trainers/{id}/` — получить данные конкретного тренера.  
- **PUT/PATCH** `/fitness/trainers/{id}/` — обновить данные тренера.  
- **DELETE** `/fitness/trainers/{id}/` — удалить тренера.  
- **GET** `/fitness/gyms/` — список залов.  
- **POST** `/fitness/gyms/` — добавить новый зал.  
- **GET** `/fitness/gyms/{id}/` — получить данные конкретного зала.  
- **GET** `/fitness/trainers-gyms/` — список связей тренеров и залов.  
- **POST** `/fitness/trainers-gyms/` — создать связь тренер-зал.  
- **GET** `/fitness/schedules/` — список расписаний.  
- **POST** `/fitness/schedules/` — создать расписание.  
- **GET** `/fitness/schedules/{id}/` — получить конкретное расписание.  
- **GET** `/fitness/bookings/` — список всех записей.  
- **POST** `/fitness/bookings/` — создать запись на тренировку.  
- **GET** `/fitness/bookings/{id}/` — получить конкретную запись. 


