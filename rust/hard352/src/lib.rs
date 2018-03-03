use std::io::{self, BufRead};
use std::error::Error;
use std::fmt;
use std::fs::File;
use std::env;
use std::io::Read;

#[derive(Debug)]
pub struct Well {
    width: usize,
    height: usize,
    squares: Vec<Vec<usize>>,
    target: usize
}

impl PartialEq for Well {
    fn eq(&self, other: &Well) -> bool {
        self.width == other.width &&
            self.height == other.height &&
            self.squares == other.squares &&
            self.target == other.target
    }
}

pub fn make_well(width: usize, height: usize, squares: Vec<Vec<usize>>, target: usize) -> Well {
    Well {
        width, height, squares, target
    }
}


pub fn get_file_str(path : &str) -> Result<String, String>{
    let mut file = File::open(path).expect("Could not open file");
    let mut buffer = String::new();
    match file.read_to_string(&mut buffer) {
        Ok(_) => Ok(buffer),
        Err(e) => Err("Could not copy contents of file to buffer".to_owned())
    }
}

pub fn parse_input(path: &str) -> Result<Well, String> {
    let file_str = match get_file_str(path) {
        Ok(val) => val,
        Err(msg) => return Err("Failed to retrieve file".to_owned())
    };
    let line_vec: Vec<&str> = file_str.split("\n").collect();
    let dimensions = line_vec[0];
    let width_height : Vec<&str> = dimensions.split(" ").collect();
    println!("{:?}", width_height);
    let width = width_height[0].trim_right().parse::<usize>().unwrap();
    //Trim in order to remove carriage returns if on Windows machine
    let height = width_height[1].trim_right().parse::<usize>().unwrap();

    let mut squares = Vec::new();

    for i in 1..height + 1{
        let mut row = Vec::new();
        let line_nums : Vec<&str>= line_vec[i].split(" ").collect();
        for i in 1..width + 1{
            let num_str : &str = line_nums[i - 1].trim_right();
            let num : usize = num_str.parse::<usize>().unwrap();
            row.push(num);
        }
        squares.push(row);
    }

    let target_str = line_vec[line_vec.len() - 1]; //Last index
    let target = target_str.parse::<usize>().unwrap();

    Ok(make_well(
        width,
        height,
        squares,
        target
    ))

}

#[cfg(test)]
mod parse_input_tests {
    use super::*;

    #[test]
    fn parse_input() {

        let simple_input_path =
            "/mnt/c/dev/git/langlearn/rust/hard352/src/test_input/simple_input.txt";
        let expected_squares = vec![vec![1, 9, 6], vec![2, 8, 5], vec![3, 7, 4]];
        let expected_output = Ok(make_well(3, 3, expected_squares, 4));
        assert_eq!(expected_output, super::parse_input(simple_input_path));
    }

    #[test]
    fn get_file_str() {
        let simple_input_path =
            "/mnt/c/dev/git/langlearn/rust/hard352/src/test_input/simple_input.txt";
        //let expected_output = Ok("3 3\n1 9 6\n2 8 6\n3 7 4\n4");
        let actual_output = super::get_file_str(simple_input_path);
        assert_eq!(true, actual_output.is_ok())
    }
}
