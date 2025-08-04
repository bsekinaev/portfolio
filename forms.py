from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class LoginForm(FlaskForm):
    name = StringField('Ваше имя', validators=[
                       DataRequired(message='Пожалуйста, введите имя'),
                       Length(min=3, max=50, message='Имя должно быть от 3 до 50 символов')])
    email = StringField('Ваш email', validators=[
        DataRequired(message='Пожалуйста, введите email'),
        Email(message='Неверный формат email')
    ])
    subject = StringField('Тема', validators=[
        DataRequired(message='Пожалуйста, введите тему')
        Length(min=3, max=100, message='Тема должна быть от 3 до 100 символов')
    ])
    message = StringField('Сообщение', validators=[
        DataRequired(message='Пожалуйста, введите сообщение'),
        Length(min=3, max=1000, message='Сообщение должно быть от 3 до 1000 символов')
    ])
    submit = SubmitField('Отправить сооьбщение')
