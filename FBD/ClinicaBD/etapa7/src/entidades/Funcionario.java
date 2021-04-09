package entidades;

public class Funcionario {

	private int id_func;
	private String nome, tipo, endereco,bairro,cep, estado;

	public Funcionario() {}
	
	public Funcionario(int id_func, String nome, String tipo, String endereco, String bairro, String cep, String estado) {
		this.id_func = id_func;
		this.nome = nome;
		this.tipo = tipo;
		this.endereco = endereco;
		this.bairro = bairro;
		this.cep = cep;
		this.estado = estado;
	}

	@Override
	public String toString() {
		return
			"Id Funcionário= " + getId_func() + "\n" +
			"Nome= " + getNome() + "\n" +
			"Tipo= " + getTipo() + "\n" +
			"Endereco= " + getEndereco() + "\n" +
			"Bairro= " + getBairro() + "\n" +
			"Cep= " + getCep() + "\n" +
			"Estado= " + getEstado();
	}

	public int getId_func() {
		return this.id_func;
	}

	public void setId_func(int id_func) {
		this.id_func = id_func;
	}

	public String getNome() {
		return this.nome;
	}

	public void setNome(String nome) {
		this.nome = nome;
	}

	public String getTipo() {
		return this.tipo;
	}

	public void setTipo(String tipo) {
		this.tipo = tipo;
	}

	public String getEndereco() {
		return this.endereco;
	}

	public void setEndereco(String endereco) {
		this.endereco = endereco;
	}

	public String getBairro() {
		return this.bairro;
	}

	public void setBairro(String bairro) {
		this.bairro = bairro;
	}

	public String getCep() {
		return this.cep;
	}

	public void setCep(String cep) {
		this.cep = cep;
	}

	public String getEstado() {
		return this.estado;
	}

	public void setEstado(String estado) {
		this.estado = estado;
	}
	
}
