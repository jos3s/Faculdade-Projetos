CREATE DATABASE clinica;

USE clinica;

CREATE TABLE funcionario(
	id_func INT PRIMARY KEY NOT NULL,
	nome VARCHAR(40) NOT NULL,
	tipo VARCHAR(12) NOT NULL,
	espec_medico VARCHAR(20),
	endereco VARCHAR(40) NOT NULL,
	bairro VARCHAR(20) NOT NULL,
	cep CHAR(9) NOT NULL,
	estado CHAR(2) NOT NULL
);

CREATE TABLE paciente(
	cpf_paciente CHAR(11) PRIMARY KEY NOT NULL,
	nome VARCHAR(40) NOT NULL,
	data_nasc DATE NOT NULL,
	alergia VARCHAR(50),
	telefone VARCHAR(11),
	endereco VARCHAR(40) NOT NULL,
	bairro VARCHAR(20) NOT NULL,
	cep CHAR(9) NOT NULL,
	estado CHAR(2) NOT NULL
);

CREATE TABLE consulta(
	id_consulta INT NOT NULL PRIMARY KEY,
	data_consulta DATE NOT NULL
);

CREATE TABLE exame(
	id_exame INT NOT NULL PRIMARY KEY,
	data_exame DATE NOT NULL,
	id_consulta INT NOT NULL,
	FOREIGN KEY (id_consulta) REFERENCES consulta
);

CREATE TABLE medico_exame(
	id_func INT NOT NULL,
	id_exame INT NOT NULL,
	FOREIGN KEY (id_func) REFERENCES funcionario,
	FOREIGN KEY (id_exame) REFERENCES exame
);

CREATE TABLE paciente_exame(
	cpf_paciente CHAR(11) NOT NULL,
	id_exame INT NOT NULL,
	FOREIGN KEY (cpf_paciente) REFERENCES paciente,
	FOREIGN KEY (id_exame) REFERENCES exame
);

CREATE TABLE enfermeiro_exame(
	id_func INT NOT NULL,
	id_exame INT NOT NULL,
	FOREIGN KEY (id_func) REFERENCES funcionario,
	FOREIGN KEY (id_exame) REFERENCES exame
);

CREATE TABLE secretario_consulta(
	id_func INT NOT NULL,
	id_consulta INT NOT NULL,
	FOREIGN KEY (id_func) REFERENCES funcionario,
	FOREIGN KEY (id_consulta) REFERENCES consulta
);

CREATE TABLE paciente_consulta(
	cpf_paciente CHAR(11) NOT NULL,
	id_consulta INT NOT NULL,
	FOREIGN KEY (cpf_paciente) REFERENCES paciente,
	FOREIGN KEY (id_consulta) REFERENCES consulta
);

CREATE TABLE medico_consulta(
	id_func INT NOT NULL,
	id_consulta INT NOT NULL,
	prescricao VARCHAR(100),
	FOREIGN KEY (id_func) REFERENCES funcionario,
	FOREIGN KEY (id_consulta) REFERENCES consulta
);