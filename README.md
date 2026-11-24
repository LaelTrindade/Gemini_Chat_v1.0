# Gemini Chat v1.0

Chat desktop com IA feito em Python. A interface usa **CustomTkinter** e as respostas vêm de um agente do **Google Gemini**, criado com **SmolAgents** (via LiteLLM).

Projeto criado para praticar o que aprendi sobre Agentes de IA com Python.

> **Projeto de estudo, não afiliado ao Google.** Gemini é uma marca do Google.

---

## Funcionalidades

- Interface escura e moderna, com balões de mensagem (usuário à direita, IA à esquerda)
- O agente mantém o contexto da conversa enquanto o app estiver aberto
- Indicador de conexão (Online/Offline) atualizado automaticamente
- O título no topo mostra o modelo configurado em `agent_svc.py`
- Envio de mensagens com o botão ou com a tecla **Enter**

---

## Tecnologias

- Python
- CustomTkinter
- Pillow (PIL)
- SmolAgents + LiteLLM
- python-dotenv
- Google Gemini API

---

## Estrutura do projeto

```
Gemini_Chat_v1.0/
├── main.py
├── .env                     # sua chave de API (você cria; não vai pro GitHub)
├── .gitignore
└── src/
    ├── assets/
    │   └── images/          # ícones da interface
    ├── services/
    │   └── agent_svc.py     # agente de IA e configuração do modelo
    ├── utils/
    │   └── config.py        # caminhos do projeto
    └── views/
        └── main_screen_vws.py   # tela principal
```

---

## Como rodar o projeto

### 1. Pré-requisitos

- **Python 3.10 ou superior** (desenvolvido com Python 3.12)
- **Git**
- Uma **chave de API do Google Gemini** (o passo 4 explica como criar)

> **Linux:** o Tkinter pode não vir instalado junto com o Python. No Ubuntu/Debian, instale com:
> ```bash
> sudo apt install python3-tk
> ```

### 2. Baixe o projeto

```bash
git clone https://github.com/LaelTrindade/Gemini_Chat_v1.0.git
cd Gemini_Chat_v1.0
```

Se preferir, baixe o `.zip` pelo botão **Code > Download ZIP** aqui no GitHub e extraia a pasta.

### 3. Crie o ambiente virtual e instale as bibliotecas

```bash
python -m venv .venv
```

Ative o ambiente virtual:

```bash
# Windows
.venv\Scripts\activate

# Linux / macOS
source .venv/bin/activate
```

Instale as dependências:

```bash
pip install customtkinter pillow python-dotenv "smolagents[litellm]"
```

### 4. Crie sua chave de API no Google AI Studio

1. Acesse [aistudio.google.com/apikey](https://aistudio.google.com/apikey) e entre com sua conta Google.
2. Aceite os termos de uso, se for o primeiro acesso.
3. Clique em **Create API key** (Criar chave de API).
4. Escolha um projeto do Google Cloud existente ou crie um novo (o AI Studio faz isso automaticamente para quem está começando).
5. Copie a chave gerada.

> O Google oferece um nível gratuito para a API Gemini, mas os limites de uso mudam com o tempo. Confira os limites atuais no painel do AI Studio.

### 5. Configure a chave no projeto

Na **raiz do projeto** (a mesma pasta do `main.py`), crie um arquivo chamado `.env` com este conteúdo:

```
GEMINI_API_KEY=cole_sua_chave_aqui
```

Troque `cole_sua_chave_aqui` pela chave que você copiou, sem aspas e sem espaços extras.

> **Windows:** se criar o arquivo pelo Bloco de Notas, salve com o tipo **"Todos os arquivos"** para o nome não virar `.env.txt`.

### 6. Execute

```bash
python main.py
```

A janela do chat vai abrir. Digite sua mensagem e aperte **Enter**.

---

## Trocando o modelo

O modelo é definido em um único lugar, no arquivo `src/services/agent_svc.py`:

```python
MODEL_ID = "gemini/gemini-3.1-flash-lite"
```

Troque pelo modelo que quiser usar, mantendo o prefixo `gemini/`. O título exibido na janela é gerado a partir desse valor, então ele se atualiza sozinho. Os nomes dos modelos disponíveis ficam na [documentação do Gemini](https://ai.google.dev/gemini-api/docs/models).

---

## Problemas comuns

| Problema | O que fazer |
|---|---|
| `Chave de API não encontrada` ao abrir | Confira se o arquivo se chama exatamente `.env`, se está na raiz do projeto e se contém `GEMINI_API_KEY=...` |
| Mensagem de erro dentro do chat (chave inválida) | Verifique se copiou a chave inteira, sem espaços ou aspas |
| Erro de limite de uso (429) | Você atingiu o limite da sua cota. Aguarde um pouco ou confira os limites no AI Studio |
| Erro ao instalar ou abrir `tkinter` no Linux | Instale com `sudo apt install python3-tk` |
| Indicador **Offline** | O app não conseguiu acessar a internet; verifique sua conexão |
| Fonte diferente do esperado | A interface usa a fonte **Inter**. Se ela não estiver instalada, o sistema usa uma fonte padrão, então o visual pode variar um pouco entre Linux e Windows |

---

## Observações importantes

- **Nunca envie seu `.env` para o GitHub.** Ele já está no `.gitignore`, mas confira com `git status` antes de commitar. Se sua chave vazar, apague-a no AI Studio e gere outra.
- O agente é um `CodeAgent` do SmolAgents, que pode executar código Python gerado pelo modelo na sua máquina. Use o projeto como estudo e evite pedir tarefas que mexam em arquivos importantes.

---

## Autor

Desenvolvido por **Lael Trindade**.
[GitHub](https://github.com/LaelTrindade) · [LinkedIn](https://www.linkedin.com/in/laeltrindade-64887720b)
