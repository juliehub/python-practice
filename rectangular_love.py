def find_love_intersection(r1,r2):
    """
    To find the rectangular intersection of two given love rectangles.
    
    Args:
    r1: love rectangle of the 1st person
    r2: love rectangle of the 2nd person
    
        Example:
        my_rectangle = {

        # Coordinates of bottom-left corner
        'left_x'   : 1,
        'bottom_y' : 1,
    
        # Width and height
        'width'    : 6,
        'height'   : 3,

        }
    
    Returns:
    love_r: the rectangular intersection of two given love rectangles
    
    
    To test this function:
    
    my_rectangle = {'left_x': 1, 'bottom_y': 1, 'width': 6, 'height': 3}
    your_rectangle = {'left_x': 5, 'bottom_y': 2, 'width': 3, 'height': 6}

    print("my_rectangle", my_rectangle)
    print("your_rectangle", your_rectangle)
    print("love_intersection_rectangle",find_love_intersection(my_rectangle,your_rectangle))
    
    The function will return:
    my_rectangle {'left_x': 1, 'bottom_y': 1, 'width': 6, 'height': 3}
    your_rectangle {'left_x': 5, 'bottom_y': 2, 'width': 3, 'height': 6}
    love_intersection_rectangle {'left_x': 5, 'bottom_y': 2, 'width': 2, 'height': 2}
    
    Example 2:
    my_rectangle = {'left_x': 1, 'bottom_y': 1, 'width': 6, 'height': 3}
    your_rectangle = {'left_x': 1000, 'bottom_y': 1000, 'width': 3, 'height': 6}
    
    The function will return
    my_rectangle {'left_x': 1, 'bottom_y': 1, 'width': 6, 'height': 3}
    your_rectangle {'left_x': 1000, 'bottom_y': 1000, 'width': 3, 'height': 6}
    love_intersection_rectangle {'left_x': 0, 'bottom_y': 0, 'width': 0, 'height': 0}

    """
    
    love_r={'left_x':0,'bottom_y':0,'width':0,'height':0}
    
    if (r2['left_x'] > r1['left_x']) and (r2['left_x'] < (r1['left_x']+r1['width'])):
        love_r['left_x'] = r2['left_x']
    else:
        if (r1['left_x'] > r2['left_x']) and (r1['left_x'] < (r2['left_x']+r2['width'])):
             love_r['left_x'] = r1['left_x']
       
    if (r2['bottom_y'] > r1['bottom_y']) and (r2['bottom_y'] < (r1['bottom_y']+r1['height'])):
        love_r['bottom_y'] = r2['bottom_y']
    else:
        if (r1['bottom_y'] > r2['bottom_y']) and (r1['bottom_y'] < (r2['bottom_y']+r2['height'])):
            love_r['bottom_y'] = r1['bottom_y']
    
    if ((r1['left_x']+r1['width']) > r2['left_x']) and ((r1['left_x']+r1['width']) < (r2['left_x']+r2['width'])):
        love_r['width'] = (r1['left_x']+r1['width']) - r2['left_x']
    else:
        if ((r2['left_x']+r2['width']) > r1['left_x']) and ((r2['left_x']+r2['width']) < (r1['left_x']+r1['width'])):
            love_r['width'] = (r2['left_x']+r2['width']) - r1['left_x']
    
    if ((r1['bottom_y']+r1['height']) > r2['bottom_y']) and ((r1['bottom_y']+r1['height']) < (r2['bottom_y']+r2['height'])):
        love_r['height'] = (r1['bottom_y']+r1['height'])-r2['bottom_y']
    else:
        if ((r2['bottom_y']+r2['height']) > r1['bottom_y']) and ((r2['bottom_y']+r2['height']) < (r1['bottom_y']+r1['height'])):
            love_r['height'] = (r2['bottom_y']+r2['height'])-r1['bottom_y']
    
    return love_r



my_rectangle = {'left_x': 1, 'bottom_y': 1, 'width': 6, 'height': 3}
your_rectangle = {'left_x': 5, 'bottom_y': 2, 'width': 3, 'height': 6}

print("my_rectangle", my_rectangle)
print("your_rectangle", your_rectangle)
print("love_intersection_rectangle",find_love_intersection(my_rectangle,your_rectangle))
