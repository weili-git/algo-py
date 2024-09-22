package code

func validUtf8(data []int) bool {
	for i := 0; i < len(data); i++ {
		if data[i]&128 == 0 {
			continue
		}
		n := 0
		check := 64
		for data[i]&check == check {
			n++
			check /= 2
			if n >= 4 {
				return false
			}
		}
		if n == 0 || i+n >= len(data) {
			return false
		}
		for j := 0; j < n; j++ {
			if data[i+j+1]&192 != 128 {
				return false
			}
		}
		i += n
	}
	return true
}
