"""
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    tp = tuple(integer_list)
    result = hash(tp)
    print(result)

"""

if __name__ == '__main__':
    n = int(input())
    integer_list = []
    for _ in range(n):
        integer_list.append(int(input()))
    tp = tuple(integer_list)
    result = hash(tp)
    print(result)
