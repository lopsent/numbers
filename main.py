import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit, QMessageBox
import random

class GuessNumberGame(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Угадай число')
        self.setGeometry(100, 100, 300, 200)

        self.number_to_guess = random.randint(0, 100)
        self.attempts = 5

        self.layout = QVBoxLayout()

        self.info_label = QLabel('Угадайте число от 0 до 100')
        self.layout.addWidget(self.info_label)

        self.hint_label = QLabel('')
        self.layout.addWidget(self.hint_label)
        self.hint2_label = QLabel('')
        self.layout.addWidget(self.hint2_label)

        self.input_layout = QHBoxLayout()
        self.input_label = QLabel('Введите число:')
        self.input_layout.addWidget(self.input_label)
        self.input_field = QLineEdit()
        self.input_layout.addWidget(self.input_field)
        self.layout.addLayout(self.input_layout)

        self.submit_button = QPushButton('Проверить')
        self.submit_button.clicked.connect(self.checkNumber)
        self.layout.addWidget(self.submit_button)

        self.restart_button = QPushButton('Начать заново')
        self.restart_button.clicked.connect(self.restartGame)
        self.layout.addWidget(self.restart_button)

        self.setLayout(self.layout)

    def checkNumber(self):
        guess_text = self.input_field.text()
        if not guess_text.isdigit():
            QMessageBox.warning(self, 'Ошибка', 'Пожалуйста, введите только цифры.')
            return

        guess = int(guess_text)
        if guess < 0 or guess > 100:
            QMessageBox.warning(self, 'Ошибка', 'Пожалуйста, введите число от 0 до 100.')
            return

        if guess < self.number_to_guess:
            self.hint_label.setText('Загаданное число больше')
        elif guess > self.number_to_guess:
            self.hint_label.setText('Загаданное число меньше')
        else:
            self.hint_label.setText('Вы угадали!')
            self.submit_button.setEnabled(False)
            self.input_field.setEnabled(False)
            return

        self.attempts -= 1
        if self.attempts == 0:
            self.hint2_label.setText(f'Вы проиграли. Было загадано число {self.number_to_guess}')
            self.submit_button.setEnabled(False)
            self.input_field.setEnabled(False)
        else:
            self.hint2_label.setText(f'У вас осталось {self.attempts} попыток. Попробуйте еще раз')

    def restartGame(self):
        self.number_to_guess = random.randint(0, 100)
        self.attempts = 5
        self.hint_label.setText('')
        self.submit_button.setEnabled(True)
        self.input_field.setEnabled(True)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    game = GuessNumberGame()
    game.show()
    sys.exit(app.exec())