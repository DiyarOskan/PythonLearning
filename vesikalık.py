#coding=utf8
from PIL import Image

def resize_image(input_path, output_path, new_width, new_height):
    # Open the image file
    with Image.open(input_path) as img:
        # Resize the image
        resized_img = img.resize((new_width, new_height))
        # Save the resized image
        resized_img.save(output_path)

# Example usage
input_path = "C:\Users\ASUS\Desktop\diyar\benn.jpg"  # Provide the path to your input image
output_path = "diyar.jpg"  # Provide the path for the output image
new_width = 600  # Set the new width in pixels
new_height = 600  # Set the new height in pixels

resize_image(input_path, output_path, new_width, new_height)





