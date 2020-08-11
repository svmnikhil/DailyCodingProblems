#given an integer n, return the longest consecutive run of 1's in binary representation
#i.e. given 156, return 3. 156 -> 10011100 has 3 consecutive 1's in the number

n = int(input("enter number: "))

#formats all numerical inputs to binary
to_binary = lambda x: format(x, 'b') 

bin_rep = to_binary(n)
count = 0
highest = count

for i, j in enumerate(bin_rep):

  if int(j) == 1:
    count += 1

    if count >= highest:
      highest = count

  else: 
    count = 0

print(highest)
  