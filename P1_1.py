def can_king_move(x1, y1, x2, y2, checkerboard):

    if x1 == x2 and y1 == y2:
        return "No"
    
   
    dx = abs(x1 - x2)
    dy = abs(y1 - y2)
    
   
    if dx > 1 or dy > 1:
        return "No"
    
    
    if checkerboard[x2][y2] == 1:
        return "No"
    
   
    return "Yes"


x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())

print(can_king_move(x1, y1, x2, y2, checkerboard))
