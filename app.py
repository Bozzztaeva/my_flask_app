from flask import Flask, render_template, request, redirect, url_for

# Создаем экземпляр приложения Flask
app = Flask(__name__)

# Определение маршрута для главной страницы
@app.route('/')
def home():
    # Отображаем шаблон index.html
    return render_template('index.html')

if __name__ == '__main__':
    # Запуск приложения в режиме отладки
    app.run(debug=True, port=5001)
