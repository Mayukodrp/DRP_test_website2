import os

files = [
    "index.html",
    "index_de.html",
    "index_fr.html",
    "index_it.html",
    "index_ja.html",
    "index_zh.html"
]

emojis_to_remove = [
    "🌍",
    "🚢",
    "💰",
    "💼",
    "📊",
    "🇨🇦",
    "🇬🇧",
    "🇯🇵"
]

base_path = "/Users/mayukookada/Desktop/DRPwebsite"

for file_name in files:
    file_path = os.path.join(base_path, file_name)
    if os.path.exists(file_path):
        print(f"Processing {file_name}...")
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        new_content = content
        for emoji in emojis_to_remove:
            new_content = new_content.replace(emoji, "")
            
        # Also remove the empty div class="feature-icon" if it's empty now?
        # The plan said "Remove the emoji character".
        # If I remove the emoji, the div will be <div class="feature-icon"></div>.
        # The CSS has margin-bottom: 1rem; and font-size: 3rem;
        # An empty div might still take up space or look weird.
        # Let's remove the whole div if it's empty or contains only whitespace.
        # But simply replacing the emoji is what was agreed. 
        # Let's stick to replacing the emoji first. 
        # If the user wants to remove the space, I can do that later.
        # Actually, the user said "remove emojis". 
        # Let's just remove the characters for now.
        
        if new_content != content:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"Updated {file_name}")
        else:
            print(f"No changes in {file_name}")
    else:
        print(f"File not found: {file_path}")
