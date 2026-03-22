SET search_path TO dw;

INSERT INTO dw.dim_etudiant (nom, prenom, date_naissance, sexe, niveau, filiere, email, telephone) VALUES
  ('KOUADIO', 'Hipolite', '2000-03-15', 'M', 'Master 2', 'BDGL', 'hipolite.kouadio@ufhb.ci', '0701020304'),
  ('ASSI', 'Marie', '2001-06-20', 'F', 'Master 1', 'BDGL', 'marie.assi@ufhb.ci', '0705060708'),
  ('BAMBA', 'Ibrahim', '1999-11-10', 'M', 'Licence 3', 'INFO', 'ibrahim.bamba@ufhb.ci', '0709101112');

INSERT INTO dw.dim_matiere (code_matiere, libelle, coefficient, volume_horaire, semestre, niveau) VALUES
  ('BDD401', 'Bases de Données Avancées', 3.0, 45, 'S1', 'Master 2'),
  ('SYS402', 'Systèmes d''Information', 2.0, 30, 'S1', 'Master 2'),
  ('ALG301', 'Algorithmique & Structures', 3.0, 40, 'S2', 'Licence 3');

INSERT INTO dw.dim_enseignant (nom, prenom, grade, specialite, email, departement) VALUES
  ('YOBOUE', 'Kouamé', 'Professeur', 'Bases de Données', 'k.yoboue@ufhb.ci', 'Informatique'),
  ('KOFFI', 'Ama', 'Maître de Conférences', 'Systèmes d''Information', 'a.koffi@ufhb.ci', 'Informatique'),
  ('DIALLO', 'Seydou', 'Maître Assistant', 'Algorithmique', 's.diallo@ufhb.ci', 'Mathématiques');

INSERT INTO dw.dim_equipement (designation, type_equipement, quantite, salle, etat, date_acquisition) VALUES
  ('Ordinateur Dell', 'Informatique', 20, 'Salle Info A', 'Bon', '2022-09-01'),
  ('Vidéoprojecteur Epson', 'Audiovisuel', 5, 'Amphi 1', 'Bon', '2021-01-15'),
  ('Tableau Blanc', 'Mobilier', 10, 'Salle B', 'Usagé', '2019-03-10');

INSERT INTO dw.dim_temps (date_complete, jour_semaine, mois, trimestre, annee, semestre, annee_academique) VALUES
  ('2025-01-15', 'Mercredi', 'Janvier', 'T1', 2025, 'S1', '2024-2025'),
  ('2025-02-20', 'Jeudi', 'Février', 'T1', 2025, 'S1', '2024-2025'),
  ('2025-06-10', 'Mardi', 'Juin', 'T2', 2025, 'S2', '2024-2025');

INSERT INTO dw.fait_performances (id_etudiant, id_matiere, id_enseignant, id_equipement, id_date, note_controle_continu, note_examen, annee_academique) VALUES
  (1, 1, 1, 1, 1, 14.50, 15.00, '2024-2025'),
  (2, 2, 2, 2, 2, 12.00, 11.50, '2024-2025'),
  (3, 3, 3, 3, 3, 8.50, 10.00, '2024-2025');
