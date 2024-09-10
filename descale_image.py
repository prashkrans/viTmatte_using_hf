import cv2

def descale_image(input_image):
    # Get the original image dimensions
    height, width = input_image.shape[:2]
    descaled_image = input_image

    # Here, min performs better than max, since the current model works well with 512 pixels - only for inpainting
    # Since we have to upscale the inpainted low res image, 1024 is a better choice
    # Using min as 1024/1024 = 1 as inpainted image once descaled can be used again without descaling
    # multiple revisions could be done without descaling - [Verified]
    critical_pixel = 1536 # Ideal value = 1024, 1536 and even 2048 (slow) works without CUDA 00M [Tested]
    # >=2560, 3072, 4096 gives CUDA OOM Error
    # Since, 2048 works fine, upscaling is only required by a scale factor of ~3x i.e. 1/0.34 (not 4x)
    descale_factor = min(critical_pixel/height, critical_pixel/width)  # Verified 1024 x 1024 works perfectly fine

    print(f'descale_factor = {descale_factor}')

    # Calculate the new dimensions while maintaining the aspect ratio
    # Descale only when descale factor is less than 1
    if descale_factor < 1:
        width = int(width * descale_factor)
        height = int(height * descale_factor)
        # Resize the image using OpenCV
        descaled_image = cv2.resize(input_image, (width, height), interpolation=cv2.INTER_AREA)

    return descaled_image
