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

		Medico med = new Medico();
		MedicoDAO baseMedico = new MedicoJDBCDAO();

		String menu = "Escolha uma opção:\n1 - Exibir Médicos \n2 - Cadastrar Médicos \n3 - Alterar Atributos do Médico \n4 - Deletar Médicos";
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
				criarMedico(med);
				baseMedico.salvar(med);
				JOptionPane.showMessageDialog(null, "Médicos adicionado ao banco de dados");
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
				JOptionPane.showMessageDialog(null, "Opção Inválida");
				break;
			}
		}while (option != '5');


	}


	public static void listarTabelasMedico(List<Medico> baseMedico){
		StringBuilder list = new StringBuilder();
		list.append("Funcionários:\n");
		for(Medico con : baseMedico) {
			list.append(con).append("\n");
		}

		StringBuilder lista = new StringBuilder();
		lista.append(list);

		JOptionPane.showMessageDialog(null, lista);
	}

	public static void criarMedico(Medico med) {
		int id = Integer.parseInt(JOptionPane.showInputDialog("Digite o ID:", med.getId_func()));
		String nome = JOptionPane.showInputDialog("Digite o Nome: ", med.getNome());
		String espc = JOptionPane.showInputDialog("Digite a Especialidade: ", med.getEspecialidade());
		String end = JOptionPane.showInputDialog("Digite o Endereço", med.getEndereco());
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
		med.setTipo("Mï¿½dico");
	}


	public static void atualizarMedico(MedicoDAO baseMedico) {
		int id = Integer.parseInt(JOptionPane.showInputDialog("Digite o ID do Médico", null));
		Medico med = baseMedico.buscar(id);
		if(med == null) {
            JOptionPane.showMessageDialog(null, "O ID não está registrado na base de dados ou não é do tipo Médico");
        }else{
        	String[] options = {"Nome", "Especialidade", "Endereço", "Bairro", "CEP", "Estado"};
        	int opt = JOptionPane.showOptionDialog(null	, "Qual dado desse médico queres alterar?", "Alterar Valores",
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
        		JOptionPane.showMessageDialog(null, "Erro ao selecionar opção!");
        		break;
        	}

        }
	}

	public static void deletarMedico(MedicoDAO baseMedico) {
		int id = Integer.parseInt(JOptionPane.showInputDialog("Digite o ID do Médico a ser excluido: "));
		if(baseMedico.buscar(id) == null) {
            JOptionPane.showMessageDialog(null, "O ID não está registrado na base de dados ou não é tipo Médico");
        }else{
            baseMedico.deletar(id);
            JOptionPane.showMessageDialog(null, "Médico deletado do banco de dados");
        }

	}
}

