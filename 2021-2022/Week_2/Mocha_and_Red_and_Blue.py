if __name__ == '__main__':
    t=int(input())
    for i in range(t):
        n=int(input())
        s=input()
        if s=='?'*n:
            s='B'+s[1:]
        while '?' in s:
            s=s.replace('?R','BR')
            s=s.replace('?B','RB')
            s=s.replace('R?','RB')
            s=s.replace('B?','BR')
        print(s)

#https://codeforces.com/problemset/problem/1559/B
