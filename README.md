# Bitcoin Price Tracker

Esse programa foi desenvolvido para automatizar o envio de e-mail via G-Mail utilizando Python. 


## 🔧 Ferramentas Utilizadas

-   smtplib: para fazer realizar todos os tramits de segurança para que o seu e-mail possa ser enviado.
-   email.message: para recolher os dados de envior do e-mail e fazer o envio do e-mail de forma automatizada.


## ⚙️ Como Funciona

-   Antes de rodar a aplicação, o usuário pode alterar as informações de texto que estão encontradas entre paragráfos(<p></p>) na variável body que está presente dentro da função (def send_email()).
-   Ao ser iniciada, a aplicação solicitará ao usuário o seu email, nome, email do destinatário e nome do destinatário. 
-   Após o preenchimento dos dados o usuário deve esperar o sinal no prompt indicando que o email foi enviado (Email enviado).
-   Após alguns segundos o destinatário deverá receber o email definido pelo usuário.

## ⚠️ Recomendações

-   Recomendo que os usuários não deixem suas senhas de e-mail digitadas no código.
-   Para solucionar essa questão, eu recomendo que o usuário crie um arquivo de texto qualquer como por exemplo "senha automail" e defina esse arquivo com a extenção ".py".
-   Nesse arquivo, recomendo ao usuário que digite o seguinte código password1 = str('Digite aqui a sua senha').
-   Utilize acima dos imports do código do autoMail.py, a seguinte linha de comando "from senha automail import password1" para importar esse repositório de senhas na sua aplicação e modifique no codigo do autoMail.py a linha referente ao password 'password = "Digite a sua senha" por password = password1" 
-   Após isso, coloque o seu arquivo "senha automail" no mesmo diretório em que se encontra o autoMail.py.
-   Com isso, a sua aplicação se tornará mais segura.

## 💻 Como executar o código

- Instalar Python
- Para executar esse código, você precisa ter as seguintes bibliotecas instaladas: smtplib e email.message. Elas geralmente já vem previamente instaladas com o Python mas podem ser instaladas usando o gerenciador de pacotes Python pip com os seguinte comandos: (pip install) 
- Para executar o arquivo (python **autoMail.py**)
