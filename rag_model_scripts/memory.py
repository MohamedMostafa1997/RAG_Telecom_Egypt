from langchain_classic.memory import ConversationBufferMemory

def create_memory():
    return ConversationBufferMemory(
        k=5,
        memory_key="chat_history",
        return_messages=True,
        output_key="answer",
    )