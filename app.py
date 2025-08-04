from flask import Flask, render_template, jsonify, request, flash, redirect, url_for
from config import Config
from models import db, Profile, Project
from datetime import datetime, timezone  # Исправлено на timezone-aware datetime
from flask_mail import Mail, Message
from flask_wtf import FlaskForm  # Добавлен импорт FlaskForm
from wtforms import StringField, TextAreaField, SubmitField  # Добавлены поля формы
from wtforms.validators import DataRequired, Email  # Добавлены валидаторы


app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
mail = Mail(app)

# Определение формы контактов
class ContactForm(FlaskForm):
    name = StringField('Имя', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    subject = StringField('Тема', validators=[DataRequired()])
    message = TextAreaField('Сообщение', validators=[DataRequired()])
    submit = SubmitField('Отправить')

# Контекстный процессор для добавления переменной now во все шаблоны
@app.context_processor
def inject_now():
    return {'now': datetime.now(timezone.utc)}  # Исправлено на timezone-aware

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

        projects = [
            Project(
                title="Мой сайт-портфолио",
                description="Этот сайт, который вы сейчас просматриваете! Создан с использованием Flask, SQLAlchemy и современных веб-технологий.",
                technologies="Python, Flask, SQLite, HTML, CSS, JavaScript",
                github_url="https://github.com/yourusername/my-portfolio",
                demo_url="http://yourportfolio.com",
                image_url="images/portfolio.png"
            ),
            Project(
                title="Игра на Python",
                description="Классическая игра 'Змейка' с использованием библиотеки Pygame. Реализованы различные уровни сложности и система рекордов.",
                technologies="Python, Pygame",
                github_url="https://github.com/yourusername/snake-game",
                demo_url=None,
                image_url="images/snake.png"
            ),
            Project(
                title="Погодное приложение",
                description="Веб-приложение для просмотра текущей погоды и прогноза на 5 дней. Интеграция с OpenWeatherMap API.",
                technologies="Python, Flask, JavaScript, API",
                github_url="https://github.com/yourusername/weather-app",
                demo_url="http://weather-app.example.com",
                image_url="images/weather.png"
            )
        ]

        for project in projects:
            db.session.add(project)

        db.session.commit()

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

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()

    if form.validate_on_submit():
        # Отправка email
        msg = Message(
            subject=f"Сообщение с портфолио: {form.subject.data}",
            sender=app.config['MAIL_DEFAULT_SENDER'],
            recipients=['your@email.com'],  # Замените на ваш реальный email
            body=f"""
            От: {form.name.data} <{form.email.data}>
            Тема: {form.subject.data}
            
            Сообщение:
            {form.message.data}
            """
        )

        try:
            mail.send(msg)
            flash('Ваше сообщение успешно отправлено! Я свяжусь с вами в ближайшее время.', 'success')
            return redirect(url_for('contact'))
        except Exception as e:
            flash(f'Произошла ошибка при отправке сообщения: {str(e)}', 'danger')

    return render_template('contact.html', page_title='Контакты', form=form)

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