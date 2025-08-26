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

## Структура проекта
FitnessSystem/
│
├── fitness/              # Приложение фитнеса
│   ├── migrations/
│   ├── models.py         # Модели (User, Trainer, Schedule и т.д.)
│   ├── views.py          # ViewSet-ы
│   ├── serializers.py    # Сериализаторы
│   ├── urls.py           # Маршруты приложения
│
├── FitnessSystem/        # Конфигурация проекта
│   ├── settings.py
│   ├── urls.py
│
├── manage.py
├── requirements.txt
└── README.md
