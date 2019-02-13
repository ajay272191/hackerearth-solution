#https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/seating-arrangement-1/
	def seatType(n):
		if((n==0) or (n==5)):
			return 'WS'
		elif((n==1) or(n==4)):
			return 'MS'
		else:
			return 'AS'
	def seatNumber(i,j,a):

		if(i%2==0):
			return a[i+1][j]
		else:
			return a[i-1][j]

	def find(n,a):

		result=[]
		for i in range(18):
			for j in range(6):
				#print(i,j,a[i][j])
				if((a[i][j]==n)):
					result.append(seatNumber(i,j,a))
					result.append(seatType(j))
					return result

	if __name__ == '__main__':
		
		test=int(input())
		for t in range(test):
			a=[]
			value=1
			result=[]
			n=int(input())
			for i in range(18):
				s=[]
				for j in range(6):
					s.append(value)
					value+=1
				if(i%2==1):
					s=list(reversed(s))
					#print(i,s)
					a.append(s)
				else:
					a.append(s)
					#print(i,s)
			result=find(n,a)
					
			#print(a)
			print(*result)