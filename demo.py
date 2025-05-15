from common import main_loop, Object, CANVAS_SIZE, FPS

G = 9.8

objects = [Object("Object", CANVAS_SIZE[0] // 2, 15, 15, "blue", 0)]

def calculate_data_func():
    global objects
    done = False
    for obj in objects:
        obj.speed += G / FPS[0]
        if obj.center_y + obj.speed > CANVAS_SIZE[1] - obj.radius:
            obj.center_y = CANVAS_SIZE[1] - obj.radius
            obj.speed = 0
            done = True
        else:
            obj.center_y = obj.center_y + obj.speed
    description = f"x:{objects[0].center_x:.2f}, y:{CANVAS_SIZE[1] - objects[0].center_y:.2f}, speed:{objects[0].speed:.2f}"
    return objects, description, done

main_loop("Demo", calculate_data_func)
