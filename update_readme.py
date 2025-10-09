import subprocess
from datetime import datetime

def run_tests():
    try:
        subprocess.check_call(["pytest", "-q"])
        return f"✅ Tests correctos {datetime.now()}"
    except subprocess.CalledProcessError:
        return f"❌ Tests fallidos {datetime.now()}"

def update_readme(status: str):
    with open("README.md", "r", encoding="utf-8") as f:
        lines = f.readlines()

    new_lines = []
    for line in lines:
        new_lines.append(line)
        if line.strip() == "## Estado de los tests":
            new_lines.append(status + "\n")
            break

    with open("README.md", "w", encoding="utf-8") as f:
        f.writelines(new_lines)

if __name__ == "__main__":
    status = run_tests()
    update_readme(status)