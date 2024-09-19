# src/contrast_enhancer.py

import cv2

class ContrastEnhancer:
    def __init__(self, method_type = 'histogram_equalization'):
        self.method_type = method_type

    def enhance_contrast(self, image):
        # Code to enhance contrast
        if self.method_type == 'clahe':
            pass
        elif self.method_type == 'histogram_equalization':
            pass
        else:
            enhanced_image = image
        return enhanced_image