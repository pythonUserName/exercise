# coding:UTF-8

# list = [1, 2, 3, 4]
# list_result = []
# for i in list:
# 	for j in list:
# 		for k in list:
# 			if(i != j) and (i != k) and (j != k):
# 				list_result.append(i*100+j*10+k)
# print "总数：", len(list_result)
# print "分别是：", list_result


list_result = []
for i in range(1, 5):
	for j in range(1, 5):
		for k in range(1, 5):
			if(i != j) and (i != k) and (j != k):
				list_result.append(i*100+j*10+k)
print "总数：", len(list_result)
print "这些数字分别是：", list_result