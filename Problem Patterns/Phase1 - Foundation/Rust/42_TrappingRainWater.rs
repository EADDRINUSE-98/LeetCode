#[derive(Debug)]
struct Solution;

impl Solution {
    pub fn trap(height: Vec<i32>) -> i32 {
        if height.len() == 0 {
            return 0;
        }
        let mut current_max_right = 0;
        let mut current_max_left = 0;
        let mut right_height_record: Vec<i32> = Vec::new();
        let mut left_height_record: Vec<i32> = Vec::new();
        let mut total_trapped_water = 0;

        // Get left wall height value for each element.
        for i in 0..height.len() {
            left_height_record.push(current_max_left);
            current_max_left = current_max_left.max(height[i]);
        }

        // Get right wall height value for each element
        for i in (0..=height.len() - 1).rev() {
            right_height_record.push(current_max_right);
            current_max_right = current_max_right.max(height[i]);
        }

        right_height_record = right_height_record.into_iter().rev().collect();

        // Compute the total trapped water
        for i in 0..height.len() {
            if right_height_record[i].min(left_height_record[i]) <= height[i] {
                total_trapped_water += 0;
                continue;
            }
            total_trapped_water += right_height_record[i].min(left_height_record[i]) - height[i];
        }
        total_trapped_water
    }
}

fn main() {
    println!(
        "{}",
        Solution::trap(vec![0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
    );
    println!("{}", Solution::trap(vec![4, 2, 0, 3, 2, 5]));
    println!("{}", Solution::trap(vec![]));
}
