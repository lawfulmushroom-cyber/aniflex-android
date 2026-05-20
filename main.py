from kivy.app import App 
from kivy.uix.boxlayout import BoxLayout 
from kivy.uix.button import Button 
from kivy.uix.label import Label 
class AniflexApp(App): 
    def build(self): 
        layout = BoxLayout(orientation='vertical') 
        label = Label(text='Aniflex', font_size=32) 
        button = Button(text='Play', size_hint=(1, 0.3)) 
        layout.add_widget(label) 
        layout.add_widget(button) 
        return layout 
if __name__ == '__main__': 
    AniflexApp().run() 
