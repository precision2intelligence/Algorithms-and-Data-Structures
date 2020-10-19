// Time: O(N^2)
// Space: O(n)
/*
时间复杂度：排序使用了O(NlogN) 的时间，每个人插入到输出队列中需要O(k) 的时间，其中 k 是当前输出队列的元素个数。总共的时间复杂度为
N−1
∑
k=0 k) = O(N^2)。
空间复杂度：O(N)，输出队列使用的空间。
*/

// 题解中golang的很好，有图示
// 学习sortSlice的用法以及copy只复制（目标，源）中最短的

/*
Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k), where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.

Note:
The number of people is less than 1,100.


Example

Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
*/
import (
	"sort"
)

func reconstructQueue(people [][]int) [][]int {
	// 按照身高h降序排序，身高一样按照k升序排序
	sort.Slice(people, func(i, j int) bool {
		return (people[i][0] > people[j][0]) || (people[i][0] == people[j][0] && people[i][1] < people[j][1])
	})

	// 把index之后的已排序序列后移，index位置插入现有元素
	for i, p := range people {
		copy(people[p[1]+1:i+1], people[p[1]:i+1])
		people[p[1]] = p
	}
	return people
}

