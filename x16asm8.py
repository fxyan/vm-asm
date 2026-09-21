# 数据类型{
#   localOffset: 当前变量的内存地址
#   len: 当前变量的字节长度
# }
offset_var = {}
localOffset = 0
currentLabel = None
globalIndexWhile = 0
globalIndexIf = 0

globalIndexWhileIf = []


# encoding 有点问题 这里超过256了 一个字节存不下思考怎么处理
encoding_dict = {
            "'A'": 1,
            "'B'": 2,
            "'C'": 3,
            "'D'": 4,
            "'E'": 5,
            "'F'": 6,
            "'G'": 7,
            "'H'": 8,
            "'I'": 9,
            "'J'": 10,
            "'K'": 11,
            "'L'": 12,
            "'M'": 13,
            "'N'": 14,
            "'O'": 15,
            "'P'": 16,
            "'Q'": 17,
            "'R'": 18,
            "'S'": 19,
            "'T'": 20,
            "'U'": 21,
            "'V'": 22,
            "'W'": 23,
            "'X'": 24,
            "'Y'": 25,
            "'Z'": 26,
            "'a'": 27,
            "'b'": 28,
            "'c'": 29,
            "'d'": 30,
            "'e'": 31,
            "'f'": 32,
            "'g'": 33,
            "'h'": 34,
            "'i'": 35,
            "'j'": 36,
            "'k'": 37,
            "'l'": 38,
            "'m'": 39,
            "'n'": 40,
            "'o'": 41,
            "'p'": 42,
            "'q'": 43,
            "'r'": 44,
            "'s'": 45,
            "'t'": 46,
            "'u'": 47,
            "'v'": 48,
            "'w'": 49,
            "'x'": 50,
            "'y'": 51,
            "'z'": 52,
            "'0'": 53,
            "'1'": 54,
            "'2'": 55,
            "'3'": 56,
            "'4'": 57,
            "'5'": 58,
            "'6'": 59,
            "'7'": 60,
            "'8'": 61,
            "'9'": 62,
            "'?'": 63,
            "'!'": 64,
            "'.'": 65,
            "'\\'": 66,
            "\"\'\"": 67,
            "\'\"\'": 68,
            "'['": 69,
            "']'": 70,
            "','": 71,
            "':'": 72,
            "';'": 73,
            "')'": 74,
            "'('": 75,
            "'>'": 76,
            "'<'": 77,
            "'^'": 78,
            "'/'": 79,
            "'*'": 80,
            "'&'": 81,
            "'+'": 82,
            "'-'": 83,
            "'='": 84,
            "'$'": 85,
            "'_'": 86,
            "' '": 87,
        }


def deal_subtract(code):
    """
    前面和add2很类似了后面的话  变成减法
    """
    global localOffset, offset_var, currentLabel
    # print(localOffset)
    res = []
    a1_offset = offset_var[code[1]]['localOffset']
    res.append('set2 a3 {}'.format(localOffset - a1_offset))
    res.append('subtract2 f1 a3 a3')
    res.append('load_from_register2 a3 a1' if offset_var[code[1]]['len'] == 2 else 'load_from_register a3 a1')
    a2_offset = offset_var[code[2]]['localOffset']
    res.append('set2 a3 {}'.format(localOffset - a2_offset))
    res.append('subtract2 f1 a3 a3')
    res.append('load_from_register2 a3 a2' if offset_var[code[2]]['len'] == 2 else 'load_from_register a3 a2')
    res.append('subtract2 a1 a2 a1')
    a3_offset = offset_var[code[3]]['localOffset']
    res.append('set2 a3 {}'.format(localOffset - a3_offset))
    res.append('subtract2 f1 a3 a3')
    res.append('save_from_register2 a1 a3' if offset_var[code[3]]['len'] == 2 else 'save_from_register a1 a3')
    return res


def deal_print(code):
    """
    将 log写入 65533
    """
    global localOffset, offset_var, currentLabel
    # print(localOffset)
    res = []
    a1_offset = offset_var[code[1]]['localOffset']
    res.append('set2 a3 {}'.format(localOffset - a1_offset))
    res.append('subtract2 f1 a3 a3')
    res.append('load_from_register2 a3 a1' if offset_var[code[1]]['len'] == 2 else 'load_from_register a3 a1')
    res.append('set2 a3 65533')
    res.append('save_from_register2 a1 a3' if offset_var[code[1]]['len'] == 2 else 'save_from_register a1 a3')
    return res


