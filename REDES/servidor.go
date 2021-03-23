package main

import (
	"fmt"
	"math/rand"
	"net"
	"sck"
	"strconv"
	"strings"
	"time"
	//"reflect"
)

var (
	idxUsers      int
	users         map[int]User
	clientesEnder map[int]*net.UDPAddr
	index         int
	endereco      *net.UDPAddr
	txtRes        []byte
	cadastrado    bool
	logado        bool
	filmes        map[int]Filme
	idxFilmes     int
)

type User struct {
	nick  string
	senha string
	end   *net.UDPAddr
	chat  bool
}

type Filme struct {
	titulo    string
	descricao string
	diretor   string
}

func verError(erro error) {
	if erro != nil {
		fmt.Println("Erro -> ", erro)
		fmt.Println("Saindo")
		panic("")
	}
}

func entrarOrCadastrar() ([]byte, int) {
	txt := "Bem vindo ao servidor\n|(1)->Entrar \n|(2)->Cadastre-se"
	buffer := []byte(txt)
	return buffer, len(buffer)
}

func exibirMenu() ([]byte, int) {
	txt := "\nMenu: \n|(1)-> Inverter String \n|(2)-> IMC \n|(3)-> Número Aleatório \n|(4)-> Mensagem direta \n|(5)-> Chat \n|(6)-> Cadastrar filme \n|(7)-> Filme Aleatório \n|(8)-> Sair \n|(9)-> Visualizar chat direto (se houver) "
	buffer := []byte(txt)
	return buffer, len(buffer)
}

func conectar_usuario(buffer_receber []byte, tam int, end_cliente *net.UDPAddr) {
	if strings.Contains(string(buffer_receber[0:tam]), "CONNECT") {
		clientesEnder[index] = end_cliente
		index++
	}
}

func cadastrarUser(parts []string, end *net.UDPAddr) ([]byte, bool) {
	if idxUsers == 1 {
		users[1] = User{parts[1], parts[2], end, false}
		res := "Usuário cadastrado com sucesso"
		idxUsers++
		txtByte := []byte(res)
		return txtByte, true
	} else {
		existeOUser := false
		for n := 1; n < idxUsers; n++ {
			if users[n].nick == parts[1] {
				existeOUser = true
			}
		}
		if !existeOUser {
			users[idxUsers] = User{parts[1], parts[2], end, false}
			res := "Usuário cadastrado com sucesso"
			idxUsers++
			txtByte := []byte(res)
			return txtByte, true
		} else {
			res := "Usuário já cadastrado, reinicie o cliente"
			txtByte := []byte(res)
			return txtByte, false
		}
	}
}

func entrarUser(parts []string, end *net.UDPAddr) ([]byte, bool) {
	existeOUser := false
	for n := 1; n < idxUsers; n++ {
		if users[n].nick == parts[1] && users[n].senha == parts[2] {
			users[n] = User{parts[1], parts[2], end, false}
			existeOUser = true
		}
	}
	if existeOUser {
		res := "Usuário logado com sucesso"
		txtByte := []byte(res)
		return txtByte, true
	} else {
		res := "Usuário inexistente, reinicie o cliente"
		txtByte := []byte(res)
		return txtByte, false
	}
}

