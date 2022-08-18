from PIL import Image
import sys

img = Image.open(sys.argv[1])

new_width = img.size[0] / (img.size[1] / 1080)
new_height = img.size[1] / (img.size[0] / 1920)


if new_width <= 1920:
    print("Scaling down to fit 1920px width")
    img.thumbnail((1920, new_height))
else:
    print("Scaling down to fit 1080px height")
    img.thumbnail((new_width, 1080))

# TODO: Add crop

img.show()
