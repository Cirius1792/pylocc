import json
import os
SUPPORTED_CONFIGS= ["extensions", "line_comment", "multi_line"]

def generate_language_docs():
    script_dir = os.path.dirname(__file__)
    language_json_path = os.path.join(script_dir, 'src', 'pylocc', 'language.json')
    output_md_path = os.path.join(script_dir, 'docs', 'docs', 'supported-languages.md')

    try:
        with open(language_json_path, 'r', encoding='utf-8') as f:
            languages_data = json.load(f)
    except FileNotFoundError:
        print(f"Error: {language_json_path} not found.")
        return
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from {language_json_path}.")
        return

    markdown_content = "---\n"
    markdown_content += "sidebar_position: 2\n"
    markdown_content += "title: Supported Languages\n"
    markdown_content += "---\n\n"
    markdown_content += "# Supported Languages\n\n"
    markdown_content += "This page lists all the programming languages supported by `pylocc` and their respective configurations.\n\n"

    for lang_name, config in sorted(languages_data.items()):
        markdown_content += f"## {lang_name}\n\n"
        supported = {i[0]:i[1] for i in  filter( lambda item: item[0] in SUPPORTED_CONFIGS, config.items()) }
        
        markdown_content += "```json\n"
        markdown_content += json.dumps({lang_name: supported}, indent=2)
        markdown_content += "\n```\n\n"

    try:
        os.makedirs(os.path.dirname(output_md_path), exist_ok=True)
        with open(output_md_path, 'w', encoding='utf-8') as f:
            f.write(markdown_content)
        print(f"Successfully generated {output_md_path}")
    except IOError as e:
        print(f"Error writing to {output_md_path}: {e}")

if __name__ == "__main__":
    generate_language_docs()