def deal_import(code):
    """
    将对应文件写入到字典中
    """
    global localOffset, offset_var, currentLabel
    # print(localOffset)
    res = []
    a1_offset = offset_var[code[1]]['localOffset']
    res.append('set2 a3 {}'.format(localOffset - a1_offset))
    res.append('subtract2 f1 a3 a3')
    res.append('load_from_register2 a3 a1' if offset_var[code[1]]['len'] == 2 else 'load_from_register a3 a1')
    res.append('set2 a3 65533')
    res.append('save_from_register2 a1 a3' if offset_var[code[1]]['len'] == 2 else 'save_from_register a1 a3')
    return res


def deal_multiply(code):
    """
    前面和add2很类似了后面的话  变成乘法
    """
    global localOffset, offset_var, currentLabel
    # print('add', localOffset, offset_var, currentLabel, code)
    res = []
    a1_offset = offset_var[code[1]]['localOffset']
    res.append('set2 a3 {}'.format(localOffset - a1_offset))
    res.append('subtract2 f1 a3 a3')
    res.append('load_from_register2 a3 a1' if offset_var[code[1]]['len'] == 2 else 'load_from_register a3 a1')
    a2_offset = offset_var[code[2]]['localOffset']
    res.append('set2 a3 {}'.format(localOffset - a2_offset))
    res.append('subtract2 f1 a3 a3')
    res.append('load_from_register2 a3 a2' if offset_var[code[2]]['len'] == 2 else 'load_from_register a3 a2')
    res.append('multiply2 a1 a2 a1')
    a3_offset = offset_var[code[3]]['localOffset']
    res.append('set2 a3 {}'.format(localOffset - a3_offset))
    res.append('subtract2 f1 a3 a3')
    res.append('save_from_register2 a1 a3' if offset_var[code[3]]['len'] == 2 else 'save_from_register a1 a3')
    return res


# 这里不支持变量的字节长度变更
def deal_var(code):
    """
    ; .var2 a 12
    ; 汇编器记录变量 a 的 offset 为 0
    ; 局部变量占用内存 localOffset = 2
    set2 a1 12
    save_from_register2 a1 f1
    ; f1 += 2
    set2 a3 2
    add2 f1 a3 f1

    """
    global localOffset
    res = []
    if offset_var.get(code[1], None) is None:
        offset_var[code[1]] = {
            'localOffset': localOffset,
            'len': 2
        }
    if len(code) == 3:
        localOffset += 2
        res.append('set2 a1 {}'.format(code[2]))
        res.append('save_from_register2 a1 f1')
        res.append('set2 a3 2'.format())
        res.append('add2 f1 a3 f1')
    else:
        localOffset += 2
        res.append('set2 a3 2')
        res.append('add2 f1 a3 f1')
    return res


def deal_var1(code):
    """
    ; .var2 a 12
    ; 汇编器记录变量 a 的 offset 为 0
    ; 局部变量占用内存 localOffset = 2
    set2 a1 12
    save_from_register2 a1 f1
    ; f1 += 2
    set2 a3 2
    add2 f1 a3 f1

    """
    global localOffset
    res = []
    if offset_var.get(code[1], None) is None:
        offset_var[code[1]] = {
            'localOffset': localOffset,
            'len': 1
        }
    if len(code) == 3:
        if offset_var.get(code[1], None) is None:
            offset_var[code[1]] = {
                'localOffset': int(code[2]),
                'len': 1
            }
        localOffset += 1
        if encoding_dict.get(code[2], None) is not None:
            # print(code[2], encoding_dict.get(code[2]))
            encode_data = encoding_dict.get(code[2])
            res.append('set a1 {}'.format(encode_data))
            res.append('save_from_register a1 f1')
            res.append('set2 a3 1')
            res.append('add2 f1 a3 f1')
        else:
            res.append('set a1 {}'.format(code[2]))
            res.append('save_from_register a1 f1')
            res.append('set2 a3 1')
            res.append('add2 f1 a3 f1')
    else:
        localOffset += 1
        res.append('set2 a3 1')
        res.append('add2 f1 a3 f1')
    return res


