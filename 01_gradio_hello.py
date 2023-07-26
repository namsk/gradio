# https://yunwoong.tistory.com/228
import gradio as gr


def greet(name):
    return "Hello " + name + "!"


# demo = gr.Interface(fn=greet, inputs="text", outputs="text")

# Customize the interface
demo = gr.Interface(fn=greet,
                    inputs=gr.inputs.Textbox(
                        lines=2, placeholder="Name Here..."),
                    outputs="text")

demo.launch()
