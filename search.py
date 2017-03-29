joindb = select * from (SELECT * 
FROM procedures 
JOIN facilities 
ON procedures.facility_name = facilities.name
JOIN procedure_type
ON procedure_type.cpt_code = facilities.cpt_code) 