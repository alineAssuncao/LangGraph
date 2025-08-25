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

# Definição do StateGraph
class GraphState(BaseModel):
    input: str
    output: str

# Função de resposta
def responder(state):
    input_message = state.input
    response = llm_model.invoke([HumanMessage(content=input_message)])
    return GraphState(
                        input=state.input,
                        output=response.content
                    )

# Criando o Graph
graph = StateGraph(GraphState)
graph.add_node("responder", responder)
graph.set_entry_point("responder")
graph.set_finish_point("responder")

# Compilando o grafo
export_graph = graph.compile()

# Gerando a imagenm png do grafo
png_bytes = export_graph.get_graph().draw_mermaid_png(
    draw_method=MermaidDrawMethod.API
)
with open("grafo_exemplo1.png", "wb") as f:
    f.write(png_bytes)

