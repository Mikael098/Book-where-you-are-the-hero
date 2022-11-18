DROP DATABASE IF EXISTS maitre_tenebre_fortier_mikael;
CREATE DATABASE maitre_tenebre_fortier_mikael;
USE maitre_tenebre_fortier_mikael;

#-----------------------------------------------------------------------------
DROP TABLE  IF EXISTS livre;
CREATE TABLE livre(
	id INT PRIMARY KEY AUTO_INCREMENT,
    titre VARCHAR(255)
);
INSERT INTO livre (titre) VALUES ('Les Maîtres des Ténèbres');


#1 Trigger -> Permet de vérifier si le titre du roman n'est pas vide, s'il est vide, un message d'erreur s'affiche
DELIMITER $$
	DROP TRIGGER IF EXISTS verifie_si_titre $$ 
	CREATE TRIGGER verifie_si_titre
	BEFORE INSERT ON livre FOR EACH ROW
	BEGIN
		IF NEW.titre = '' THEN
			SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Veuillez mettre un nom au livre';
		END IF;
	END $$
DELIMITER ;

#INSERT INTO livre (titre) VALUES ('');
#SELECT * FROM livre;
#-----------------------------------------------------------------------------
DROP TABLE  IF EXISTS chapitre;
CREATE TABLE chapitre(
	no_chapitre INT PRIMARY KEY,
    texte TEXT,
    id_livre INT,
    FOREIGN KEY(id_livre) REFERENCES livre(id)
);

#-----------------------------------------------------------------------------
DROP TABLE  IF EXISTS lien_chapitre;
CREATE TABLE lien_chapitre(
	id INT PRIMARY KEY AUTO_INCREMENT,
    no_chapitre_origine INT,
    no_chapitre_destination INT,
    FOREIGN KEY(no_chapitre_origine) REFERENCES chapitre(no_chapitre)
);
#-----------------------------------------------------------------------------

DROP TABLE  IF EXISTS item_disciplines_kai;
CREATE TABLE item_disciplines_kai(
	id INT PRIMARY KEY AUTO_INCREMENT,
    disciplines_kai_titre VARCHAR(255)
);

INSERT INTO item_disciplines_kai (disciplines_kai_titre) VALUES ('Le camouflage');
INSERT INTO item_disciplines_kai (disciplines_kai_titre) VALUES ('La chasse');
INSERT INTO item_disciplines_kai (disciplines_kai_titre) VALUES ('Le sixième sens');
INSERT INTO item_disciplines_kai (disciplines_kai_titre) VALUES ('L\'orientation');
INSERT INTO item_disciplines_kai (disciplines_kai_titre) VALUES ('La guérison');
INSERT INTO item_disciplines_kai (disciplines_kai_titre) VALUES ('La Maîtrise des armes');
INSERT INTO item_disciplines_kai (disciplines_kai_titre) VALUES ('Bouclier psychique');
INSERT INTO item_disciplines_kai (disciplines_kai_titre) VALUES ('Puissance psychique');
INSERT INTO item_disciplines_kai (disciplines_kai_titre) VALUES ('Communication animale');
INSERT INTO item_disciplines_kai (disciplines_kai_titre) VALUES ('Maîtrise psychique de la matière');

SELECT * FROM item_disciplines_kai;
#-----------------------------------------------------------------------------

DROP TABLE  IF EXISTS item_armes;
CREATE TABLE item_armes(
	id INT PRIMARY KEY AUTO_INCREMENT,
    armes_titre VARCHAR(255)
);

INSERT INTO item_armes (armes_titre) VALUES ('Le poignard');
INSERT INTO item_armes (armes_titre) VALUES ('La lance');
INSERT INTO item_armes (armes_titre) VALUES ('La masse d\'armes');
INSERT INTO item_armes (armes_titre) VALUES ('Le sabre');
INSERT INTO item_armes (armes_titre) VALUES ('Le marteau de guerre');
INSERT INTO item_armes (armes_titre) VALUES ('L\'épée');
INSERT INTO item_armes (armes_titre) VALUES ('La hache');
INSERT INTO item_armes (armes_titre) VALUES ('Le baton');
INSERT INTO item_armes (armes_titre) VALUES ('Le glaive');

#-----------------------------------------------------------------------------
DROP TABLE  IF EXISTS item_disciplines_kai_feuille_aventure;
CREATE TABLE item_disciplines_kai_feuille_aventure(
	id INT PRIMARY KEY AUTO_INCREMENT,
    disciplines_kai_id INT,
    FOREIGN KEY (disciplines_kai_id) REFERENCES item_disciplines_kai(id)
);

