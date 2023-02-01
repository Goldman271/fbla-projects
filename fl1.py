from tkinter import Button
from flet import *
class homeScreenB(UserControl):
    def _init(self,page):
        super()._init()
        self.page = page
    def build(self):
        return Column(
            controls=[
                Container(
                    height=800,
                    width=800,
                    bgcolor = "yellow",
                    
                    content=Column(
                        controls=[
                        Text('Welcome back! Please sign in below:', size=35, color="black"),                      
                            Container(
                                Button(
                                    on_click= lambda _: self.page.go('home'),
                                content=Text('Login', size=15, color='black'
                                ),
                                alignment=alignment.center
                                )
                                
                            )
                        ]
                    )
                )
            ]
        )