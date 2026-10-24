# This is a simple general-purpose chatbot built on top of the Anthropic API.
# Before running this, make sure you have exported your Anthropic API key as an environment variable:
# export ANTHROPIC_API_KEY="your-anthropic-api-key"

import anthropic
import gradio as gr

client = anthropic.Anthropic()

def predict(message, history):
    messages = [{"role": m["role"], "content": m["content"]} for m in history]
    messages.append({"role": "user", "content": message})
    partial = ""
    with client.messages.stream(messages=messages, model="claude-sonnet-5-5", max_tokens=1000) as stream:
        for text in stream.text_stream:
            partial += text
            yield partial

demo = gr.ChatInterface(predict, api_name="chat")

if __name__ == "__main__":
    demo.launch()
