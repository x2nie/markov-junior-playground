import math
import colorsys

# Function to convert hex to RGB
def hex_to_rgb(hex):
    hex = hex.lstrip('#')
    return tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))

# Function to convert RGB to HSL
def rgb_to_hsl(r, g, b):
    r /= 255.0
    g /= 255.0
    b /= 255.0
    return colorsys.rgb_to_hls(r, g, b)

# Function to calculate Euclidean distance between two RGB colors
def color_distance(color1, color2):
    r_diff = color1[0] - color2[0]
    g_diff = color1[1] - color2[1]
    b_diff = color1[2] - color2[2]
    return math.sqrt(r_diff ** 2 + g_diff ** 2 + b_diff ** 2)

# Main function to find the closest color
def find_closest_color(target_hex, palette):
    target_rgb = hex_to_rgb(target_hex)
    closest_color = None
    smallest_distance = float('inf')
    
    for color_hex in palette:
        color_rgb = hex_to_rgb(color_hex)
        distance = color_distance(target_rgb, color_rgb)
        
        if distance < smallest_distance:
            smallest_distance = distance
            closest_color = color_hex
    
    return closest_color

# Function to calculate Euclidean distance between two HSL colors
def hsl_distance(hsl1, hsl2):
    h_diff = min(abs(hsl1[0] - hsl2[0]), 1 - abs(hsl1[0] - hsl2[0]))  # Hue is circular
    s_diff = hsl1[2] - hsl2[2]  # Lightness in HSL
    l_diff = hsl1[1] - hsl2[1]  # Saturation in HSL
    return math.sqrt(h_diff ** 2 + s_diff ** 2 + l_diff ** 2)

# Main function to find the closest color using HSL
def find_closest_color_hsl(target_hex, palette):
    target_rgb = hex_to_rgb(target_hex)
    target_hsl = rgb_to_hsl(*target_rgb)
    closest_color = None
    smallest_distance = float('inf')
    
    for color_hex in palette:
        color_rgb = hex_to_rgb(color_hex)
        color_hsl = rgb_to_hsl(*color_rgb)
        distance = hsl_distance(target_hsl, color_hsl)
        
        if distance < smallest_distance:
            smallest_distance = distance
            closest_color = color_hex
    
    return closest_color


# Example usage
palette = [
    "000000", "1D2B53", "7E2553", "008751", "AB5236", "5F574F", "C2C3C7", "FFF1E8",
    "FF004D", "FFA300", "FFEC27", "00E436", "29ADFF", "83769C", "FF77A8", "FFCCAA",
    "291814", "111d35", "422136", "125359", "742f29", "49333b", "a28879", "f3ef7d",
    "be1250", "ff6c24", "a8e72e", "00b543", "065ab5", "754665", "ff6e59", "ff9d81",
    "00ffff", "5fcde4", "e4bb40", "8a6f30", "4b692f", "45107e", "847e87", "696a6a",
    "ff00ff", "9c09cc", "9badb7", "3f3f74", "37946e", "323c39", "8f974a", "524b24",
    "ff0000", "d95763", "ffffff", "cbdbfc"
]
target_color = "#c6a1a3"

# closest_color = find_closest_color(target_color, palette)
closest_color = find_closest_color_hsl(target_color, palette)
rgb = hex_to_rgb(closest_color)
print("Closest color of", target_color, 'is:', closest_color)
