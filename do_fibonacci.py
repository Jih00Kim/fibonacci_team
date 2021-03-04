def do_fibo(num):
	answer = [0,1]
	for i in range(2,num+1):
		answer.append(answer[i-1]+answer[i-2])
	#print(answer)
	#print(i)
	return answer[-1]
if __name__=='__main__':
	user_num = int(input('How many ppl are you?: '))
	result = do_fibo(user_num)
	print(result)
