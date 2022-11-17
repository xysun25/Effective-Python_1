# 编写高质量Python代码的第3个方法
# 2022/11/17
# 题目：编写接受str或bytes, 并总返回str
# 题目：编写接受str或bytes, 并总返回bytes

def to_str(bytes_or_str):
    # isinstance()方法，用来判断一个函数是否是一个已知的类型，考虑继承关系
    if isinstance(bytes_or_str,bytes):    # 如果bytes_or_str 是bytes 的实例，返回True;不是一个给定类型对象，返回False.
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return  value

def to_bytes(bytes_or_str):
    if isinstance(bytes_or_str,str):
        value = bytes_or_str.encode('utf-8')
    else:
        value = bytes_or_str
    return value




