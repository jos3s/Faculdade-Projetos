package programa;

import java.util.List;
import java.util.Scanner;

import javax.swing.JOptionPane;

import dao.MedicoDAO;
import dao.MedicoJDBCDAO;

import entidades.Medico;

public class Principal {
	public static Scanner sc=new Scanner(System.in);

	public static void main(String[] args) {

		MedicoDAO baseMedico = new MedicoJDBCDAO();

		String menu = "Escolha uma op��o:\n1 - Exibir M�dicos \n2 - Cadastrar M�dicos \n3 - Alterar Atributos do M�dico \n4 - Deletar M�dicos";
		char option;
		do {

			try {
				option = JOptionPane.showInputDialog(menu).charAt(0);
			} catch(Exception e) {
				option = 5;
				System.exit(0);
			}

			switch (option) {
			case '1':
				listarTabelasMedico(baseMedico.listar());
				break;
			case '2':
				criarMedico(baseMedico);
				break;
			case '3':
				atualizarMedico(baseMedico);
				break;
			case '4':
				deletarMedico(baseMedico);
				break;
			case '5':
				break;
			default:
				JOptionPane.showMessageDialog(null, "Op��o Inv�lida");
				break;
			}
		}while (option != '5');


	}


	public static void listarTabelasMedico(List<Medico> baseMedico){
		StringBuilder list = new StringBuilder();
		list.append("Funcion�rios:\n");
		for(Medico con : baseMedico) {
			list.append(con).append("\n");
		}

		StringBuilder lista = new StringBuilder();
		lista.append(list);

		JOptionPane.showMessageDialog(null, lista);
	}

	public static void criarMedico(MedicoDAO baseMedico) {
		try {
			Medico med=new Medico();
			int id = Integer.parseInt(JOptionPane.showInputDialog("Digite o ID:", med.getId_func()));
			String nome = JOptionPane.showInputDialog("Digite o Nome: ", med.getNome());
			String espc = JOptionPane.showInputDialog("Digite a Especialidade: ", med.getEspecialidade());
			String end = JOptionPane.showInputDialog("Digite o Endere�o", med.getEndereco());
			String bairro = JOptionPane.showInputDialog("Digite o Bairro: ", med.getBairro());
			String cep = JOptionPane.showInputDialog("Digite o CEP: ", med.getCep());
			String estado =JOptionPane.showInputDialog("Digite a sigla do Estado: ", med.getEstado());

			med.setId_func(id);
			med.setNome(nome);
			med.setEspecialidade(espc);
			med.setBairro(bairro);
			med.setEndereco(end);
			med.setEstado(estado);
			med.setCep(cep);
			med.setTipo("M�dico");
			baseMedico.salvar(med);
			JOptionPane.showMessageDialog(null, "M�dicos adicionado ao banco de dados");
		} catch (Exception e) {
			JOptionPane.showMessageDialog(null, e.getCause().getMessage());
		}
	}


	public static void atualizarMedico(MedicoDAO baseMedico) {
		int id = Integer.parseInt(JOptionPane.showInputDialog("Digite o ID do M�dico", null));
		Medico med = baseMedico.buscar(id);
		if(med == null) {
            JOptionPane.showMessageDialog(null, "O ID n�o est� registrado na base de dados ou n�o � do tipo M�dico");
        }else{
        	String[] options = {"Nome", "Especialidade", "Endere�o", "Bairro", "CEP", "Estado"};
        	int opt = JOptionPane.showOptionDialog(null	, "Qual dado desse m�dico queres alterar?", "Alterar Valores",
        			JOptionPane.DEFAULT_OPTION, JOptionPane.QUESTION_MESSAGE, null, options, options[0]);

        	String dado = JOptionPane.showInputDialog("Novo valor: ");
        	switch (opt) {
        	case 0:
        		baseMedico.atualizar(med, "nome", dado);
        		break;
        	case 1:
        		baseMedico.atualizar(med, "espec_medico", dado);
        		break;
        	case 2:
        		baseMedico.atualizar(med, "endereco", dado);
        		break;
        	case 3:
        		baseMedico.atualizar(med, "bairro", dado);
        		break;
        	case 4:
        		baseMedico.atualizar(med, "cep", dado);
        		break;
        	case 5:
        		baseMedico.atualizar(med, "estado", dado);
        		break;
        	default:
        		JOptionPane.showMessageDialog(null, "Erro ao selecionar op��o!");
        		break;
        	}

        }
	}

	public static void deletarMedico(MedicoDAO baseMedico) {
		int id = Integer.parseInt(JOptionPane.showInputDialog("Digite o ID do M�dico a ser excluido: "));
		if(baseMedico.buscar(id) == null) {
            JOptionPane.showMessageDialog(null, "O ID n�o est� registrado na base de dados ou n�o � tipo M�dico");
        }else{
            baseMedico.deletar(id);
            JOptionPane.showMessageDialog(null, "M�dico deletado do banco de dados");
        }

	}
}

