from axe14.x16asm8 import machine_code
import axe14.x16vm8 as x16vm


def task_draw_func():
    asm = """
;假设屏幕是 100x100 像素
;从内存 30000 开始，每像素 1 字节
;一共 10000 字节


;@function_draw_point x y
;它有 2 个参数分别是 x y
;它会在屏幕指定的 x y 处画一个点（颜色你自己定，写死在函数内）


;由于每像素占用 1 字节
;所以需要使用操作一字节数据的 save_from_register 函数

jump @1024

.memory 1024
set2 f1 3

.var2 x 5
.var2 y 5
.call @function_draw_point x y

halt

; 画图
@function_draw_point
    ; 取出x a1
    ; 取出y a2
    ; y-1 * 100 放回a2处
    ; y+x 放回a1处
    ; 将a1处内存地址修改为红色11000011
    ; 返回
    .var2 x
    .var2 y
    ; 获取y
    set2 a3 2
    subtract2 f1 a3 a3
    load_from_register2 a3 a1

    ; 设置a3 为100
    set2 a3 100

    ; 计算乘法 因为y * 100 + 30000 + x的值才是坐标
    multiply2 a1 a3 a1
    set2 a3 30000
    add2 a1 a3 a1

    ; 获取x
    set2 a3 4
    subtract2 f1 a3 a3
    load_from_register2 a3 a2

    ; x + y
    add2 a1 a2 a1

    ; 将对应的内存写为红色
    set2 a2 11000011
    save_from_register a2 a1

    .return 4    
    """
    memory = machine_code(asm)
    print(memory)
    # print('end')
    # print(memory)
    memory = memory + (65536 - len(memory)) * [0]
    # print(memory)
    cpu = x16vm.AxePU(memory)
    cpu.run()
    res = cpu.memory[30000:40000]
    print('res', res)
    main(res)
    output = [
        cpu.regs['a1'],
    ]
    expected = [
        0,
    ]
    print(expected, output)
    # assert expected == output


def task_draw_func_clear_wait():
    asm = """
;假设屏幕是 100x100 像素
;从内存 30000 开始，每像素 1 字节
;一共 10000 字节


;@function_draw_point x y
;它有 2 个参数分别是 x y
;它会在屏幕指定的 x y 处画一个点（颜色你自己定，写死在函数内）


;由于每像素占用 1 字节
;所以需要使用操作一字节数据的 save_from_register 函数

jump @1024

.memory 1024
set2 f1 3

.var2 x 5
.var2 y 5
.call @function_draw_point x y

halt

; 画图
@function_draw_point
    ; 取出x a1
    ; 取出y a2
    ; y-1 * 100 放回a2处
    ; y+x 放回a1处
    ; 将a1处内存地址修改为红色11000011
    ; 返回
    .var2 x
    .var2 y
    ; 获取y
    set2 a3 2
    subtract2 f1 a3 a3
    load_from_register2 a3 a1

    ; 设置a3 为100
    set2 a3 100

    ; 计算乘法 因为y * 100 + 30000 + x的值才是坐标
    multiply2 a1 a3 a1
    set2 a3 30000
    add2 a1 a3 a1

    ; 获取x
    set2 a3 4
    subtract2 f1 a3 a3
    load_from_register2 a3 a2

    ; x + y
    add2 a1 a2 a1

    ; 将对应的内存写为红色
    set2 a2 11000011
    save_from_register a2 a1

    .return 4    
    """
    memory = machine_code(asm)
    print(memory)
    # print('end')
    # print(memory)
    memory = memory + (65536 - len(memory)) * [0]
    # print(memory)
    cpu = x16vm.AxePU(memory)
    cpu.run()
    res = cpu.memory[30000:40000]
    print('res', res)
    main(res)
    output = [
        cpu.regs['a1'],
    ]
    expected = [
        0,
    ]
    print(expected, output)
    # assert expected == output


import pygame
# py代码
def parse_rgba(val):
    rgba_list = list()
    for _ in range(4):
        rgba_list.append((val & 3) * 85)
        val >>= 2
    return rgba_list[::-1]


def main(data):
    print(data)
    width, height = 400, 400
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()
    running = True
    fps = 30
    count = 0
    for i in data:
        x_pos = count % 100 * 4
        y_pos = count // 100 * 4
        colors = parse_rgba(i)
        if i != 0:
            print('data', i)
            print(x_pos, y_pos, count)
            for z in range(4):
                for j in range(4):
                    # 这里直接画一个4*4的东西出来
                    x = x_pos + j
                    y = y_pos + z
                    position = (x, y)
                    color = (colors)
                    screen.set_at(position, color)

                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            running = False

                    pygame.display.flip()
                    clock.tick(fps)
        count += 1
    while True:
        pass



# task_func()
# task_if()
# task_else()
# task_muit()
# task_var_string()
# task_string()
# task_len_func()
task_draw_func()


# with open('stringlib8.a16') as f:
#     print(f.readlines())
#     for line in f.readlines():
#         print(line, type(line))