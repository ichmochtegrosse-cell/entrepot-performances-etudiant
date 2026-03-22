SET search_path TO dw;

SELECT
    e.nom || ' ' || e.prenom AS etudiant,
    m.libelle AS matiere,
    f.note_controle_continu AS note_cc,
    f.note_examen AS note_exam,
    f.note_finale,
    CASE
        WHEN f.note_finale >= 16 THEN 'Très Bien'
        WHEN f.note_finale >= 14 THEN 'Bien'
        WHEN f.note_finale >= 12 THEN 'Assez Bien'
        WHEN f.note_finale >= 10 THEN 'Passable'
        ELSE 'Insuffisant'
    END AS mention
FROM dw.fait_performances f
JOIN dw.dim_etudiant e ON f.id_etudiant = e.id_etudiant
JOIN dw.dim_matiere m ON f.id_matiere = m.id_matiere
ORDER BY f.note_finale DESC;
