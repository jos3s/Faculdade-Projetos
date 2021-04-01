-- Visualiza o nome do medico, paciente, id da consulta e data da consulta
CREATE VIEW DADOS_CONSULTAS AS SELECT DISTINCT me.nome as medicoNome, pa.nome as pacienteNome, c.ID_CONSULTA, c.DATA_CONSULTA
FROM FUNCIONARIO AS ME, PACIENTE AS PA, CONSULTA AS C,
MEDICO_CONSULTA AS MC, PACIENTE_CONSULTA AS PC
WHERE ME.ID_FUNC = MC.ID_FUNC AND  MC.ID_CONSULTA=C.ID_CONSULTA AND
PA.CPF_PACIENTE = PC.CPF_PACIENTE AND PC.ID_CONSULTA=C.ID_CONSULTA;

-- select * from dados_consultas order by pacientenome;

-- Visualizar todas as consultas de cada Médico ordenado por nome do Médico
SELECT f.nome, f.tipo, mc.id_consulta FROM funcionario as f,medico_consulta as mc 
WHERE f.id_func=mc.id_func and f.tipo='Médico' order by f.nome;

-- Visualizar todos os pacientes que tem alergia
select * from paciente WHERE alergia IS NOT NULL;

-- Visualizar todas as consultas que ocorreram em 2021
select id_consulta, 
from consulta
where data_consulta between '2021-01-01' and '2021-12-31'

-- Contar todas as consultas que ocorreram em 2021
select COUNT(*) as Nconsultas2021 from consulta
where data_consulta between '2021-01-01' and '2021-12-31'

-- Visualiza o nome dos paciente e a data das suas consultas
SELECT p.nome, c.data_consulta FROM paciente as p, consulta as c, paciente_consulta as pc
WHERE p.cpf_paciente=pc.cpf_paciente and pc.id_consulta=c.id_consulta
GROUP BY p.nome,c.data_consulta;

-- Vizualiza todos os tipos de médicos na clínica
SELECT DISTINCT TIPO FROM FUNCIONARIO;