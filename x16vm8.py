from x16asm import machine_code

class AxePU(object):
    def __init__(self, memory):
        self.memory = memory
        self.regs = dict(
            pa=0,
            a1=0,
            a2=0,
            a3=0,
            c1=0,
            f1=0,
        )
        self.encoding = {
            "A": [
                0b11111100,
                0b00010010,
                0b11111100,
                0b00000000,
            ],
            "B": [
                0b11111110,
                0b10010010,
                0b01101100,
                0b00000000,
            ],
            "C": [
                0b01111100,
                0b10000010,
                0b10000010,
                0b00000000,
            ],
            "D": [
                0b11111110,
                0b10000010,
                0b01111100,
                0b00000000,
            ],
            "E": [
                0b11111110,
                0b10010010,
                0b10000010,
                0b00000000,
            ],
            "F": [
                0b11111110,
                0b00010010,
                0b00000010,
                0b00000000,
            ],
            "G": [
                0b01111100,
                0b10000010,
                0b11100010,
                0b00000000,
            ],
            "H": [
                0b11111110,
                0b00010000,
                0b11111110,
                0b00000000,
            ],
            "I": [
                0b10000010,
                0b11111110,
                0b10000010,
                0b00000000,
            ],
            "J": [
                0b10000010,
                0b10000010,
                0b01111110,
                0b00000000,
            ],
            "K": [
                0b11111110,
                0b00011000,
                0b11100110,
                0b00000000,
            ],
            "L": [
                0b11111110,
                0b10000000,
                0b10000000,
                0b00000000,
            ],
            "M": [
                0b11111110,
                0b00001100,
                0b11111110,
                0b00000000,
            ],
            "N": [
                0b11111110,
                0b00000010,
                0b11111100,
                0b00000000,
            ],
            "O": [
                0b01111100,
                0b10000010,
                0b01111100,
                0b00000000,
            ],
            "P": [
                0b11111110,
                0b00010010,
                0b00001100,
                0b00000000,
            ],
            "Q": [
                0b01111100,
                0b01000010,
                0b10111100,
                0b00000000,
            ],
            "R": [
                0b11111110,
                0b00010010,
                0b11101100,
                0b00000000,
            ],
            "S": [
                0b10001100,
                0b10010010,
                0b01100010,
                0b00000000,
            ],
            "T": [
                0b00000010,
                0b11111110,
                0b00000010,
                0b00000000,
            ],
            "U": [
                0b01111110,
                0b10000000,
                0b11111110,
                0b00000000,
            ],
            "V": [
                0b01111110,
                0b10000000,
                0b01111110,
                0b00000000,
            ],
            "W": [
                0b11111110,
                0b01100000,
                0b11111110,
                0b00000000,
            ],
            "X": [
                0b11101110,
                0b00010000,
                0b11101110,
                0b00000000,
            ],
            "Y": [
                0b00001110,
                0b11110000,
                0b00001110,
                0b00000000,
            ],
            "Z": [
                0b11100010,
                0b10011010,
                0b10000110,
                0b00000000,
            ],
            "a": [
                0b00110000,
                0b01001000,
                0b01111000,
                0b00000000,
            ],
            "b": [
                0b01111110,
                0b01001000,
                0b00110000,
                0b00000000,
            ],
            "c": [
                0b00110000,
                0b01001000,
                0b01001000,
                0b00000000,
            ],
            "d": [
                0b00110000,
                0b01001000,
                0b01111110,
                0b00000000,
            ],
            "e": [
                0b00110000,
                0b01101000,
                0b01011000,
                0b00000000,
            ],
            "f": [
                0b10001000,
                0b01111100,
                0b00001010,
                0b00000000,
            ],
            "g": [
                0b00010000,
                0b10101000,
                0b01111000,
                0b00000000,
            ],
            "h": [
                0b01111110,
                0b00001000,
                0b01110000,
                0b00000000,
            ],
            "i": [
                0b00000000,
                0b01110100,
                0b00000000,
                0b00000000,
            ],
            "j": [
                0b10010000,
                0b01110100,
                0b00000000,
                0b00000000,
            ],
            "k": [
                0b01111110,
                0b00010000,
                0b01101000,
                0b00000000,
            ],
            "l": [
                0b00000000,
                0b01111110,
                0b00000000,
                0b00000000,
            ],
            "m": [
                0b01111000,
                0b00010000,
                0b01111000,
                0b00000000,
            ],
            "n": [
                0b01111000,
                0b00001000,
                0b01110000,
                0b00000000,
            ],
            "o": [
                0b00110000,
                0b01001000,
                0b00110000,
                0b00000000,
            ],
            "p": [
                0b11111000,
                0b00101000,
                0b00010000,
                0b00000000,
            ],
            "q": [
                0b00010000,
                0b00101000,
                0b11111000,
                0b00000000,
            ],
            "r": [
                0b01111000,
                0b00010000,
                0b00001000,
                0b00000000,
            ],
            "s": [
                0b01010000,
                0b01111000,
                0b00101000,
                0b00000000,
            ],
            "t": [
                0b00001000,
                0b00111100,
                0b01001000,
                0b00000000,
            ],
            "u": [
                0b00111000,
                0b01000000,
                0b01111000,
                0b00000000,
            ],
            "v": [
                0b00111000,
                0b01000000,
                0b00111000,
                0b00000000,
            ],
            "w": [
                0b01111000,
                0b00100000,
                0b01111000,
                0b00000000,
            ],
            "x": [
                0b01011000,
                0b00110000,
                0b01011000,
                0b00000000,
            ],
            "y": [
                0b10011000,
                0b10100000,
                0b01111000,
                0b00000000,
            ],
            "z": [
                0b01001000,
                0b01101000,
                0b01011000,
                0b00000000,
            ],
            "0": [
                0b00111000,
                0b01010100,
                0b00111000,
                0b00000000,
            ],
            "1": [
                0b01001000,
                0b01111100,
                0b01000000,
                0b00000000,
            ],
            "2": [
                0b01100100,
                0b01010100,
                0b01001000,
                0b00000000,
            ],
            "3": [
                0b01000100,
                0b01010100,
                0b00101000,
                0b00000000,
            ],
            "4": [
                0b00111100,
                0b00100000,
                0b01111000,
                0b00000000,
            ],
            "5": [
                0b01011100,
                0b01010100,
                0b00100100,
                0b00000000,
            ],
            "6": [
                0b00111000,
                0b01010100,
                0b00100000,
                0b00000000,
            ],
            "7": [
                0b00000100,
                0b00000100,
                0b01111100,
                0b00000000,
            ],
            "8": [
                0b00101000,
                0b01010100,
                0b00101000,
                0b00000000,
            ],
            "9": [
                0b00001000,
                0b01010100,
                0b00111000,
                0b00000000,
            ],
            "?": [
                0b00000010,
                0b01010010,
                0b00001110,
                0b00000000,
            ],
            "!": [
                0b00000000,
                0b01011110,
                0b00000000,
                0b00000000,
            ],
            ".": [
                0b00000000,
                0b01000000,
                0b00000000,
                0b00000000,
            ],
            "\\": [
                0b00000110,
                0b00011000,
                0b01100000,
                0b00000000,
            ],
            "'": [
                0b00000000,
                0b00000110,
                0b00000000,
                0b00000000,
            ],
            '"': [
                0b00000110,
                0b00000000,
                0b00000110,
                0b00000000,
            ],
            "[": [
                0b01111110,
                0b01000010,
                0b00000000,
                0b00000000,
            ],
            "]": [
                0b01000010,
                0b01111110,
                0b00000000,
                0b00000000,
            ],
            ",": [
                0b10000000,
                0b01000000,
                0b00000000,
                0b00000000,
            ],
            ":": [
                0b00000000,
                0b01010000,
                0b00000000,
                0b00000000,
            ],
            ";": [
                0b10000000,
                0b01010000,
                0b00000000,
                0b00000000,
            ],
            ")": [
                0b01000010,
                0b00111100,
                0b00000000,
                0b00000000,
            ],
            "(": [
                0b00111100,
                0b01000010,
                0b00000000,
                0b00000000,
            ],
            ">": [
                0b01000100,
                0b00101000,
                0b00010000,
                0b00000000,
            ],
            "<": [
                0b00010000,
                0b00101000,
                0b01000100,
                0b00000000,
            ],
            "^": [
                0b00000100,
                0b00000010,
                0b00000100,
                0b00000000,
            ],
            "/": [
                0b01100000,
               0b00011000,
               0b00000110,
               0b00000000,
            ],
            "*": [
                0b01010100,
                0b00111000,
                0b01010100,
                0b00000000,
            ],
            "&": [
                0b01110100,
                0b01011010,
                0b11100100,
                0b00000000,
            ],
            "+": [
                0b00010000,
                0b00111000,
                0b00010000,
                0b00000000,
            ],
            "-": [
                0b00010000,
                0b00010000,
                0b00010000,
                0b00000000,
            ],
            "=": [
                0b00101000,
                0b00101000,
                0b00101000,
                0b00000000,
            ],
            "$": [
                0b00101100,
                0b01111110,
                0b00110100,
                0b00000000,
            ],
            "_": [
                0b10000000,
                0b10000000,
                0b10000000,
                0b00000000,
            ],
            " ": [
                0b00000000,
                0b00000000,
                0b00000000,
                0b00000000,
            ],
        }

    def set_register(self, register, value):
        r = register
        if r == 0:
            self.regs['pa'] = value
        elif r == 16:
            self.regs['a1'] = value
        elif r == 32:
            self.regs['a2'] = value
        elif r == 48:
            self.regs['a3'] = value
        elif r == 80:
            self.regs['f1'] = value

    def register(self, register):
        r = register
        if r == 0:
            return self.regs['pa']
        elif r == 16:
            return self.regs['a1']
        elif r == 32:
            return self.regs['a2']
        elif r == 48:
            return self.regs['a3']
        elif r == 64:
            return self.regs['c1']
        elif r == 80:
            return self.regs['f1']

    def write_encoding(self):
        count = 65024
        for k, v in self.encoding.items():
            for j in v:
                self.memory[count] = j
                count += 1

    def run(self):
        self.write_encoding()
        while True:
            pa = self.regs['pa']
            # print('last', self.regs, self.memory[pa: pa+5])
            op = self.memory[pa]
            # print('pa:', pa, 'op:', op)
            if op == 0: # set
                r = self.memory[pa + 1]
                v = self.memory[pa + 2]
                self.regs['pa'] += 3
                self.set_register(r, v)
            elif op == 1: # load
                v = self.memory[pa + 1] + 256 * self.memory[pa + 2]
                r = self.memory[pa + 3]
                self.regs['pa'] += 4
                self.set_register(r, self.memory[v])
                # self.memory[v] = self.register(r)
            elif op == 2: # add
                r1 = self.memory[pa + 1]
                r2 = self.memory[pa + 2]
                r3 = self.memory[pa + 3]
                self.regs['pa'] += 4
                # self.set_register(r, v)
                v = self.register(r1) + self.register(r2)
                if v > 256:
                    v -= 256
                self.set_register(r3, v)
            elif op == 3: # save
                r = self.memory[pa + 1]
                v = self.memory[pa + 2] + 256 * self.memory[pa + 3]
                self.regs['pa'] += 4
                # self.set_register(r, v)
                # print('op 3', v)
                self.memory[v] = self.register(r)
            elif op == 4: # compare
                r1 = self.memory[pa + 1]
                r2 = self.memory[pa + 2]
                self.regs['pa'] += 3
                # self.set_register(r, v)
                # print(self.regs, self.register(r1), self.register(r2))
                if self.register(r1) > self.register(r2):
                    self.regs['c1'] = 2
                elif self.register(r1) == self.register(r2):
                    self.regs['c1'] = 1
                elif self.register(r1) < self.register(r2):
                    self.regs['c1'] = 0
            elif op == 5: # jump_if_less
                v = self.memory[pa + 1] + self.memory[pa + 2] * 256
                # print('yrdy', v, self.regs['c1'])
                self.regs['pa'] += 3
                if self.regs['c1'] == 0:
                    # print('???1')
                    self.regs['pa'] = v
            elif op == 6: # jump
                v = self.memory[pa + 1] + self.memory[pa + 2] * 256
                self.regs['pa'] += 2
                self.regs['pa'] = v
            elif op == 8: # set2
                r = self.memory[pa + 1]
                v = self.memory[pa + 2] + self.memory[pa + 3] * 256
                self.regs['pa'] += 4
                self.set_register(r, v)
            elif op == 11: # save2
                r = self.memory[pa + 1]
                v = self.memory[pa + 2] + self.memory[pa + 3] * 256
                self.regs['pa'] += 4
                self.memory[v] = self.register(r) % 256
                self.memory[v+1] = self.register(r) // 256
                if v == 65534:
                    print(self.memory[v: v+2])
            elif op == 9: # load2
                v = self.memory[pa + 1] + self.memory[pa + 2] * 256
                r = self.memory[pa + 3]
                self.regs['pa'] += 4
                self.set_register(r, self.memory[v])
            elif op == 10: # add2
                r1 = self.memory[pa + 1]
                r2 = self.memory[pa + 2]
                r3 = self.memory[pa + 3]
                self.regs['pa'] += 4
                # self.set_register(r, v)
                v = self.register(r1) + self.register(r2)
                self.set_register(r3, v)
            elif op == 12: # subtract2
                r1 = self.memory[pa + 1]
                r2 = self.memory[pa + 2]
                r3 = self.memory[pa + 3]
                self.regs['pa'] += 4
                # self.set_register(r, v)
                v = self.register(r1) - self.register(r2)
                self.set_register(r3, v)
            elif op == 13: # load_from_register
                r1 = self.memory[pa + 1]
                r2 = self.memory[pa + 2]

                self.regs['pa'] += 3
                # self.set_register(r, v)
                v = self.register(r1)
                v = self.memory[v]
                if v > 256:
                    v -= 256
                self.set_register(r2, v)
            elif op == 14: #  load_from_register
                r1 = self.memory[pa + 1]
                r2 = self.memory[pa + 2]
                self.regs['pa'] += 3
                v = self.register(r1)
                v = self.memory[v] + self.memory[v+1] * 256
                self.set_register(r2, v)
            elif op == 7: # save_from_register
                r1 = self.memory[pa + 1]
                r2 = self.memory[pa + 2]

                self.regs['pa'] += 3
                # self.set_register(r, v)
                v = self.register(r1)
                v2 = self.register(r2)
                # print('v2', v2, r1, r2, self.memory[:50])
                self.memory[v2] = v % 256
            elif op == 15: # save_from_register2
                r1 = self.memory[pa + 1]
                r2 = self.memory[pa + 2]

                self.regs['pa'] += 3
                # self.set_register(r, v)
                v = self.register(r1)
                v2 = self.register(r2)
                self.memory[v2] = v % 256
                self.memory[v2+1] = v // 256
                if v2 == 65534:
                    print(self.memory[v2: v2+2])
            elif op == 16: # jump_from_register
                r1 = self.memory[pa + 1]
                v = self.register(r1)
                self.regs['pa'] = v
            elif op == 17:  # shift_right
                r1 = self.memory[pa + 1]
                r2 = self.memory[pa + 2]
                r3 = self.memory[pa + 3]
                v1 = self.register(r1)
                v2 = self.register(r2)
                v3 = v1 >> v2
                self.set_register(r3, v3)
                self.regs['pa'] += 4
            elif op == 19:  # and
                r1 = self.memory[pa + 1]
                r2 = self.memory[pa + 2]
                r3 = self.memory[pa + 3]
                v1 = self.register(r1)
                v2 = self.register(r2)
                v3 = v1 & v2
                self.set_register(r3, v3)
                self.regs['pa'] += 4
            elif op == 20:  # multiply2
                r1 = self.memory[pa + 1]
                r2 = self.memory[pa + 2]
                r3 = self.memory[pa + 3]
                v1 = self.register(r1)
                v2 = self.register(r2)
                v3 = v1 * v2
                self.set_register(r3, v3)
                self.regs['pa'] += 4
            elif op == 21: # jump_if_equal
                v = self.memory[pa + 1] + self.memory[pa + 2] * 256
                # print('yrdy', v, self.regs['c1'])
                self.regs['pa'] += 3
                if self.regs['c1'] == 1:
                    self.regs['pa'] = v
            else:
                return


