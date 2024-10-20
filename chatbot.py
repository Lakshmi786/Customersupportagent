from langgraph.graph import StateGraph, MessagesState
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import ToolNode
from tools import query_knowledge_base, search_for_product_reccommendations
import os

prompt = """#Purpose
You are a customer service chatbot for a flower shop company. You can help customer achieve the goals listed below

#Goals

1. Answer questions the user might have relating to the serives offered
2. Recommend products to the based on their preferences

#Tone
Helpful and friendly. Use flower related puns or gen-z emojis to keep things lighthearted

"""

chat_template = ChatPromptTemplate.from_messages(
    [
        ('system',prompt),
        ('placeholder',"{messages}")
    ]
)

with open('./.env','r', encoding = 'utf-8') as f:
    for line in f:
        key , value = line.strip().split('=')
        os.environ[key] = value



llm = ChatOpenAI( model = 'gpt-4o',openai_api_key = os.environ['OPENAI_API_KEY'])

def call_agent(message_state :MessagesState):
    print(message_state)
    example_message = 'hello'
    return { 'messages' : [example_message,example_message]}


graph = StateGraph(MessagesState)

graph.add_node('agent',call_agent)

graph.add_edge('agent','__end__')

graph.set_entry_point('agent')

app = graph.compile()

updated_messages = app.invoke({
    'messages' : ['Hello']
})