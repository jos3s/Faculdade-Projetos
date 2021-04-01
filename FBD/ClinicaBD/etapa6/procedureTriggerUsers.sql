--
--Local Procedure: Cria uma consulta de acordo com os IDs do Secretário que criou a consulta
--e do Médico que vai realizar a consulta, além do CPF do Paciente e da data da consulta.
--
CREATE PROCEDURE criarConsulta(idCons int, idSec int, idMed int,
cpfPac char(40), dataCons date) 
LANGUAGE 'plpgsql' as $$
    BEGIN
        INSERT INTO consulta VALUES (idCons, dataCons);
        INSERT INTO secretario_consulta VALUES (idSec, idCons);
        INSERT INTO paciente_consulta VALUES (cpfPac, idCons);
        INSERT INTO medico_consulta VALUES (idMed, idCons);
	END 
$$
--
--Trigger
--
CREATE FUNCTION novo_medico()
RETURNS trigger AS $$
	BEGIN
		IF NEW.tipo = 'Médico' AND NEW.espec_medico IS NULL THEN
			RAISE EXCEPTION 'A especialidade do Dr. % deve ser registrada.', NEW.nome;
		END IF;
		return NEW;
	END
$$ LANGUAGE 'plpgsql'

CREATE TRIGGER checar_especialidade
AFTER INSERT ON funcionario
FOR EACH ROW
EXECUTE FUNCTION novo_medico()

--INSERT INTO funcionario VALUES  (11,'Vinicius Lima','Médico',null,'Rua da Vida Mansa','Vilao Matias','62720-000','PA');
--DELETE FROM funcionario WHERE id_func = 11

--
-- Criando User com acesso somente leitura
--
CREATE USER readbd LOGIN ENCRYPTED PASSWORD 'readbd' NOSUPERUSER INHERIT NOCREATEDB NOCREATEROLE NOREPLICATION VALID UNTIL 'infinity';
GRANT CONNECT ON DATABASE clinica TO readbd;
GRANT USAGE ON SCHEMA public TO readbd;
GRANT SELECT ON ALL TABLES IN SCHEMA public TO readbd;
GRANT SELECT ON ALL SEQUENCES IN SCHEMA public TO readbd;
--
-- Criando User com acesso total
--
CREATE USER admbd LOGIN SUPERUSER CREATEDB CREATEROLE INHERIT ENCRYPTED PASSWORD 'bdadm'