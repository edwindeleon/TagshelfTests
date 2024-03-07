import numpy as np
# Función para convertir de RGB a HSV
def rgb_to_hsv(rgb):
    r, g, b = rgb[..., 0], rgb[..., 1], rgb[..., 2]
    max_value = np.maximum.reduce(rgb, axis=-1)
    min_value = np.minimum.reduce(rgb, axis=-1)

    delta = max_value - min_value

    # Calcular el tono
    hue = np.zeros_like(max_value)
    nonzero_indices = delta != 0
    mask = r == max_value
    hue[mask & nonzero_indices] = (g - b)[mask & nonzero_indices] / delta[mask & nonzero_indices]

    mask = g == max_value
    hue[mask & nonzero_indices] = 2.0 + (b - r)[mask & nonzero_indices] / delta[mask & nonzero_indices]

    mask = b == max_value
    hue[mask & nonzero_indices] = 4.0 + (r - g)[mask & nonzero_indices] / delta[mask & nonzero_indices]

    hue = (hue * 60) % 360

    # Calcular la saturación
    saturation = np.where(max_value != 0, delta / max_value, 0)

    # Valor del cálculo
    value = max_value

    return np.stack([hue, saturation * 100, value * 100], axis=-1)

#Función para convertir de HSV a RGB
def hsv_to_rgb(hsv):
    h, s, v = hsv[..., 0], hsv[..., 1] / 100.0, hsv[..., 2] / 100.0

    c = v * s
    x = c * (1 - np.abs(((h / 60) % 2) - 1))
    m = v - c

    mask = (h < 60)
    rgb1 = np.stack([c, x, np.zeros_like(c)], axis=-1)

    mask2 = (h < 120) & (h >= 60)
    rgb2 = np.stack([x, c, np.zeros_like(c)], axis=-1)

    mask3 = (h < 180) & (h >= 120)
    rgb3 = np.stack([np.zeros_like(c), c, x], axis=-1)

    mask4 = (h < 240) & (h >= 180)
    rgb4 = np.stack([np.zeros_like(c), x, c], axis=-1)

    mask5 = (h < 300) & (h >= 240)
    rgb5 = np.stack([x, np.zeros_like(c), c], axis=-1)

    mask6 = (h < 360) & (h >= 300)
    rgb6 = np.stack([c, np.zeros_like(c), x], axis=-1)

    rgb = np.where(mask[..., None], rgb1, np.zeros_like(rgb1))
    rgb = np.where(mask2[..., None], rgb2, rgb)
    rgb = np.where(mask3[..., None], rgb3, rgb)
    rgb = np.where(mask4[..., None], rgb4, rgb)
    rgb = np.where(mask5[..., None], rgb5, rgb)
    rgb = np.where(mask6[..., None], rgb6, rgb)

    return (rgb + m) * 255

# Ejemplo de uso
rgb = np.array([[[255, 0, 0], [0, 255, 0], [0, 0, 255]]], dtype=np.uint8)
hsv = rgb_to_hsv(rgb)
print("RGB a HSV:")
print(hsv)

rgb_converted = hsv_to_rgb(hsv)
print("HSV a RGB:")
print(rgb_converted)
