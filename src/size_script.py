import os
from PIL import Image

def resize_images(input_folder, output_folder, max_width, max_height):
    """
    Resize images to fit within max_width and max_height while maintaining aspect ratio.
    Args:
        input_folder (str): Path to the folder containing the images.
        output_folder (str): Path to the folder to save the resized images.
        max_width (int): Maximum width of the resized images.
        max_height (int): Maximum height of the resized images.
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for file_name in os.listdir(input_folder):
        file_path = os.path.join(input_folder, file_name)
        if not os.path.isfile(file_path):
            continue

        try:
            with Image.open(file_path) as img:
                # Check if file is a supported image format
                if img.format not in ["JPEG", "PNG"]:
                    print(f"Skipping unsupported file format: {file_name}")
                    continue

                # Calculate the new dimensions while maintaining aspect ratio
                img.thumbnail((max_width, max_height))

                # Save the resized image to the output folder
                output_path = os.path.join(output_folder, file_name)
                img.save(output_path)
                print(f"Resized and saved: {file_name}")
        except Exception as e:
            print(f"Error processing {file_name}: {e}")

# Configuration
input_folder = "/Users/palina/WebstormProjects/polina4k.github.io/src/art"
output_folder = "/Users/palina/WebstormProjects/polina4k.github.io/src/art1"
max_width = 800  # Desired maximum width
max_height = 800  # Desired maximum height

resize_images(input_folder, output_folder, max_width, max_height)

