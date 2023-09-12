from PIL import Image

# Load your 4 separate images
image_paths = ['box_scaled_Transfer 0.tiff', 'box_scaled_Transfer 1.tiff', 'box_scaled_Transfer 2.tiff', 'box_scaled_Transfer 3.tiff']
images = [Image.open(path) for path in image_paths]

# Get the dimensions of the individual images
image_width, image_height = images[0].size

# Calculate the dimensions of the composite image
composite_width = image_width * 2 # Assuming you want 3 images in a row
composite_height = image_height * 2 # Assuming you want 3 images in a column

# Create a new blank image for the composite
composite_image = Image.new('RGB', (composite_width, composite_height))

# Paste the individual images onto the composite image
for i in range(4):
    row = i // 2
    col = i % 2
    composite_image.paste(images[i], (col * image_width, row * image_height))

# Save the composite image
composite_image.save('scaled_composite.tiff', quality = 100)


# Load your 4 separate images for total Assay
image_paths = ['box_total_Transfer 0.tiff', 'box_total_Transfer 1.tiff', 'box_total_Transfer 2.tiff', 'box_total_Transfer 3.tiff']
images = [Image.open(path) for path in image_paths]

# Get the dimensions of the individual images
image_width, image_height = images[0].size

# Calculate the dimensions of the composite image
composite_width = image_width * 2 # Assuming you want 3 images in a row
composite_height = image_height * 2  # Assuming you want 3 images in a column

# Create a new blank image for the composite
composite_image = Image.new('RGB', (composite_width, composite_height))

# Paste the individual images onto the composite image
for i in range(4):
    row = i // 2
    col = i % 2
    composite_image.paste(images[i], (col * image_width, row * image_height))

# Save the composite image
composite_image.save('total_composite.tiff', quality = 100)
