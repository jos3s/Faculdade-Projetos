package dao;

import java.util.List;

import entidades.Funcionario;

public interface FuncionarioDAO {

	public void salvar(Funcionario func);
	
	public void deletar(int id);
	
	public Funcionario buscar(int id);
	
	public List<Funcionario> listar();
	
	public List<Funcionario> buscarPorTipo(String tipo);
	
	public List<Funcionario> buscarPorNome(String nome);
	
}
