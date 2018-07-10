echo "você precisa do pyinstaller instalado para seu ambiente python"
mkdir pyinstaller
cd pyinstaller
pyinstaller -F ../src/fancoil_hec-python-arduino-simulador.py --icon="../resources/icon.ico" --clean
echo "verifique o binario em: pyinstaller/dist/fancoil_hec-python-arduino-simulador.exe"

