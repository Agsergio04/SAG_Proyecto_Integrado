import subprocess
from datetime import datetime


def run_tests():
    """Ejecuta las pruebas de la carpeta actual usando pytest.

    Returns:
        str: Mensaje de estado de las pruebas con un prefijo seguido
             por la fecha y hora actual en formato "YYYY-MM-DD HH:MM:SS".

    Raises:
        subprocess.CalledProcessError: Si pytest retorna un código distinto de cero.
    """
    try:
        # El metodo strftime sirve para pasar un objeto tipo datetime, date o time a cadena de texto
        subprocess.check_call(["pytest", "-q"])
        
        return f"✅ Tests correctos {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    
    except subprocess.CalledProcessError:

        return f"❌ Tests fallidos {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"


def update_readme(status: str):
    """Actualiza el archivo README.md con el estado de las pruebas.

    Args:
        status (str): Mensaje generado por `run_tests()` indicando
                      el estado de las pruebas.

    Returns:
        None
    """
    with open("README.md", "r", encoding="utf-8") as f:
        lines = f.readlines()

    new_lines = []
    for line in lines:
        new_lines.append(line)
        if line.strip() == "### Estado de los tests":
            new_lines.append("\n" + status + "\n")

    with open("README.md", "w", encoding="utf-8") as f:
        f.writelines(new_lines)


if __name__ == "__main__":
    status = run_tests()
    update_readme(status)
