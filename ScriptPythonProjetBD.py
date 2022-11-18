import sys
import mysql.connector
import keyboard

# Importer la classe Ui_MainWindow du fichier MainWindow.py
from PageUIpython import Ui_MainWindow

# Les librairies PyQT5
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication, QMainWindow

mydb = mysql.connector.connect(
    host="localhost",
    user="joueur",
    password="qwerty",
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
        self.SelectionLivre()
        self.lineEditChapitreVoulu.setText("0")
        self.PremierChapitre()
        self.ButtonChangerChapitre.clicked.connect(self.AfficherChapitre)
        self.RemplissageComboBoxArmes()
        self.RemplissageComboBoxDisciplineKai()
        self.RemplissageComboxBoxDisciplineKaiActuel()
        self.RemplissageComboxBoxArmesActuel()
        self.ButtonAjouterFeuilleAventure.clicked.connect(self.AjoutFeuilleAventure)
        self.ButtonNouvelleSauvegarde.clicked.connect(self.NouvelleSauvegarde)

        texteSauvegarde = self.comboBoxSauvegarde.currentText()    

    #Permet de remplir le comboxBox des livres disponibles
    def SelectionLivre(self):
        
        mycursor.execute("SELECT titre FROM livre")
        myresult = mycursor.fetchall()

        str =''
        for x in myresult:
            for data in x:
                str+=data
            self.comboBoxLivreDisponible.addItem(str)


    #Permet d'afficher le chapitre en question en prenant en compte l'id que l'utilisateur a entré
    def AfficherChapitre(self):

        id_chapitre = self.lineEditChapitreVoulu.text()

        mycursor.execute("SELECT texte FROM chapitre WHERE no_chapitre=%s",(id_chapitre,))
        myresult = mycursor.fetchall()

        str =''
        for x in myresult:
            for data in x:
                str+=data
            self.labelChapitre.setText(str)


    #Permet d'afficher le l'épilogue et le premier chapitre sans a avoir que l'utilisateur ne fasse quoi que ce soit
    def PremierChapitre(self):


        mycursor.execute("SELECT texte FROM chapitre WHERE no_chapitre=0")
        myresult = mycursor.fetchall()
        str =''
        for x in myresult:
            for data in x:
                str+=data

        mycursor.execute("SELECT texte FROM chapitre WHERE no_chapitre=1")
        myresult = mycursor.fetchall()
        str1 =''
        for x in myresult:
            for data in x:
                str1+=data
            self.labelChapitre.setText(str+str1)



    #Permet de remplir le comboxBox des armes disponibles
    def RemplissageComboBoxArmes(self):

        mycursor.execute("SELECT armes_titre FROM item_armes")
        myresult = mycursor.fetchall()
        
        str =''
        for x in myresult:
            for data in x:
                str+=data
            self.comboBoxArmes.addItem(str)
            str=''



    #Permet de remplir le comboxBox des disciplines Kai disponibles
    def RemplissageComboBoxDisciplineKai(self):

        mycursor.execute("SELECT disciplines_kai_titre FROM item_disciplines_kai")
        myresult = mycursor.fetchall()
        
        str =''
        for x in myresult:
            for data in x:
                str+=data
            self.comboBoxDisciplinesKai.addItem(str)
            str=''
    
    #Permet de remplir le comboBox des disciplines kai de l'utilisateur actuellement équipé
    def RemplissageComboxBoxDisciplineKaiActuel(self):

        mycursor.execute("SELECT disciplines_kai_titre FROM item_disciplines_kai INNER JOIN item_disciplines_kai_feuille_aventure ON item_disciplines_kai.id=item_disciplines_kai_feuille_aventure.disciplines_kai_id INNER JOIN feuille_aventure ON disciplines_kai_id=disciplines_kai WHERE item_disciplines_kai.id=feuille_aventure.disciplines_kai")
        myresult = mycursor.fetchall()
        
        str =''
        for x in myresult:
            for data in x:
                str+=data
            self.comboBoxDisciplinesKaiActuel.addItem(str)
            str=''

    #Permet de remplir le comboBox des armes de l'utilisateur actuellement équipé
    def RemplissageComboxBoxArmesActuel(self):

        mycursor.execute("SELECT armes_titre FROM item_armes INNER JOIN item_armes_feuille_aventure ON item_armes.id=item_armes_feuille_aventure.armes_id INNER JOIN feuille_aventure ON armes_id=armes WHERE item_armes.id=feuille_aventure.armes")
        myresult = mycursor.fetchall()
        
        str =''
        for x in myresult:
            for data in x:
                str+=data
            self.comboBoxArmesActuel.addItem(str)
            str=''

    def AjoutFeuilleAventure(self):

        texteSauvegarde = self.comboBoxSauvegarde.currentText()

        TexteArmes=self.comboBoxArmes.currentText()
        if TexteArmes=="Le poignard":
            ReponseArmes=1
        if TexteArmes=="La lance":
            ReponseArmes=2
        if TexteArmes=="La masse d'armes":
            ReponseArmes=3
        if TexteArmes=="Le sabre":
            ReponseArmes=4
        if TexteArmes=="Le marteau de guerre":
            ReponseArmes=5
        if TexteArmes=="L'épée":
            ReponseArmes=6
        if TexteArmes=="La hache":
            ReponseArmes=7
        if TexteArmes=="Le baton":
            ReponseArmes=8
        if TexteArmes=="Le glaive":
            ReponseArmes=9


        TexteDisciplines_kai=self.comboBoxDisciplinesKai.currentText()
        if TexteDisciplines_kai=="Le camouflage":
            ReponseDisciplines_kai=1
        if TexteDisciplines_kai=="La chasse":
            ReponseDisciplines_kai=2
        if TexteDisciplines_kai=="Le sixième sens":
            ReponseDisciplines_kai=3
        if TexteDisciplines_kai=="L'orientation":
            ReponseDisciplines_kai=4
        if TexteDisciplines_kai=="La guérison":
            ReponseDisciplines_kai=5
        if TexteDisciplines_kai=="La Maîtrise des armes":
            ReponseDisciplines_kai=6
        if TexteDisciplines_kai=="Bouclier psychique":
            ReponseDisciplines_kai=7
        if TexteDisciplines_kai=="Puissance psychique":
            ReponseDisciplines_kai=8
        if TexteDisciplines_kai=="Communication animale":
            ReponseDisciplines_kai=9
        if TexteDisciplines_kai=="Maîtrise psychique de la matière":
            ReponseDisciplines_kai=10

        if texteSauvegarde=="Sauvegarde 1":

            sql="INSERT INTO feuille_aventure (sauvegarde, armes, disciplines_kai) VALUES (1, %s, %s)"
            val = (ReponseArmes, ReponseDisciplines_kai)

        if texteSauvegarde=="Sauvegarde 2":          
            sql="INSERT INTO feuille_aventure (sauvegarde, armes, disciplines_kai) VALUES (2, %s, %s)"
            val = (ReponseArmes, ReponseDisciplines_kai)

        if texteSauvegarde=="Sauvegarde 3":         
            sql="INSERT INTO feuille_aventure (sauvegarde, armes, disciplines_kai) VALUES (3, %s, %s)"
            val = (ReponseArmes, ReponseDisciplines_kai)
        

        mycursor.execute(sql, val)
        mydb.commit()

        self.comboBoxArmesActuel.addItem(TexteArmes)
        self.comboBoxDisciplinesKaiActuel.addItem(TexteDisciplines_kai)


    def NouvelleSauvegarde(self):
        texteSauvegarde = self.comboBoxSauvegarde.currentText()
        
        if texteSauvegarde=="Sauvegarde 1":

            chapitreActuel1= self.lineEditChapitreVoulu.text()
            listeArmesActuel1 = self.comboBoxArmesActuel.currentText()
            listeDisciplinesKaiActuel1= self.comboBoxDisciplinesKaiActuel.currentText()

        if texteSauvegarde=="Sauvegarde 2":

            chapitreActuel2= self.lineEditChapitreVoulu.text()
            listeArmesActuel2 = self.comboBoxArmesActuel.currentText()
            listeDisciplinesKaiActuel2= self.comboBoxDisciplinesKaiActuel.currentText()

        if texteSauvegarde=="Sauvegarde 3":

            chapitreActuel3= self.lineEditChapitreVoulu.text()
            listeArmesActuel3 = self.comboBoxArmesActuel.currentText()
            listeDisciplinesKaiActuel3= self.comboBoxDisciplinesKaiActuel.currentText()


        def ChargerSauvegarde():
            if texteSauvegarde=="Sauvegarde 1":
                self.comboBoxArmesActuel.clear()
                self.comboBoxDisciplinesKaiActuel.clear()
                self.lineEditChapitreVoulu.setText(chapitreActuel1)
                self.AfficherChapitre()
                self.comboBoxArmesActuel.addItem(listeArmesActuel1)
                self.comboBoxDisciplinesKaiActuel.addItem(listeDisciplinesKaiActuel1)

            if texteSauvegarde=="Sauvegarde 2":
                self.comboBoxArmesActuel.clear()
                self.comboBoxDisciplinesKaiActuel.clear()
                self.lineEditChapitreVoulu.setText(chapitreActuel2)
                self.AfficherChapitre()
                self.comboBoxArmesActuel.addItem(listeArmesActuel2)
                self.comboBoxDisciplinesKaiActuel.addItem(listeDisciplinesKaiActuel2)

            if texteSauvegarde=="Sauvegarde 3":
                self.comboBoxArmesActuel.clear()
                self.comboBoxDisciplinesKaiActuel.clear()
                self.lineEditChapitreVoulu.setText(chapitreActuel3)
                self.AfficherChapitre()
                self.comboBoxArmesActuel.addItem(listeArmesActuel3)
                self.comboBoxDisciplinesKaiActuel.addItem(listeDisciplinesKaiActuel3)   

        def SupprimerSauvegarde():

            self.comboBoxArmesActuel.clear()
            self.comboBoxDisciplinesKaiActuel.clear()
            self.lineEditChapitreVoulu.setText("0")

            if texteSauvegarde=="Sauvegarde 1":
                chapitreActuel1="0"
            if texteSauvegarde=="Sauvegarde 2":
                chapitreActuel2="0"
            if texteSauvegarde=="Sauvegarde 3":
                chapitreActuel3="0"

            self.PremierChapitre()
        
        self.ButtonChargerSauvegarde.clicked.connect(ChargerSauvegarde)
        self.ButtonSupprimerSauvegarde.clicked.connect(SupprimerSauvegarde)

        if texteSauvegarde=="Sauvegarde 2":

            chapitreActuel2= self.lineEditChapitreVoulu.text()
            listeArmesActuel2 = self.comboBoxArmesActuel.currentText()
            listeDisciplinesKaiActuel2= self.comboBoxDisciplinesKaiActuel.currentText()

        if texteSauvegarde=="Sauvegarde 3":

            chapitreActuel3= self.lineEditChapitreVoulu.text()
            listeArmesActuel3 = self.comboBoxArmesActuel.currentText()
            listeDisciplinesKaiActuel3= self.comboBoxDisciplinesKaiActuel.currentText()

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()