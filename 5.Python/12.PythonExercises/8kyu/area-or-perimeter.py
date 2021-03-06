def area_or_perimeter(lt, w):
    return lt*w if lt == w else (lt+w)*2


print(area_or_perimeter(4, 4), 16)
print(area_or_perimeter(6, 10), 32)


'''
# Details
    You are given the length and width of a 4-sided polygon. The polygon can either be a rectangle
    or a square.
    If it is a square, return its area. If it is a rectangle, return its perimeter.
        area_or_perimeter(6, 10) - -> 32
        area_or_perimeter(4, 4) - -> 16
'''