INSERT INTO item_disciplines_kai_feuille_aventure (disciplines_kai_id) VALUES (1);
INSERT INTO item_disciplines_kai_feuille_aventure (disciplines_kai_id) VALUES (2);
INSERT INTO item_disciplines_kai_feuille_aventure (disciplines_kai_id) VALUES (3);
INSERT INTO item_disciplines_kai_feuille_aventure (disciplines_kai_id) VALUES (4);
INSERT INTO item_disciplines_kai_feuille_aventure (disciplines_kai_id) VALUES (5);
INSERT INTO item_disciplines_kai_feuille_aventure (disciplines_kai_id) VALUES (6);
INSERT INTO item_disciplines_kai_feuille_aventure (disciplines_kai_id) VALUES (7);
INSERT INTO item_disciplines_kai_feuille_aventure (disciplines_kai_id) VALUES (8);
INSERT INTO item_disciplines_kai_feuille_aventure (disciplines_kai_id) VALUES (9);
INSERT INTO item_disciplines_kai_feuille_aventure (disciplines_kai_id) VALUES (10);

#-----------------------------------------------------------------------------
DROP TABLE  IF EXISTS item_armes_feuille_aventure;
CREATE TABLE item_armes_feuille_aventure(
	id INT PRIMARY KEY AUTO_INCREMENT,
    armes_id INT,
    FOREIGN KEY (armes_id) REFERENCES item_armes(id)
);

INSERT INTO item_armes_feuille_aventure (armes_id) VALUES (1);
INSERT INTO item_armes_feuille_aventure (armes_id) VALUES (2);
INSERT INTO item_armes_feuille_aventure (armes_id) VALUES (3);
INSERT INTO item_armes_feuille_aventure (armes_id) VALUES (4);
INSERT INTO item_armes_feuille_aventure (armes_id) VALUES (5);
INSERT INTO item_armes_feuille_aventure (armes_id) VALUES (6);
INSERT INTO item_armes_feuille_aventure (armes_id) VALUES (7);
INSERT INTO item_armes_feuille_aventure (armes_id) VALUES (8);
INSERT INTO item_armes_feuille_aventure (armes_id) VALUES (9);

#-----------------------------------------------------------------------------

DROP TABLE  IF EXISTS feuille_aventure;
CREATE TABLE feuille_aventure(
	id INT PRIMARY KEY AUTO_INCREMENT,
    id_livre INT,
    sauvegarde INT,
    disciplines_kai INT,
    disciplines_kai_notes VARCHAR(255),
    armes INT,
    objets VARCHAR(255),
    repas VARCHAR(255),
    objets_speciaux VARCHAR(255),
    bourse INT,
    habilete INT,
    endurance INT,
    chapitre_actuel INT,
    FOREIGN KEY(id_livre) REFERENCES livre(id),
    FOREIGN KEY(disciplines_kai) REFERENCES item_disciplines_kai_feuille_aventure(disciplines_kai_id),
    FOREIGN KEY(armes) REFERENCES item_armes_feuille_aventure(armes_id)
);


#2 Trigger -> Permet de vérifier si la bourse n'est pas dans le négatif, si c'est le cas un message d'erreur apparaît
DELIMITER $$
	DROP TRIGGER IF EXISTS verifie_si_bourse_positif $$ 
	CREATE TRIGGER verifie_si_bourse_positif
	BEFORE INSERT ON feuille_aventure FOR EACH ROW
	BEGIN
		IF NEW.bourse < 0 THEN
			SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'La bourse ne peut pas être dans le négatif';
		END IF;
	END $$
DELIMITER ;

#INSERT INTO feuille_aventure (bourse) VALUES(-1);
#SELECT * FROM feuille_aventure;

#-----------------------------------------------------------------------------
#Création de l'user
#CREATE USER joueur IDENTIFIED BY 'qwerty';
GRANT UPDATE ON feuille_aventure TO 'joueur';
GRANT SELECT ON livre TO 'joueur';
GRANT SELECT ON chapitre TO 'joueur';
GRANT SELECT ON item_armes TO 'joueur';
GRANT SELECT ON item_disciplines_kai TO 'joueur';
GRANT SELECT ON feuille_aventure TO 'joueur';
GRANT SELECT ON item_disciplines_kai_feuille_aventure TO 'joueur';
GRANT SELECT ON item_armes_feuille_aventure TO 'joueur';
GRANT INSERT ON feuille_aventure TO 'joueur';
GRANT DELETE ON feuille_aventure TO 'joueur';

SELECT * FROM feuille_aventure;
SELECT armes_titre FROM item_armes INNER JOIN item_armes_feuille_aventure ON item_armes.id=item_armes_feuille_aventure.armes_id INNER JOIN feuille_aventure ON armes_id=armes WHERE item_armes.id=feuille_aventure.armes
