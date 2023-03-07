 """Exercices en salle de classe"""


from classes.etudiant import *
#creer liste etudiant
#afficher liste etudiant

# etd1 = Etudiant()
# etd1.nom = "Morand"
# etd1.prenom = "Honiel"
# etd1.no_dossier = "01003"


# etd2 = Etudiant()
# etd2.nom = "Graville"
# etd2.prenom = "Stanley"
# etd2.no_dossier = "01005"

# etd4 = Etudiant()
# etd4.nom = "Edson"
# etd4.prenom = "Charles"
# etd4.no_dossier = "01004"

etd1 = Etudiant("Morand", "Honiel", "01003")
etd2 = Etudiant("Graville", "Stanley", "01005")
etd4 = Etudiant("Edson", "Charles", "01004")

etd1.presenter()

etudiants = []
etudiants.append(str(etd1))
etudiants.append(str(etd2))
etudiants.append(str(etd4))

#print(etudiants)


