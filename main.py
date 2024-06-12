import convert
import sys
import os
from PyQt5 import QtWidgets, uic, QtCore
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import pyqtSignal
import pyttsx3
import find
from deeppavlov import configs, build_model

model = build_model('squad_ru_bert')

class Window1(QtWidgets.QMainWindow):
    login_data = pyqtSignal(str, str)

    def __init__(self):
        super(Window1, self).__init__()
        self.setWindowTitle('Window1')
        uic.loadUi('press.ui', self)
        self.pushButton.clicked.connect(self.enter)
        self.pushButton_2.clicked.connect(self.diss)

    def enter(self):
        self.question = convert.record_volume()
        answer = find.find(self.question, model)
        self.login_data.emit(self.question, answer)
        self.close()

    def diss(self):
        self.close()

class Window2(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window2, self).__init__()
        self.setWindowTitle('Window2')
        uic.loadUi('untitled.ui', self)
        self.pushButton.clicked.connect(self.enter)
        self.pushButton_2.clicked.connect(self.diss)

    def enter(self):
        self.close()

    def diss(self):
        self.close()

class Window3(QtWidgets.QMainWindow):
    number_data = pyqtSignal(str)

    def __init__(self):
        super(Window3, self).__init__()
        self.setWindowTitle('Window1')
        uic.loadUi('main.ui', self)
        self.show()
        dir = [x[0].strip("data\\") for x in os.walk("data")]
        del dir[0]
        dir = [ ''.join(line.split()) for line in dir ]
        self.comboBox.addItems(dir)
        self.main = ExampleApp()
        self.pushButton.clicked.connect(self.enter)
        self.pushButton_2.clicked.connect(self.diss)

    def enter(self):
        self.number = self.comboBox.currentText()
        with open("number.txt", "w") as file:
            file.write(str(self.number))
        self.main.show()
        self.close()

    def diss(self):
        self.close()

class ExampleApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('mywindow.ui', self)
        self.setWindowTitle("VoiceHelper")
        self.setFixedSize(1460, 750)
        self.w1 = Window1()
        self.w2 = Window2()
        self.last_question = ""
        self.last_answer = ""        
        self.pushButton.clicked.connect(self.start)
        self.pushButton_2.clicked.connect(self.search)
        self.pushButton_9.clicked.connect(self.audio)
        self.textEdit.setReadOnly(True)
        self.pushButton_8.clicked.connect(self.present)
        self.pushButton_3.clicked.connect(self.score)
        self.pushButton_4.clicked.connect(self.score)
        self.pushButton_5.clicked.connect(self.score)
        self.pushButton_6.clicked.connect(self.score)   
        self.pushButton_7.clicked.connect(self.score)
        self.w1.login_data[str, str].connect(self.audio_input)
        self.movie = QMovie("material/robot.png")
        self.label.setMovie(self.movie)
        self.movie.start()

    def score(self):
        self.w2.show()
        if self.last_question != "":
            print(self.last_question, self.last_answer)

    def present(self):
        number = ""
        
        with open("number.txt", encoding="utf-8") as file:
            for item in file:
                number += item

        os.system(f"data\{number}\present.ppsx")

    def search(self):
        self.question = self.textEdit_2.toPlainText()
        answer = find.find(self.question, model)
        if answer != 0:
            self.textEdit.append(f"Вы: {self.question}")
            self.textEdit.append(f"Ответ: {answer}")
            self.textEdit_2.clear()
            self.last_question = self.question
            self.last_answer = answer
        else:
            self.textEdit.append(f"Необходимо ввести текст вопроса!")
            self.textEdit_2.clear()  

    def audio(self):
        if self.last_answer != "":
            engine = pyttsx3.init()
            engine.say(self.last_answer)
            engine.runAndWait()

    def audio_input(self, question, answer):
        if answer != 0:
            self.textEdit.append(f"Вы: {question}")
            self.textEdit.append(f"Ответ: {answer}")
            self.textEdit_2.clear()  
            self.last_question = question
            self.last_answer = answer
        else:
            self.textEdit.append(f"Необходимо ввести текст вопроса!")
            self.textEdit_2.clear() 

    def start(self):
        self.w1.show()

def main():
    app = QtWidgets.QApplication(sys.argv) 
    window = Window3()  
    app.exec_() 

if __name__ == '__main__': 
    main() 
