from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langgraph.prebuilt import create_react_agent # reciocina e age
from langchain_core.tools import tool
from langchain_core.runnables.graph import MermaidDrawMethod
from dotenv import load_dotenv
import os

# Carrega a API Key
load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY")

# Definição do modelo
llm_model = ChatOpenAI(model="gpt-3.5-turbo", api_key=API_KEY)

# Define o prompt do sistema
system_message = SystemMessage(content="""
                            Você é um assistente.
                            Se o usuário pedir contas, use a ferramenta 'somar'.
                            Caso contrário, apenas responder normalmente.
                            """)

# Definido a tool de soma
@tool("somar")
def somar(valores: str) -> str:
    """Soma dois números separados por virgula"""
    try:
        a, b = map(float, valores.split(","))
        return str(a + b)
    except Exception as e:
        return f"Erro ao somar: {str(e)}"

# Criação do agente com LangGraph
tools = [somar]
graph = create_react_agent(
    model=llm_model, 
    tools=tools, 
    prompt=system_message
    )
export_graph = graph

# Extrair a resposta final
def extrair_resposta_final(result):
    ai_message = [m for m in result["messages"] if isinstance(m, AIMessage) and m.content]
    if ai_message:
        return ai_message[-1].content
    else:
        return "Nenhuma resposta final encontrada"
    
# Testando o agente
if __name__ == "__main__":
    # resposta da tool
    entrada1 = HumanMessage(content="Quanto é 8 + 5?")
    result1 = export_graph.invoke({"messages": [entrada1]})
    for m in result1["messages"]:
        print(m)
    resposta_texto_1 = extrair_resposta_final(result1)
    print("Resposta 1: ", resposta_texto_1)

    # respota sem a tool
    entrada2 = HumanMessage(content="Quem pintou a Monalisa?")
    result2 = export_graph.invoke({"messages": [entrada2]})
    for m in result2["messages"]:
        print(m)
    resposta_texto_2 = extrair_resposta_final(result2)
    print("Resposta 2: ", resposta_texto_2)


# Gerando a imagenm png do grafo
png_bytes = export_graph.get_graph().draw_mermaid_png(
    draw_method=MermaidDrawMethod.API
)
with open("grafo_exemplo2.png", "wb") as f:
    f.write(png_bytes)
