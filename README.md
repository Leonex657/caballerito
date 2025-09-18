Esta aplicacion esta hecha el flet una app de decisiones en mi caso intente hacer uno tipo aventura dando distintos finales y opciones no tantas pero para pasar el rato estan bien y lograr entretener al usuario

Al tener distintos caminos enseñare la manera de que cada pregunta va junto a su final que llevara o igual a otra pregunta asi teniendo distintas maneras de poder digamos disfrutar esta aventura 

RESPUESTAS SI:

si actual == "inicio" → ir a pregunta2_si
si actual == "p2_si" → ir a pregunta3_si
si actual == "p4_si" → ir a pregunta5_si
si actual == "p3_si" → ir a pregunta5_si
si actual == "p5_si" → ir a pregunta6_si
si actual == "p6_si" → ir a pregunta7_si
si actual == "p7_si" → ir a pregunta8_si
si actual == "p8_si" → ir a pregunta9_si
si actual == "p9_si" → ir a pregunta10_si
si actual == "p10_si" → ir a final_bueno

RESPUESTAS NO:

si actual == "inicio" → ir a final_medio
si actual == "p2_si" → ir a pregunta4_si
si actual == "p4_si" → ir a pregunta5_si
si actual == "p5_si" → ir a pregunta6_si
si actual == "p6_si" → ir a final_aburrido
si actual == "p8_si" → ir a final_malo
si actual == "p9_si" → ir a pregunta10_si

BOTON REINICIO PARA TENER LA APP DESDE EL INICIO por si llegan a sacar el final o darle a una respuesta por error
Reiniciar (on_reset)

REQUISITOS: 
En la computadora de la escuela descargamos la version mas reciente en este caso la 3.13.7, junto a esta en la terminal de visual studio descargamoss flet y sus herramientas
Esto puede cambiar en cada computadora porque alguna te llegara a pedir descargalo desde windows shell todo los programas y herramientas a utilizar

<img width="1267" height="718" alt="image" src="https://github.com/user-attachments/assets/3e713559-681d-4588-907d-aaf5b033de75" />
<img width="1270" height="706" alt="image" src="https://github.com/user-attachments/assets/38c04a22-2592-49d7-aeb9-326bdd54bb94" />
<img width="1262" height="712" alt="image" src="https://github.com/user-attachments/assets/bb6d710c-ff6b-4ade-bb75-cab1b628b9c3" />
