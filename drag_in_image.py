from kivy.app import App
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import Screen, ScreenManager


#Builder.load_file("kv/window.kv")
#class window(Window):
#    pass

class easter_egg(Widget):
    pass

class WindowFileDropExampleApp(App):
    def build(self):
        Builder.load_string('''
<easter_egg>:
    BoxLayout:
        size: self.size
        padding: 50
        spacing: 50
        canvas:
            Color:
                rgb: (0.3, 0.3, 0.3)
            Rectangle:
                size: root.size

        Button:
            text: "Return"
            font_size: "20sp"
            size_hint: None, None
            size: 150, 40
            # on_press: root.manager.current = 'command'                  
''')
        self.wid = easter_egg()
        file_path = Window.bind(on_dropfile=self._on_file_drop)
#        print(file_path)
        return self.wid
    
    def _on_file_drop(self, window, file_path):
        print(file_path)
        return file_path

if __name__ == '__main__':
    WindowFileDropExampleApp().run()
