from PIL import Image, ImageDraw, ImageFont

# Path to the handwriting font file
font_path = 'QEScottwilliams.ttf'  # Replace with your font file path

# Text to convert
text_to_convert = """
If okavela akkada meeku APAAR ID kanapadaka pothe ... View all ani untadhi kadha .. adi click chesi , APAAR ID ani search cheste... ABC ID Delhi dhi osthadhi, adi click chesi , mee details fill chesi , get document ani click cheyandi
"""

# Create an image with white background
image = Image.new('RGB', (800, 1000), 'white')
draw = ImageDraw.Draw(image)

# Load the font
font_size = 24
font = ImageFont.truetype(font_path, font_size)

# Draw the text onto the image
draw.text((20, 20), text_to_convert, fill='black', font=font)

# Save the image
image.save('handwritten_text.png')

print("Text-to-handwriting conversion completed! Image saved as 'handwritten_text.png'.")
