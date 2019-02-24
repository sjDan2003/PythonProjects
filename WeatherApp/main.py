from kivy.app import App


# This is the App window we want to launch. Kivy will find a file
# that is named after this class minus App. So WeatherApp will find
# a file called weather.kv
class WeatherApp(App):

    def build(self):
        pass

if __name__ == "__main__":
    WeatherApp().run()
