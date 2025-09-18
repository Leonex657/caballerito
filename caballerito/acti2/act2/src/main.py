import flet as ft

def main(page: ft.Page):
    page.title = "La gran aventura"
    page.window_width = 420
    page.window_height = 720
    
    estado = {"actual": "inicio"}
    
    titulo = ft.Text("El caballerito🐲", size=22, weight="bold")
    texto = ft.Text("", size=18)
    imagen = ft.Image(src="", width=280, height=180, fit=ft.ImageFit.CONTAIN, visible=False)

    btn_si = ft.ElevatedButton("Si")
    btn_no = ft.ElevatedButton("No")
    btn_reset = ft.ElevatedButton("Reiniciar", icon=ft.Icons.REFRESH)
    botones = ft.Row([btn_si, btn_no], alignment=ft.MainAxisAlignment.CENTER, spacing=20)
    
    def mostrar_inicio():
        estado["actual"] = "inicio"
        page.bgcolor = None
        texto.value = "¿Quieres empezar una gran aventura de accion?⚔️🛡️"
        imagen.src = "bosque.png"
        imagen.visible = True 
        btn_si.visible = True
        btn_no.visible = True

        
        page.update()
        
    def a_pregunta2_si():
        estado["actual"] = "p2_si"
        texto.value = "!BIEN¡😁, Empezamos, Quieres una espada⚔️?"
        imagen.src = "espada.png"
        imagen.visible = True
        page.update()

    def a_pregunta3_si():
        estado["actual"] = "p3_si"
        texto.value = "Buena eleccion, Sigues explorando"
        imagen.src = "explorar.png"
        imagen.visible = True
        page.update()
    
    def a_pregunta4_si():
        estado["actual"] = "p4_si"
        texto.value = "Entonces iras a puño limpio"
        imagen.src = "puño.png"
        imagen.visible = True
        page.update()
        
    def a_pregunta5_si():
        estado["actual"] = "p5_si"
        texto.value = "Salio  un ogro de los arbustos lo atacas?"
        imagen.src = "arbusto.png"
        imagen.visible = True
        page.update()
        
    def a_pregunta6_si():
        estado["actual"] = "p6_si"
        texto.value = "Sigues llendo por el bosque ves algo volando vas a ver?"
        imagen.src = "dragon.png"
        imagen.visible = True
        page.update()
        
    def a_pregunta7_si():
        estado["actual"] = "p7_si"
        texto.value = "Es la bestia del bosque la enfrentas?"
        imagen.src = "dragon2.png"
        imagen.visible = True
        page.update()
        
    def a_pregunta8_si():
        estado["actual"] = "p8_si"
        texto.value = "Te pones enfrenta de la bestia y le pegas"
        imagen.src = "Tirado.png"
        imagen.visible = True
        page.update()
        
    def a_pregunta9_si():
        estado["actual"] = "p9_si"
        texto.value = "Esquivas a la bestia dandole el golpe final y matandola"
        imagen.src = "esquivo.png"
        imagen.visible = True
        btn_no.visible = False
        page.update()
        
    def a_pregunta10_si():
        estado["actual"] = "p10_si"
        texto.value = "Te llevas un diente de la bestia como trofeo"
        imagen.src = "diente.png"
        imagen.visible = True
        btn_no.visible = False
        page.update()
        
    def final_bueno():
        estado["actual"] = "final_bueno"
        texto.value = "Bien has matado al rey del bosque"
        page.bgcolor = ft.Colors.GREEN
        imagen.src = "trofeo.png"
        btn_si.visible = False
        btn_no.visible = False
        page.update()
        
    def final_medio():
        estado["actual"] = "final_medio"
        texto.value = "💤🥱Eres un aburrido quedate a dormir."
        page.bgcolor = ft.Colors.ORANGE
        imagen.src = "cama.png"
        btn_si.visible = False
        btn_no.visible = False
        page.update()
    
    def final_malo():
        estado["actual"] = "final_malo"
        texto.value = "No diste el ultimo golpe moriste"
        page.bgcolor = ft.Colors.RED
        imagen.src = "gameover.png1"
        btn_si.visible = False
        btn_no.visible = False
        page.update()
        

    def final_aburrido():
        estado["actual"] = "final aburrido"
        texto.value = "No seguiste explorando y te fuiste a tu casa"
        page.bgcolor = ft.Colors.GREY
        imagen.src = "aburrido.png"
        btn_si.visible = False
        btn_no.visible = False
        page.update()

    def on_si(e):
        if estado["actual"] == "inicio":
            a_pregunta2_si()
        elif estado["actual"] == "p2_si":
            a_pregunta3_si()
        elif estado["actual"] == "p4_si":
            a_pregunta5_si()
        elif estado["actual"] == "p3_si":
            a_pregunta5_si()
        elif estado["actual"] == "p5_si":
            a_pregunta6_si()
        elif estado["actual"] == "p6_si":
            a_pregunta7_si()
        elif estado["actual"] == "p7_si":
            a_pregunta8_si()
        elif estado["actual"] == "p8_si":
            a_pregunta9_si()
        elif estado["actual"] == "p9_si":
            a_pregunta10_si()
        elif estado ["actual"] == "p10_si":
            final_bueno()

    def on_no(e):
        if estado["actual"] == "inicio":
            final_medio()
        elif estado ["actual"] == "p2_si":
            a_pregunta4_si()
        elif estado ["actual"] == "p4_si":
            a_pregunta5_si()
        elif estado["actual"] == "p5_si":
            a_pregunta6_si()
        elif estado["actual"] == "p7_si":
            final_aburrido()
        elif estado["actual"] == "p3_si":
            final_aburrido()
        elif estado["actual"] == "p6_si":
            final_aburrido()
        elif estado ["actual"] == "p8_si":
            final_malo()
        elif estado["actual"] == "p9_si":
            a_pregunta10_si()

    def on_reset(e):
        mostrar_inicio()


    btn_si.on_click = on_si
    btn_no.on_click = on_no
    btn_reset.on_click = on_reset
    
    page.add(ft.Column([titulo, texto, imagen, botones, btn_reset], alignment=ft.MainAxisAlignment.START, horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=16, expand=True))
    mostrar_inicio()
    
ft.app(target=main)