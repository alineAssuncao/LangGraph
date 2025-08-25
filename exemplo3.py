from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from langgraph.graph import StateGraph
from pydantic import BaseModel
from langchain_core.runnables.graph import MermaidDrawMethod
from dotenv import load_dotenv
import os

# Carrega a API Key
load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY")

# Definição do modelo
llm_model = ChatOpenAI(model="gpt-3.5-turbo", api_key=API_KEY)

# Define o estado da graph
class GraphState(BaseModel):
    input:str
    output:str
    tipo: str = None

# Função de realizar calculo
def realizar_calculo(state: GraphState) -> GraphState:
    return GraphState(input=state.input,
                      output="Resposta de calculo ficticio: 42")

# Função para responder perguntas normais
def responder_curiosidades(state:GraphState) -> GraphState:
    response = llm_model.invoke([HumanMessage(content=state.input)])
    return GraphState(input=state.input,
                      output=response.content)

# Função para tratar perguntas não conhecidas
def responder_erro(state:GraphState) -> GraphState:
    return GraphState(input=state.input,
                      output="Desculpe, não entendi a pergunta.")

# Função de classificação dos nodes
def classificar(state: GraphState) -> GraphState:
    pergunta = state.input.lower()
    if any(palavra in pergunta for palavra in ["soma", "quanto é", "+", "calcular"]):
        tipo = "calculo"
    elif any(palavra in pergunta for palavra in ["quem", "onde", "quando", "por que", "qual"]):
        tipo = "curiosidade"
    else:
        tipo = "erro"
    return GraphState(input=state.input,
                      output="",
                      tipo=tipo)

# Criando o Graph e Adicionando os nodes
graph = StateGraph(GraphState)
graph.add_node("classificar", classificar)
graph.add_node("realizar_calculo", realizar_calculo)
graph.add_node("responder_curiosidades", responder_curiosidades)
graph.add_node("responder_erro", responder_erro)

# Adicionando condicionais
graph.add_conditional_edges(
    "classificar",
    lambda state: {
        "calculo": "realizar_calculo",
        "curiosidade": "responder_curiosidades",
        "erro": "responder_erro"
    }[state.tipo]
)

# Definindo entrada e saida e compilação
graph.set_entry_point("classificar")
graph.set_finish_point(["realizar_calculo", "responder_curiosidades", "responder_erro"])
export_graph = graph.compile()

# Testando o projeto
if __name__ == "__main__":
    exemplos = [
        "Quanto é 10 + 5?",
        "Quem inventou a lâmpada?",
        "Me diga um comando especial"
    ]
    for exemplo in exemplos:
        result = export_graph.invoke(GraphState(input=exemplo, output=""))
        print(f"pergunta: {exemplo}\nResposta: {result['output']}\n")

# Gerando a imagenm png do grafo
png_bytes = export_graph.get_graph().draw_mermaid_png(
    draw_method=MermaidDrawMethod.API
)
with open("grafo_exemplo3.png", "wb") as f:
    f.write(png_bytes)
