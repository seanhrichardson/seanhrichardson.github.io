import subprocess
import sys
import os
import shutil
import time

def convert_md_to_pdf(md_file_path):
    # Ensure the input path is relative to the current working directory
    md_file_path = os.path.abspath(md_file_path)

    # Check if the input file has a .md extension
    if not md_file_path.endswith(".md"):
        print("Error: Input file must have a .md extension.")
        sys.exit(1)
    
    # Get the directory and base name of the input file
    base_dir = os.path.dirname(md_file_path)  # Directory of the .md file
    base_name = os.path.splitext(os.path.basename(md_file_path))[0]  # Name without extension
    
    # Define the output paths
    tex_folder = os.path.join(base_dir, "tex")
    tex_file_path = os.path.join(tex_folder, f"{base_name}.tex")
    pdf_file_path = os.path.join(tex_folder, f"{base_name}.pdf")
    final_pdf_file_path = os.path.join(base_dir, f"{base_name}.pdf")
    
    # Create the "tex" folder if it doesn't exist
    if not os.path.exists(tex_folder):
        os.makedirs(tex_folder)

    # The sed command to apply transformations and the pandoc command to convert the file
    bash_command = f"sed 's/\\\\\\\\/\\\\/g; s/\\\\_/_/g; s/\\\\\\*/\\*/g' {md_file_path} | pandoc -f markdown+tex_math_dollars+tex_math_single_backslash -t latex --standalone -V author=\"Sean Richardson\" -V geometry:margin=1in -o {tex_file_path}"

    try:
        # Execute the bash command to convert .md to .tex
        subprocess.run(bash_command, shell=True, check=True)
        print(f"Successfully converted {md_file_path} to {tex_file_path}")
        
        # Compile the .tex file into a .pdf twice (from the tex folder)
        subprocess.run(f"pdflatex -output-directory {tex_folder} {tex_file_path}", shell=True, check=True)
        subprocess.run(f"pdflatex -output-directory {tex_folder} {tex_file_path}", shell=True, check=True)
        print(f"Successfully compiled {tex_file_path} to {pdf_file_path}")
        
        # Wait for the .pdf file to exist, check every 0.5 seconds for up to 5 seconds
        for _ in range(10):
            if os.path.exists(pdf_file_path):
                break
            time.sleep(0.5)

        # If the .pdf file still doesn't exist, raise an error
        if not os.path.exists(pdf_file_path):
            print(f"Error: {pdf_file_path} was not created.")
            sys.exit(1)
        
        # Copy the resulting .pdf back to the original folder
        shutil.copy(pdf_file_path, final_pdf_file_path)
        print(f"Successfully copied {pdf_file_path} to {final_pdf_file_path}")
        
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Check if a file path was provided as an argument
    if len(sys.argv) != 2:
        print("Usage: python3 convert.py <path_to_md_file>")
        sys.exit(1)

    # Get the markdown file path from the command line argument
    md_file_path = sys.argv[1]

    # Convert the markdown file to PDF
    convert_md_to_pdf(md_file_path)
