impl Solution {
    pub fn min_operations(nums: Vec<i32>, queries: Vec<i32>) -> Vec<i64> {

        let mut nums = nums;
        nums.sort();

        let n = nums.len();
        let mut ans = Vec::new();
        let mut prefix = vec![0i64; n + 1];
        for i in 0..n {
            prefix[i + 1] = prefix[i] + nums[i] as i64;
        }

        for x in queries {
            let i = match nums.binary_search(&x) {
                Ok(i) => i,
                Err(i) => i,
            };

            let result = (x as i64) * (2 * i as i64 - n as i64) + prefix[n] - 2 * prefix[i];
            ans.push(result);
        }

        ans
    }
}