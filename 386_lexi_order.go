package code

func lexicalOrder(n int) []int {
	res := make([]int, n)
	num := 1
	for i := 0; i < n; i++ {
		res[i] = num
		if num*10 <= n {
			num *= 10
		} else {
			for num%10 == 9 || num+1 > n { // 末尾搜索完毕
				num /= 10
			}
			num++
		}
	}
	return res
}