def deal_var_string(code):
    """
    .var-string s1 "String_Rocks!"

    """
    global localOffset
    res = []
    # 重复赋值问题我这里不做处理
    str_data = code[-1][1:-1]
    offset_var[code[1]] = {
        'localOffset': localOffset,
        'len': len(str_data) + 1
    }
    # 因为要在末尾增加一个0所以localOffset要多+1
    localOffset += len(str_data) + 1
    print('str_data', str_data)
    for i in str_data:
        i = "'" + i + "'" if i != "'" else '"' + i + '"'
        print(i, encoding_dict.get(i), "?")
        encode_data = encoding_dict.get(i)
        res.append('set a1 {}'.format(encode_data))
        res.append('save_from_register a1 f1')
        res.append('set2 a3 1')
        res.append('add2 f1 a3 f1')
    # 在数组末尾增加0作为字符串结束的标示符
    res.append('set a1 0')
    res.append('save_from_register a1 f1')
    res.append('set2 a3 1')
    res.append('add2 f1 a3 f1')
    return res


def deal_call(code):
    """
; f1 现在是 7
    ; 使用 .call 调用函数的时候 pa 要存在内存 7 8
    ; 所以我们把变量存到内存 9 10 和 11 12
    ; 变量a 存在内存  9 10
    ; 变量b 存在内存 11 12

    ; 读取变量  变量a  到 a1
    set2 a3 4
    subtract2 f1 a3 a3
    load_from_register2 a3 a1

    ; 把 变量a（现在在 a1） 存到内存 9 10 也就是 f1+2 的地方
    set2 a3 2
    add2 f1 a3 a3
    save_from_register2 a1 a3

    ; 读取变量  变量b  到 a1
    set2 a3 2
    subtract2 f1 a3 a3
    load_from_register2 a3 a1

    ; 把 变量b（现在在 a1） 存到内存 11 12 也就是 f1+4 的地方
    set2 a3 4
    add2 f1 a3 a3
    save_from_register2 a1 a3

    .call @function_add

    set2 a1 12
    set2 a3 2
    add2 f1 a3 a3
    save_from_register2 a1 a3
    """
    global localOffset, offset_var, encoding_dict
    res = []
    auto = 2
    # print(dict, offset_var, localOffset, offset_var.get(code[2]),  code)
    if len(code) > 2:
        for i in code[2:]:
            # print(i)
            # 这里判断是否是编码参数
            if encoding_dict.get(i, None) is not None:
                encode_data = encoding_dict.get(i)
                res.append('set2 a3 {}'.format(auto))
                res.append('add2 f1 a3 a3')
                res.append('set2 a1 {}'.format(encode_data))
                res.append('save_from_register2 a1 a3')
                auto += 2
            else:
                # 判断是不是数字参数
                try:
                    i = int(i)
                    res.append('set2 a3 {}'.format(auto))
                    res.append('add2 f1 a3 a3')
                    res.append('set2 a1 {}'.format(i))
                    res.append('save_from_register2 a1 a3')
                    auto += 2
                except:
                    if i[0] == '&':
                        offset_var_1 = offset_var.get(i[1:])['localOffset']
                        res.append('set2 a3 {}'.format(localOffset - offset_var_1))
                        res.append('subtract2 f1 a3 a1')
                        res.append('set2 a3 {}'.format(auto))
                        res.append('add2 f1 a3 a3')
                        res.append('save_from_register2 a1 a3')
                        auto += 2
                    # 变量参数
                    elif offset_var.get(i) is not None:
                        offset_var_len = offset_var.get(i)['len']
                        offset_var_1 = offset_var.get(i)['localOffset']
                        res.append('set2 a3 {}'.format(localOffset - offset_var_1))
                        res.append('subtract2 f1 a3 a3')
                        res.append('load_from_register2 a3 a1' if offset_var_len == 2 else 'load_from_register a3 a1')
                        res.append('set2 a3 {}'.format(auto))
                        res.append('add2 f1 a3 a3')
                        res.append('save_from_register2 a1 a3' if offset_var_len == 2 else 'save_from_register a1 a3')
                        auto += offset_var.get(i)['len']
                    else:
                        # 这里未做处理关于不同字节的变量  如果没有被赋值     这里是没有记录过的参数 暂时不处理
                        res.append('set2 a3 {}'.format(auto))
                        res.append('add2 f1 a3 a3')
                        res.append('save_from_register2 a1 a3')
                        auto += 2
    # 函数默认需要的调用值
    res.append('set2 a3 14')
    res.append('add2 pa a3 a3')
    res.append('save_from_register2 a3 f1')
    res.append('set2 a3 2')
    res.append('add2 f1 a3 f1')
    res.append('jump {}'.format(code[1]) if code[1][0] == '@' else 'jump {}'.format('@function_' + code[1]))

    return res


