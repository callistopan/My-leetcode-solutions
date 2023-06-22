use std::collections::HashMap;
impl Solution {
    pub fn max_number_of_balloons(text: String) -> i32 {
       let mut counts: HashMap<char, i32> = HashMap::new();
        let mut result = i32::max_value();

        for c in text.chars() {
            *counts.entry(c).or_insert(0) += 1;
        }

        let balloon_count: HashMap<char, i32> = [
            ('b', 1),
            ('a', 1),
            ('l', 2),
            ('o', 2),
            ('n', 1),
        ]
        .iter()
        .cloned()
        .collect();

        for (c, count) in balloon_count.iter() {
            if let Some(text_count) = counts.get(c) {
                result = result.min(*text_count / count);
            } else {
                result = 0; // One of the required characters is missing, so no balloons can be formed
                break;
            }
        }

        result 
    }
}