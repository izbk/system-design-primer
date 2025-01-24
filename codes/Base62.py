def to_base62(num):
    base62_chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if num == 0:
        return base62_chars[0]
    base62_str = ""
    while num > 0:
        num, remainder = divmod(num, 62)
        base62_str = base62_chars[remainder] + base62_str
    return base62_str

if __name__ == '__main__':
    # 示例
    num = 123456789
    base62_str = to_base62(num)
    print(f"数字 {num} 的 Base62 编码是: {base62_str}")