def deal_add(code):
    """
    ; 读取变量 a 到 a1
    ; 读取的地址计算方式是 localOffset - a.offset 也就是 6-0 = 6
    set2 a3 6
    subtract2 f1 a3 a3
    load_from_register2 a3 a1

    ; 读取变量 b 到 a2
    ; 读取的地址计算方式是 localOffset - b.offset 也就是 6-2 = 4
    set2 a3 4
    subtract2 f1 a3 a3
    load_from_register2 a3 a2

    ; c = a + b
    ; 计算 a + b 并存入 a1 寄存器
    add2 a1 a2 a1
    ; 写入 a1 的值到变量 c
    ; 读取的地址计算方式是 localOffset - c.offset 也就是 6-4 = 2
    set2 a3 2
    subtract2 f1 a3 a3
    save_from_register2 a1 a3

    """
    global localOffset, offset_var, currentLabel
    # print('add', localOffset, offset_var, currentLabel, code)
    res = []
    # 这里是一个字典
    a1_offset = offset_var[code[1]]['localOffset']
    res.append('set2 a3 {}'.format(localOffset-a1_offset))
    res.append('subtract2 f1 a3 a3')
    res.append('load_from_register2 a3 a1' if offset_var[code[1]]['len'] == 2 else 'load_from_register a3 a1')
    a2_offset = offset_var[code[2]]['localOffset']
    res.append('set2 a3 {}'.format(localOffset-a2_offset))
    res.append('subtract2 f1 a3 a3')
    res.append('load_from_register2 a3 a2' if offset_var[code[2]]['len'] == 2 else 'load_from_register a3 a2')
    res.append('add2 a1 a2 a1')
    a3_offset = offset_var[code[3]]['localOffset']
    res.append('set2 a3 {}'.format(localOffset-a3_offset))
    res.append('subtract2 f1 a3 a3')
    res.append('save_from_register2 a1 a3' if offset_var[code[3]]['len'] == 2 else 'save_from_register a1 a3')
    return res


def deal_return(code):
    """
    ; 读取变量 c 到 a1 来返回函数
    ; 读取的地址计算方式是 localOffset - c.offset 也就是 6-4 = 2
    set2 a3 2
    subtract2 f1 a3 a3
    load_from_register2 a3 a1

    ; 这里的 6 即为 localOffset
    .return 6
    """
    global localOffset, offset_var, currentLabel
    # print(localOffset)
    res = []
    a1_offset = offset_var[code[1]]['localOffset']
    a1_offset_len = offset_var[code[1]]['len']
    res.append('set2 a3 {}'.format(localOffset-a1_offset))
    res.append('subtract2 f1 a3 a3')
    res.append('load_from_register2 a3 a1' if a1_offset_len == 2 else 'load_from_register a3 a1')
    res.append('set2 a3 {}'.format(localOffset + 2))
    res.append('subtract2 f1 a3 f1')
    res.append('load_from_register2 f1 a2')
    res.append('jump_from_register a2')
    return res


def deal_return_value(code):
    """
    .return_value c
    这句 .return_value c 的作用就是把 a1 寄存器的值写入到变量 c
    """
    global localOffset, offset_var, localOffset
    # print(localOffset)
    res = []
    a1_offset = offset_var[code[1]]['localOffset']
    a1_offset_len = offset_var[code[1]]['len']
    res.append('set2 a3 {}'.format(localOffset-a1_offset))
    res.append('subtract2 f1 a3 a3')
    res.append('save_from_register2 a1 a3' if a1_offset_len == 2 else 'save_from_register a1 a3')
    return res


