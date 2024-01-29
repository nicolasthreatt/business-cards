from kivy.app import App
from kivy.core.window import Window
from kivy.graphics import Ellipse, Color
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


class CircularImage(BoxLayout):
    def __init__(self, **kwargs):
        super(CircularImage, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.size_hint = (None, None)
        self.circle = None

        # Calculate size relative to screen dimensions
        self.image_size = min(Window.width, Window.height) * 0.3
        self.size = (self.image_size, self.image_size)

        # Position slightly lower than the top center
        self.pos_hint = {'center_x': 0.5, 'top': 0.85}

        # Bind update_position method to on_size event
        self.bind(size=self.update_position)
        self.bind(pos=self.update_position)
    
    def update_position(self, *args):
        """Recalculate the position of the circular image"""
        if self.circle is not None:
            circle_size = min(self.width, self.height)
            circle_pos = (0.5 * (Window.width - circle_size), Window.height - circle_size - 250)
            self.circle.pos = circle_pos

    def on_size(self, instance, value):
        """Draw the circular image on the canvas before"""
        if self.circle is None:
            with self.canvas.before:
                Color(0, 0, 0)  # Black circle color
                self.circle = Ellipse(size=self.size, pos=self.pos)
        self.update_position()



class BusinessCardApp(App):
    def build(self):
        # Set the window background color to white
        Window.clearcolor = (1, 1, 1, 1)

        # Create the main layout (BoxLayout)
        layout = BoxLayout(orientation='vertical', padding=10, spacing=5)
        layout.background_color = (1, 1, 1, 1)  # White background color

        # Add a circular image for the business card (profile picture) above the labels
        profile_image = CircularImage()
        layout.add_widget(profile_image)

        # Create a vertical BoxLayout for labels with reduced spacing
        labels_layout = BoxLayout(orientation='vertical')

        # Add labels for other business card information to labels_layout
        name_box = BoxLayout(height=50)
        name_label = Label(text="Your Name", font_size=36, color=(0, 0, 0, 1), bold=True) 
        name_box.add_widget(name_label)

        title_box = BoxLayout(size_hint_y=None, height=30)
        title_label = Label(text="Your Title", font_size=24, color=(0, 0, 0, 1))
        title_box.add_widget(title_label)

        labels_layout.add_widget(name_box)
        labels_layout.add_widget(title_box)

        #  Add labels layout to the main layout
        layout.add_widget(labels_layout)

        # Create a vertical BoxLayout for buttons with default spacing
        buttons_layout = BoxLayout(orientation='vertical')
    
        # Add buttons for contact information to buttons_layout
        phone_button = Button(text="Phone: 123-456-7890", on_press=self.on_phone_press, size_hint=(1, None), height=50)
        email_button = Button(text="Email: your.email@example.com", on_press=self.on_email_press, size_hint=(1, None), height=50)
        buttons_layout.add_widget(phone_button)
        buttons_layout.add_widget(email_button)

        # Add buttons layout to the main layout
        layout.add_widget(buttons_layout)

        return layout

    def on_phone_press(self, instance):
        # Action to perform when phone button is pressed
        print("Dialing phone number: 123-456-7890")

    def on_email_press(self, instance):
        # Action to perform when email button is pressed
        print("Opening email client for: your.email@example.com")


# Run the application
if __name__ == '__main__':
    Window.size = (390, 844)  # iPhone 12 resolution (1170x2532) scaled by 0.33 for better visualization
    BusinessCardApp().run()
