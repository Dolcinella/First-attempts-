from application import Application
from ocean import Ocean

ocean1 = Ocean()  # создание океана
ocean1.add_predator()  # добавление хищников
ocean1.add_prey()  # добавление добычи
ocean1.add_obstacles()  # добавление препятствий
app = Application(ocean1)  # подключение к классу для вывода в UI
app.start_application()  # вывод океана на экран
