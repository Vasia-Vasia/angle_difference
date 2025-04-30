def diff(angle_1, angle_2):
    min_angle = min(angle_1, angle_2) % 360
    max_angle = max(angle_1, angle_2) % 360
    x = max_angle - min_angle
    y = 360 - x
    result = min(x, y)
    return abs(result)

# Проверка

angle_1 = 30
angle_2 = 240

print(diff(angle_1, angle_2))