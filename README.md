# Bitcoin Price Tracker

Esse programa foi desenvolvido para automatizar o envio de e-mail via G-Mail utilizando Python. 


## 🔧 Ferramentas Utilizadas

-   smtplib: para fazer realizar todos os tramits de segurança para que o seu e-mail possa ser enviado.
-   email.message: para recolher os dados de envio do e-mail e fazer o envio do e-mail de forma automatizada.
-   pandas: para acessar a lista de emails em um arquivo Excel.

## ⚙️ Como Funciona

-   Antes de rodar a aplicação, o usuário pode alterar as informações de texto que estão encontradas entre paragráfos(<p></p>) na variável body que está presente dentro da função (def send_email()).
- Lembre-se também de colar o diretório onde a sua lista de email que deve conter "Nome" e "Email" como colunas na variável df "df = pd.read_excel(r'diretório completo para localizar o seu arquivo xlsx')", deixei um arquivo chamado "emailslist.xlsx" no repositório, esse arquivo pode ser preenchido com os nomes e emails e ser utilizado como a sua lista de email para essa aplicação.
-   Ao ser iniciada, a aplicação solicitará ao usuário o seu email, nome e a sua senha⚠️. 
-   Após o preenchimento dos dados o usuário deve esperar o sinal no prompt indicando que o email foi enviado (Email enviado).
-   Após alguns segundos o destinatário deverá receber o email definido pelo usuário.

## ⚠️ Recomendações

-   É provavel que seja necessário que você crie uma senha de app para que o google permita a utilização dessa aplicação.
-   Para solucionar a questão das senhas, na sua conta google ,você precisará clickar em Gerenciador sua Conta do Google > Segurança.
-   Em Segurança, você deve procurar a opção "Como fazer login no Google", clickar em "Senhas de App" e nessa opção seguir o passo a passo para gerar uma senha de app.
-   A sua senha de app deve ser utilizada no momento em que o aplicativo solicitar que você digite a sua senha, isso fará com que os possíveis erros de execução se encerrem.

## 💻 Como executar o código

- Instalar Python
- Para executar esse código, você precisa ter as seguintes bibliotecas instaladas: smtplib, email.message e pandas. Algumas dessas bibliotecas geralmente já vem previamente instaladas com o Python mas podem ser instaladas usando o gerenciador de pacotes Python pip com os seguinte comandos: (pip install) 
- Para executar o arquivo (python **autoMail.py**)
