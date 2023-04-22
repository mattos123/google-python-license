# google-python-license

## Funcionalidades

- Temas dark e light
- Preview em tempo real
- Modo tela cheia
- Multiplataforma
Utilizaremos o google sheets para criar um sistema de validação de licenciamento utilizando python e apis do google drive e google sheets
<br />
Crie uma conta no ambiente cloud da google, e ative as respectivas apis que usamos em nosso codigo python
<br />
Busque pela api do google drive:
![image](https://user-images.githubusercontent.com/21156270/233754676-001cd6bf-f120-407c-b1cd-6b8667940cde.png)
<br />
Ative-a
![image](https://user-images.githubusercontent.com/21156270/233754758-fdb1e106-f17a-4338-863a-bc204e1e9c26.png)
<br />
Agora buscaremos pela api do google sheets e a ativaremos da mesma forma que fizemos anteriormente
<br />
![image](https://user-images.githubusercontent.com/21156270/233754841-f0fd9599-7982-4556-9e65-f45ef89992fc.png)
<br />
Com estas etapas inicias, sua conta no ambiente google cloud tem ativada as apis necessárias para o nosso codigo se conectar ao arquivo do google sheets via google drive, e ler e escrever o arquivo atraves do google sheets
<br />
![image](https://user-images.githubusercontent.com/21156270/233754436-b5ae74ba-c42c-44a1-a7f2-283150fa85a0.png)
<br />
Agora é necessário gerar um arquivo .json contendo as credenciais que a api do google drive e google sheets, define para poder realizar o post
<br />
![image](https://user-images.githubusercontent.com/21156270/233754998-74d1d09a-c859-4d53-9c32-781943ecd09c.png)
Crie suas credenciais utilizando o método contas de serviço
<br />
![image](https://user-images.githubusercontent.com/21156270/233755372-205cdb9b-36c1-4d2c-90b2-04f9a8b262c8.png)
<br />
Defina um nome para sua conta de serviço
![image](https://user-images.githubusercontent.com/21156270/233755454-2981f7e2-d06a-4bec-89c9-5c05ccf6fd3f.png)
<br />
Agora precisamos definir as permissões que a conta de serviço criada terão sobre o post e get
![image](https://user-images.githubusercontent.com/21156270/233755570-a11dc766-d3d1-4178-a952-9e345a7e8a5d.png)
<br />
Definimos a permissão da conta de servico como editor, e continuamos
![image](https://user-images.githubusercontent.com/21156270/233755595-d5bd2917-3d28-4185-bfd7-81f4b7ee7e1e.png)
<br />
Concluimos a criação da conta de serviço
![image](https://user-images.githubusercontent.com/21156270/233755644-b643c286-ef29-4e2e-a60c-a12911971dc7.png)
<br />
Gerencie sua conta de serviço e navegue ate a aba "Chaves", clique em adicionar chave, em seguida criar nova chave
![image](https://user-images.githubusercontent.com/21156270/233755732-2e5a9a7e-2e52-4f6a-a3b6-7e47aabfbfbf.png)
<br />
Defina o tipo de chave como json, e clique em criar
![image](https://user-images.githubusercontent.com/21156270/233755768-39c19608-5319-4c4d-a3bc-fd89c8d8be94.png)
<br />
Após criar a chave, a mesma sera baixada para seu computador, salve este arquivo como backup
![image](https://user-images.githubusercontent.com/21156270/233755819-7b67bbd7-0ab8-4a34-86d9-0baf5339d3e1.png)
<br />
Crie uma copia de sua chave, na mesma pasta onde temos o nosso codigo em python, e renomeio o arquivos para "credenciais"
![image](https://user-images.githubusercontent.com/21156270/233756240-048bc1b4-d005-49c7-bd76-0917b31aef8f.png)
<br />
Com o ambiente cloud devidamente configurado, e chave criada, iremos agora criar a planilha no google sheets.
![image](https://user-images.githubusercontent.com/21156270/233756970-ed6a252b-7407-4e76-96e6-374612361301.png)
<br />
A planilha deve conter 7 colunas e uma quantidade pequena de linhas(utilizando muitas linhas na planilha e as apis gratuitas, ficamos limitados a um numero de consultas por minuto, tendo em vista que nosso codigo varre todas as linhas da planilha para validar o licenciamento, devemos evitar uma planilha muito longa), sendo elas:
<br />
cliente,	software,	licenca,	tempo,	data_cadastro,	ativada,	data_ativacao
<br />
![image](https://user-images.githubusercontent.com/21156270/233757009-da4f1629-e65a-402a-a55c-3620e2dce00e.png)
<br />
É necessário compartilhar a planilha com a conta de serviço que ficara responsavel pela comuniacao da nossa planilha com nossa aplicação final
<br />
![image](https://user-images.githubusercontent.com/21156270/233757524-278c1365-b81d-4147-a153-e52e7486be6f.png)
<br />
Acesse seu painel de gerenciamento de credenciais dentro do google cloud, copie o email criado para a conta de serviço,
<br />
![image](https://user-images.githubusercontent.com/21156270/233757571-7d234d17-1900-4620-aaac-18043ef7d787.png)
<br />
Com o endereço de email da conta de serviço em maos, volte a sua planilha e cole o endereco de email conforme a foto, e defina o email como editor da planilha
<br />
![image](https://user-images.githubusercontent.com/21156270/233757698-3cd42cda-15cb-40f2-b9d6-84017faf8e16.png)
<br />
Após criar a planilha e as devidas colunas será necessário criar alguns scripts na planilha
![image](https://user-images.githubusercontent.com/21156270/233757160-317399d7-0597-4634-aa52-771d9843ad1f.png)
<br />
O primeiro script, irá diminuir os dias de licença que o usuario tem, e ativará a licença no primeiro uso dela, baseado no valor da coluna "ativada"
<br />
![image](https://user-images.githubusercontent.com/21156270/233763849-f315ec90-bc58-48ea-a684-36cdcb3da3ad.png)
<br />
O segundo script realiza o auto preenchimento do campo data_cadastro, ao inserir o nome de um novo cliente, e ira gerar um numero de licença aleatorio, baseado em qual software foi selecionado da lista de validação de dados da coluna 2 (b)
<br />
![image](https://user-images.githubusercontent.com/21156270/233763905-cc4c138e-74ad-43d5-b71b-91d860b53c73.png)
<br />
Aqui está um exemplo de como a configurar a validação de dados para a coluna 2 (b)
<br />
![image](https://user-images.githubusercontent.com/21156270/233764070-eb213e81-822d-4d2c-8b81-787a6a02a735.png)
<br />
Após criarmos os scripts é necessário definirmos os seus acionadores de tempo
<br />
![image](https://user-images.githubusercontent.com/21156270/233757815-50174b38-86a3-45e4-97b9-54e56f0720cc.png)
<br />
Criaremos o um acionador que chama a o parametro de execução "diminuirValor", vinculado ao segundo script, um acionaor baseado no tempo, em horas, sendo executado de hora em hora na nossa planilha
(resumidamente, o que fazemos é comparar a ultima data de alteracao do documento feita pela conta de servico, e se essa data for > que a data atual por 24 horas, o script remove 1 dia do tempo disponivel da licença)
![image](https://user-images.githubusercontent.com/21156270/233757911-3ae4a306-88b9-4265-b836-1d2a5bf27784.png)
<br /> 
Planilha configurada, significa que ao preencher os campos marcados em vermelho na planilha, e ativar a licença via software, os campos marcados em amarelo serão preenchidos automaticamente
<br />
![image](https://user-images.githubusercontent.com/21156270/233764148-db6dfeb0-073c-4b69-b381-b9dd9001f4e6.png)
<br /> 
Ao inserir o codigo de licença gerado automaticamente pela planilha no software, o mesmo ira buscar a licença inserida na interface, em todas as linhas da coluna 2(b) planilha e se encontrar a licença , ela estiver com tempo > 0, e ativa < 1 ele ira ativar a licença e comecara a descontar o tempo a cada 24h a partir da ativacao
<br/>
![image](https://user-images.githubusercontent.com/21156270/233764395-83bc80d1-2e2d-406c-8d79-2b031185d3d9.png)
<br/>
Agora deixe sua criativade fluir e aprimore este codigo, crie um formulario para cadastro de clientes nesta planilha que criamos, utilize o sistema de validacao de licenciamento para vender seu software etc..
<br/>
Compreendendo o codigo voce pode adicionar outras colunas na planilha para liberar acessos a determinadas funcoes do software atraves de modificacoes no codigo

