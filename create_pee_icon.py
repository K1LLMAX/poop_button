from PIL import Image, ImageDraw

# Create a new image with a transparent background
width = 200
height = 200
image = Image.new('RGBA', (width, height), (0, 0, 0, 0))
draw = ImageDraw.Draw(image)

# Draw a more stylized droplet shape
droplet_points = [
    (100, 40),   # Top point
    (140, 90),   # Right curve top
    (150, 120),  # Right curve bottom
    (130, 150),  # Right bottom curve
    (100, 160),  # Bottom point
    (70, 150),   # Left bottom curve
    (50, 120),   # Left curve bottom
    (60, 90),    # Left curve top
]

# Draw the main droplet with yellow color
main_color = (255, 255, 0, 230)  # Slightly transparent yellow
draw.polygon(droplet_points, fill=main_color)

# Add a highlight for 3D effect
highlight_points = [
    (100, 55),   # Top
    (120, 90),   # Right
    (110, 120),  # Bottom
    (80, 90),    # Left
]
highlight_color = (255, 255, 180, 180)  # Semi-transparent lighter yellow
draw.polygon(highlight_points, fill=highlight_color)

# Add a slight shadow for depth
shadow_points = [
    (130, 110),  # Top
    (140, 130),  # Right
    (130, 140),  # Bottom
    (120, 130),  # Left
]
shadow_color = (218, 218, 0, 100)  # Semi-transparent darker yellow
draw.polygon(shadow_points, fill=shadow_color)

# Save with transparency
image.save('pee.png', 'PNG') 