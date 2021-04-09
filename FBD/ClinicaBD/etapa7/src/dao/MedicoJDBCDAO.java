package dao;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

import conexao.Conector;
import conexao.DAOException;
import entidades.Medico;

public class MedicoJDBCDAO implements MedicoDAO{

	public void salvar(Medico med) {
		Connection con = null;
		try {
			con = Conector.getConnection();
			String sql = "insert into funcionario (id_func, nome, tipo, "
					+ "espec_medico, endereco, bairro, cep, estado) "
					+ "values (?, ?, ?, ?, ?, ?, ?, ?)";
			PreparedStatement pst;
			pst = con.prepareStatement(sql);
			pst.setInt(1, med.getId_func());
			pst.setString(2, med.getNome());
			pst.setString(3, med.getTipo());
			pst.setString(4, med.getEspecialidade());
			pst.setString(5, med.getEndereco());
			pst.setString(6, med.getBairro());
			pst.setString(7, med.getCep());
			pst.setString(8, med.getEstado());
			pst.executeUpdate();
		} catch(SQLException e) {
			throw new DAOException("A operação não pôde ser realizada.", e);
		} finally {
			try {
				if (con != null)
					con.close();
			} catch (SQLException e) {
				throw new DAOException("Não foi possível finalizar a conexão.",e);
			}
		}
	}
	
	public void atualizar(Medico med, String column, String data) {
        Connection con = null;
        try {
            con = Conector.getConnection();
            String sql = "update funcionario set "+ column+"= ? where id_func = ? and tipo='Médico'";
            PreparedStatement pst;
            pst = con.prepareStatement(sql);
            //pst.setString(1, column);
            pst.setString(1, data);
            pst.setInt(2, med.getId_func());
            pst.executeUpdate();
        } catch(SQLException e) {
            throw new DAOException("A operação não pôde ser realizada.", e);
        } finally {
            try {
                if (con != null)
                    con.close();
            } catch (SQLException e) {
                throw new DAOException("Não foi possível finalizar a conexão.",e);
            }
        }
    }
	
	public void deletar(int id) {
		Connection con = null;
		try {
			con = Conector.getConnection();
			String sql = "delete from funcionario where id_func = ?";
			PreparedStatement pst = con.prepareStatement(sql);
			pst.setInt(1, id);
			pst.executeUpdate();
		} catch(SQLException e) {
			throw new DAOException("A operação não pôde ser realizada.", e);
		} finally {
			try {
				if (con != null)
					con.close();
			} catch (SQLException e) {
				throw new DAOException("Não foi possível finalizar a conexão.",e);
			}
		}
	}
	
	public Medico buscar(int id) {
		Connection con = null;
		Medico med = null;
		try {
			con = Conector.getConnection();
			String sql = "select id_func, nome, tipo, espec_medico, endereco, bairro, "
					+ "cep, estado from funcionario where id_func = ? and tipo = 'Médico' ORDER by id_func";
			PreparedStatement pst = con.prepareStatement(sql);
			pst.setInt(1, id);
			ResultSet rs = pst.executeQuery();
			if (rs.next()) {
				med = map(rs);
			}
		} catch(SQLException e) {
			throw new DAOException("A operação não pôde ser realizada.", e);
		} finally {
			try {
				if (con != null)
					con.close();
			} catch (SQLException e) {
				throw new DAOException("Não foi possível finalizar a conexão.",e);
			}
		}
		return med;
	}
	
	public List<Medico> listar(){
		Connection con = null;
		List<Medico> meds = null;
		try {
			con = Conector.getConnection();
			String sql = "select id_func, nome, tipo, espec_medico, endereco, bairro, "
					+ "cep, estado from funcionario where tipo = 'Médico'";
			PreparedStatement pst = con.prepareStatement(sql);
			ResultSet rs = pst.executeQuery();
			meds = new ArrayList<Medico>();
			while (rs.next()) {
				Medico m = map(rs);
				meds.add(m);
			}
		} catch(SQLException e) {
			throw new DAOException("A operação não pôde ser realizada.", e);
		} finally {
			try {
				if (con != null)
					con.close();
			} catch (SQLException e) {
				throw new DAOException("Não foi possível finalizar a conexão.",e);
			}
		}
		return meds;
	}
	
	public List<Medico> buscarPorNome(String nome){
		Connection con = null;
		List<Medico> meds = null;
		try {
			con = Conector.getConnection();
			String sql = "select id_func, nome, tipo, espec_medico, endereco, bairro, "
					+ "cep, estado from funcionario where nome = ?";
			PreparedStatement pst = con.prepareStatement(sql);
			pst.setString(1, "%" + nome.toUpperCase() + "%");
			ResultSet rs = pst.executeQuery();
			meds = new ArrayList<Medico>();
			while (rs.next()) {
				Medico m = map(rs);
				meds.add(m);
			}
		} catch(SQLException e) {
			throw new DAOException("A operação não pôde ser realizada.", e);
		} finally {
			try {
				if (con != null)
					con.close();
			} catch (SQLException e) {
				throw new DAOException("Não foi possível finalizar a conexão.",e);
			}
		}
		return meds;
	}
	
	private Medico map(ResultSet rs) throws SQLException {
		Medico med = new Medico();
		med.setId_func(rs.getInt("id_func"));
		med.setNome(rs.getString("nome"));
		med.setTipo(rs.getString("tipo"));
		med.setEspecialidade(rs.getString("espec_medico"));
		med.setEndereco(rs.getString("endereco"));
		med.setBairro(rs.getString("bairro"));
		med.setCep(rs.getString("cep"));
		med.setEstado(rs.getString("estado"));
		return med;
	}
	
}
