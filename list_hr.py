if __name__ == '__main__':
    N = int(input())
    li = []
    for i in range(N):
        str = input()
        ins = str.split()
        cmd = ins[0]
        args = ins[1:]
        if cmd == "insert":
            li.insert(int(args[0]), int(args[1]))

        elif cmd == "print":
            print(li)
        elif cmd == "remove":
            li.remove(int(args[0]))

        elif cmd == "append":
            li.append(int(args[0]))

        elif cmd == "sort":
            li.sort()

        elif cmd == "pop":
            li.pop()

        elif cmd == "reverse":
            li.reverse()

