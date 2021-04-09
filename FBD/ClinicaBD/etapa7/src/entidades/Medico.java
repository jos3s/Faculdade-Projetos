package entidades;

public class Medico extends Funcionario{

	private String especialidade;


	public Medico() {}
	
	public Medico(int id_func, String nome, String tipo, String espec, String endereco, String bairro, String cep, String estado) {
		super(id_func, nome, tipo, endereco, bairro, cep, estado);
		this.especialidade=espec;
	}

	
	@Override
	public String toString() {
		return "Medico: "+ super.toString() +"\n"+ "Especialidade=" + especialidade ;
	}

	public Medico(String especialidade) {
		this.especialidade = especialidade;
	}

	public String getEspecialidade() {
		return this.especialidade;
	}

	public void setEspecialidade(String especialidade) {
		this.especialidade = especialidade;
	}
	
}
