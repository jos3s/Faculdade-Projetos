# Modelo Relacional

Tabelas formatadas no modelo relacional textual:

**Funcionario**(IdFunc, Nome, Tipo, Telef, EspecMed, Rua, NumMoradia,
Bairro, CEP, Estado)

**Paciente**(CpfPac, Nome, DataNasc, Alergia, Telef, Rua, NumMoradia,
Bairro, CEP, Estado)

**Exames**(IdExame, DataHora, IdConsulta)

- IdConsulta referencia *Consulta*

**MedicoExame**(IdFunc, IdExame)

- IdFunc referencia *Funcionario (Médico)*  
- IdExame referencia *Exames*

**PacienteExame**(CpfPaciente, IdExame)

- CpfPaciente referencia *Paciente*  
- IdExame referencia *Consulta*  

**EnfermeiroExame**(IdFunc, IdExame)

- IdFunc referencia *Funcionario (Enfermeiro)*  
- IdExame referencia *Exame*

**Consultas**(IdConsulta, DataHora)

**SecretarioConsulta**(IdFunc, IdConsulta)

- IdFunc referencia *Funcionario (Secretário)*  
- IdConsulta referencia *Consulta*  

**ConsultasPaciente**(CpfPac, IdConsulta)

- IdConsulta referencia *Consulta*  
- CpfPac referencia *Paciente*  

**MedicoConsulta**(IdFunc, IdConsulta, Prescrição)

- IdFunc referencia *Funcionario (Médico)*  
- IdConsulta referencia *Consulta*  
