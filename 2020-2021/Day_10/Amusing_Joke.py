def Amusing_Joke(letters,pile):
   
   if len(letters)!=len(pile):
       return('NO')
   
   letters=sorted(letters)
   pile=sorted(pile)
   
   if letters==pile:
       return('YES')
   else:
       return('NO')
   

if __name__ =='__main__':
     s1=input()
     s2=input()
     pile=input()
     
     print(Amusing_Joke(s1+s2 , pile))
     
     
     
     
     
     
     
#time=O(2n)
