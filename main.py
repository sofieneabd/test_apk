import flet as ft

def sof(p: ft.Page):
   p.title= "Sofiene abdelhedi"
   p.bgcolor= ft.Colors.BLUE_200
   p.window.width, p.window.height= 399, 700
   p.window.top, p.window.left= 10, 960
   p.vertical_alignment= ft.MainAxisAlignment.START
   p.horizontal_alignment=ft.CrossAxisAlignment.CENTER
   lbl= ft.Text("First App تطبيقي الأول", color="Black", size=20)
   def fermer(e):
        page.window.destroy()  # Ferme la fenêtre
   
   info='''
   name= sofiene
   age=43
   '''
   lb2= ft.Text(info)

   p.add(lbl,
         lb2,
         ft.ElevatedButton("Close Me", on_click= fermer, icon=ft.Icons.CLOSE),
         ft.TextField(label="write here", icon=ft.Icons.INFO)
         )
   p.update()
ft.run(sof)
