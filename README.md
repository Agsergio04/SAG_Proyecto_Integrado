# Proyecto Intermodular Integrado 
En este repositorio se albergara todo el codigo referido al primer proyecto relacionado con las siguientes asignaturas:    
- Desarrollo web Entorno Cliente
- Desarrollo web Entorno Servidor
- Despliegue de Aplicaciones Web 

En este caso voy a utilizar de ejemplo el primer apartado de esta actividad
 

## Testing    
En este apartado lo que encontraremos es el resultado de los test realizados por la CI:    

### Estado de los tests    

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
     - "Returs" : descibre que argumentos devuelve la funcion
     - "Raises" : descibre que tipo de error se dispara en caso de que la ejecucion de la funcion sea fallida 
 * Codigo completo documentado:
https://github.com/Agsergio04/SAG_Proyecto_Integrado/blob/8bb3f1930c2d07f0c023c647c7aadb57215c23e6/update_readme.py#L1-L51

c).- **Multiformato. ¿Qué segundo formato** (además de HTML) **generaste? Explica la configuración o comandos del workflow y herramientas que lo producen.**  

d).- **Colaboración. Explica cómo GitHub facilita mantener la documentación** (actualizaciones del README.md y de /docs) **cuando colaboran varias personas** (PRs, reviews, checks de CI, protección de ramas).  

e).- **Control de versiones. Muestra mensajes de commit que evidencien el nuevo workflow. ¿Son claros y descriptivos? Justifícalo. Además de un conjunto de mensajes de tus commits.**  

f).- **Accesibilidad y seguridad. ¿Qué medidas/configuración del repositorio garantizan que solo personal autorizado accede al código y la documentación?** (p. ej., repositorio privado, equipos, roles, claves/secretos, branch protection).  

g).- **Instalación/uso documentados. Indica dónde en el README.md explicas el funcionamiento del workflow y dónde detallas las herramientas y comandos de documentación.**  

h).- **Integración continua. Justifica por qué el workflow utilizado es CI. ¿Qué evento dispara automáticamente la generación/actualización de la documentación** (p. ej., push, pull_request, workflow_dispatch)?  
