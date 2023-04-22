import gspread
import sys
import random
import datetime
import os
import time
import base64
import json
from oauth2client.service_account import ServiceAccountCredentials

#ARQUIVO JSON CODIFICADO EM BASE64
chave_b64 = "string" # substituir pela string codificada em base64

def ler_planilha(licenca):
    # Define as credenciais de autenticação
    scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
    credenciais = ServiceAccountCredentials.from_json_keyfile_dict(json.loads(base64.b64decode(chave_b64)), scope)  
    # Conecta-se à API do Google Sheets
    cliente = gspread.authorize(credenciais)    
    # Abre a planilha
    planilha = cliente.open("licenciamento")    
    # Seleciona a primeira página da planilha
    pagina = planilha.sheet1    
    # Lê o conteúdo da quarta coluna
    # percorre as células da coluna 2 e imprime o valor da célula correspondente na coluna 4
    for i in range(1, pagina.row_count):
        if pagina.cell(i, 3).value == str(licenca):
            print('Licença validada')
            if int(pagina.cell(i, 4).value) < 1:
                print('Licença Expirada')
                return False, None, None
            else:
                print(pagina.cell(i, 4).value + ' Dia(s) de licença disponivel.')
                print('Bem vindo '+ pagina.cell(i, 1).value)
                print('Esta licença lhe concede acesso ao '+ pagina.cell(i, 2).value)
                dia_expira = int(pagina.cell(i, 4).value)
                nome_cliente = str(pagina.cell(i, 1).value)
                
            # Verifica se a célula na coluna 6 tem valor diferente de '1'
                if pagina.cell(i, 6).value != '1':
                    # Se tiver valor diferente de '1', atualiza para '1'
                    print('licença ativada')
                    pagina.update_cell(i, 6, '1')
                    # Preenche a célula 7 com a data e hora atual
                    agora = datetime.datetime.now().strftime("%d/%m/%y %H:%M:%S")
                    pagina.update_cell(i, 7, agora)
            return True, dia_expira, nome_cliente
    else:
        
        print('Licença inválida')
        return False, None, None
#ler_planilha(333)

def logo():
    os.system('cls')
    clear = "\x1b[0m"
    colors = [36, 32, 34, 35, 31, 37]

    x = """ 
             /$$$$$$$  /$$     /$$ /$$$$$$$$ /$$   /$$  /$$$$$$  /$$   /$$
            | $$__  $$|  $$   /$$/|__  $$__/| $$  | $$ /$$__  $$| $$$ | $$
            | $$  \ $$ \  $$ /$$/    | $$   | $$  | $$| $$  \ $$| $$$$| $$
            | $$$$$$$/  \  $$$$/     | $$   | $$$$$$$$| $$  | $$| $$ $$ $$
            | $$____/    \  $$/      | $$   | $$__  $$| $$  | $$| $$  $$$$
            | $$          | $$       | $$   | $$  | $$| $$  | $$| $$\  $$$
            | $$          | $$       | $$   | $$  | $$|  $$$$$$/| $$ \  $$
            |__/          |__/       |__/   |__/  |__/ \______/ |__/  \__/                                                                                                                                                                                          
                            Desenvolvido por Gabriel Mattos                    
			                  """
    for N, line in enumerate( x.split( "\n" ) ):
        sys.stdout.write( " \x1b[1;%dm%s%s\n " % (random.choice( colors ), line, clear) )
        time.sleep( 0.05 )


#logo()