use std::convert::TryInto;

#[derive(Debug)]
struct Solution;

impl Solution {
    pub fn search(nums: Vec<i32>, target: i32) -> i32 {
        if nums.len() == 1 {
            if nums[0] == target {
                return 0;
            } else {
                return -1;
            }
        }
        let mut low = 0;
        let mut high = nums.len() - 1;
        let mut mid;
        while low <= high {
            mid = (low + high) / 2;
            if nums[mid] == target {
                return mid.try_into().unwrap();
            }
            if nums[mid] < target {
                low = mid + 1;
                continue;
            }
            if mid == 0 {
                break;
            }
            high = mid - 1;
        }
        -1
    }
}

fn main() {
    println!("{}", Solution::search(vec![-1, 0, 3, 5, 9, 12], 9));
    println!("{}", Solution::search(vec![-1, 0, 3, 5, 9, 12], 2));
    println!("{}", Solution::search(vec![1], 1));
    println!("{}", Solution::search(vec![1], 2));
    println!("{}", Solution::search(vec![1, 100], 100));
    println!("{}", Solution::search(vec![1, 100], 1));
    println!("{}", Solution::search(vec![1, 100], 2));
    println!("{}", Solution::search(vec![5], -5));
    println!("{}", Solution::search(vec![2, 5], 0));
}
