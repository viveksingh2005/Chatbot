import os
import openai
import gradio as gr

openai.api_key = "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"

start_sequence = "\nAI:"
restart_sequence = "\nHuman:"

prompt="The following is a conversation with an AI assistant.\n\nVivek: Hello, who are you?\nAI: I am an AI created by OpenAI by VIVEK SINGH. Ask me your questions\n ",
    

def openai_create(prompt):
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=0.9,
    max_tokens=150,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.6,
    stop=[" Human:", " AI:"]
    )
    return response.choices[0].text

def conversation_history(input,history):
    history = history or[]
    s = list(sum(history,()))
    s.append(input)
    inp = ''.join(s)
    output = openai_create(inp)
    history.append((input, output))
    return history, history 

blocks = gr.Blocks()

with blocks:
    chatbot = gr.Chatbot()
    message = gr.Textbox(placeholder=prompt)
    state = gr.State()
    submit = gr.Button("Click")
    submit.click(conversation_history,inputs=[message,state], outputs=[chatbot,state])

blocks.launch(share=True)    

   


