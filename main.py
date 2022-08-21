from PIL import Image
import sys

# Receive the arguments for the wallpaper and panel size
wallpaper_width = int(sys.argv[1])
wallpaper_height = int(sys.argv[2])
panel_height = int(sys.argv[3])

if len(sys.argv) < 5:
    print("Usage: main.py width height panel-height <image>")
    sys.exit(1)

img = Image.open(sys.argv[4])

new_width = img.size[0] / (img.size[1] / wallpaper_height)
# new_height is strictly not needed here, could be inside the else statement, but I'm keeping it here for clarity
new_height = img.size[1] / (img.size[0] / wallpaper_width)


if new_width <= wallpaper_width:
    print("Scaling down to fit width")
    img.thumbnail((wallpaper_width, new_height))
    crop_height = (img.size[1] - wallpaper_height) / 2
    # Crop the image to the center of the image
    print("Cutting excess height")
    wallpaper_crop = img.crop((0, crop_height, wallpaper_width,
                               wallpaper_height + crop_height))
    wallpaper_crop.save("Wallpaper.png")  # Save the wallpaper
    # Crop the Panel background to the bottom of the image
    panel_crop = wallpaper_crop.crop(
        (0, wallpaper_height - panel_height, wallpaper_width, wallpaper_height))
    panel_crop.save("Panel.png")  # Save the panel background
else:
    print("Scaling down to fit height")
    img.thumbnail((new_width, wallpaper_height))
    crop_width = (new_width - wallpaper_width) / 2
    # Crop wallpaper to the center of the image
    print("Cutting excess width")
    wallpaper_crop = img.crop(
        (crop_width, 0, wallpaper_width + crop_width, wallpaper_height))
    wallpaper_crop.save("Wallpaper.png")  # Save the wallpaper
    # Crop the Panel background to the bottom of the image
    panel_crop = wallpaper_crop.crop(
        (0, wallpaper_height - panel_height, wallpaper_width, wallpaper_height))
    panel_crop.save("Panel.png")  # Save the panel background

print("Done, check the folder for Wallpaper.png and Panel.png")
