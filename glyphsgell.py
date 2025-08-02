import streamlit as st

# Initialize Echo Archive
if "echo_archive" not in st.session_state:
    st.session_state.echo_archive = []

# Terminal UI
st.title("🌀 GlyphShell Terminal")
command = st.text_input("Enter your glyphic command:")

# Command Handler
def handle_command(cmd):
    # Placeholder logic
    if cmd.lower() == "reboot":
        return "🔁 Ceremonial Reboot initiated. Sigils realigning..."
    elif cmd.lower() == "echo":
        return "🔊 Echoing past glyphs..."
    elif cmd.lower().startswith("sigil "):
        sigil_name = cmd[6:]
        return f"🎨 Editing sigil: {sigil_name}"
    else:
        return f"🌀 Unknown glyph: '{cmd}'. Try again or consult the Echo Archive."

# Process Command
if command:
    result = handle_command(command)
    st.session_state.echo_archive.append((command, result))
    st.markdown(f"**Command:** `{command}`")
    st.markdown(f"**Response:** {result}")

# Echo Archive Display
st.subheader("📜 Echo Archive")
for cmd, res in reversed(st.session_state.echo_archive[-10:]):
    st.markdown(f"`{cmd}` → {res}")
