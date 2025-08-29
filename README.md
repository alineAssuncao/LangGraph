# 🔗 LangGraph — Agentes Inteligentes com Fluxos Condicionais

## 💡 Visão Geral

Este projeto foi desenvolvido como parte dos estudos do curso [Desenvolvimento de Agentes de IA: Do Zero ao Avançado](https://www.udemy.com/course/desenvolvimento-de-agentes-de-ia-do-zero-ao-avancado), ministrado por Rodrigo Macedo e Paulo Andrade, PhD.

O objetivo é explorar o uso do **LangGraph**, uma extensão do LangChain que permite criar agentes com **fluxos personalizados**, **lógica condicional** e **controle de estados**. Com LangGraph, é possível construir agentes que tomam decisões com base em contexto, retornam a estados anteriores, e seguem caminhos dinâmicos — ideal para aplicações complexas e interativas.

---

## 🧠 Conceitos Aplicados

- **LangGraph**: Framework baseado em grafos de estados para controle de fluxo em agentes LLM.
- **LangChain**: Base para integração com LLMs, ferramentas e memória.
- **LLMs (Large Language Models)**: Modelos de linguagem como GPT usados para raciocínio e geração de respostas.
- **Stateful Agents**: Agentes que mantêm contexto e tomam decisões com base em histórico.
- **Conditional Routing**: Direcionamento de tarefas com base em condições definidas.

---

## 🛠️ Tecnologias Utilizadas

- `Python`  
- `LangGraph`  
- `LangChain`  
- `OpenAI API`  
- `dotenv` para variáveis de ambiente  
- `YAML` para configuração de fluxos e ferramentas

---

## 🚀 Primeiros Passos

### ✅ Pré-requisitos
- Python 3.10+
- pip
- Chave de API (OpenAI ou outro provedor LLM)

### 📦 Instalação e Ambiente Virtual

```bash
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Configure o arquivo `.env` com sua chave de API:
```env
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxx
```

▶️ Executando o Projeto
```bash
python main.py
```

Ou, se houver interface web:

```bash
streamlit run app.py
```

📁 Estrutura do Projeto
```
LangGraph/
├── main.py               # Execução principal
├── graph_config.yaml     # Configuração do fluxo de estados
├── agents/               # Definição dos agentes e funções
├── .env                  # Chave de API
├── requirements.txt      # Dependências
└── README.md             # Documentação
```

## 📚 Aprendizados
- Criação de agentes com lógica condicional e controle de estados
- Modelagem de fluxos dinâmicos com LangGraph
- Integração de ferramentas externas com LangChain
- Orquestração de decisões complexas com LLMs
- Aplicação de IA generativa em cenários reais

## 🔮 Próximos Passos
- Adicionar múltiplos agentes com papéis distintos
- Criar ciclos de decisão e retorno de estados
- Integrar com CrewAI para coordenação multiagente
- Desenvolver visualizações dos fluxos com ferramentas gráficas

## 👩‍💻 Autora

Aline Assunção

Engenheira de Qualidade em transição para Inteligência Artificial

📫 [LinkedIn](https://www.linkedin.com/in/alineassuncaoai/)  

📬 aline.jassuncao@gmail.com

>_"Agentes inteligentes não seguem apenas comandos — eles escolhem caminhos."_















