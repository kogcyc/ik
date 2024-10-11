import os
import shutil
import markdown

def copy_content_to_output(root_dir):
    content_dir = os.path.join(root_dir, 'content')
    output_dir = os.path.join(root_dir, 'output')
    
    # Step 3: Copy all content from content to output
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)  # Clear output directory if it exists
    shutil.copytree(content_dir, output_dir)
    
    return output_dir

def convert_markdown_to_html_in_output(output_dir):
    # Step 4: Move to output directory and convert .md to .html
    for subdir, _, files in os.walk(output_dir):
        for file in files:
            if file.endswith('.md'):
                md_file_path = os.path.join(subdir, file)
                html_file_path = os.path.splitext(md_file_path)[0] + '.html'
                
                # Convert Markdown to HTML
                with open(md_file_path, 'r', encoding='utf-8') as md_file:
                    md_content = md_file.read()
                    html_content = markdown.markdown(md_content)
                
                # Write the HTML content to a new .html file
                with open(html_file_path, 'w', encoding='utf-8') as html_file:
                    html_file.write(html_content)
                
                # Optionally, delete the original .md file
                os.remove(md_file_path)

def static_site_generator():
    # Step 1: Start at the root directory
    root_dir = os.getcwd()  # Get the current working directory
    
    # Step 2: Go to root/content dir
    output_dir = copy_content_to_output(root_dir)
    
    # Step 4: Convert .md files in the output directory to .html
    convert_markdown_to_html_in_output(output_dir)

if __name__ == "__main__":
    static_site_generator()
