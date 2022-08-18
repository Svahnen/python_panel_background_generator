from PIL import Image
import sys

final_width = 1920  # Change here to the desired width
final_height = 1080  # Change here to the desired height


# Dont touch anything below this line
img = Image.open(sys.argv[1])

new_width = img.size[0] / (img.size[1] / final_height)
# new_height is strictly not needed here, could be inside the else statement, but I'm keeping it here for clarity
new_height = img.size[1] / (img.size[0] / final_width)


if new_width <= final_width:
    print("Scaling down to fit width")
    img.thumbnail((final_width, new_height))
    crop_height = (img.size[1] - final_height) / 2
    img_crop = img.crop((0, crop_height, final_width,
                        final_height + crop_height))
else:
    print("Scaling down to fit height")
    img.thumbnail((new_width, final_height))
    crop_width = (new_width - final_width) / 2
    img_crop = img.crop(
        (crop_width, 0, final_width + crop_width, final_height))

img_crop.show()
