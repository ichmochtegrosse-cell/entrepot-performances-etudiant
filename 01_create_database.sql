CREATE SCHEMA IF NOT EXISTS dw;
SET search_path TO dw;

CREATE TABLE IF NOT EXISTS dw.dim_etudiant (
    id_etudiant SERIAL PRIMARY KEY,
    nom VARCHAR(100) NOT NULL,
    prenom VARCHAR(100) NOT NULL,
    date_naissance DATE,
    sexe CHAR(1),
    niveau VARCHAR(50),
    filiere VARCHAR(100),
    email VARCHAR(150),
    telephone VARCHAR(20)
);

CREATE TABLE IF NOT EXISTS dw.dim_matiere (
    id_matiere SERIAL PRIMARY KEY,
    code_matiere VARCHAR(20) NOT NULL UNIQUE,
    libelle VARCHAR(150) NOT NULL,
    coefficient NUMERIC(3,1),
    volume_horaire INTEGER,
    semestre VARCHAR(10),
    niveau VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS dw.dim_enseignant (
    id_enseignant SERIAL PRIMARY KEY,
    nom VARCHAR(100) NOT NULL,
    prenom VARCHAR(100) NOT NULL,
    grade VARCHAR(80),
    specialite VARCHAR(120),
    email VARCHAR(150),
    departement VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS dw.dim_equipement (
    id_equipement SERIAL PRIMARY KEY,
    designation VARCHAR(150) NOT NULL,
    type_equipement VARCHAR(80),
    quantite INTEGER DEFAULT 0,
    salle VARCHAR(80),
    etat VARCHAR(50),
    date_acquisition DATE
);

CREATE TABLE IF NOT EXISTS dw.dim_temps (
    id_date SERIAL PRIMARY KEY,
    date_complete DATE NOT NULL UNIQUE,
    jour_semaine VARCHAR(20),
    mois VARCHAR(20),
    trimestre VARCHAR(5),
    annee INTEGER,
    semestre VARCHAR(5),
    annee_academique VARCHAR(20)
);

CREATE TABLE IF NOT EXISTS dw.fait_performances (
    id_note SERIAL PRIMARY KEY,
    id_etudiant INTEGER REFERENCES dw.dim_etudiant(id_etudiant),
    id_matiere INTEGER REFERENCES dw.dim_matiere(id_matiere),
    id_enseignant INTEGER REFERENCES dw.dim_enseignant(id_enseignant),
    id_equipement INTEGER REFERENCES dw.dim_equipement(id_equipement),
    id_date INTEGER REFERENCES dw.dim_temps(id_date),
    note_controle_continu NUMERIC(4,2),
    note_examen NUMERIC(4,2),
    note_finale NUMERIC(4,2) GENERATED ALWAYS AS (ROUND((note_controle_continu + 2 * note_examen) / 3, 2)) STORED,
    annee_academique VARCHAR(20)
);
