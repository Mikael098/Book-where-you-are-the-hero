import sys
import mysql.connector
import keyboard

# Importer la classe Ui_MainWindow du fichier MainWindow.py
from PageRechercheChapitreUI import Ui_MainWindow

# Les librairies PyQT5
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication, QMainWindow

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="maitre_tenebre_fortier_mikael"
)

mycursor = mydb.cursor()

# En paramêtre de la classe MainWindow on va hériter des fonctionnalités
# de QMainWindow et de notre interface Ui_MainWindow
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        # On va créer la fenêtre avec cette commande
        self.setupUi(self)

        self.lineEditChapitreVoulu.setText("0")
        self.PremierChapitre()
        self.ButtonChangerChapitre.clicked.connect(self.AfficherChapitre)


    def AfficherChapitre(self):

        id_chapitre = self.lineEditChapitreVoulu.text()

        mycursor = mydb.cursor()
        mycursor.execute("SELECT texte FROM chapitre WHERE no_chapitre=%s",(id_chapitre,))
        myresult = mycursor.fetchall()

        str =''
        for x in myresult:
            for data in x:
                str+=data
            print(str)
            self.labelChapitre.setText(str)
        print(str)


    def PremierChapitre(self):
        mycursor = mydb.cursor()
        mycursor.execute("SELECT texte FROM chapitre WHERE no_chapitre=0")
        myresult = mycursor.fetchall()

        str =''
        for x in myresult:
            for data in x:
                str+=data
            print(str)
            self.labelChapitre.setText(str)
    
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()