import sys

matrix = [[0 for x in range(100)] for y in range(100)]

def solve(field, n, m):
	res_string = "Field #{}:\n".format(field)
	for i in range(n):
		line = ""
		for j in range(m):
			if matrix[i][j] == 1:
				line += '*'
				continue

			res = 0
			if j > 0 and i > 0 and matrix[i-1][j-1] == 1:
				res += 1
			if j > 0 and matrix[i][j-1] == 1:
				res += 1
			if j > 0 and i < n and matrix[i+1][j-1] == 1:
				res += 1
			if i > 0 and matrix[i-1][j] == 1:
				res += 1
			if i < n and matrix[i+1][j] == 1:
				res += 1
			if j < m and i > 0 and matrix [i-1][j+1] == 1:
				res += 1
			if j < m and matrix[i][j+1] == 1:
				res += 1
			if j < m and i < n and matrix[i+1][j+1] == 1:
				res += 1
			line += str(res)

		if i != n-1:
			res_string += str(line) + "\n"
		else:
			res_string += str(line)
	return res_string

def main():
	field = 1
	k = -1
	res = ""
	for line in sys.stdin:
		if k == -1:
			(n, m) = [int(x) for x in line.split()]
			k += 1
			if n == m == 0:
				break

			# Space between fields
			if field != 1:
				res += "\n\n"
		else:
			for i, character in enumerate(line):
				if character == "*":
					matrix[k][i] = 1
			k += 1
			if k == n:
				res += solve(field,n,m)
				field += 1
				k = -1
	return res

if __name__ == '__main__':
	main()