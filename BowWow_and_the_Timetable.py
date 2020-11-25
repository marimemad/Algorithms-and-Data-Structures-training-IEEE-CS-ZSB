
def binary_to_decimal(n):
    return(int(n,2))



def calc_time(n):
    
    n=binary_to_decimal(n)
    count=0
    t=1
    
    while t<n:
        count+=1
        t*=4
    return(count)



if __name__=='__main__':
    num=input()
    print(calc_time(num))





'''

binaryString = input()

# Find Max Bit in the binary string
maxBit = len(binaryString) - 1  # O(1)
# Count Number of Ones in the binary String
numberOfOnes = binaryString.count('1')  # O(n)
# Number of missed stations
numberOfMissedStations = 0  # O(1)
if maxBit % 2 != 0:  # O(1)
    maxBit += 1
    numberOfOnes = 0

numberOfMissedStations = maxBit // 2  # O(1)
if numberOfOnes > 1:  # O(1)
    numberOfMissedStations += 1

print(numberOfMissedStations)

# Overall time complexity is # O(n)

'''
