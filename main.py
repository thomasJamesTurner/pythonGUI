import flet as ft

class SearchBar(ft.Row):
    def __init__(self):
        super().__init__()
        self.search_input = ft.TextField(label="Search", autofocus=True)
        self.result_label = ft.Column()

        self.search_input.on_change = self.search
        
        # Add the search bar and result label to the Row (or the container of your choice)
        self.controls = [self.search_input, self.result_label]

    def search(self):
        search_query = self.search_input.value.strip().lower()
        
        # Update the result label based on the search query
        if search_query:
            self.result_label.controls = [ft.Text(f"Searching for: {search_query}")]
        else:
            self.result_label.controls = [ft.Text("Please enter a search query.")]
        
        # Update the page to reflect the changes
        self.page.update()

def main(page: ft.Page):
    # Add the custom Task widget to the page
    page.add(SearchBar())


ft.app(main)
