# climate_controller-simulator

Simulador, feito em Python 3.6, de um protótipo de climatizador feito enquanto eu estagiava no Hospital Martagão Gesteira, em 2017.

--------------------------------

## Iniciando

Baixe o script em algum lugar do seu computador.

Eu também empacotei o script e os módulos em um binário para Windows. [DOWNLOAD](https://github.com/requeijaum/climate_controller-simulator/blob/master/climate_controller-simulator-win32-bin.zip)

---------------------------

### Pré-requisitos

#### Caso você não tenha escolhido baixar o binário - e sim o script... baixe o PIP para Python 3 antes. 

[Se vire e dê seus pulos](https://pip.pypa.io/en/stable/installing/).
Você vai precisar importar os seguintes módulos:

Em uma máquina *nix/BSD:

```
sudo -H python3 -m pip install pySerial simplejson 
```

Pode existir ainda a necessidade de importar o serial.tools.list_ports:

```
sudo -H python3 -m pip install serial.tools.list_ports
```


Caso dê tudo certo: o script vai executar normalmente e você não terá nenhum aviso de erro por falta de módulos não-importados.
Caso ocorra algum problema: verifique as issues desse repositório. 


--------------------------

### Eu uso Windows !

Eu desenvolvi esse simulador utilizando o Mac OS X 10.5 com Python 3. A maneira dele tratar a porta serial e o protocolo RFCOMM diferem do Windows. Verifique [esta issue](https://github.com/requeijaum/climate_controller-simulator/issues/1) caso você esteja tendo problemas.

--------------------------

### Root/privilégios de administrador podem ser necessários

Eu tive problemas com o pySerial tentando acessar as portas seriais sem os privilégios necessários de usuário. Esse comportamento pode variar. Por isso: recomendo executar o script como super-usuário/administrador/root.

---------------------------

## Rodando

### 0 - EXECUTE O PROGRAMA COMO ADMINISTRADOR/ROOT;
#### 1 - Selecione a porta serial ou RFCOMM Bluetooth;
#### 2 - Um JSON irá ser pré-carregado e enviado por toda eternidade;
#### 3 - Você pode enviar um JSON para alterar parâmetros do simulador;

```
Enviando "{ "t3":23 }" altera o valor de temperatura máxima.

```
#### 4 - Você pode receber dados e realizar o parsing do JSON;
#### 5 - Parabéns!

--------------------------------
## Referência do JSON

```javascript
json_main = {
	"a":0, 
	"b":0, 
	"m":0, 
	"p":0, 
	"pd1":1200, 
	"pd2":1700, 
	"pl1":700, 
	"pl2":1300, 
	"s":0, 
	"t1":20, 
	"t2":23, 
	"t3":25, 
	"tt":5 
}
```

* "a" é o parâmetro de controle automático;
* "b" é um bit que uso para polling de dados;
* "m" é um valor entre 0 e 127 para máscara de bits de um vetor que representa os 7 dias da semana;
* "p" é o bit que indica presença na sala;
* "pd#" e "pl#" são números inteiros que representam hora (ex: 12:00 = 1200; 5:30 = 530);
* "s" é um bit flag para Status - não lembro exatamente pra quê utilizo;
* "t[1,2,3]" são números inteiros de 2 algarismos que representam temperaturas em graus Celsius - mínima, atual e máxima, respectivamente;
* "tt" é um número que representa os minutos de limiar da operação do climatizador;

------

### Sobre o buffer de recepção

É importante usar "\n" no início de cada comando a enviar - pois eu implementei um algoritmo que apenas seleciona o último comando recebido, dentro do espaço de tempo para receber. Isso evita algum travamento lógico ou erro na decodificação do JSON caso hajam vários comandos recebidos rapidamente ainda no buffer.

---------------------


## Construído com:

* [Python 3.6](https://docs.python.org/3/) - Linguagem do script
* [PyInstaller](http://www.pyinstaller.org/documentation.html) - Empacotador


## Contribuindo

Faça o que quiser. Mas leia a licença --> [LICENSE]


## Agradecimentos

* Obrigado StackOverflow - por existir
* Obrigado Miquéias Vasconcelos por me iniciar no mundo do Python.
* Obrigado Victor Ben-Hur pela oportunidade e pelo desafio de testar meus conhecimentos.
 
