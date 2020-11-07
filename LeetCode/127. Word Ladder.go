func idxOf(word string, wordList []string) int {
	for i, s := range wordList {
		if word == s {
			return i
		}
	}
	return -1
}

func hasOneDiff(word1, word2 string) bool {
	count := 0
	for i := 0; i < len(word1); i++ {
		if word1[i] == word2[i] {
			continue
		} else {
			count++
			if count > 1 {
				return false
			}
		}
	}
	if count == 1 {
		return true
	}
	return false
}

func ladderLength(beginWord string, endWord string, wordList []string) int {
	length := 0
	startQueqe := []string{beginWord}
	endQueqe := []string{endWord}
	startUsed := make([]bool, len(wordList))
	endUsed := make([]bool, len(wordList))
	if i := idxOf(endWord, wordList); i == -1 {
		return 0
	} else {
		endUsed[i] = true
	}

	for len(startQueqe) > 0 {
		length++
		l := len(startQueqe) // 这里易错，不能i<len(wordList)，因为后面长度增加了
		for i := 0; i < l; i++ {
			for j, w := range wordList {
				if !startUsed[j] && hasOneDiff(startQueqe[i], w) {
					startUsed[j] = true
					startQueqe = append(startQueqe, w)
					// length++ 这里不能加，否则每个差一个字母的都会引起length增加
					if endUsed[j] {
						return length + 1
					}
				}
			}
		}
		startQueqe = startQueqe[l:]
		startQueqe, endQueqe = endQueqe, startQueqe
		startUsed, endUsed = endUsed, startUsed
	}
	return 0
}