if __name__ == '__main__':
    s=input()

    len1=s.count('1')
    index2=s.find('2')
    if index2==-1:
        s=list(s)
        s.sort()
        print(''.join(s))

    else:
        temp=s[:index2]

        zero=temp.count('0')
        result='0'*zero+'1'*len1+s[index2:].replace('1','')

        print(result)
