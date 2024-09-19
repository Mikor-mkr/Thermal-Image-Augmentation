# src/main_controller.py

''''
This file will contain the MainController class
 responsible for orchestrating the workflow.
'''

from image_processor import ImageProcessor
from noise_reducer import NoiseReducer
from contrast_enhancer import ContrastEnhancer

class MainController:
    def __init__(self, filter_type = 'median', kernel_size=3, method_type='clahe'):
        self.image_processor = ImageProcessor()
        self.noise_reducer = NoiseReducer(filter_type = filter_type,
                                          kernel_size = kernel_size)
        self.contrast_enhancer = ContrastEnhancer(method_type = method_type)
    
    def process_image(self, input_path, output_path):
        # Load the image.
        image = self.image_processor.load_image(input_path)

        # Apply noise reduction.
        denoised_image = self.noise_reducer.apply_filter(image)
        
        # Enhance contrast.
        enhanced_image = self.contrast_enhancer.enhance_contrast(denoised_image)    

        # Save and display the result.
        self.image_processor.save_image(enhanced_image, output_path)
        self.image_processor.display_image(enhanced_image, title='Enhanced Image')
