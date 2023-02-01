from flet import *
from fl import views_Handler

def main(page: Page):
    

    def routeChange(route):
        print(page.route)
        page.views.clear()
        page.views.append(
            views_Handler(page)[page.route]
        )


    page.on_route_change = routeChange
    page.go('home')

app(target=main)





# if you want to open it on the browser, use this line of code: app(target=main, view=WEB_BROWSER)