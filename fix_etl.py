import psycopg2
import pandas as pd
from datetime import datetime
import getpass

pw = getpass.getpass('Mot de passe PostgreSQL : ')
conn = psycopg2.connect(host='localhost', port=5432, database='entrepot_performances_etudiant', user='postgres', password=pw)
cursor = conn.cursor()
cursor.execute('SET search_path TO dw;')

notes = pd.read_excel('donnees_sources.xlsx', sheet_name='Notes_Fact', header=1)

for _, row in notes.iterrows():
    cursor.execute("""
        INSERT INTO dw.fait_performances
        (id_etudiant, id_matiere, id_enseignant, id_equipement, id_date, note_controle_continu, note_examen, annee_academique)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """, (int(row['ID_Etudiant']), int(row['ID_Matiere']), int(row['ID_Enseignant']),
          1, int(row['ID_Date']), float(row['Note_CC']), float(row['Note_Examen']), str(row['Annee_Academique'])))

conn.commit()
cursor.close()
conn.close()
print('🎉 ETL terminé avec succès !')
print(f'   Timestamp : {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
print('   Excel vers PostgreSQL : DONE')
