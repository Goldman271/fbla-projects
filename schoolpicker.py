from flet import *
from fl import views_Handler

def main(page: Page):
    def search(query):
        query = searchField.value

    searchField = TextField(hint_text="Enter school code or school name...", capitalization="words")
    submit = ElevatedButton(text="submit", on_click=search)
    page.add(
        searchField, submit
    )

app(target = main)