func main() {
	index = 1
	clientesEnder = make(map[int]*net.UDPAddr)
	idxUsers = 1
	users = make(map[int]User)
	cadastrado = false
	logado = false
	idxFilmes = 1
	filmes = make(map[int]Filme)

	socket := sck.AbrirSocketServidor("udp", sck.CriarEndereco("127.0.0.1", 10301))
	defer socket.Close()

	for {
		buffer_receber := make([]byte, 1024)
		tam, end_cliente, erro := socket.ReadFromUDP(buffer_receber)
		verError(erro)

		if strings.Contains(string(buffer_receber[0:tam]), "CONNECT") {
			conectar_usuario(buffer_receber, tam, end_cliente)
			buffer, tamB := entrarOrCadastrar()
			_, erro = socket.WriteToUDP(buffer[0:tamB], end_cliente)
		}

		if strings.Contains(string(buffer_receber[0:tam]), "L1") || strings.Contains(string(buffer_receber[0:tam]), "E2") {
			parts := strings.Split(string(buffer_receber[0:tam]), ";")
			if parts[0] == "E2" {
				txtRes, cadastrado = cadastrarUser(parts, end_cliente)
				tamR := len(txtRes)
				_, erro = socket.WriteToUDP(txtRes[0:tamR], end_cliente)
			} else {
				txtRes, logado = entrarUser(parts, end_cliente)
				tamR := len(txtRes)
				_, erro = socket.WriteToUDP(txtRes[0:tamR], end_cliente)
			}
		}

		if logado || cadastrado {
			if (!strings.Contains(string(buffer_receber[0:tam]), "MENU")) || strings.Contains(string(buffer_receber[0:tam]), "MENUR") {
				buffer, tamB := exibirMenu()
				_, erro = socket.WriteToUDP(buffer[0:tamB], end_cliente)
			} else if strings.Contains(string(buffer_receber[0:tam]), "MENU") {
				parts := strings.Split(string(buffer_receber[0:tam]), ";")
				switch parts[1] {
				case "1":
					if len(parts) == 3 {
						txt := "RES;" + Reverse(parts[2])
						txtRes = []byte(txt)
						x0 := len(txtRes)
						_, erro = socket.WriteToUDP(txtRes[0:x0], end_cliente)
					}
				case "2":
					if len(parts) == 3 {
						txt := "RES;" + imc(parts[2]) 
						txtRes = []byte(txt)
						x0 := len(txtRes)
						_, erro = socket.WriteToUDP(txtRes[0:x0], end_cliente)
					}

				case "3":
					if len(parts) == 3 {
						txt := "RES;" + numAleatorio(parts[2])
						txtRes = []byte(txt)
						x0 := len(txtRes)
						_, erro = socket.WriteToUDP(txtRes[0:x0], end_cliente)
					}

				case "4":
					if len(parts) == 3 {
						chatDireto(parts[2], socket, end_cliente)
					}
				case "5":
					if len(parts) == 3 {
						//fmt.Println("server")
						ativarChat(end_cliente)
						chat(parts[2], socket, end_cliente)
					}
				case "6":
					if len(parts) == 3 {
						txt := "RES;" + cadastrarFilme(parts[2])
						txtRes = []byte(txt)
						x0 := len(txtRes)
						_, erro = socket.WriteToUDP(txtRes[0:x0], end_cliente)
					}
				case "7":
					if len(parts) == 2 {
						filme := filmeAleatorio()
						txt := "RES;" + filme
						txtRes = []byte(txt)
						x0 := len(txtRes)
						_, erro = socket.WriteToUDP(txtRes[0:x0], end_cliente)
					}
				case "8":
					if len(parts) == 2 {
						desconectar(end_cliente)
					}
				}
			}
		}
	}
}

func Reverse(s string) string {
	runes := []rune(s)
	for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
		runes[i], runes[j] = runes[j], runes[i]
	}
	return string(runes)
}

func imc(msg string) string {
	parts := strings.Split(msg, ",")
	altura, _ := strconv.ParseFloat(parts[0], 64)
	peso, _ := strconv.ParseFloat(parts[1], 64)
	imc := peso / (altura * altura)
	txt := "Seu IMC é: " + fmt.Sprintf("%.2f", imc)
	return txt
}

func numAleatorio(msg string) string {
	numAle := geraNumAleatorio(msg)
	res := "Seu numero aleatório é: " + numAle
	return res
}

func geraNumAleatorio(msg string) string {
	rand.Seed(time.Now().UnixNano())
	parts := strings.Split(msg, ",") 
	min, _ := strconv.Atoi(parts[0])
	max, _ := strconv.Atoi(parts[1])
	return strconv.Itoa(rand.Intn(max-min+1) + min)
}