def run(memory):
    cpu = AxePU(memory)
    cpu.run()
    pass


# memory = machine_code('''
#     jump @1024
#     ; 从第四个字节开始，剩下的 1021 个字节都是我们的
#     ; 下面是内存 1024 开始的内容
#     ; 初始化 f1 寄存器，这是需要我们手动做的
#     .memory 1024
#     set2 f1 3       ; 设置 f1 寄存器为 3，我们用这个寄存器里的内存地址来保存函数返回后应该跳转的地址
#     ; 我们要在接下来的的内存存放函数定义，所以直接跳转到 @function_define_end 避免执行函数
#     jump @function_define_end
#     ; 定义一个函数 function_multiply，接受两个参数，返回两个数的乘积
#     ; 参数通过 a1 a2 得到，返回值通过 a1 传给调用方
#     @function_multiply
#     ; 用 a3 来作为循环的下标 i
#     set2 a3 1
#     ; 我们需要在循环中把 a3 + 1，并且把 a1 累加
#     ; 由于我们只有 3 个通用寄存器可用，我们需要用 3 个内存来暂存 a1 a2 a3 的值
#     ; 因为我们现在是自主决定使用所有内存，所以我们可以手动指定使用的内存区域
#     ; 我们把 65534 65532 65530 这三个地址拿来存储 a1 a2 a3 的值
#     ; 我们先保存 a1
#     save2 a1 @65534
#     set2 a1 0
#     @while_start            ; 循环开始
#     compare a2 a3
#     jump_if_less @while_end ; 一旦 a2 小于 a3，就结束循环
#     ; 我们用 a2 来作为临时寄存器使用
#     ; 因此先把 a2 的值保存到 65532, 然后利用 a2 把 a3+1
#     save2 a2 @65532
#     set2 a2 1
#     add2 a3 a2 a3
#     ; 把循环开始之前暂存的 a1 放到 a2 中然后累加到 a1
#     load2 @65534 a2
#     add2 a1 a2 a1
#     ; 恢复 a2 的值并跳转到循环开始
#     load2 @65532 a2
#     jump @while_start
#     @while_end
#     ; 函数结束了，这时候 a1 存的就是 a1*a2 的值
#     ; f1 寄存器里面存储的是函数调用前的地址，我们让 f1-2，然后把它取出来, 然后返回
#     set2 a3 2
#     subtract2 f1 a3 f1
#     load_from_register2 f1 a2
#     jump_from_register a2
#     ; 所有函数定义结束的标记（但我们这个例子中，只有一个函数定义）
#     @function_define_end
#     ; 我们来调用前面的 multiply 函数
#     set2 a1 300     ; a1 是 300
#     set2 a2 10      ; a2 是 10
#     ; 保存 pa 到 f1 所表示的内存中
#     ; 请特别注意下面的写法
#     ; save_from_register2 长度是 3 字节
#     ; jump 长度是 3 字节
#     ; set2 add2 各自占用 4 字节
#     ; 所以我们用它们两句之前的 add2 来修正函数返回时候的正确地址(也就是 14)
#     ; cpu 读了 add2 这句后就会把 pa + 4（add2 占用 4 字节）
#     ; 然后才会执行 add2，所以执行 add2 这句的时候只需要把 pa + 6 就能指向 jump @function_multiply 的下一句
#     set2 a3 14
#     add2 pa a3 a3
#     save_from_register2 a3 f1   ; 这行指令占 3 字节
#     ; 保存后，要把 f1 的值 +2
#     set2 a3 2                   ; 这行指令占 4 字节
#     add2 f1 a3 f1               ; 这行指令占 4 字节
#     ; 跳转到函数
#     jump @function_multiply     ; 这行指令占 3 字节
#     ; 函数返回了，这里的 a1 就是我们想要的返回值
#     halt
#     ''')
# memory = memory + (65536 - len(memory)) * [0]
# run(memory)
