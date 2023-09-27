# Binance order book

Складаєтся із трьох частин:
- binance_book система для отримання данних через сокет та передачі у таскменеджер Redis
- save_data асинхронний запис даних у MongoDB, як окремий сервіс для того, щоб можна було 
створити окремий воркер через Celery у випадку, якщо система не буде встигати записувати 
отримінні дані
- html легке представлення на Flask, як 

## Запуск проекту
Вам знадобиться Git, Docker та Python 3.10
1. Стягти репозиторій
2. Перейти у діреторію проєкту
3. Виконати команду `docker-compose up -d --build`

# Подивитись Web представлення
 Після запуску проєкту відкрити в браузері `http://localhost:8000`
 

# P.S.
Планував доробити автоматичне оновлення даних на вебсторінці