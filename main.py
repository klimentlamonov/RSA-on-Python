################################################################################
##
## Make RSA Protocol - using main_ui.py (GUI)
## Made by Lamonov K.A. 2020
##
################################################################################


from PySide2 import QtWidgets
from main_ui import Ui_Form
import sys
from random import randint

# create application
app = QtWidgets.QApplication(sys.argv)

# create form and init UI
Form = QtWidgets.QWidget()
ui = Ui_Form()
ui.setupUi(Form)
Form.show()

# logic part
gretings = "##########################\n##   Make RSA Protocol  ##\n##     Using Python     ##\n##                      ##\n##       Made by        ##\n##     Lamonov K.A.     ##\n##        2020          ##\n##########################"
togo = "Чтобы запустить программу введите сообщение в поле 'Отправитель А', введите p и q, затем нажмите кнопку [Начать].\n"
error = "########ERROR########\nИсправте ошибку и нажмите кнопку [Начать]\n"

def printConsol(string):
	ui.plainTextEdit_3.appendPlainText( string )

def myHash(text):
	i = 0
	myHash = 0
	lenght = len(text)
	while i < lenght:
		myHash += lenght + i
		i += 1
	return myHash

def checkPrime(p, q): # проверка на простоту 1-ый способ
	flag = 0
	i = 2
	while i <= int(p ** 0.5):
	    if p % i == 0:
	       	flag += 1
	       	break
	    i += 1

	i = 2
	while i <= int(q ** 0.5):
	    if q % i == 0:
	       	flag += 2
	       	break
	    i += 1

	return flag

def nod(f, s):
	i = 1
	lst = []
	if f > s:
		min = s
	elif f <= s:
		min = f

	while i <= min:
		if f % i == 0 and s % i == 0:
			lst.append(i)
		i += 1
	return lst[-1]

def findD(e, fe):
	d = 0
	while (d * e) % fe != 1:
		d += 1
	return d

def createPQ():
	lst = []
	for num in range(2, 201):
		if checkPrime(num, 4) == 2:
			lst.append(num)

	flag = 0
	while flag != 2:
		i = randint(0, len(lst) - 1)
		if flag == 0:
			p = lst[i]
		elif flag == 1:
			q = lst[i]
		flag += 1
	return p, q

def startRSA():
	p, q = createPQ()
	ui.lineEdit.insert(str(p))
	ui.lineEdit_2.insert(str(q))
	if not(str(p).isdigit() and str(q).isdigit()):
		printConsol( "Ошибка. В поля для p и q введите целые числа!" )
		printConsol( error )
	else:
		printConsol( "Введены числа\np = " + str(p))
		printConsol( "q = " + str(q))
		printConsol( "~~~~~~~~~~~~~~~~~~~~~~~" )

		printConsol( "Выполним проверку на простоту чисел..." )
		p = int(p)
		q = int(q)
		flagPrime = False
		if checkPrime(p, q) == 3:
		    printConsol( "Проверка: Провал. Оба числа не являются простыми" )
		elif checkPrime(p, q) == 1:
		    printConsol( "Проерка: Провал. Число p не является простым" )
		elif checkPrime(p, q) == 2:
		    printConsol( "Проерка: Провал. Число q не является простым" )
		elif checkPrime(p, q) == 0:
		    printConsol("Проерка: Успех. Оба числа являются простыми")
		    flagPrime = True
		printConsol( "~~~~~~~~~~~~~~~~~~~~~~~" )

		if flagPrime == False:
			printConsol( "Необходимо, чтобы числа p и q были простыми.\n" )
			printConsol( error )
		else:
			# first step making keys by RSA algoritm 
			printConsol( "ЭТАП 1. Генерируем ключи по алгоритму RSA.\n" )
			printConsol( "1.1 Вычисляем n" )
			n = p * q
			printConsol( "n = " + str(n) + "\n")

			printConsol( "1.2 Вычисляем функцию Эйлера" )
			fe = (p - 1)*(q - 1)
			printConsol( "fe(n) = " + str(fe) + "\n")

			printConsol( "1.3 Выбираем открый ключ e. Взаимно простой с результатом функции Эйлера" )
			while True:
				e = randint(1, fe)
				if nod(e, fe) == 1:
					printConsol( "e = " + str(e) + "\n" )
					break

			printConsol( "1.4 Вычисляем закрытый ключ d." )
			d = findD(e, fe)
			printConsol( "d = " + str(d) + "\n")

			printConsol( "Успех. Ключи сгенерированы." )
			printConsol( "~~~~~~~~~~~~~~~~~~~~~~~" )

			return n, d, e

def textMessage(n,d):
	printConsol( "ЭТАП 2. Отправка сообщений и Электронной подписи\n" )
	printConsol( "2.1 Вычисление хеш-образа h = h(T), где T - исходное сообщение\n" )
	text = ui.plainTextEdit.toPlainText()
	if text == "":
		printConsol("\nОшибка. В поле 'Отравитель А' отсутствует текст сообщения.\n")
		printConsol( error )
	else:
		h = myHash(text)
		printConsol( "h = " + str(h) + "\n" )

		printConsol( "2.2 Выроботка цифровой подписи s" )
		s = (h ** d) % n
		printConsol( "s = " + str(s) + "\n" )

		printConsol( "Успех. Элктронная подпись создана." )
		printConsol( "~~~~~~~~~~~~~~~~~~~~~~~" )
		ui.plainTextEdit.appendPlainText( "\n#########\nХэш-сумма сообщения h(T) = " + str(h) )

		return text, s

def checkMessage(text, e, n, s):
	printConsol( "ЭТАП 3. Получения сообщения и проверка электронной подписи.\n" )
	printConsol( "3.1 Вычисление хеш образа по полученному сообщению h' = h(T')." )
	h_ = myHash(text)
	ui.plainTextEdit_2.appendPlainText( text + "\n\n#########\nХэш-сумма сообещния h'(T') = " + str(h_))
	printConsol( "h' = " + str(h_) + "\n")

	printConsol( "3.2 Вычисление хеш-образа из цифровой подписи." )
	h = (s ** e) % n
	printConsol( "h = " + str(h) + "\n")

	printConsol( "3.3 Сравнение h' и h." )
	if h == h_:
		printConsol( "Успех. Сообщение T действительно отправлено А." )
	else:
		printConsol( "Провал. Полученное сообщения не было отправелно А." )









def bp_start(): # проверка простых чисел на простоту, генерация ключей и отправка их участинкам переписки 
	printConsol( "Начинаем..." )
	n, d, e = startRSA()

	text, s = textMessage(n, d)

	checkMessage(text, e, n, s)
	


def bp_refresh():
	ui.plainTextEdit_3.setPlainText(gretings)
	ui.plainTextEdit_3.appendPlainText(togo)
	ui.plainTextEdit.setPlainText( "" )
	ui.plainTextEdit_2.setPlainText( "" )
	ui.lineEdit.clear()
	ui.lineEdit_2.clear()



ui.plainTextEdit_3.setPlainText(gretings)
ui.plainTextEdit_3.appendPlainText(togo)

ui.pushButton_3.clicked.connect( bp_start )
ui.pushButton_4.clicked.connect( bp_refresh )


# launch
sys.exit(app.exec_())