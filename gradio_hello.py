# https://yunwoong.tistory.com/228
import gradio as gr


def greet(name):
    return "Hello " + name + "!"


demo = gr.Interface(fn=greet, inputs="text", outputs="text")

demo.launch()
