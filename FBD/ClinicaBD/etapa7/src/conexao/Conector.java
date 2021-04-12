package conexao;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class Conector {

	public static Connection getConnection() throws SQLException {
		return  DriverManager.getConnection("jdbc:postgresql://localhost/clinica", "admbd", "bdadm");
	}
	
}
