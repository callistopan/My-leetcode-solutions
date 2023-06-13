use std::collections::HashMap;



impl Solution {
    pub fn equal_pairs(grid: Vec<Vec<i32>>) -> i32 {
        let mut count = 0;
        let n = grid.len();

        let mut row_counter: HashMap<Vec<i32>, i32> = HashMap::new();
        for row in &grid {
            let row_tuple: Vec<i32> = row.clone();
            *row_counter.entry(row_tuple).or_insert(0) += 1;
        }

        for c in 0..n {
            let col: Vec<i32> = (0..n).map(|i| grid[i][c]).collect();
            count += row_counter.get(&col).unwrap_or(&0);
        }

        count
    }
}
