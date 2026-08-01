#[derive(Debug)]
struct Solution;

impl Solution {
    pub fn search_range(nums: Vec<i32>, target: i32) -> Vec<i32> {
        if nums.len() == 0 {
            return vec![-1_i32, -1_i32];
        }
        let mut low: isize = 0;
        let mut high: isize = (nums.len() - 1) as isize;
        let mut leftmost: isize = -1;
        let mut mid: isize = 0;
        // for leftmost target range
        while low <= high {
            mid = (low + high) / 2;
            if nums[mid as usize] == target {
                leftmost = mid;
                high = mid - 1;
                continue;
            }
            if nums[mid as usize] < target {
                low = mid + 1;
                continue;
            }
            high = mid - 1;
        }
        low = 0;
        high = (nums.len() - 1) as isize;
        let mut rightmost = -1;
        // for rightmost target range
        while low <= high {
            mid = (low + high) / 2;
            if nums[mid as usize] == target {
                rightmost = mid;
                low = mid + 1;
                continue;
            }
            if nums[mid as usize] < target {
                low = mid + 1;
                continue;
            }
            high = mid - 1;
        }
        vec![leftmost as i32, rightmost as i32]
    }
}

fn main() {
    println!("{:?}", Solution::search_range(vec![5, 7, 7, 8, 8, 10], 8));
    println!("{:?}", Solution::search_range(vec![5, 7, 7, 8, 8, 10], 6));
    println!("{:?}", Solution::search_range(vec![], 0));
}