def deal_func(code):
    """
    思路总结  插入@function 作为函数开始
    插入 .var xx  增加参数
    在 var map中增加return 的长度 例如1 或者2
    .function add:2 a:2 b:1

    首先把 add这个处理了
    """
    global localOffset, offset_var, currentLabel
    res = []
    # print('fucn', localOffset, offset_var, currentLabel)
    # 先处理add
    func_str_list = code[1].split(':')
    res.append('@function_{}'.format(func_str_list[0]))
    offset_var = {}
    localOffset = 0
    currentLabel = func_str_list[0]
    offset_var[func_str_list[0]] = int(func_str_list[1])
    for i in code[2:]:
        var_list = i.split(':')
        if int(var_list[1]) == 2:
            res_list = deal_var(['.var2', var_list[0]])
        else:
            res_list = deal_var1(['.var1', var_list[0]])
        for i in res_list:
            res.append(i)
    return res


def deal_while(code):
    """
    用法如下
    注意，只支持 < == 两个比较符号
    .while a < b {
        ; code
    }
    实现如下
    ; .while 展开
    @while_start
        ; .compare 意会
        .compare a b
        jump_if_less @while_body
        jump @while_end
        @while_body
            ; code
        jump @while_start
    @while_end
    """
    global localOffset, offset_var, currentLabel, globalIndexWhile, globalIndexWhileIf
    res = []
    # print('fucn', localOffset, offset_var, currentLabel, code)
    res.append('@while_start_{}'.format(globalIndexWhile))
    # 翻译.compare a b
    # 取出a
    a1_offset = offset_var[code[1]]['localOffset']
    a1_offset_len = offset_var[code[1]]['len']
    res.append('set2 a3 {}'.format(localOffset-a1_offset))
    res.append('subtract2 f1 a3 a3')
    res.append('load_from_register2 a3 a1' if a1_offset_len == 2 else 'load_from_register a3 a1')
    # 取出b
    a2_offset = offset_var[code[3]]['localOffset']
    a2_offset_len = offset_var[code[3]]['len']
    res.append('set2 a3 {}'.format(localOffset - a2_offset))
    res.append('subtract2 f1 a3 a3')
    res.append('load_from_register2 a3 a2' if a2_offset_len == 2 else 'load_from_register a3 a2')
    # compare a b
    res.append('compare a1 a2')
    if code[2] == '<':
        res.append('jump_if_less @while_body_{}'.format(globalIndexWhile))
    else:
        res.append('jump_if_equal @while_body_{}'.format(globalIndexWhile))
    res.append('jump @while_end_{}'.format(globalIndexWhile))
    res.append('@while_body_{}'.format(globalIndexWhile))
    # 增加while队列的先入先出
    globalIndexWhileIf.append({
        'type': 'while',
        'index': globalIndexWhile
    })
    globalIndexWhile += 1
    return res


def deal_if(code):
    """
    新增伪指令 .if
    用法如下
    注意，只支持 < == 两个比较符号
    .if a < b
        ; code
    .endif


    与 .while 一样
    我们的用一个全局的变量 globalIndexIf 来记录当前是第几个 if
    从 0 开始


    实现如下
    @if_0
        .compare a b
        jump_if_less @if_body_0
        jump @if_end_0
        @if_body_0
            ; code
    @if_end_0
    """
    global localOffset, offset_var, currentLabel, globalIndexIf, globalIndexWhileIf
    res = []
    print('fucn', localOffset, offset_var, currentLabel, code)
    res.append('@if_{}'.format(globalIndexIf))
    # 翻译.compare a b
    # 取出a
    a1_offset = offset_var[code[1]]['localOffset']
    a1_offset_len = offset_var[code[1]]['len']
    res.append('set2 a3 {}'.format(localOffset-a1_offset))
    res.append('subtract2 f1 a3 a3')
    res.append('load_from_register2 a3 a1' if a1_offset_len == 2 else 'load_from_register a3 a1')
    # 取出b
    a2_offset = offset_var[code[3]]['localOffset']
    a2_offset_len = offset_var[code[3]]['len']
    res.append('set2 a3 {}'.format(localOffset - a2_offset))
    res.append('subtract2 f1 a3 a3')
    res.append('load_from_register2 a3 a2' if a2_offset_len == 2 else 'load_from_register a3 a2')
    # compare a b
    res.append('compare a1 a2')
    if code[2] == '<':
        res.append('jump_if_less @if_body_{}'.format(globalIndexIf))
    else:
        res.append('jump_if_equal @if_body_{}'.format(globalIndexIf))
    # 应对else的情况
    if len(code) == 5:
        res.append('jump @if_else_{}'.format(globalIndexIf))
    else:
        res.append('jump @if_end_{}'.format(globalIndexIf))
    res.append('@if_body_{}'.format(globalIndexIf))
    # 增加if队列的先入先出
    globalIndexWhileIf.append({
        'type': 'if',
        'index': globalIndexIf
    })
    globalIndexIf += 1
    return res


