import os
import subprocess


def build_docs():
    # Clean RST Files for pyquations
    clean_cmd = [
        "rm",
        "-rf",
        "_api/*",
    ]
    subprocess.run(clean_cmd, check=True)

    # Build RST Files for pyquations
    sphinx_apidoc_cmd = [
        "sphinx-apidoc",
        "-o",
        "_api",
        "../pyquations",
    ]
    subprocess.run(sphinx_apidoc_cmd, check=True)

    rename_rst_header()

    # Clean Previous Builds
    make_clean_cmd = ["make", "clean"]
    subprocess.run(make_clean_cmd, check=True, cwd=".")

    # Create HTML Documentation
    make_html_cmd = ["make", "html"]
    subprocess.run(make_html_cmd, check=True, cwd=".")


def rename_rst_header():
    # Rename the header of the index.rst file
    with open("_api/modules.rst", "r") as file:
        lines = file.readlines()

    # Modify the first line
    title = "API Reference"
    lines[0] = f"{title}\n"
    lines[1] = "=" * len(title) + "\n"

    with open("_api/modules.rst", "w") as file:
        file.writelines(lines)


if __name__ == "__main__":
    try:
        # Change working directory to the directory of this script
        script_dir = os.path.dirname(os.path.abspath(__file__))
        os.chdir(script_dir)

        build_docs()
        print("Documentation build completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
