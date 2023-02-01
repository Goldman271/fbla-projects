from flet import *
from fl import views_Handler

def main(page: Page):
    
  page.add(
        AppBar(
            bgcolor="lightblue",
                

                title=Text("Forsyth County FBLA", color="White", weight="bold"),

        actions=[
        IconButton(
            icon=icons.SEARCH,
            icon_color=colors.BLACK
            
        )
        ]        
        )
        ),

        
    

app(target=main)





# if you want to open it on the browser, use this line of code: app(target=main, view=WEB_BROWSER)
