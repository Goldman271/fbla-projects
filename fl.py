from flet import *
from login import homeScreenB
from home import LoginB
def views_Handler(page):
    return {
     'login':View(
            route='login',
            controls=[
             homeScreenB(page)  
            ]
        ),
      'home':View(
            route='home',
            controls=[
                    LoginB(page)
                ]
        )  
    }

    
    

