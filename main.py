arr1 = [0,1550,3100,4650,6200,7200,7750,8000,8000,8000]
arr2 = [0,1100,2200,3300,4400,5500,6500,7200,7600,7600]
arr3 = [0,2100,4200,6300,7500,7700,7800,7800,7800,7800]

# Function to calculate the overall grade
def calc_grade(x,y,z):
	if(x==y and y==z and x==0):
		return 0
	return ((0.9*x) + (1.4*y) + (1.2*z))/(x+y+z)

count = 0
# list to store the tons supplied 
tons = []
# list to store the different rucks combinations
trucks = []
# list to store the total cost 
cost = []

# Solution Code
for i in range(0,len(arr1)):
	for j in range(0,len(arr2)):
		for k in range(0,len(arr3)):
			grade = calc_grade(arr1[i],arr2[j],arr3[k])
			tot_tons = arr1[i]+arr2[j]+arr3[k]

			# Constraints Applied i.e (tons >=15000) and 1.15 <= grade <=1.25
			if tot_tons >= 15000 and grade>=1.15 and grade <=1.25 :
				tons.append(tot_tons)
				total = 3*1000
				if(i==0):
					total = total - 1000
				if(j==0):
					total = total - 1000
				if(k==0):
					total = total - 1000
				total = total + (i+j+k)*720
				cost.append(total)
				trucks.append([i,j,k])
				count = count + 1



j = 0
k = 99999999
nos= 0
for i in range(0,len(cost)):
	p = trucks[i][0] + trucks[i][1] + trucks[i][2]
	# Constraint Applied for minimum cost and minimum trucks required
	if(k>=cost[i]) and nos<=p :
		j = i
		k = cost[i]
		nos = p


print("Total Cost: ")
print(cost[j])

print("Total Trucks required at each Shovels: ")
print(trucks[j])

print("Total tons supplied: ")
print(tons[j])

# Answers :
# Total Cots: 10200
# Total Turcks required at each shovels: [3, 4, 3]
# Total tons supp;ied: 15350
