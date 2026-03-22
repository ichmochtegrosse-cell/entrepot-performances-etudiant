"""
ETL — Entrepôt de Données Performances Étudiants
Equivalent du job Talend TOS-DI
Auteur : KOUADIO KOUASSI HIPOLITE — Master 2 BDGL UFHB
"""
import psycopg2
import pandas as pd
from datetime import datetime

# ============================================================
# CONFIGURATION CONNEXION POSTGRESQL
# ============================================================
conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="entrepot_performances_etudiant",
    user="postgres",
    password=input("Mot de passe PostgreSQL : ")
)
cursor = conn.cursor()
cursor.execute("SET search_path TO dw;")
print("✅ Connexion PostgreSQL OK")

# ============================================================
# EXTRACTION — Lecture du fichier Excel
# ============================================================
EXCEL_FILE = "donnees_sources.xlsx"
print(f"\n📂 Lecture du fichier Excel : {EXCEL_FILE}")

etudiants   = pd.read_excel(EXCEL_FILE, sheet_name="Etudiants",    header=1)
matieres    = pd.read_excel(EXCEL_FILE, sheet_name="Matieres",     header=1)
enseignants = pd.read_excel(EXCEL_FILE, sheet_name="Enseignants",  header=1)
equipements = pd.read_excel(EXCEL_FILE, sheet_name="Equipements",  header=1)
dim_temps   = pd.read_excel(EXCEL_FILE, sheet_name="Dim_Temps",    header=1)
notes       = pd.read_excel(EXCEL_FILE, sheet_name="Notes_Fact",   header=1)

print(f"  → {len(etudiants)} étudiants")
print(f"  → {len(matieres)} matières")
print(f"  → {len(enseignants)} enseignants")
print(f"  → {len(equipements)} équipements")
print(f"  → {len(dim_temps)} dates")
print(f"  → {len(notes)} notes")

# ============================================================
# TRANSFORMATION & CHARGEMENT — dim_etudiant
# ============================================================
print("\n⚙️  Chargement dim_etudiant...")
cursor.execute("TRUNCATE dw.fait_performances, dw.dim_etudiant, dw.dim_matiere, dw.dim_enseignant, dw.dim_equipement, dw.dim_temps RESTART IDENTITY CASCADE;")

for _, row in etudiants.iterrows():
    cursor.execute("""
        INSERT INTO dw.dim_etudiant (nom, prenom, date_naissance, sexe, niveau, filiere, email, telephone)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """, (row['Nom'], row['Prenom'], row['Date_Naissance'], row['Sexe'],
          row['Niveau'], row['Filiere'], row['Email'], str(row['Telephone'])))
print(f"  ✅ {len(etudiants)} étudiants chargés")

# dim_matiere
print("⚙️  Chargement dim_matiere...")
for _, row in matieres.iterrows():
    cursor.execute("""
        INSERT INTO dw.dim_matiere (code_matiere, libelle, coefficient, volume_horaire, semestre, niveau)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (row['Code_Matiere'], row['Libelle'], row['Coefficient'],
          row['Volume_Horaire'], row['Semestre'], row['Niveau']))
print(f"  ✅ {len(matieres)} matières chargées")

# dim_enseignant
print("⚙️  Chargement dim_enseignant...")
for _, row in enseignants.iterrows():
    cursor.execute("""
        INSERT INTO dw.dim_enseignant (nom, prenom, grade, specialite, email, departement)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (row['Nom'], row['Prenom'], row['Grade'],
          row['Specialite'], row['Email'], row['Departement']))
print(f"  ✅ {len(enseignants)} enseignants chargés")

# dim_equipement
print("⚙️  Chargement dim_equipement...")
for _, row in equipements.iterrows():
    cursor.execute("""
        INSERT INTO dw.dim_equipement (designation, type_equipement, quantite, salle, etat, date_acquisition)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (row['Designation'], row['Type'], row['Quantite'],
          row['Salle'], row['Etat'], row['Date_Acquisition']))
print(f"  ✅ {len(equipements)} équipements chargés")

# dim_temps
print("⚙️  Chargement dim_temps...")
for _, row in dim_temps.iterrows():
    cursor.execute("""
        INSERT INTO dw.dim_temps (date_complete, jour_semaine, mois, trimestre, annee, semestre, annee_academique)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (row['Date'], row['Jour'], row['Mois'], row['Trimestre'],
          row['Annee'], row['Semestre'], row['Annee_Academique']))
print(f"  ✅ {len(dim_temps)} dates chargées")

# fait_performances
print("⚙️  Chargement fait_performances...")
for _, row in notes.iterrows():
    cursor.execute("""
        INSERT INTO dw.fait_performances
        (id_etudiant, id_matiere, id_enseignant, id_equipement, id_date, note_controle_continu, note_examen, annee_academique)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """, (int(row['ID_Etudiant']), int(row['ID_Matiere']), int(row['ID_Enseignant']),
          int(row['ID_Equipement']), int(row['ID_Date']),
          float(row['Note_CC']), float(row['Note_Examen']), row['Annee_Academique']))
print(f"  ✅ {len(notes)} notes chargées")

# ============================================================
# COMMIT & FERMETURE
# ============================================================
conn.commit()
cursor.close()
conn.close()

print("\n🎉 ETL terminé avec succès !")
print(f"   Timestamp : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print("   Excel → PostgreSQL : DONE ✅")