def deal_endif(code):
    """

    """
    global localOffset, offset_var, currentLabel, globalIndexWhile, globalIndexWhileIf
    res = []
    data = globalIndexWhileIf.pop()
    if data['type'] == 'if':
        res.append('@if_end_{}'.format(data['index']))
    return res


def deal_while_if_end(code):
    """
    用来翻译if或则while end的时候对应的 }

    目前只有while  后续增加if的时候从这里处理


    用法如下
    注意，只支持 < == 两个比较符号
    .if a < b {
        ; code if
    } .else {
        ; code else
    }
    包含else的处理
        @if_0
        .compare a b
        jump_if_less @if_body_0
      ; 注意这里
        jump @if_else_0
        @if_body_0
            ; code if
            jump @if_end_0
    @if_else_0
        ; code else
    @if_end_0
    """
    global localOffset, offset_var, currentLabel, globalIndexWhile, globalIndexWhileIf
    res = []
    # print('while_if_end', localOffset, offset_var, currentLabel)
    data = globalIndexWhileIf.pop()
    # print(data)
    if len(code) > 1:
        res.append('jump @if_end_{}'.format(data['index']))
        res.append('@if_else_{}'.format(data['index']))
        globalIndexWhileIf.append(data)
    elif data['type'] == 'while':
        res.append('jump @while_start_{}'.format(data['index']))
        res.append('@while_end_{}'.format(data['index']))
    elif data['type'] == 'if':
        res.append('@if_end_{}'.format(data['index']))
    return res


def register_mapper():
    regs = dict(
        pa=0b00000000,
        a1=0b00010000,
        a2=0b00100000,
        a3=0b00110000,
        c1=0b01000000,
        f1=0b01010000,
    )
    return regs


def remove_comments(asm):
    ls = []
    for line in asm.split('\n'):
        if ';' in line:
            i = line.index(';')
            l = line[:i]
            ls.append(l)
        else:
            ls.append(line)
    code = '\n'.join(ls)
    return code


def deal_log(code):
    reg = register_mapper()
    res = []
    if reg.get(code[1]) is not None:
        res.append('save2 {} @65534'.format(code[1]))
    return res


def memory_address(memory):
    m = memory[1:]
    # print('mem', m)
    try:
        m = int(m)
        last = m >> 8
        first = m & 255
        # print('test', first, last, m)
        m = [first, last]
    except ValueError:
        pass
    return m


