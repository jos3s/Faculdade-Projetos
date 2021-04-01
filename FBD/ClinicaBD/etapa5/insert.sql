--
--FUNCIONARIO
--
INSERT INTO funcionario(id_func,nome,tipo,endereco,bairro,cep,estado)  
VALUES(1,'Castro Barrico','Secretário','Borboletas Psicodélicas, 567','Paulo I','78900-000','CE'),
(2,'Mayara Vargas','Enfermeiro','Travessa Maravilha Tristeza, 123','Centro','12865-897','CE'),
(3,'Stephanie Robalo', 'Enfermeiro','Rua Três Maria, 240','Lagoa Santa','34780-000','CE'),
(4,'Marcos Belmonte','Enfermeiro','Avenida Mauricio II, 230','Centro','34567-000','CE'),
(5,'Benjamim Baía','Secretário','Avenidade Lorenzo, 350','Centro','45600-000','CE');

INSERT INTO funcionario(id_func,nome,tipo,espec_medico,endereco,bairro,cep,estado) 
VALUES(6,'Alexandre Souto','Médico','Pediatra','Jaime Leonel Chaves, 203','Monsenhor Otavio','62930-000','CE'),
(7,'Jacinta Valadão','Médico','Clínico Geral','Ninho das Águias, 220','Nova Itupuã','34567-000','CE'),
(8,'Sarah Fazendeiro','Médico','Oftalmologista','Rua dos Bastidores, 340','Guarujá','45600-100','CE'),
(9,'Malika Fontoura','Médico','Clínico Geral','Rua das Vilas, 500','Docas','63900-000','CE'),
(10,'Maximiano Delgado','Médico','Otorrino','Francisco Remijo, 566','Centro','62930-000','CE');
--
--PACIENTE
--
INSERT INTO paciente (cpf_paciente,nome,data_nasc,alergia,telefone,endereco,bairro,cep,estado)
VALUES ('34245243276','Ronaldo Aguiar','1970-10-30','Amendoim','88994366139','Rua Jaime Leonel Chaves, 723','Monsenhor Otavio','62930-000','CE'),
('24653277893','Carlos Avila','1980-12-12',null,'88932458377','Avenida Francisco Remijo, 546','Centro','62930-000','CE'),
('24655642345','Maria Bastos','1985-12-01','Camarão, castanha','88956339854','Francisco Remijo, 546','Centro','62930-000','CE'),
('12345678910','Dráusio Varella','1973-03-10',null,'88992977114','Rua dos Portos, 233','Docas','63900-000','RS'),
('12367587431','Laura Avila','1982-01-23',null,'88955667788','Avenida Francisco Remijo, 546','Centro','62930-000','CE'),
('98765432106','Cassandra Aguiar','1965-06-18',null,'88999871234','Rua das Vilas, 575','Docas','63900-000','RS'),
('55559876244','Cassio Santos','1975-06-29',null,'88924412207','Rua da Conceição, 744','Sao Mauricio','62290-000','AM'),
('55559049556','Elma Maria','1981-11-10','Camarão, tomate, partículas de poeira','88978875543','Rua dos Portos, 988','Docas','63900-000','RS'),
('74572454955','Jeferson Raimundo','1922-12-01',null,'88997532489','Rua dos Bastidores, 711','Sao Cristóvão','67800-000','SP'),
('79837295432','Olivia Palito','1979-03-10',null,'88992453277','Avenida Ninho das Águias, 339','Miríade','67850-000','PB');
--
--CONSULTAS
--
INSERT INTO consulta(id_consulta,data_consulta) 
VALUES (1,'2021-10-08'), (2,'2021-05-08'), (3,'2021-07-29'), (4,'2021-01-10'), (5,'2022-12-10'),  
(6,'2021-09-30'), (7,'2021-08-25'), (8,'2021-03-21'), (9,'2022-06-01'), (10,'2022-04-01');
--
--EXAMES
--
INSERT INTO exame (id_exame,data_exame,id_consulta)
VALUES (1,'2021-10-11',1), (2,'2021-10-15',2), (3,'2021-08-07',3), 
(4,'2021-10-12',4), (5,'2021-01-19',5), (6,'2021-01-25',6), (7,'2021-01-31',7), 
(8,'2021-09-01',8), (9,'2022-06-18',9), (10,'2022-04-23',10);
--
--MEDICOEXAME
--
INSERT INTO medico_exame(id_func,id_exame)
VALUES (5,4), (6,3), (5,9), (9,10), (8,1),
(8,6), (9,7), (6,8), (10,2), (7,5);
--
--PACIENTEEXAME
--
INSERT INTO paciente_exame(cpf_paciente, id_exame) 
VALUES ('34245243276',4), ('24653277893',2), ('24655642345',7), ('12345678910',5), ('55559049556',10),
('55559876244',1), ('74572454955',3), ('12367587431',6), ('79837295432',8), ('98765432106',9);
--
--ENFERMEIROEXAME
-- 
INSERT INTO enfermeiro_exame(id_func, id_exame) 
VALUES (2,4), (4,2), (2,7), (3,6), (2,5), (4,8), (2,10), (3,9), (4,3), (3,1);
--
--SECRETARIOCONSULTA
--
INSERT INTO secretario_consulta(id_func, id_consulta) 
VALUES (1,4), (5,2), (5,7), (5,6), (1,5), (1,8), (5,10), (1,9), (5,3), (1,1);
--
--CONSULTASPACIENTE
--
INSERT INTO paciente_consulta(cpf_paciente,id_consulta) 
VALUES ('24653277893',1), ('79837295432',2), ('74572454955',3), ('12345678910',4), ('24655642345',5),
('55559876244',6), ('55559049556',7), ('12367587431',8), ('98765432106',9), ('34245243276',10);
--
--MEDICOCONSULTA
--
INSERT INTO medico_consulta(id_func, id_consulta) 
VALUES (10,1), (6,3), (8,5), (10,8), (9,10),
(8,4), (6,2), (7,6), (6,9), (9,7);