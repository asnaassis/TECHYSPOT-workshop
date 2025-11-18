import gradio
from groq import Groq
client= Groq(
    api_key="*****AKIIR",
)
def initialize_messages():
    return [{"role": "system",
             "content": """You are a highly experienced medical doctor with
        strong expertise in diagnosing health conditions and providing
        clear, professional medical guidance. Your role is to assist
        people by offering accurate, compassionate, and practical health
        advice based on established medical knowledge."""}]



messages_prmt = initialize_messages()
print(type(messages_prmt))
def customLLMBot(user_input, history):
    global messages_prmt

    messages_prmt.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        messages=messages_prmt,
        model="llama-3.3-70b-versatile",
    )
    print(response)
    LLM_reply = response.choices[0].message.content
    messages_prmt.append({"role": "doctor", "content": LLM_reply})

    return LLM_reply
iface = gradio.ChatInterface(customLLMBot,
                     chatbot=gradio.Chatbot(height=300),
                     textbox=gradio.Textbox(placeholder="Ask me a question related to healthissue"),
                     title="Doctor ChatBot",
                     description="Chat bot for doctor",
                     theme="soft",
                     examples=["hi","Ask medical issues"]
                     )
iface.launch(share=True)