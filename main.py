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
def printConsol(string):
	ui.plainTextEdit_3.appendPlainText( string )

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


def bp_start(): # Генерация простых чисел, проверка их на простату, генерация ключей и отправка их участинкам переписки 
	printConsol( "Начинаем..." )
	#
	p = ui.lineEdit.text()
	q = ui.lineEdit_2.text()
	if not(p.isdigit() and q.isdigit()):
		printConsol( "Ошибка. В поля для p и q введите целые числа и нажмите кнопку [НАЧАТЬ]!" )
		printConsol( "~~~~~~~~~~~~~~~~~~~~~~~" )
	else:
		printConsol( "Введены числа\np = " + str(p))
		printConsol( "q = " + str(q))
		printConsol( "~~~~~~~~~~~~~~~~~~~~~~~" )

		printConsol( "Выполним проверку на простоту чисел..." )
		p = int(p)
		q = int(q)
		flagPrime = False
		if checkPrime(p, q) == 3:
		    printConsol( "Проверка 1: Провл. Оба числа не являются простыми" )
		elif checkPrime(p, q) == 1:
		    printConsol( "Проерка 1: Провал. Число p не является простым" )
		elif checkPrime(p, q) == 2:
		    printConsol( "Проерка 1: Провал. Число q не является простым" )
		elif checkPrime(p, q) == 0:
		    printConsol("Проерка 1: Успех. Оба числа являются простыми")
		    flagPrime = True
		printConsol( "~~~~~~~~~~~~~~~~~~~~~~~" )

		if flagPrime == False:
			printConsol( "Необходимо, чтобы числа p и q были простыми. Введите новые числа и нажмите кнопку [НАЧАТЬ].\n" )
		else:
			printConsol( "ЭТАП 1. Генерируем ключи по алгоритму RSA.\n" )
			printConsol( "1.1 Вычисляем n" )
			n = p * q
			printConsol( "n = p * q = " + str(p) + " * " + str(q) + " = " + str(n) + "\n")
			printConsol( "1.2 Вычисляем функцию Эйлера" )
			fe = (p - 1)*(q - 1)
			printConsol( "fe(n) = (p - 1)*(q - 1) = (" + str(p) + " - 1" + ")*(" + str(q) + " - 1" + ") = " + str(fe) + "\n")

	        




def bp_send():
	printConsol( "Сообщение получателю B отправляется...\n" )

def bp_check():
	printConsol( "Сообщение, отправленное получаетелю B проверяется и расшифровывается...\n" )

def bp_refresh():
	ui.plainTextEdit_3.setPlainText(gretings)
	ui.plainTextEdit_3.appendPlainText("Чтобы запустить программу введите p и q затем нажмите кнопку [НАЧАТЬ], расположенную ниже.\n")


ui.plainTextEdit_3.setPlainText(gretings)
ui.plainTextEdit_3.appendPlainText("Чтобы запустить программу введите p и q затем нажмите кнопку [НАЧАТЬ], расположенную ниже.\n")

ui.pushButton.clicked.connect( bp_send )
ui.pushButton_2.clicked.connect( bp_check )
ui.pushButton_3.clicked.connect( bp_start )
ui.pushButton_4.clicked.connect( bp_refresh )


# launch
sys.exit(app.exec_())