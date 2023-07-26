# https://wooiljeong.github.io/etc/intro-gradio/
import gradio as gr


def greet(name, is_morning, temperature):
    message = "Good morning " if is_morning else "Good evening "
    greeting = f"{message} {name}. It is {temperature} degrees today"
    celsius = (temperature - 32) * 5 / 9
    return greeting, round(celsius, 2)


demo = gr.Interface(
    fn=greet,
    inputs=["text", "checkbox", gr.Slider(0, 100)],
    outputs=["text", "number"],
)
demo.launch()
