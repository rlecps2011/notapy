import xml.etree.ElementTree as ET
import os

diretorio = './xml/'
arquivos = os.listdir(diretorio)

contador = 0
contador2 = 0
contador3 = 0

for arquivo in arquivos:
    xml = ET.parse(f'{diretorio}{arquivo}')
    ns='{http://www.portalfiscal.inf.br/nfe}'
    raiz = xml.getroot()
    contador3 += 1

    #verifica sem tem xped na nota.

    if raiz.find(f'{ns}NFe/{ns}infNFe/{ns}det/[@nItem="1"]/{ns}prod/{ns}xPed') is not None:
        contador += 1
        nf_numero = raiz.find(f'{ns}NFe/{ns}infNFe/{ns}ide/{ns}nNF').text
        nf_serie = raiz.find(f'{ns}NFe/{ns}infNFe/{ns}ide/{ns}serie').text
        for_cnpj = raiz.find(f'{ns}NFe/{ns}infNFe/{ns}emit/{ns}CNPJ').text
        for_nome = raiz.find(f'{ns}NFe/{ns}infNFe/{ns}emit/{ns}xNome').text

        print (f'Nota: {nf_numero}, {nf_serie} fornecedor: {for_nome}, cnpj: {for_cnpj} \n')
    else:
        contador2 += 1

print(contador, 'notas com xped\n')
print(contador2, 'notas sem xped\n')
print(contador3, 'notas analisadas\n')