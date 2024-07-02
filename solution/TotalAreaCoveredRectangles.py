def calculate(rectangles):
    if not rectangles:
        return 0
    xlines = []
    for x0, y0, x1, y1 in set(rectangles):
        xlines.append((x0, True, y0, y1))
        xlines.append((x1, False, y0, y1))
        # делаем два треуголника
    area, prev_x = 0, 0
    segments = {}
    sorted_xlines = sorted(xlines)
    for x, is_open, y0, y1 in sorted_xlines:
        if x > prev_x:
            height, y = 0, 0
            for l, h in sorted(segments):
                height += max(0, (h - max(l, y)))
                y = max(y, h)
            area += (x - prev_x) * height
            prev_x = x
        segments.setdefault((y0, y1), 0)
        if is_open:
            segments[(y0, y1)] += 1
        else:
            segments[(y0, y1)] -= 1
        if not segments[(y0, y1)]:
            del segments[(y0, y1)]
    return area


rectangles = [(3, 3, 8, 5), (6, 3, 8, 9), (11, 6, 14, 12)]
print(calculate(rectangles))  # Вывод: 36
