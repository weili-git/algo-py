package code

func findRightInterval(intervals [][]int) []int {
	n := len(intervals)
	if n == 1 {
		if intervals[0][0] == intervals[0][1] {
			return []int{0}
		} else {
			return []int{-1}
		}
	}
	res := make([]int, n)
	for i := 0; i < n; i++ {
		res[i] = -1
		for j := 0; j < n; j++ {
			if intervals[j][0] >= intervals[i][1] {
				if res[i] == -1 {
					res[i] = j
				} else {
					if intervals[j][0] < intervals[res[i]][0] {
						res[i] = j
					}
				}
			}
		}
	}
	return res
}

// 二分法优化 O(NlogN)
