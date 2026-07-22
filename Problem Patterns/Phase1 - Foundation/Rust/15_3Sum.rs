#[derive(Debug)]
struct Solution;

impl Solution {
    pub fn three_sum(nums: Vec<i32>) -> Vec<Vec<i32>> {
        let mut nums: Vec<i32> = nums;
        nums.sort_unstable();
        let mut ptr1: usize;
        let mut three_sum_combinations: Vec<Vec<i32>> = vec![];
        let mut ptr2;
        let mut ptr3;
        for ptr1 in 0..(nums.len() - 2) {
            ptr2 = ptr1 + 1;
            ptr3 = nums.len() - 1;
            if ptr1 > 0 && nums[ptr1] == nums[ptr1 - 1] {
                continue;
            }
            while ptr3 > ptr2 {
                while ptr3 > ptr2 && nums[ptr1] + nums[ptr2] + nums[ptr3] != 0 {
                    while ptr3 > ptr2 && nums[ptr1] + nums[ptr2] + nums[ptr3] < 0 {
                        ptr2 += 1;
                    }
                    while ptr3 > ptr2 && nums[ptr1] + nums[ptr2] + nums[ptr3] > 0 {
                        ptr3 -= 1;
                    }
                }
                if ptr3 > ptr2 && nums[ptr1] + nums[ptr2] + nums[ptr3] == 0 {
                    three_sum_combinations.push(vec![nums[ptr1], nums[ptr2], nums[ptr3]]);
                }
                ptr2 += 1;
                while ptr3 > ptr2 && nums[ptr2] == nums[ptr2 - 1] {
                    ptr2 += 1;
                }
                ptr3 -= 1;
                while ptr3 > ptr2 && nums[ptr3] == nums[ptr3 + 1] {
                    ptr3 -= 1;
                }
            }
        }
        three_sum_combinations
    }
}

fn main() {
    println!("{:?}", Solution::three_sum(vec![-1, 0, 1, 2, -1, -4]));
    println!("{:?}", Solution::three_sum(vec![0, 1, 1]));
    println!("{:?}", Solution::three_sum(vec![0, 0, 0]));
}
