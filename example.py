import time
import flet as ft

def main(page: ft.Page):
    # add/update controls on Page
    t = ft.Text()
    page.add(t)
    for i in range(10):
        t.value = f"Step {i}"
        page.update()
        time.sleep(5)
       
    


   
    
    #t = ft.Text(value= "Hello, world!", color="lightblue")
    #page.controls.append(t)
    #age.update()
    

ft.app(target=main)
