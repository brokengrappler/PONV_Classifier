
SELECT *
FROM ponvfull p 
WHERE nausea_24h NOTNULL OR ponv notnull;

-- Return count of procedures
select pf.surgical_procedure, pt.procedure_en, count(1)
from ponvfull pf
INNER JOIN proc_trans pt ON pt.surgical_procedure = pf.surgical_procedure 
group by pt.surgical_procedure, pf.surgical_procedure 
order by count(1) DESC;

-- Creating Dummy Variable Table, used below
SELECT  trtbl.patientid, trtbl.procedure_en,
count(CASE WHEN procedure_en = 'Gastrointestinal'THEN 1 END) AS Gastrointestinal,
	count(CASE WHEN procedure_en = 'Mastectomy'THEN 1 END) AS Mastectomy,
	count(CASE WHEN procedure_en = 'Thoracic'THEN 1 END) AS Thoracic,
	count(CASE WHEN procedure_en = 'Nephrectomy'THEN 1 END) AS Nephrectomy,
	count(CASE WHEN procedure_en = 'Hysterectomy'THEN 1 END) AS Hysterectomy,
	count(CASE WHEN procedure_en = 'Exploratory Laparotomy'THEN 1 END) AS Exploratory_Laparotomy,
	count(CASE WHEN procedure_en = 'Other'THEN 1 END) AS Other,
	count(CASE WHEN procedure_en = 'Spine Surgery'THEN 1 END) AS Spine_Surgery,
	count(CASE WHEN procedure_en = 'Cystectomy'THEN 1 END) AS Cystectomy,
	count(CASE WHEN procedure_en = 'Prostatectomy'THEN 1 END) AS Prostatectomy,
	count(CASE WHEN procedure_en = 'Hepatectomy'THEN 1 END) AS Hepatectomy,
	count(CASE WHEN procedure_en = 'Plastic'THEN 1 END) AS Plastic,
	count(CASE WHEN procedure_en = 'Cytoreduction'THEN 1 END) AS Cytoreduction,
	count(CASE WHEN procedure_en = 'Anexectomy/Ovariectomy/'THEN 1 END) AS Anexectomy_Ovariectomy,
	count(CASE WHEN procedure_en = 'Head/Neck'THEN 1 END) AS Head_Neck,
	count(CASE WHEN procedure_en = 'Orthopedic'THEN 1 END) AS Orthopedic,
	count(CASE WHEN procedure_en = 'Hysterectomy VLP'THEN 1 END) AS Hysterectomy_VLP,
	count(CASE WHEN procedure_en = 'Extensive Lymphadenectomy'THEN 1 END) AS Extensive_Lymphadenectomy,
	count(CASE WHEN procedure_en = 'Esophagectomy'THEN 1 END) AS Esophagectomy,
	count(CASE WHEN procedure_en = 'Breast Lumpectomy'THEN 1 END) AS Breast_Lumpectomy,
	count(CASE WHEN procedure_en = 'Pancreatectomy'THEN 1 END) AS Pancreatectomy,
	count(CASE WHEN procedure_en = 'Hip Arthoplasty'THEN 1 END) AS Hip_Arthoplasty,
	count(CASE WHEN procedure_en = 'Soft Tissue Resection'THEN 1 END) AS Soft_Tissue_Resection,
	count(CASE WHEN procedure_en = 'Limb Amputation'THEN 1 END) AS Limb_Amputation,
	count(CASE WHEN procedure_en = 'Gallbladder'THEN 1 END) AS Gallbladder
FROM 
(SELECT patientid, pt.surgical_procedure, pt.procedure_en
FROM ponvfull pf
INNER JOIN proc_trans pt ON pf.surgical_procedure = pt.surgical_procedure) AS trtbl
GROUP BY trtbl.patientid, trtbl.procedure_en;


-- Joining master table with dummy table;
-- Create new table with dummy vars and filter null PONV outcomes
CREATE TABLE ponv_dummy as
WITH dummytbl AS (
SELECT  trtbl.patientid, trtbl.procedure_en,
count(CASE WHEN procedure_en = 'Gastrointestinal'THEN 1 END) AS Gastrointestinal,
	count(CASE WHEN procedure_en = 'Mastectomy'THEN 1 END) AS Mastectomy,
	count(CASE WHEN procedure_en = 'Thoracic'THEN 1 END) AS Thoracic,
	count(CASE WHEN procedure_en = 'Nephrectomy'THEN 1 END) AS Nephrectomy,
	count(CASE WHEN procedure_en = 'Hysterectomy'THEN 1 END) AS Hysterectomy,
	count(CASE WHEN procedure_en = 'Exploratory Laparotomy'THEN 1 END) AS Exploratory_Laparotomy,
	count(CASE WHEN procedure_en = 'Other'THEN 1 END) AS Other,
	count(CASE WHEN procedure_en = 'Spine Surgery'THEN 1 END) AS Spine_Surgery,
	count(CASE WHEN procedure_en = 'Cystectomy'THEN 1 END) AS Cystectomy,
	count(CASE WHEN procedure_en = 'Prostatectomy'THEN 1 END) AS Prostatectomy,
	count(CASE WHEN procedure_en = 'Hepatectomy'THEN 1 END) AS Hepatectomy,
	count(CASE WHEN procedure_en = 'Plastic'THEN 1 END) AS Plastic,
	count(CASE WHEN procedure_en = 'Cytoreduction'THEN 1 END) AS Cytoreduction,
	count(CASE WHEN procedure_en = 'Anexectomy/Ovariectomy/'THEN 1 END) AS Anexectomy_Ovariectomy,
	count(CASE WHEN procedure_en = 'Head/Neck'THEN 1 END) AS Head_Neck,
	count(CASE WHEN procedure_en = 'Orthopedic'THEN 1 END) AS Orthopedic,
	count(CASE WHEN procedure_en = 'Hysterectomy VLP'THEN 1 END) AS Hysterectomy_VLP,
	count(CASE WHEN procedure_en = 'Extensive Lymphadenectomy'THEN 1 END) AS Extensive_Lymphadenectomy,
	count(CASE WHEN procedure_en = 'Esophagectomy'THEN 1 END) AS Esophagectomy,
	count(CASE WHEN procedure_en = 'Breast Lumpectomy'THEN 1 END) AS Breast_Lumpectomy,
	count(CASE WHEN procedure_en = 'Pancreatectomy'THEN 1 END) AS Pancreatectomy,
	count(CASE WHEN procedure_en = 'Hip Arthoplasty'THEN 1 END) AS Hip_Arthoplasty,
	count(CASE WHEN procedure_en = 'Soft Tissue Resection'THEN 1 END) AS Soft_Tissue_Resection,
	count(CASE WHEN procedure_en = 'Limb Amputation'THEN 1 END) AS Limb_Amputation,
	count(CASE WHEN procedure_en = 'Gallbladder'THEN 1 END) AS Gallbladder
FROM 
(SELECT patientid, pt.surgical_procedure, pt.procedure_en
FROM ponvfull pf
INNER JOIN proc_trans pt ON pf.surgical_procedure = pt.surgical_procedure) AS trtbl
GROUP BY trtbl.patientid, trtbl.procedure_en
)
SELECT DISTINCT ON (dummytbl.patientid) *
FROM ponvfull p
INNER JOIN dummytbl USING (patientid)
WHERE ponv NOTNULL OR nausea_24h NOTNULL;


SELECT *
FROM ponv_dummy pd 
LIMIT 10