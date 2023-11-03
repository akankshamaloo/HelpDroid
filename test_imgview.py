import kivy
import kivymd
from kivy.app import App
from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFlatButton
from kivymd.uix.imagelist import MDImageList
from kivymd.uix.popup import MDDialog
class GalleryApp(App):
    def build(self):
        layout = MDBoxLayout(orientation='vertical')

        # Create an image list
        image_list = MDImageList()

        # Add images to the image list
        for image in ['img1.jpg', 'img2.jpg', 'img3.jpg']:
            image_list.add_widget(MDFlatButton(text=image, on_release=self.show_image, args=[image]))

        # Add the image list to the layout
        layout.add_widget(image_list)

        return layout

    def show_image(self, image):
        # Create a popup to show the full image
        popup = MDDialog()

        # Add an image to the popup
        popup.add_widget(MDFlatButton(text='Close', on_release=popup.dismiss))

        # Set the image source
        popup.content_cls.image_source = image

        # Open the popup
        popup.open()
if __name__ == '__main__':
    GalleryApp().run()
