from flask import Flask, render_template, jsonify
from config import Config
from models import db, Profile, Project
from datetime import datetime


app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

# Инициализация базы данных при запуске приложения
with app.app_context():
    db.create_all()
    if not Profile.query.first():
        my_profile = Profile(
            name="Батраз Секинаев",
            title="Junior Python Developer",
            about="Привет! Я начинающий разработчик Python. Создаю веб-приложения и игры на Python. Мой фидбек: \"Я люблю Python!\"",
            skills="Python, Django, Flask, SQL, GIT, GitHub, GitVerse"
        )
        db.session.add(my_profile)

        # Добавляем тестовые проекты
        projects = [
            Project(
                title="Мой сайт-портфолио",
                description="Этот сайт, который вы сейчас просматриваете! Создан с использованием Flask, SQLAlchemy и современных веб-технологий.",
                technologies="Python, Flask, SQLite, HTML, CSS, JavaScript",
                github_url="https://github.com/yourusername/my-portfolio",
                demo_url="http://yourportfolio.com",
                image_url="images/portfolio.png"  # Упрощенный путь
            ),
            Project(
                title="Игра на Python",
                description="Классическая игра 'Змейка' с использованием библиотеки Pygame. Реализованы различные уровни сложности и система рекордов.",
                technologies="Python, Pygame",
                github_url="https://github.com/yourusername/snake-game",
                demo_url=None,
                image_url="images/snake.png"  # Упрощенный путь
            ),
            Project(
                title="Погодное приложение",
                description="Веб-приложение для просмотра текущей погоды и прогноза на 5 дней. Интеграция с OpenWeatherMap API.",
                technologies="Python, Flask, JavaScript, API",
                github_url="https://github.com/yourusername/weather-app",
                demo_url="http://weather-app.example.com",
                image_url="images/weather.png"  # Упрощенный путь
            )
        ]

        for project in projects:
            db.session.add(project)

        db.session.commit()

# Контекстный процессор для добавления переменной now во все шаблоны
@app.context_processor
def inject_now():
    return {'now': datetime.utcnow()}

@app.route('/')
def index():
    return render_template('index.html', page_title='Главная')

@app.route('/about')
def about():
    profile = Profile.query.first()
    return render_template('about.html', page_title='Обо мне', profile=profile)

@app.route('/projects')
def projects():
    projects_list = Project.query.all()
    return render_template('projects.html', page_title='Мои проекты', projects=projects_list)

@app.route('/contact')
def contact():
    return render_template('contact.html', page_title='Контакты')

@app.route('/api/console')
def api_console():
    return render_template('api_console.html', page_title='Консоль API')

@app.route('/api/profile')
def get_profile():
    profile = Profile.query.first()
    if profile:
        return jsonify(profile.to_dict())
    return jsonify({"error": "Профиль не найден"}), 404

@app.route('/api/projects')
def get_projects():
    projects = Project.query.all()
    projects_data = [project.to_dict() for project in projects]
    return jsonify(projects_data)

if __name__ == '__main__':
    app.run(debug=True)