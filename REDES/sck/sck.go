package sck

import (
	"fmt"
	"net"
	"strconv"
	"strings"
)

var (
	endereco *net.UDPAddr
)

func verError(erro error) {
	if erro != nil {
		fmt.Println("Erro -> ", erro)
		fmt.Println("Saindo")
		panic("")
	}
}

func CriarEndereco(ip string, porta int) *net.UDPAddr {
	var endereco *net.UDPAddr
	endereco = new(net.UDPAddr)
	ipParts := strings.Split(ip, ".")
	var ipPartsByte [4]byte
	for i, parts := range ipParts {
		x, _ := strconv.Atoi(parts)
		ipPartsByte[i] = byte(x)
	}
	endereco.IP = net.IPv4(ipPartsByte[0], ipPartsByte[1], ipPartsByte[2], ipPartsByte[3])
	endereco.Port = porta
	return endereco
}

func AbrirSocketServidor(tipo string ,endereco *net.UDPAddr, ) *net.UDPConn {
	fmt.Println("Iniciando o servidor...")

	end := strings.Join([]string{endereco.IP.String(), strconv.Itoa(endereco.Port)}, ":")

	endereco, erro := net.ResolveUDPAddr(tipo, end)
	verError(erro)
	fmt.Println("Endereço foi resolvido")

	Socket, erro := net.ListenUDP("udp", endereco)
	verError(erro)
	fmt.Println("Servidor iniciado")
	return Socket
}

func AbrirSocketCliente(endereco, porta, tipo string) *net.UDPConn {
	fmt.Println("Iniciando cliente")
	Endereco, erro := net.ResolveUDPAddr(tipo, porta)
	verError(erro)
	Endereco_local, erro := net.ResolveUDPAddr(tipo, endereco)
	verError(erro)
	fmt.Println("Endereço foi resolvido")
	Socket, erro := net.DialUDP("udp", Endereco_local, Endereco)
	verError(erro)
	fmt.Println("Cliente foi iniciado")
	return Socket
}

func ExibirMsgDoServidor(Socket *net.UDPConn) {
	for {
		buffer_receber := make([]byte, 2048)
		tam, _, erro := Socket.ReadFromUDP(buffer_receber)
		verError(erro)

		fmt.Println(string(buffer_receber[0:tam]))
	}
}


func IPsIguais(endCliente, endComparar *net.UDPAddr) bool {
	ip := endCliente.IP.String()
	port := strconv.Itoa(endCliente.Port)
	end_cliente := ip + ":" + port
	
	ip = endComparar.IP.String()
	port = strconv.Itoa(endComparar.Port)
	end_comparar := ip + ":" + port

	if end_cliente != end_comparar{
		return false
	}
	return true
}