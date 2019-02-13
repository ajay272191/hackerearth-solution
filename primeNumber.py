#https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/prime-number-8/

def checkPrime(n):

	if(n==2):
		return 1
	else:
		for i in range(2,n):

			if(n%i==0):
				return 0
	return 1

if __name__ == '__main__':
	
	n=int(input())
	result=[]
	for i in range(2,n+1):

		if(checkPrime(i)):
			result.append(i)
	print(*result)