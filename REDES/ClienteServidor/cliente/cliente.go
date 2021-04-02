package main

import (
	//"bufio"
	"fmt"
	//"os"
	"net"
	"sck"
	"strconv"
	"strings"
)

func ver_erro(erro error) {
	if erro != nil {
		fmt.Println("Erro -> ", erro)
		fmt.Println("Saindo")
		panic("")
	}
}

type usuario struct {
	nick  string
	senha string
}

var (
	nick               string
	esc                bool
	entrarCadastrarNum int
	msg_txt            string
	perfil             usuario
	menuEscolha        int
	resposta           string
	nomeFilme          string
	descricaoFilme     string
	diretorFilme       string
	cadastro           bool
	sair               bool
	altura             int
	peso               int
	msgServidor        string
)

func enviarMsg(socket *net.UDPConn, msg string) {
	buffer_envio := []byte(msg)
	_, erro := socket.Write(buffer_envio)
	ver_erro(erro)
}

func entrarCadastrar(msgServidor string, socket *net.UDPConn) {
	entrarCadastrar := "Bem vindo ao servidor\n|(1)->Entrar \n|(2)->Cadastre-se"
	if strings.Contains(msgServidor, entrarCadastrar) {
		for esc {
			fmt.Print("Digite a sua escolha:")
			fmt.Scanln(&msg_txt)
			entrarCadastrarNum, _ = strconv.Atoi(msg_txt)
			if entrarCadastrarNum == 1 || entrarCadastrarNum == 2 {
				esc = false
			}
		}
		if entrarCadastrarNum == 1 {
			fmt.Print("Digite o seu nick:")
			fmt.Scanln(&perfil.nick)
			fmt.Print("Digite a sua senha:")
			fmt.Scanln(&perfil.senha)
			msg := "L1;" + perfil.nick + ";" + perfil.senha
			enviarMsg(socket, msg)
		} else {
			fmt.Print("Cadastre o seu nick:")
			fmt.Scanln(&perfil.nick)
			fmt.Print("Cadastre a sua senha:")
			fmt.Scanln(&perfil.senha)
			msg := "E2;" + perfil.nick + ";" + perfil.senha
			enviarMsg(socket, msg)
		}
	}
}

