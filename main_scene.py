from pico2d import * 
import gfw
from girl import Girl

import os
os.chdir('C:\\Users\\USER\\Documents\\GitHub\\parksumin2022180015\\res')

world = gfw.World(['bg', 'fg', 'player'])

def enter():
    cw, ch = get_canvas_width(), get_canvas_height()
    cx, cy = cw // 2, ch // 2
    world.append(gfw.Sprite('base_scene1.jpg', cx, cy), world.layer.bg)
    global girl
    girl = Girl()
    world.append(girl, world.layer.player)

def exit():
    world.clear()
    print('[main.exit()]')

def pause():
    print('[main.pause()]')

def resume():
    print('[main.resume()]')

def handle_event(e):
    if e.type == SDL_KEYDOWN and e.key == SDLK_RETURN:
        # gfw.push(sub_scene)
        return True # 이 이벤트는 처리했음을 알린다
    if e.type == SDL_KEYDOWN and e.key == SDLK_1:
        print(world.objects)

    girl.handle_event(e)

if __name__ == '__main__':
    gfw.start_main_module()