# 根据上面的资料，实现下面的函数
def machine_code(asm):
    """
    asm 是汇编语言字符串
    返回 list, list 中每个元素是一个 1 字节的数字
    """
    global currentLabel, offset_var, localOffset
    res = []
    regs = register_mapper()
    bef_lines = asm.split('\n')
    res_lines = []
    # 预处理一遍import 目前不支持嵌套导入
    for bef_line in bef_lines:
        if bef_line.strip() == '':
            res_lines.append(bef_line)
            continue
        bef_code = bef_line.strip().split()
        if bef_code[0] == '.import':
            files = open('{}'.format(bef_code[1])).read().split('\n')
            print('files', files)
            for file in files:
                res_lines.append(file)
        else:
            res_lines.append(bef_line)
    memory = []
    offset = 0
    label_address = {}
    pri = ''
    lines = []
    for line in res_lines:
        if line.strip() == '':
            continue
        code = line.strip().split()
        op = code[0]
        if op == '.call':   # todo 这个指令会优化一下之后会合并两个方式
            if len(code) == 2:
                lines.append('set2 a3 14')
                lines.append('add2 pa a3 a3')
                lines.append('save_from_register2 a3 f1')
                lines.append('set2 a3 2')
                lines.append('add2 f1 a3 f1')
                lines.append('jump {}'.format(code[1]))
            else:
                res_call = deal_call(code)
                for x in res_call:
                    lines.append(x)
        elif op == '.return':  # todo 这里要修复一下因为两个return可以合并成一个
            if len(code) == 2 and offset_var.get(code[1]) is not None:
                res_return = deal_return(code)
                for x in res_return:
                    lines.append(x)
            elif len(code) == 1:
                lines.append('set2 a3 {}'.format(localOffset + 2))
                lines.append('subtract2 f1 a3 f1')
                lines.append('load_from_register2 f1 a2')
                lines.append('jump_from_register a2')
            else:
                lines.append('set2 a3 {}'.format(str(int(code[1]) + 2)))
                lines.append('subtract2 f1 a3 f1')
                lines.append('load_from_register2 f1 a2')
                lines.append('jump_from_register a2')
        elif op == '.log':
            res_log = deal_log(code)
            for x in res_log:
                lines.append(x)
        elif op == '.var2':
            res_var = deal_var(code)
            for x in res_var:
                lines.append(x)
        elif op == '.var':
            res_var = deal_var1(code)
            for x in res_var:
                lines.append(x)
        elif op == '.add2':
            res_add = deal_add(code)
            for x in res_add:
                lines.append(x)
        elif op == '.subtract2':
            res_add = deal_subtract(code)
            for x in res_add:
                lines.append(x)
        elif op == '.multiply2':
            res_add = deal_multiply(code)
            for x in res_add:
                lines.append(x)
        elif op == '.return_value':
            res_add = deal_return_value(code)
            for x in res_add:
                lines.append(x)
        elif op == '.function':
            res_add = deal_func(code)
            for x in res_add:
                lines.append(x)
        elif op == '.while':
            res_add = deal_while(code)
            for x in res_add:
                lines.append(x)
        elif op == '.if':
            res_add = deal_if(code)
            for x in res_add:
                lines.append(x)
        elif op == '.endif':
            res_add = deal_endif(code)
            for x in res_add:
                lines.append(x)
        elif op == '}':
            res_add = deal_while_if_end(code)
            for x in res_add:
                lines.append(x)
        elif op == '.function_end':
            # 加上函数结束标示
            lines.append('@{}_end'.format(currentLabel))
        # 从这里判断一个函数的各种数据，包含清空处理
        elif op == '.var-string':
            res_add = deal_var_string(code)
            for x in res_add:
                lines.append(x)
        elif op == '.print':
            res_add = deal_print(code)
            for x in res_add:
                lines.append(x)
        elif op == '.import':
            res_add = deal_import(code)
            for x in res_add:
                lines.append(x)
        elif op[0] == '@':
            # print(code)
            if currentLabel and currentLabel + '_end' == code[1:]:
                offset_var = {}
                localOffset = 0
                currentLabel = None
            else:
                currentLabel = code[0][1:]
            lines.append(line)
        else:
            lines.append(line)
    for line in lines:
        # 跳过空行
        if line.strip() == '':
            continue
        code = line.strip().split()

        for i in code:
            pri += i + ' '
        pri += '\n'
        # print(code)
        # print(memory)
        op = code[0]
        if op == 'set':
            offset += 3
            reg = code[1]
            reg = regs[reg]
            value = int(code[2])
            memory.append(0)
            memory.append(reg)
            memory.append(value)
        elif op == 'load':
            offset += 4
            # mem = int(code[1][1:])
            mem = memory_address(code[1])
            reg = code[2]
            reg = regs[reg]
            memory.append(1)
            memory.append(mem)
            memory.append(reg)
        elif op == 'save':
            offset += 4
            # mem = int(code[2][1:])
            mem = memory_address(code[2])
            # print('save', code[1])
            reg = code[1]
            reg = regs[reg]
            memory.append(3)
            memory.append(reg)
            memory.append(mem)
        elif op == 'add':
            offset += 4
            r1 = regs.get(code[1])
            r2 = regs.get(code[2])
            r3 = regs.get(code[3])
            memory.append(2)
            memory.append(r1)
            memory.append(r2)
            memory.append(r3)
        elif op == 'compare':
            offset += 3
            r1 = regs.get(code[1])
            r2 = regs.get(code[2])
            memory.append(4)
            memory.append(r1)
            memory.append(r2)
        elif op == 'jump_if_less':
            offset += 3
            # mem = int(code[1][1:])
            mem = memory_address(code[1])
            memory.append(5)
            memory.append(mem)
        elif op == 'jump':
            offset += 3
            mem = memory_address(code[1])
            memory.append(6)
            memory.append(mem)
        elif op == 'halt':
            offset += 1
            memory.append(255)
        elif op[0] == '@':
            # 处理 label
            last = offset >> 8
            first = offset & 255
            value = [first, last]
            label_address[op[1:]] = value
        elif op == 'add2':
            offset += 4
            r1 = regs.get(code[1])
            r2 = regs.get(code[2])
            r3 = regs.get(code[3])
            memory.append(10)
            memory.append(r1)
            memory.append(r2)
            memory.append(r3)
        elif op == 'jump_from_register':
            offset += 2
            r1 = regs.get(code[1])
            memory.append(16)
            memory.append(r1)
        elif op == 'load_from_register2':
            offset += 3
            r1 = regs.get(code[1])
            r2 = regs.get(code[2])
            memory.append(14)
            memory.append(r1)
            memory.append(r2)
        elif op == 'load_from_register':
            offset += 3
            r1 = regs.get(code[1])
            r2 = regs.get(code[2])
            memory.append(13)
            memory.append(r1)
            memory.append(r2)
        elif op == 'subtract2':
            offset += 4
            r1 = regs.get(code[1])
            r2 = regs.get(code[2])
            r3 = regs.get(code[3])
            memory.append(12)
            memory.append(r1)
            memory.append(r2)
            memory.append(r3)
        elif op == 'jump_if_less':
            offset += 3
            # mem = int(code[1][1:])
            mem = memory_address(code[1])
            memory.append(5)
            memory.append(mem)
        elif op == 'set2':
            # print('code', code)
            offset += 4
            reg = code[1]
            reg = regs[reg]
            value = int(code[2])
            last = value >> 8
            first = value & 255
            # print('test', first, last, value)
            value = [first, last]
            memory.append(8)
            memory.append(reg)
            memory.append(value)
        elif op == 'load2':
            offset += 4
            # mem = int(code[1][1:])
            mem = memory_address(code[1])
            reg = code[2]
            reg = regs[reg]
            memory.append(9)
            memory.append(mem)
            memory.append(reg)
        elif op == 'save2':
            offset += 4
            mem = memory_address(code[2])
            reg = code[1]
            reg = regs[reg]
            memory.append(11)
            memory.append(reg)
            memory.append(mem)
        elif op == 'save_from_register2':
            offset += 3
            r1 = regs.get(code[1])
            r2 = regs.get(code[2])
            memory.append(15)
            memory.append(r1)
            memory.append(r2)
        elif op == 'save_from_register':
            offset += 3
            r1 = regs.get(code[1])
            r2 = regs.get(code[2])
            memory.append(7)
            memory.append(r1)
            memory.append(r2)
        elif op == '.memory':
            offset = 1024
            memory .append('.memory')
        elif op == 'shift_right':
            offset += 4
            r1 = regs.get(code[1])
            r2 = regs.get(code[2])
            r3 = regs.get(code[3])

            memory.append(17)
            memory.append(r1)
            memory.append(r2)
            memory.append(r3)
        elif op == 'and':
            offset += 4
            r1 = regs.get(code[1])
            r2 = regs.get(code[2])
            r3 = regs.get(code[3])

            memory.append(19)
            memory.append(r1)
            memory.append(r2)
            memory.append(r3)
        elif op == 'multiply2':
            offset += 4
            r1 = regs.get(code[1])
            r2 = regs.get(code[2])
            r3 = regs.get(code[3])

            memory.append(20)
            memory.append(r1)
            memory.append(r2)
            memory.append(r3)
        elif op == 'jump_if_equal':
            offset += 3
            # mem = int(code[1][1:])
            mem = memory_address(code[1])
            memory.append(21)
            memory.append(mem)


    print('pri', pri)
    print('label, ', label_address)
    # 替换 label 为内存地址
    for i, e in enumerate(memory):
        if isinstance(e, str) and e != '.memory':
            print(label_address, e, memory)
            memory[i] = label_address[e]
    for i in memory:
        if i == '.memory':
            memory_len = 1024 - len(res)
            res += [0] * memory_len
        elif type(i) != list:
            res.append(i)
        else:
            for j in i:
                res.append(j)
    return res