func cadastrarFilme(msg string) string {
	parts := strings.Split(msg, ",") 
	if idxFilmes == 1 {
		filmes[1] = Filme{parts[0], parts[1], parts[2]}
		idxFilmes++
		return "Filme adicionando com sucesso"
	} else {
		temOFilme := false
		for n := 1; n <= idxFilmes; n++ {
			if filmes[n].titulo == parts[0] {
				temOFilme = true
			}
		}
		if !temOFilme {
			filmes[idxFilmes] = Filme{parts[0], parts[1], parts[2]}
			idxFilmes++
			return "Filme adicionando com sucesso"
		} else {
			return "Filme já está na lista"
		}
	}
}

func filmeAleatorio() string {
	if idxFilmes == 2 {
		_, existe := filmes[1]
		if existe {
			txt := "Seu filme aleatorio é:" + filmes[1].titulo + "\nDescrição: " + filmes[1].descricao + "\nDiretor: " + filmes[1].diretor
			return txt
		} else {
			return "Não há filmes cadastrados\n"
		}
	} else if idxFilmes > 2 {
		minMax := "1," + strconv.Itoa(idxFilmes-1)
		numFilme, _ := strconv.Atoi(geraNumAleatorio(minMax))
		txt := "Seu filme aleatorio é:" + filmes[numFilme].titulo + "\nDescrição: " + filmes[numFilme].descricao + "\nDiretor: " + filmes[numFilme].diretor
		return txt
	} else {
		return "Não há filmes cadastrados\n"
	}
}

func chatDireto(msg string, socket *net.UDPConn, endCliente *net.UDPAddr) {
	parts := strings.Split(msg, ",") 
	ex := false
	for i := 1; i < idxUsers; i++ {
		if users[i].nick == parts[0] {
			ex = true
		}
	}
	if ex {
		for _, u := range users {
			if len(parts) == 2 && u.end != nil && u.nick == parts[0] {
				txt := "CD;" + parts[0] + ":" + parts[1]
				txtByte := []byte(txt)
				tam := len(txtByte)
				_, erro := socket.WriteToUDP(txtByte[0:tam], u.end)
				verError(erro)
				txt = "RES;Mensagem enviada"
				txtByte = []byte(txt)
				tam = len(txtByte)
				_, erro = socket.WriteToUDP(txtByte[0:tam], endCliente)
			} else if len(parts) == 2 && u.end == nil && u.nick == parts[0] {
				txt := "RES;Usuário não está online"
				txtByte := []byte(txt)
				tam := len(txtByte)
				_, erro := socket.WriteToUDP(txtByte[0:tam], endCliente)
				verError(erro)
			}
		}
	} else {
		txt := "RES;Usuário é inexistente"
		txtByte := []byte(txt)
		tam := len(txtByte)
		_, erro := socket.WriteToUDP(txtByte[0:tam], endCliente)
		verError(erro)
	}

}

func ativarChat(endCliente *net.UDPAddr) {
	for idx, u := range users {
		if u.end != nil && sck.IPsIguais(endCliente, u.end) {
			users[idx] = User{users[idx].nick, users[idx].senha, users[idx].end, true}
			break
		}
	}

}

func chat(msg string, socket *net.UDPConn, endCliente *net.UDPAddr) {
	userChat := 1
	for _, u := range users {
		if strings.Contains(msg, "SAIR") {
			txt := "CHAT;SAIR"
			txtByte := []byte(txt)
			tam := len(txtByte)
			fmt.Println("enviouSair")
			_, erro := socket.WriteToUDP(txtByte[0:tam], u.end)
			verError(erro)
		} else if u.chat {
			userChat++
			if u.end != nil && !sck.IPsIguais(endCliente, u.end) {
				txt := "CHAT;" + msg
				txtByte := []byte(txt)
				tam := len(txtByte)
				fmt.Println("enviou")
				_, erro := socket.WriteToUDP(txtByte[0:tam], u.end)
				verError(erro)
			}
		}
	}
}

func desconectar(endCliente *net.UDPAddr) {
	for idx, u := range users {
		if u.end != nil && sck.IPsIguais(endCliente, u.end) {
			users[idx] = User{u.nick, u.senha, nil, false}
			break
		}
	}
}