func main() {
	socket := sck.AbrirSocketCliente("127.0.0.1:0", ":10301", "udp")
	defer socket.Close()
	//go sck.ExibirMsgDoServidor(socket)
	//buff_scan := bufio.NewReader(os.Stdin)
	if strings.EqualFold(nick, "") {
		buffer_envio := []byte("CONNECT")
		_, erro := socket.Write(buffer_envio)
		ver_erro(erro)
	}
	esc = true
	cadastro = false
	for {
		buffer_receber := make([]byte, 1024)
		tam, _, _ := socket.ReadFromUDP(buffer_receber)
		msgServidor = string(buffer_receber[0:tam])
		if strings.Contains(msgServidor, "RES") || strings.Contains(msgServidor, "CD") {
			fmt.Print("----------\n")
			parts := strings.Split(msgServidor, ";")
			fmt.Print(parts[1])
		} else {
			fmt.Println(msgServidor)
		}
		if strings.Contains(msgServidor, " logado com sucesso") || strings.Contains(msgServidor, "cadastrado com sucesso") {
			cadastro = true
		}
		if !cadastro {
			entrarCadastrar(msgServidor, socket)
		}
		esc = true
		txtMenu := "\nMenu:"
		if strings.Contains(msgServidor, txtMenu) {
			for esc {
				fmt.Print("Digite a sua escolha:")
				fmt.Scanln(&msg_txt)
				fmt.Print("----------\n")
				menuEscolha, _ = strconv.Atoi(msg_txt)
				if menuEscolha >= 1 || menuEscolha <= 9 {
					esc = false
					if menuEscolha != 7 {
						msg := "MENU;" + strconv.Itoa(menuEscolha)
						enviarMsg(socket, msg)
					}
				}
			}
		}

		if menuEscolha == 1 {
			fmt.Println("Digite uma frase (SAIR para sair):")
			for {
				fmt.Scanln(&msg_txt)
				if strings.Contains(msg_txt, "SAIR") {
					msg := "MENUR"
					enviarMsg(socket, msg)
					break
				} else {
					msg := "MENU;1;" + msg_txt
					enviarMsg(socket, msg)
				}
				for {
					tam, _, _ = socket.ReadFromUDP(buffer_receber)
					msgServidor = string(buffer_receber[0:tam])
					parts := strings.Split(msgServidor, ";")
					if parts[0] == "RES" {
						fmt.Println(parts[1])
						break
					}
				}
			}
		} else if menuEscolha == 2 {
			for {
				fmt.Println("Digite a sua altura(metros) usando '.' como separador e seu peso(kg) (Use ',' para separar os valores): ")
				fmt.Scanln(&msg_txt)
				if len(strings.Split(msg_txt, ",")) == 2 {
					msg := "MENU;2;" + msg_txt 
					enviarMsg(socket, msg)
					for {
						tam, _, _ = socket.ReadFromUDP(buffer_receber)
						msgServidor = string(buffer_receber[0:tam])
						parts := strings.Split(msgServidor, ";")
						if parts[0] == "RES" {
							fmt.Println(parts[1])
							msg := "MENUR"
							enviarMsg(socket, msg)
							break
						}
					}
					break
				}
			}
		} else if menuEscolha == 3 {
			fmt.Println("Digite menor valor e o maior do range do seu numero aleatorio (Separe com ','): ")
			fmt.Scanln(&msg_txt)
			msg := "MENU;3;" + msg_txt
			enviarMsg(socket, msg)
			for {
				tam, _, _ = socket.ReadFromUDP(buffer_receber)
				msgServidor = string(buffer_receber[0:tam])
				parts := strings.Split(msgServidor, ";")
				if parts[0] == "RES" {
					fmt.Println(parts[1])
					msg := "MENUR"
					enviarMsg(socket, msg)
					break
				}
			}
		} else if menuEscolha == 4 {
			fmt.Println("Digite o nick do perfil e a mensagem em seguida (separados por ','): ")
			fmt.Scanln(&msg_txt)
			msg := "MENU;4;" + msg_txt
			enviarMsg(socket, msg)
			for {
				tam, _, _ = socket.ReadFromUDP(buffer_receber)
				msgServidor = string(buffer_receber[0:tam])
				parts := strings.Split(msgServidor, ";")
				if parts[0] == "RES" {
					fmt.Println(parts[1])
					msg := "MENUR"
					enviarMsg(socket, msg)
					break
				}
			}
		} else if menuEscolha == 5 {
			fmt.Print("Digite uma frase pro chat (SAIR para sair): ")
			for {
				fmt.Scanln(&msg_txt)
				if strings.Contains(msg_txt, "SAIR") {
					msg := "MENU;5;SAIR"
					enviarMsg(socket, msg)
					break
				} else {
					msg := "MENU;5;" + perfil.nick + ": " + msg_txt
					enviarMsg(socket, msg)
				}
				for {
					tam, _, _ = socket.ReadFromUDP(buffer_receber)
					msgServidor = string(buffer_receber[0:tam])
					parts := strings.Split(msgServidor, ";")
					if parts[0] == "CHAT" && parts[1] != "SAIR" {
						fmt.Println(parts[1])
						break
					} else {
						break
					}
				}
			}
		} else if menuEscolha == 6 {
			fmt.Print("Digite o nome do filme: ")
			fmt.Scanln(&nomeFilme)
			fmt.Print("Digite a descrição do filme: ")
			fmt.Scanln(&descricaoFilme)
			fmt.Print("Digite o nome do diretor do filme: ")
			fmt.Scanln(&diretorFilme)
			if !strings.EqualFold(nomeFilme, "") && !strings.EqualFold(descricaoFilme, "") && !strings.EqualFold(diretorFilme, "") {
				msg := "MENU;6;" + nomeFilme + "," + descricaoFilme + "," + diretorFilme
				enviarMsg(socket, msg)
				for {
					tam, _, _ = socket.ReadFromUDP(buffer_receber)
					msgServidor = string(buffer_receber[0:tam])
					parts := strings.Split(msgServidor, ";")
					if parts[0] == "RES" {
						fmt.Println(parts[1])
						msg := "MENUR"
						enviarMsg(socket, msg)
						break
					}
				}
			}
		} else if menuEscolha == 7 {
			enviarMsg(socket, "MENU;7")
			for {
				tam, _, _ = socket.ReadFromUDP(buffer_receber)
				msgServidor = string(buffer_receber[0:tam])
				parts := strings.Split(msgServidor, ";")
				if parts[0] == "RES" {
					fmt.Println(parts[1])
					msg := "MENUR"
					enviarMsg(socket, msg)
					break
				}
			}
		} else if menuEscolha == 8 {
			enviarMsg(socket, "MENU;8")
			fmt.Println("Desconectado do servidor, encerrando programa...")
			break
		} else if menuEscolha == 9 {
			for {
				tam, _, _ = socket.ReadFromUDP(buffer_receber)
				msgServidor = string(buffer_receber[0:tam])
				parts := strings.Split(msgServidor, ";")
				if parts[0] == "CD" {
					fmt.Println(parts[1])
					msg := "MENUR"
					enviarMsg(socket, msg)
					break
				}
			}
		}
	}
}
