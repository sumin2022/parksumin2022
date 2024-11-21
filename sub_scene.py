import gfw


import os
os.chdir('C:\\Users\\USER\\Documents\\GitHub\\parksumin2022180015\\res')

world = gfw.World(['bg'])

def enter():
    cw, ch = 800, 600
    cx, cy = cw // 2, ch // 2
    world.append(gfw.Sprite('base_scene2.jpg', cx, cy), world.layer.bg)

def exit():
    world.clear()
    print('[sub.exit()]')

def pause():
    pass

def resume():
    pass

def handle_event(e):
    pass

if __name__ == '__main__':
    gfw.start_main_module()

