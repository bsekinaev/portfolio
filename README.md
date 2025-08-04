# Портфолио на Flask 
![Flask Portfolio](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)
Темное неоновое портфолио, созданное с использованием Flask, с интерактивными элементами и REST API.
## ✨ Особенности
- **Современный дизайн** в темном неоновом стиле
- **Интерактивная API консоль** для тестирования REST API
- **Адаптивная верстка** для всех устройств
- **Система проектов** с фильтрацией по технологиям
- **Контактная форма** с отправкой email
- **Анимации и эффекты** для улучшения пользовательского опыта
## 🚀 Технологии
- **Backend**: Python, Flask, Flask-SQLAlchemy, Flask-WTF, Flask-Mail
- **Frontend**: HTML5, CSS3 (с использованием CSS-переменных), JavaScript
- **База данных**: SQLite
- **API**: RESTful API для доступа к данным портфолио
- **Деплой**: Готово к деплою на Heroku, Vercel или PythonAnywhere
## 🛠️ Установка и запуск
### Требования
- Python 3.8+
- pip
### Инструкция по установке
1. Клонируйте репозиторий:
```bash
git clone https://github.com/batraz-sekinae/flask-portfolio.git
cd flask-portfolio
```
2. Создайте виртуальное окружение:
```bash
python -m venv venv
source venv/bin/activate  # Для Linux/MacOS
venv\Scripts\activate    # Для Windows
```
3. Установите зависимости:
```bash
pip install -r requirements.txt
```
4. Создайте файл конфигурации `.env` (на основе примера):
```bash
cp .env.example .env
```
5. Заполните конфигурацию в `.env`:
```ini
SECRET_KEY=your-very-secret-key
MAIL_USERNAME=your-email@example.com
MAIL_PASSWORD=your-email-password
```
6. Инициализируйте базу данных:
```bash
python app.py
```
7. Запустите приложение:
```bash
python app.py
```
8. Откройте в браузере: [http://localhost:5000](http://localhost:5000)
## 🖥️ Структура проекта
```
flask-portfolio/
├── app/
│   ├── __init__.py
│   ├── app.py                 # Главное приложение
│   ├── config.py              # Конфигурация
│   ├── forms.py               # Формы (контактная форма)
│   ├── models.py              # Модели базы данных
│   ├── templates/             # HTML шаблоны
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── about.html
│   │   ├── projects.html
│   │   ├── contact.html
│   │   └── api_console.html
│   └── static/
│       ├── css/
│       │   ├── main.css
│       │   ├── neon.css
│       │   ├── forms.css
│       │   └── animations.css
│       ├── js/
│       │   └── main.js
│       └── images/
│           ├── portfolio.png
│           ├── snake.png
│           └── weather.png
├── .env.example               # Пример конфигурации среды
├── requirements.txt           # Зависимости
├── .gitignore                 # Игнорируемые файлы
└── README.md                  # Этот файл
```
## 🌐 API Endpoints
- `GET /api/profile` - Получить данные профиля в формате JSON
- `GET /api/projects` - Получить список проектов в формате JSON
  Пример использования:
```bash
curl http://localhost:5000/api/profile
```
Ответ:
```json
{
  "about": "Привет! Я начинающий разработчик Python...",
  "id": 1,
  "name": "Батраз Секинаев",
  "skills": [
    "Python",
    "Django",
    "Flask",
    "SQL",
    "GIT",
    "GitHub",
    "GitVerse"
  ],
  "title": "Junior Python Developer"
}
```
## 🎨 Скриншоты
### Главная страница
![Главная страница](screenshots/home.png)
### Проекты
![Страница проектов](screenshots/projects.png)
### API Консоль
![API Консоль](screenshots/api_console.png)
### Обо мне
![Страница обо мне](screenshots/about.png)
### Контакты
![Контактная форма](screenshots/contact.png)
## 📄 Лицензия
Этот проект распространяется под лицензией MIT. См. файл [LICENSE](LICENSE) для получения дополнительной информации.
---
**Разработано с ❤️ Батразом Секинаевым**  
[![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/batraz-sekinae)
[![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/batraz-sekinae)
[![Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/batraz_sekinae)
```
