package dao;

import java.util.List;

import entidades.Medico;

public interface MedicoDAO {

	public void salvar(Medico med);
	
	public void deletar(int id);
	
	public void atualizar(Medico med, String column, String data);
	
	public Medico buscar(int id);
	
	public List<Medico> listar();
	
	public List<Medico> buscarPorNome(String nome);
	
}
