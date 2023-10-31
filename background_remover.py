import os
from datetime import datetime
from rembg import remove


class BackgroundRemover:
    def __init__(self, input_folder, output_folder):
        self.input_folder = input_folder
        self.output_folder = output_folder

    def process_images(self):
        today = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
        process_folder = os.path.join(self.output_folder, today)
        os.makedirs(process_folder, exist_ok=True)

        for filename in os.listdir(self.input_folder):
            if filename.endswith(('.png', '.jpg', '.jpeg')):
                input_path = os.path.join(self.input_folder, filename)
                output_path = os.path.join(process_folder, filename)
                self.remove_background(input_path, output_path)
                self.move_originals(input_path, process_folder)

    def remove_background(self, input_path, output_path):
        with open(input_path, 'rb') as inp, open(output_path, 'wb') as out:
            background_output = remove(inp.read())
            out.write(background_output)

    def move_originals(self, input_path, output_path):
        original_folder = os.path.join(output_path, 'originals')
        os.makedirs(original_folder, exist_ok=True)
        file_name = os.path.basename(input_path)
        new_path = os.path.join(original_folder, file_name)
        os.rename(input_path, new_path)


if __name__ == '__main__':
    input_folder = 'input'
    output_folder = 'output'
    remover = BackgroundRemover(input_folder, output_folder)
    remover.process_images()
