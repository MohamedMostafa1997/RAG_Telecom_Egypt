from rag_model_scripts.chatbot import TelecomEgyptChatbot
from gradio_ui import create_interface

if __name__ == "__main__":
    chatbot = TelecomEgyptChatbot()
    chatbot.setup()

    demo = create_interface(chatbot)
    demo.launch(share=True)