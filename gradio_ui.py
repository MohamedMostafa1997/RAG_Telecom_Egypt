import gradio as gr

def create_interface(chatbot):

    css = """
    .gradio-container { background-color: #FFFFFF; }
    .chatbot .message.bot { background-color: #F0F4FF; border-right: 4px solid #003399; }
    .chatbot .message.user { background-color: #003399; color: white; }
    footer { display: none; }
    """

    def chat_fn(message, history, uploaded_file):
        return chatbot.chat(message, history, uploaded_file)

    def reset_memory():
        chatbot.reset_memory()

    with gr.Blocks(
        title="Telecom Egypt Intelligent Assistant",
        theme=gr.themes.Soft(primary_hue=gr.themes.colors.purple),
        css=css
    ) as demo:

        gr.Markdown("""
        <div style='background-color:#003399; padding:20px; border-radius:8px; margin-bottom:10px'>
            <h1 style='color:white; margin:0'>Telecom Egypt — WE Assistant</h1>
            <p style='color:#FFD700; margin:5px 0 0'>مساعدك الذكي WE</p>
        </div>
        """)

        clear_btn = gr.Button("Clear Chat")
        clear_btn.click(fn=reset_memory, outputs=[])

        gr.ChatInterface(
            fn=chat_fn,
            additional_inputs=[
                gr.File(
                    label="Upload Document (PDF, DOCX, TXT, Image)",
                    file_types=[".pdf", ".docx", ".txt", ".html", ".png", ".jpg", ".jpeg"],
                )
            ],
            examples=[
                ["ما هي خطط الإنترنت المتاحة في المنزل؟"],
                ["What are the prepaid mobile plans?"],
                ["في عروض على النت دلوقتي؟"],
                ["عايز أعرف أسعار خطط WE Gold"],
                ["How do I pay my bill online?"],
            ],
        )

    return demo