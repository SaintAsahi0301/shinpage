"""Welcome to Pynecone! This file outlines the steps to create a basic app."""
from pcconfig import config

import pynecone as pc

docs_url = "https://pynecone.io/docs/getting-started/introduction"
filename = f"{config.app_name}/{config.app_name}.py"


class State(pc.State):
    """The app state."""
    color: str = "blue"

    def change(self):
        self.color = "red"    
    pass


def index() -> pc.Component:
    return pc.center(
        pc.button(
            "버튼",
            # color_scheme="blue",
            color_scheme=State.color,
            border_radius="1em",
            on_click=State.change,    
        ),
    )


# Add state and page to the app.
app = pc.App(state=State)
app.add_page(index)
app.compile()
