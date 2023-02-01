from flet import *

class LoginB(UserControl):
    def init(self,page):
        super().init()
        self.page = page
    
    def build(self):
        return Column(
            controls=[
                Container(
                        height=800,
                        width=800,
                        bgcolor = "lightblue",
                        content=Column(
                            controls=[
                                Text('Welcome home!', size=35, color="black"),
                                Container(
                                    on_click= lambda _: self.page.go('login'),
                                    content= Text('Sign Out', size=15, color="black"),
                                    alignment=alignment.center
                                )
                            ]
                        )
                    )
            ]
        )