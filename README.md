# climate_controller-simulator

Simulador, feito em Python 3.6, de um protótipo de climatizador feito enquanto eu estagiava no Hospital Martagão Gesteira, em 2017.


## Iniciando

Baixe o script em algum lugar do seu computador.
Eu também empacotei o script e os módulos em um binário para Windows.

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


## Rodando

### 0 - EXECUTE O PROGRAMA COMO ADMINISTRADOR/ROOT;
#### 1 - Selecione a porta serial ou RFCOMM Bluetooth;
#### 2 - Um JSON irá ser pré-carregado e enviado por toda eternidade;
#### 3 - Você pode enviar um JSON para alterar parâmetros;

```
Enviando "{ "t3":23 }" irá a temperatura máxima.

```
#### 4 - Você pode receber dados e realizar o parsing do JSON!
#### 5 - Parabéns!


## Construído com:

* [Python 3.6](https://docs.python.org/3/) - Linguagem do script
* [PyInstaller](http://www.pyinstaller.org/documentation.html) - Empacotador


## Contribuindo

Faça o que quiser. Mas leia a licença --> [LICENSE]


## Agradecimentos

* Obrigado StackOverflow - por existir
* Obrigado Miquéias Vasconcelos por me iniciar no mundo do Python

