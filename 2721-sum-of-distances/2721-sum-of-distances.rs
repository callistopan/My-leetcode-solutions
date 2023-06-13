use std::collections::HashMap;
impl Solution {
    pub fn distance(nums: Vec<i32>) -> Vec<i64> {
        let n = nums.len();
        let mut res = vec![0; n];
        let mut d: HashMap<i32, Vec<usize>> = HashMap::new();

        for (i, num) in nums.iter().enumerate() {
            d.entry(*num).or_insert(Vec::new()).push(i);
        }

        for (_, indexes) in d {
            let total_sum: i64 = indexes.iter().map(|&index| index as i64).sum();
            let mut pre_sum: i64 = 0;

            for (i, &index) in indexes.iter().enumerate() {
                let post_sum = total_sum - pre_sum - index as i64;

                // i - p1 + i - p2 .....
                res[index] += (index as i64) * (i as i64); // pre sum all i s
                res[index] -= pre_sum; // subtract all the previous indexes

                // a1 - i + a2 - i + ...
                res[index] -= (index as i64) * ((indexes.len() - i - 1) as i64); // pre sum all i s
                res[index] += post_sum;

                pre_sum += index as i64;
            }
        }

        res
    }
}