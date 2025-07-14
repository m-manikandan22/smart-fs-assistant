import gradio as gr
from core.llm import get_llm_response
from core.command import parse_command, route_command

def chat_interface(user_input):
    try:
        llm_output = get_llm_response(user_input)
        print("🧠 RAW LLM:", repr(llm_output))  # Optional debug

        commands = parse_command(llm_output)
        results = []

        for i, cmd in enumerate(commands, start=1):
            action_name = cmd.get("action", "unknown")
            output = route_command(cmd)
            results.append(f"{i}. ✅ {action_name.replace('_', ' ').title()}: {output}")

        return f"🧠 Interpreted:\n{llm_output}\n\n✅ Result:\n" + "\n".join(results)

    except Exception as e:
        return f"❌ Error: {str(e)}"

# Create Gradio Interface
iface = gr.Interface(
    fn=chat_interface,
    inputs=gr.Textbox(lines=2, placeholder="Ask me something..."),
    outputs="text",
    title="🤖 Smart FS Assistant",
    description="Ask natural language commands to manage your local file system.",
    theme="default"
)

if __name__ == "__main__":
    iface.launch()
