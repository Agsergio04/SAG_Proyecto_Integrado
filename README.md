# Proyecto Intermodular Integrado 
En este repositorio se albergara todo el codigo referido al primer proyecto relacionado con las siguientes asignaturas:    
- Desarrollo web Entorno Cliente
- Desarrollo web Entorno Servidor
- Despliegue de Aplicaciones Web 

En este caso voy a utilizar de ejemplo el primer apartado de esta actividad    

# Funcionamiento del workflow   
Teniendo el siguiente workflow :   
https://github.com/Agsergio04/SAG_Proyecto_Integrado/blob/4c928cfd755b4d5e0cb1c3c799c3fa81fd0d2af7/.github/workflows/ci.yaml#L1-L70    
Tenemos que el flujo del workflow es el siguiente:   
## Flujo del workflow "Integracion Continua con AutoCommit"

El flujo del workflow "Integracion Continua con AutoCommit" realiza una serie de pasos automáticos cada vez que se hace un push a la rama `main` o se ejecuta manualmente. Aquí tienes el flujo explicado paso a paso:

### Inicio del workflow
- Se activa automáticamente con cada push a la rama `main` o mediante ejecución manual (`workflow_dispatch`).
https://github.com/Agsergio04/SAG_Proyecto_Integrado/blob/4c928cfd755b4d5e0cb1c3c799c3fa81fd0d2af7/.github/workflows/ci.yaml#L3-L7
### Permisos
- El workflow tiene permisos de escritura para poder realizar commits en el repositorio.
https://github.com/Agsergio04/SAG_Proyecto_Integrado/blob/4c928cfd755b4d5e0cb1c3c799c3fa81fd0d2af7/.github/workflows/ci.yaml#L8-L9
### Preparación del entorno
- Se realiza el checkout del repositorio para obtener el código más reciente.
- Se configura Python en la versión 3.13.
https://github.com/Agsergio04/SAG_Proyecto_Integrado/blob/4c928cfd755b4d5e0cb1c3c799c3fa81fd0d2af7/.github/workflows/ci.yaml#L11-L22
### Instalación de dependencias
- Se instalan las herramientas necesarias: `pytest` para ejecutar pruebas y `pdoc` para generar documentación.
https://github.com/Agsergio04/SAG_Proyecto_Integrado/blob/4c928cfd755b4d5e0cb1c3c799c3fa81fd0d2af7/.github/workflows/ci.yaml#L25-L26
### Ejecución de pruebas y actualización del README
- Se ejecuta el script `update_readme.py`, que corre los tests y actualiza el archivo README.md con el estado de las pruebas.
https://github.com/Agsergio04/SAG_Proyecto_Integrado/blob/4c928cfd755b4d5e0cb1c3c799c3fa81fd0d2af7/.github/workflows/ci.yaml#L29-L30
### Commit automático del README
- Se realiza un commit automático del archivo README.md actualizado.
https://github.com/Agsergio04/SAG_Proyecto_Integrado/blob/4c928cfd755b4d5e0cb1c3c799c3fa81fd0d2af7/.github/workflows/ci.yaml#L32-L36
### Generación de documentación HTML
- Se crea la carpeta `documentacion` si no existe.
- Se genera la documentación en formato HTML usando pdoc y se guarda en la carpeta `documentacion`.
https://github.com/Agsergio04/SAG_Proyecto_Integrado/blob/4c928cfd755b4d5e0cb1c3c799c3fa81fd0d2af7/.github/workflows/ci.yaml#L39-L43
### Commit automático de la documentación HTML
- Se añade la documentación generada al índice git y se realiza un commit automático.
https://github.com/Agsergio04/SAG_Proyecto_Integrado/blob/4c928cfd755b4d5e0cb1c3c799c3fa81fd0d2af7/.github/workflows/ci.yaml#L45-L52
### Conversión de HTML a Markdown
- Se instala la herramienta pandoc.
- Se convierte el archivo HTML generado por pdoc a Markdown limpio usando pandoc y sed para limpiar etiquetas innecesarias.
https://github.com/Agsergio04/SAG_Proyecto_Integrado/blob/4c928cfd755b4d5e0cb1c3c799c3fa81fd0d2af7/.github/workflows/ci.yaml#L55-L61
- Primero se convierte la documentación HTML a Markdown con pandoc y luego se limpia el Markdown resultante eliminando etiquetas innecesarias con sed.
### Commit automático de la documentación Markdown
- Se añade el archivo Markdown generado al índice git y se realiza un commit automático.
https://github.com/Agsergio04/SAG_Proyecto_Integrado/blob/4c928cfd755b4d5e0cb1c3c799c3fa81fd0d2af7/.github/workflows/ci.yaml#L63-L70

### Evidencia de configuracion ssh    
* Aqui incluyo una imagen donde se verifica el estado de mi clave ssh:
 <img width="1200" height="70" alt="Captura de pantalla 2025-10-16 010907" src="https://github.com/user-attachments/assets/59f94470-59ae-4117-97d1-f71edc7ce3aa" />
 

# Testing    
En este apartado lo que encontraremos es el resultado de los test realizados por la CI:    

### Estado de los tests    

✅ Tests correctos 2025-10-15 23:15:27

✅ Tests correctos 2025-10-15 23:11:32

✅ Tests correctos 2025-10-15 22:20:43

✅ Tests correctos 2025-10-15 22:18:41

✅ Tests correctos 2025-10-15 21:57:04

✅ Tests correctos 2025-10-15 21:29:09

✅ Tests correctos 2025-10-15 21:00:04

✅ Tests correctos 2025-10-15 20:50:25

✅ Tests correctos 2025-10-15 19:48:31

✅ Tests correctos 2025-10-15 17:59:18

