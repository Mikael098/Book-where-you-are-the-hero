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

#Permet de se connecter à un utilisateur avec des droits limités
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


        #Déclaration des fonctions
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

        self.lineEdit_objets.setText("")
        self.lineEdit_repas.setText("")
        self.lineEdit_objetsSpeciaux.setText("")

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


        
        ReponseObjets = self.lineEdit_objets.text()
        ReponseRepas = self.lineEdit_repas.text()
        ReponseObjetsSpeciaux = self.lineEdit_objetsSpeciaux.text()
        ReponseChapitre=self.lineEditChapitreVoulu.text()
        


        if texteSauvegarde=="Sauvegarde 1":

            sql="INSERT INTO feuille_aventure (sauvegarde, armes, disciplines_kai, objets, repas, objets_speciaux,chapitre_actuel) VALUES (1, %s, %s, %s, %s, %s,%s)"
            val = (ReponseArmes, ReponseDisciplines_kai, ReponseObjets, ReponseRepas, ReponseObjetsSpeciaux, ReponseChapitre)

        if texteSauvegarde=="Sauvegarde 2":          
            sql="INSERT INTO feuille_aventure (sauvegarde, armes, disciplines_kai, objets, repas, objets_speciaux,chapitre_actuel) VALUES (2, %s, %s, %s, %s, %s,%s)"
            val = (ReponseArmes, ReponseDisciplines_kai, ReponseObjets, ReponseRepas, ReponseObjetsSpeciaux, ReponseChapitre)

        if texteSauvegarde=="Sauvegarde 3":         
            sql="INSERT INTO feuille_aventure (sauvegarde, armes, disciplines_kai, objets, repas, objets_speciaux,chapitre_actuel) VALUES (3, %s, %s, %s, %s, %s,%s)"
            val = (ReponseArmes, ReponseDisciplines_kai, ReponseObjets, ReponseRepas, ReponseObjetsSpeciaux, ReponseChapitre)
        

        mycursor.execute(sql, val)
        mydb.commit()

        self.comboBoxArmesActuel.addItem(TexteArmes)
        self.comboBoxDisciplinesKaiActuel.addItem(TexteDisciplines_kai)


    def NouvelleSauvegarde(self):

        #SupprimerSauvegarde()
        texteSauvegarde = self.comboBoxSauvegarde.currentText()

        TexteArmes=self.comboBoxArmes.currentText()
        if TexteArmes=="Le poignard":
            listeArmesActuel=1
            listeArmesActuelNom ="Le poignard"

        if TexteArmes=="La lance":
            listeArmesActuel=2
            listeArmesActuelNom ="La lance"

        if TexteArmes=="La masse d'armes":
            listeArmesActuel=3
            listeArmesActuelNom ="La masse d'armes"

        if TexteArmes=="Le sabre":
            listeArmesActuel=4
            listeArmesActuelNom ="Le sabre"

        if TexteArmes=="Le marteau de guerre":
            listeArmesActuel=5
            listeArmesActuelNom ="Le marteau de guerre"

        if TexteArmes=="L'épée":
            listeArmesActuel=6
            listeArmesActuelNom ="L'épée"

        if TexteArmes=="La hache":
            listeArmesActuel=7
            listeArmesActuelNom ="La hache"

        if TexteArmes=="Le baton":
            listeArmesActuel=8
            listeArmesActuelNom ="Le baton"

        if TexteArmes=="Le glaive":
            listeArmesActuel=9
            listeArmesActuelNom ="Le glaive"


        TexteDisciplines_kai=self.comboBoxDisciplinesKai.currentText()
        if TexteDisciplines_kai=="Le camouflage":
            listeDisciplinesKaiActuel=1
            listeDisciplinesKaiActuelNom="Le camouflage"

        if TexteDisciplines_kai=="La chasse":
            listeDisciplinesKaiActuel=2
            listeDisciplinesKaiActuelNom="La chasse"

        if TexteDisciplines_kai=="Le sixième sens":
            listeDisciplinesKaiActuel=3
            listeDisciplinesKaiActuelNom="Le sixième sens"

        if TexteDisciplines_kai=="L'orientation":
            listeDisciplinesKaiActuel=4
            listeDisciplinesKaiActuelNom="L'orientation" 

        if TexteDisciplines_kai=="La guérison":
            listeDisciplinesKaiActuel=5
            listeDisciplinesKaiActuelNom="La guérison"

        if TexteDisciplines_kai=="La Maîtrise des armes":
            listeDisciplinesKaiActuel=6
            listeDisciplinesKaiActuelNom="La Maîtrise des armes"

        if TexteDisciplines_kai=="Bouclier psychique":
            listeDisciplinesKaiActuel=7
            listeDisciplinesKaiActuelNom="Bouclier psychique"

        if TexteDisciplines_kai=="Puissance psychique":
            listeDisciplinesKaiActuel=8
            listeDisciplinesKaiActuelNom="Puissance psychique"

        if TexteDisciplines_kai=="Communication animale":
            listeDisciplinesKaiActuel=9
            listeDisciplinesKaiActuelNom="Communication animale"         

        if TexteDisciplines_kai=="Maîtrise psychique de la matière":
            listeDisciplinesKaiActuel=10
            listeDisciplinesKaiActuelNom="Maîtrise psychique de la matière"

        texteSauvegarde = self.comboBoxSauvegarde.currentText()
        
        if texteSauvegarde=="Sauvegarde 1":

            chapitreActuel1= self.lineEditChapitreVoulu.text()
            ObjetsActuel1 = self.lineEdit_objets.text()
            RepasActuel1 = self.lineEdit_repas.text()
            ObjetsSpeciauxActuel1 = self.lineEdit_objetsSpeciaux.text()
            ChapitreActuel1 = self.lineEditChapitreVoulu.text()
            listeDisciplinesKaiActuel1 = listeDisciplinesKaiActuel
            listeArmesActuel1 = listeArmesActuel
            


            sql="INSERT INTO feuille_aventure (sauvegarde, armes, disciplines_kai, objets, repas, objets_speciaux, chapitre_actuel) VALUES (1, %s, %s, %s, %s, %s, %s)"
            val = (listeArmesActuel1, listeDisciplinesKaiActuel1, ObjetsActuel1, RepasActuel1, ObjetsSpeciauxActuel1, ChapitreActuel1)

        if texteSauvegarde=="Sauvegarde 2":

            chapitreActuel2= self.lineEditChapitreVoulu.text()
            listeArmesActuel2 = self.comboBoxArmesActuel.currentText()
            listeDisciplinesKaiActuel2= self.comboBoxDisciplinesKaiActuel.currentText()
            ObjetsActuel2 = self.lineEdit_objets.text()
            RepasActuel2 = self.lineEdit_repas.text()
            ObjetsSpeciauxActuel2 = self.lineEdit_objetsSpeciaux.text()
            ChapitreActuel2 = self.lineEditChapitreVoulu.text()
            listeDisciplinesKaiActuel2 = listeArmesActuel
            listeArmesActuel2 = listeArmesActuel

            sql="INSERT INTO feuille_aventure (sauvegarde, armes, disciplines_kai, objets, repas, objets_speciaux, chapitre_actuel) VALUES (2, %s, %s, %s, %s, %s, %s)"
            val = (listeArmesActuel2, listeDisciplinesKaiActuel2, ObjetsActuel2, RepasActuel2, ObjetsSpeciauxActuel2, ChapitreActuel2)


        if texteSauvegarde=="Sauvegarde 3":

            chapitreActuel3= self.lineEditChapitreVoulu.text()
            listeArmesActuel3 = self.comboBoxArmesActuel.currentText()
            listeDisciplinesKaiActuel3= self.comboBoxDisciplinesKaiActuel.currentText()
            ChapitreActuel3 = self.lineEditChapitreVoulu.text()
            ObjetsActuel3 = self.lineEdit_objets.text()
            RepasActuel3 = self.lineEdit_repas.text()
            ObjetsSpeciauxActuel3 = self.lineEdit_objetsSpeciaux.text()
            listeDisciplinesKaiActuel3 = listeArmesActuel
            listeArmesActuel3 = listeArmesActuel

            sql="INSERT INTO feuille_aventure (sauvegarde, armes, disciplines_kai, objets, repas, objets_speciaux, chapitre_actuel) VALUES (3, %s, %s, %s, %s, %s, %s)"
            val = (listeArmesActuel3, listeDisciplinesKaiActuel3, ObjetsActuel3, RepasActuel3, ObjetsSpeciauxActuel3, ChapitreActuel3)

        mycursor.execute(sql, val)
        mydb.commit()


        def ChargerSauvegarde():

            #Il faudrait que je fasse un sélect pour extraire les données pour les afficher 
            if texteSauvegarde=="Sauvegarde 1":
                
                #mycursor.execute("SELECT armes FROM feuille_aventure WHERE sauvegarde=1")
                #myresult = mycursor.fetchone()
                #str =''
                #for x in myresult:
                #    for data in x:
                #        str+=data
                #print(str)
                #self.comboBoxArmesActuel.addItem(str)
                #str=''

                self.comboBoxArmesActuel.clear()
                self.comboBoxDisciplinesKaiActuel.clear()

                self.AfficherChapitre()
                self.lineEditChapitreVoulu.setText(chapitreActuel1)
                self.comboBoxArmesActuel.addItem(listeArmesActuelNom)
                self.comboBoxDisciplinesKaiActuel.addItem(listeDisciplinesKaiActuelNom)
                self.lineEdit_objets.setText(ObjetsActuel1)
                self.lineEdit_repas.setText(RepasActuel1)
                self.lineEdit_objetsSpeciaux.setText(ObjetsSpeciauxActuel1)


            if texteSauvegarde=="Sauvegarde 2":
                self.comboBoxArmesActuel.clear()
                self.comboBoxDisciplinesKaiActuel.clear()
                self.lineEditChapitreVoulu.setText(chapitreActuel2)
                self.AfficherChapitre()
                self.comboBoxArmesActuel.addItem(listeArmesActuelNom)
                self.comboBoxDisciplinesKaiActuel.addItem(listeDisciplinesKaiActuelNom)
                self.lineEdit_objets.setText(ObjetsActuel2)
                self.lineEdit_repas.setText(RepasActuel2)
                self.lineEdit_objetsSpeciaux.setText(ObjetsSpeciauxActuel2)

            if texteSauvegarde=="Sauvegarde 3":
                self.comboBoxArmesActuel.clear()
                self.comboBoxDisciplinesKaiActuel.clear()
                self.lineEditChapitreVoulu.setText(chapitreActuel3)
                self.AfficherChapitre()
                self.comboBoxArmesActuel.addItem(listeArmesActuel3)
                self.comboBoxDisciplinesKaiActuel.addItem(listeDisciplinesKaiActuelNom)   
                self.lineEdit_objets.setText(ObjetsActuel3)
                self.lineEdit_repas.setText(RepasActuel3)
                self.lineEdit_objetsSpeciaux.setText(ObjetsSpeciauxActuel3)

        def SupprimerSauvegarde():

            self.comboBoxArmesActuel.clear()
            self.comboBoxDisciplinesKaiActuel.clear()
            self.lineEditChapitreVoulu.setText("0")

            self.lineEdit_objets.setText("")
            self.lineEdit_repas.setText("")
            self.lineEdit_objetsSpeciaux.setText("")

            if texteSauvegarde=="Sauvegarde 1":
                chapitreActuel1="0"
                mycursor.execute("DELETE FROM feuille_aventure WHERE sauvegarde = 1")

            if texteSauvegarde=="Sauvegarde 2":
                chapitreActuel2="0"
                mycursor.execute("DELETE FROM feuille_aventure WHERE sauvegarde = 2")

            if texteSauvegarde=="Sauvegarde 3":
                chapitreActuel3="0"
                mycursor.execute("DELETE FROM feuille_aventure WHERE sauvegarde = 3")

            mydb.commit()
            self.PremierChapitre()
        
        self.ButtonChargerSauvegarde.clicked.connect(ChargerSauvegarde)
        self.ButtonSupprimerSauvegarde.clicked.connect(SupprimerSauvegarde)



app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()