################################################################################
##
## Make RSA Protocol - using main_ui.py (GUI)
## Made by Lamonov K.A. 2020
##
################################################################################


from PySide2 import QtWidgets
from main_ui import Ui_Form
from random import randint
import sys

# create application
app = QtWidgets.QApplication(sys.argv)

# create form and init UI
Form = QtWidgets.QWidget()
ui = Ui_Form()
ui.setupUi(Form)
Form.show()

# logic
GREETINGS = "##########################\n##   Make RSA Protocol  ##\n##     Using Python     ##\n##                      ##\n##       Made by        ##\n##     Lamonov K.A.     ##\n##        2020          ##\n##########################"
TOGO = "Чтобы запустить программу введите сообщение в поле 'Отправитель А', затем нажмите кнопку [START].\n"
ERROR = "########ERROR########\nИсправте ошибку и нажмите кнопку [Начать]\n"

class RSA:
	def __init__(self, *pq):  # konstructor 
		self.p = pq[0][0]
		self.q = pq[0][1]
	
	def start(self):  # firs step making n, eler-func, e & d
		self.n = self.p * self.q
		self.eler = (self.p - 1) * (self.p - 1)
		while True:
			self.e = randint(1, self.eler)
			if nod(self.e, self.eler) == 1: break
		self.d = 0
		while (self.d * self.e) % self.eler != 1:
			self.d += 1

class DigitalSignature:
	def __init__(self, text, d, n):
		self.n = n
		self.h = myHash(text)
		self.s = (self.h ** d) % self.n
	
	def check(self, text, e):
		self._h = myHash(text)
		self.h = (self.s ** e) % self.n
		


def printConsol(string):  # print in plaintext
	ui.plainTextEdit.appendPlainText(string)

def checkPrime(digital):  # check digital for prime
	for i in range(2, int(digital ** 0.5) - 1):
		if digital % i == 0: return False
	return True

def createPQ():  # create random prime p & q
	lst = [num for num in range(2, 201) if checkPrime(num)]
	p = lst[randint(0, len(lst) - 1)]
	q = lst[randint(0, len(lst) - 1)]
	return p, q

def nod(f, s):  # NOD
	lst = []
	if f > s:
		_min = s 
	else:
		_min = f
	for i in range(1, _min + 1):
		if f % i == 0 and s % i == 0:
			lst.append(i)
	return lst[-1]

def myHash(text):
	myHash = 0
	for i in range(len(text)):
		myHash += len(text) + i
	return myHash

def bp():  # button logic
	ui.plainTextEdit.setPlainText(GREETINGS)
	ui.plainTextEdit_3.setPlainText("Получатель B")

	x = RSA(createPQ())

	printConsol( "Числа\np = " + str(x.p))
	printConsol( "q = " + str(x.q))
	printConsol( "~~~~~~~~~~~~~~~~~~~~~~~" )

	x.start()

	printConsol( "ЭТАП 1. Генерируем ключи по алгоритму RSA.\n" )
	printConsol( "1.1 Вычисляем n" )
	printConsol( "n = " + str(x.n) + "\n")

	printConsol( "1.2 Вычисляем функцию Эйлера" )
	printConsol( "fe(n) = " + str(x.eler) + "\n")

	printConsol( "1.3 Выбираем открый ключ e. Взаимно простой с результатом функции Эйлера" )
	printConsol( "e = " + str(x.e) + "\n" )

	printConsol( "1.4 Вычисляем закрытый ключ d." )
	printConsol( "d = " + str(x.d) + "\n")

	printConsol( "Успех. Ключи сгенерированы." )
	printConsol( "~~~~~~~~~~~~~~~~~~~~~~~" )

	printConsol( "ЭТАП 2. Отправка сообщений и Электронной подписи\n" )
	printConsol( "2.1 Вычисление хеш-образа h = h(T), где T - исходное сообщение\n" )

	y = DigitalSignature(ui.plainTextEdit_2.toPlainText(), x.d, x.n)

	printConsol( "h = " + str(y.h) + "\n" )

	printConsol( "2.2 Выроботка цифровой подписи s" )
	printConsol( "s = " + str(y.s) + "\n" )

	printConsol( "Успех. Электронная подпись создана." )
	printConsol( "~~~~~~~~~~~~~~~~~~~~~~~" )

	printConsol( "ЭТАП 3. Получения сообщения и проверка электронной подписи.\n" )
	printConsol( "3.1 Вычисление хеш образа по полученному сообщению h' = h(T')." )

	ui.plainTextEdit_3.setPlainText(ui.plainTextEdit_2.toPlainText())
	ui.plainTextEdit_2.appendPlainText( "\n#########\nХэш-сумма сообщения h(T) = " + str(y.h))
	y.check(ui.plainTextEdit_3.toPlainText(), x.e)

	ui.plainTextEdit_3.appendPlainText("\n\n#########\nХэш-сумма сообещния h'(T') = " + str(y._h))
	printConsol( "h' = " + str(y._h) + "\n")

	printConsol( "3.2 Вычисление хеш-образа из цифровой подписи." )
	printConsol( "h = " + str(y.h) + "\n")

	printConsol( "3.3 Сравнение h' и h." )
	if y.h == y._h:
		printConsol( "Успех. Сообщение T действительно отправлено А." )
	else:
		printConsol( "Провал. Полученное сообщения не было отправелно А." )

		
	# button actions
ui.pushButton.clicked.connect(bp)


	# actions
ui.plainTextEdit.setPlainText(GREETINGS)
ui.plainTextEdit_2.setPlainText("Отправитель A")
ui.plainTextEdit_3.setPlainText("Получатель B")

ui.plainTextEdit.appendPlainText(TOGO)



# launch
sys.exit(app.exec_())