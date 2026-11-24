import os
from dotenv import load_dotenv
from smolagents import CodeAgent, LiteLLMModel

load_dotenv()
api_key = os.getenv('GEMINI_API_KEY')

if not api_key:
    raise ValueError('Chave de API não encontrada.')

MODEL_ID = "gemini/gemini-3.1-flash-lite"
MODEL_NAME = MODEL_ID.split('/')[-1].replace('-', ' ').title()

agente = CodeAgent(
    tools = [],
    model = LiteLLMModel(
    model_id = MODEL_ID,
        api_key = api_key,
    )
)


def chamar_agente(mensagem: str):

    resultado = agente.run(mensagem, reset = False)
    return resultado