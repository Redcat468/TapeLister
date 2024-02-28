import os
import tkinter as tk
from tkinter import filedialog

def scan_dir(path, indent=0):
    html = ""
    for item in sorted(os.listdir(path)):
        full_path = os.path.join(path, item)
        if os.path.isdir(full_path):
            html += "    " * indent + f"<li><span class='dir'><strong>{item}</strong></span><ul class='nested'>\n"
            html += scan_dir(full_path, indent + 1)
            html += "    " * indent + "</ul></li>\n"
        else:
            html += "    " * indent + f"<li class='file'>{item}</li>\n"
    return html

def ask_for_directory():
    root = tk.Tk()
    root.withdraw()
    folder_selected = filedialog.askdirectory()
    return folder_selected

start_path = ask_for_directory()

if start_path:
    root_name = os.path.basename(start_path)
    html_content = f"""
    <!DOCTYPE html>
    <html lang="fr">
    <head>
    <meta charset="UTF-8">
    <title>{root_name}</title>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #f0f0f0;
            color: #333;
            margin: 0;
            padding: 20px;
        }}
        h1 {{
            color: #0066cc;
        }}
        .dir {{
            cursor: pointer;
            padding: 5px 0;
            font-weight: bold; /* Met en gras le texte des dossiers */
        }}
        .dir::before, .dir.expanded::before {{
            font-size: 14px;
            margin-right: 5px;
            cursor: pointer;
        }}
        .dir::before {{
            content: "▶";
            color: #cc6600;
        }}
        .dir.expanded::before {{
            content: "▼";
            color: #cc6600;
        }}
        ul, li {{
            list-style-type: none;
        }}
        ul {{
            padding-left: 20px;
        }}
        .nested {{
            display: none;
        }}
        .active {{
            display: block;
        }}
        .file {{
            color: #555;
            margin-left: 20px;
        }}
    </style>
    </head>
    <body>

    <h1>{root_name}</h1>

    <ul id="myUL">
    {scan_dir(start_path)}
    </ul>

    <script>
        var toggler = document.getElementsByClassName("dir");
        for (var i = 0; i < toggler.length; i++) {{
            toggler[i].addEventListener("click", function() {{
                this.parentElement.querySelector(".nested").classList.toggle("active");
                this.classList.toggle("expanded");
            }});
        }}
    </script>

    </body>
    </html>
    """

    output_filename = f"{root_name}.html"
    with open(output_filename, "w", encoding='utf-8') as f:
        f.write(html_content)
    print(f"L'arborescence a été générée avec succès dans '{output_filename}'.")
else:
    print("Aucun dossier n'a été sélectionné.")
