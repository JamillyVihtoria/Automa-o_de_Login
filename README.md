# 🖥️ Automação com Selenium - SauceDemo
Este foi meu primeiro código de automação utilizando Python + Selenium + PyAutoGUI. O script automatiza o login no site SauceDemo, adiciona produtos ao carrinho e valida se o processo ocorreu corretamente.

# 🚀 O que ele Faz?
- Abre o navegador Chrome e acessa o site SauceDemo.
- Preenche os campos de login com usuário e senha de teste.
- Realiza o login e espera a página inicial carregar.
- Clica em uma notificação na tela (simulado com PyAutoGUI).
- Adiciona dois produtos ao carrinho.
- Abre o carrinho e exibe mensagens no console confirmando a automação.

# 🛠️ Ferramentas Utilizadas
- Python
- Selenium WebDriver
- PyAutoGUI
- WebDriverWait para sincronização
- ChromeDriver

# ▶️ Como executar
- Clone o Repositório

- Instale as Dependências:
  pip install selenium pyautogui
  
- Baixe e configure o ChromeDriver compatível com a versão do seu navegador:
  https://developer.chrome.com/docs/chromedriver/downloads?hl=pt-br
  
- Execute o script