✅ Tests correctos 2025-10-15 17:50:59

✅ Tests correctos 2025-10-13 13:47:26

✅ Tests correctos 2025-10-13 13:40:34

✅ Tests correctos 2025-10-13 13:07:52

✅ Tests correctos 2025-10-13 13:04:22

✅ Tests correctos 2025-10-13 13:01:22

✅ Tests correctos 2025-10-13 12:56:18

✅ Tests correctos 2025-10-13 12:54:15

✅ Tests correctos 2025-10-13 12:42:41

✅ Tests correctos 2025-10-13 12:33:32

✅ Tests correctos 2025-10-13 12:27:45

✅ Tests correctos 2025-10-09 09:48:11    



# Preguntas sobre el Workflow y Documentación

## Herramientas utilizadas

a).- **Identificación de herramientas de generación de documentación. ¿Qué herramienta o generador** (p. ej., Sphinx, pdoc, Javadoc, Doxygen, Dokka) **utilizaste en el workflow para crear la documentación en /documentacion?**  
 * Para la generacion de documentacion en formato `HTML` he utilizado la herramienta Pdoc.
 * Para la generacion de documentacion en formato `Markdown` he utilizado la herramienta llamada Pandoc.
   
b).- **Documentación de componentes. Muestra un fragmento del código con comentarios/docstrings estructurados** (p. ej., :param, :return: o etiquetas equivalentes) **que haya sido procesado por la herramienta. Comenta qué estilo de documentación has utilizado:** (p. ej., reStructuredText, Google Style, KDoc)  
 * Funcion test del script update_readme.py documentada :
https://github.com/Agsergio04/SAG_Proyecto_Integrado/blob/8bb3f1930c2d07f0c023c647c7aadb57215c23e6/update_readme.py#L8-L24
 * A la hora de usar el estilo de documentacion en un estilo Google Style utilizando las siguientes etiquetas : 
     - "Returs" : descibre que argumentos devuelve la funcion.
     - "Raises" : descibre que tipo de error se dispara en caso de que la ejecucion de la funcion sea fallida.
 * Codigo completo documentado:
https://github.com/Agsergio04/SAG_Proyecto_Integrado/blob/8bb3f1930c2d07f0c023c647c7aadb57215c23e6/update_readme.py#L1-L51

c).- **Multiformato. ¿Qué segundo formato** (además de HTML) **generaste? Explica la configuración o comandos del workflow y herramientas que lo producen.**    
 * La documentacion realizada en `html` generada es la [siguiente](https://github.com/Agsergio04/SAG_Proyecto_Integrado/blob/main/documentacion/update_readme.html)
 * La documentacion  realizada en `Markdown` generada es la [siguiente](https://github.com/Agsergio04/SAG_Proyecto_Integrado/blob/main/documentacion/documentacion.md)

d).- **Colaboración. Explica cómo GitHub facilita mantener la documentación** (actualizaciones del README.md y de /docs) **cuando colaboran varias personas** (PRs, reviews, checks de CI, protección de ramas).  

* GitHub facilita la colaboración mediante Pull Requests (PRs) que permiten revisión de código y documentación antes de integrarlos en la rama principal. Los checks de integración continua (CI) se ejecutan automáticamente para validar que los cambios no rompen la documentación ni el código. Las protecciones de rama evitan que se realicen commits directos sin revisión, manteniendo la calidad y coherencia en la documentación de `/documentacion` y en el README.md.

e).- **Control de versiones. Muestra mensajes de commit que evidencien el nuevo workflow. ¿Son claros y descriptivos? Justifícalo. Además de un conjunto de mensajes de tus commits.**  
 * Sabiendo que los [commits](https://github.com/Agsergio04/SAG_Proyecto_Integrado/commits?author=Agsergio04) son realmente descriptivos con las frases siendo en su mayoria concisas,sin la necesidad de sobreargumentarlas o que exista la necesidad de añadirle una descripcion.

f).- **Accesibilidad y seguridad. ¿Qué medidas/configuración del repositorio garantizan que solo personal autorizado accede al código y la documentación?** (p. ej., repositorio privado, equipos, roles, claves/secretos, branch protection).  
 * En este proyecto no he aplicado una seguridad como tal a la hora de privatizar el acceso al codigo y a la documentacion pero podria aplicar para implementarle algo de seguridad como por ejemplo tener el repositorio en privado y a la hora de las invitaciones a dicho repo asignar diferentes roles como :
 * "Read" : solo es capaz de ver el codigo y la documentacion pero sin la capacidad de hacer cambios.
 * "Triage " :  gestionar issues y pull requests, pero no modificar el código.
 * "Write " : puede hacer cambios en el codigo y la documentacion.
 * "Maintain " : puede gestionar el repositorio pero no puede remover ni modificar elementos sustanciales.
 * "Admin" : total control en la integridad del repositorio siendo capaz incluso de poder borrar el repositorio.
 

g).- **Instalación/uso documentados. Indica dónde en el README.md explicas el funcionamiento del workflow y dónde detallas las herramientas y comandos de documentación.**  
 * En el readme se encuentra al inicio del documento en el apartado "Explicacion del workflow".

h).- **Integración continua. Justifica por qué el workflow utilizado es CI. ¿Qué evento dispara automáticamente la generación/actualización de la documentación** (p. ej., push, pull_request, workflow_dispatch)?    
 * El workflow utilizado se implementa cada vez que se le hace un `push ` a la rama main del repositorio. Siendo asignado esto en esta parte del documento `yaml`:
   https://github.com/Agsergio04/SAG_Proyecto_Integrado/blob/4c928cfd755b4d5e0cb1c3c799c3fa81fd0d2af7/.github/workflows/ci.yaml#L3-L5
