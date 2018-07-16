
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW, CENTER
from toga.color import RED, WHITE


class Pyrriors(toga.App):

    def handle_input(self, widget, **kwargs):
        input_text = self.text_input.value

        self.chat.data.append(
            icon=toga.Icon('resources/user.png'),
            title='You',
            subtitle=input_text,
        )

        self.text_input.value = ''

        self.chat.scroll_to_bottom()


    def setupGUI(self):
        self.playerMatBG = toga.Image(path='resources/playmat.png')
        self.playerBagImage = toga.Image(path='resources/user.png')
        self.playerMatContainer = toga.ImageView(self.playerMatBG, style=Pack(padding=0))
        self.playerBagContainer = toga.ImageView(self.playerBagImage, style=Pack(padding=0, width=25, height=50))

        self.boxBasicDies = toga.Box(style=Pack(flex=1, direction=ROW))
        self.boxPlayerMat = toga.Box(children=[self.playerBagContainer, self.playerMatContainer], style=Pack(flex=1, direction=ROW, background_color=RED))
        self.main_window.content = toga.Box(
            children=[self.boxPlayerMat],
            style=Pack(direction=COLUMN)
        )


    def startup(self):
        # Create a main window with a name matching the app
        self.main_window = toga.MainWindow(title=self.name)

        # Create a main content box
        # main_box = toga.Box()

        # Add the content on the main window
        # self.main_window.content = main_box
        self.setupGUI()
        # Show the main window
        self.main_window.show()


def main():
    return Pyrriors('Pyrriors', 'org.pyrriors.pyrriors')

