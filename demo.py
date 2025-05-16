from common import main_loop, Object, CANVAS_SIZE

FPS = (24, 1/24)
SCALE = 5
G = 9.8

objects = [
    Object("Object BLUE", CANVAS_SIZE[0] // 2, 15, 15, "blue", 0),
    Object("Object RED", CANVAS_SIZE[0] // 4, CANVAS_SIZE[1] - 15, 15, "red", -8)
]

def calculate_data_func():
    global objects
    description = ""
    done = True
    for obj in objects:
        obj.speed += G / FPS[0]
        if obj.center_y + SCALE * obj.speed > CANVAS_SIZE[1] - obj.radius:
            obj.center_y = CANVAS_SIZE[1] - obj.radius
            obj.speed = 0
        else:
            obj.center_y = obj.center_y + SCALE * obj.speed
            done = False
        description += f"{obj.title}\tx: {obj.center_x:.2f}, y: {CANVAS_SIZE[1] - obj.center_y:.2f}, speed: {obj.speed:.2f}\n"
    return objects, description, FPS[1], done

main_loop("Demo", calculate_data_func)
