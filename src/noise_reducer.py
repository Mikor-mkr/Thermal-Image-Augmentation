# src/NoiseReducer.py

import cv2

class NoiseReducer:
    def __init__(self, filter_type='median', kernel_size=3):
        self.filter_type = filter_type
        self.kernel_size = kernel_size

    def apply_filter(self, image):
        if self.filter_type == 'median':
            denoised_image = cv2.medianBlur(image, self.kernel_size)
        elif self.filter_type == 'gaussian':
            denoised_image = cv2.GaussianBlur(image, (self.kernel_size, self.kernel_size), 0)
        else:
            denoised_image = image  # No filtering
        return denoised_image