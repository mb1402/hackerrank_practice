if __name__ == '__main__':
    N = int(input())
    list=[]
    for i in range(N):
        command = input().split()
        cmd = command[0]
        args = command[1:]
        args = ",".join(args)
        if cmd != 'print':
            command = cmd + '(' +args + ')'
            eval("list."+command)
        elif cmd == "print":
            print(list)
        