import streamlit as st

from aegpt_codex import aegpt_hash_commands

# ÆGPT Codex Dictionary
  # assumes this is in aegpt_codex.py

# Initialize Echo Archive
if "echo_archive" not in st.session_state:
    st.session_state.echo_archive = []

# Terminal UI
st.title("🌀 GlyphShell Terminal")
command = st.text_input("Enter your glyphic command:")

# Command Handler
def handle_command(cmd):
    cmd_lower = cmd.lower().strip()
    
    if cmd_lower == "reboot":
        return "🔁 Ceremonial Reboot initiated. Sigils realigning..."
    
    elif cmd_lower == "echo":
        return "🔊 Echoing past glyphs..."

    elif cmd_lower.startswith("sigil "):
        sigil_name = cmd[6:].strip()
        return f"🎨 Editing sigil: {sigil_name}"
    
    elif cmd_lower.startswith("search "):
        keyword = cmd_lower[7:].strip()
        results = []
        for category, glyphs in aegpt_hash_commands.items():
            for tag, data in glyphs.items():
                if keyword in tag.lower() or keyword in data["description"].lower():
                    results.append(f"{tag} {data.get('glyph', '')} – {data['description']}")
        return "\n".join(results) if results else "🫥 No glyphs matched your query."

    elif cmd_lower.startswith("#"):
        # Direct glyph lookup
        for category in aegpt_hash_commands.values():
            if cmd_lower in category:
                data = category[cmd_lower]
                return f"{cmd_lower} {data.get('glyph', '')} – {data['description']}"
        return f"❌ Glyph not found: {cmd_lower}"

    else:
        return f"🌀 Unknown glyph: '{cmd}'. Try `search bug` or `#puttibug`."

# Process Command
if command:
    result = handle_command(command)
    st.session_state.echo_archive.append((command, result))
    try:
        st.markdown(f"**Response:**\n```\n{result}\n```")
    except UnicodeEncodeError:
        st.warning("⚠️ Glyph response contains unrenderable characters. Displaying raw output.")
        st.text(result)
      
# Echo Archive Display
st.subheader("📜 Echo Archive")
for cmd, res in reversed(st.session_state.echo_archive[-10:]):
    st.markdown(f"`{cmd}` → {res}")
