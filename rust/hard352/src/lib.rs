use std::io::{self, BufRead};
use std::error::Error;
use std::fmt;
use std::fs::File;
use std::env;
use std::io::Read;

#[derive(Debug, Clone)]
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


pub fn find_square(well: Well, value: usize) -> Option<(usize, usize)> {
    for i in 0..well.width {
        for j in 0..well.height {
            if well.squares[i][j] == value {
                return Some((i, j));
            }
        }
    }
    return None
}

pub fn calculate_filling_time(well: Well) -> Option<i32> {
    let starting_square = match find_square(well.clone(), 1) {
        Some(square) => square,
        None => return None
    };

    simulate_well(well, starting_square)

}

pub fn simulate_well(well: Well, starting_square: (usize, usize)) -> Option<i32>{
    /*
    Algorithm:
        Check if path exists from source to sink if yes then done if not
        Add 1 to each node in current path - time increments by size of path
        Check for next node in path if current water level is >= node add node to path
        If next node is the sink, return current time value
    */
    let target_loc = match find_square(well.clone(), well.target) {
        Some(tl) => tl,
        None => return None
    };
    let mut current_well = well.clone();
    let mut current_path = vec![target_loc];
    let mut current_time = 0;

    while true {
        //Until we find the target location (we know it exists from pattern match above)
        if path_exists(current_well.clone(), current_path.clone(), target_loc) {
            return Some(current_time);
        }
        else if can_increase_path(current_well.clone(), current_path.clone()) {
            //Add a new node to the path, if this node is the target node it will
            //be found on the next iteration of the loop
            increase_path(&mut current_well, &mut current_path);
        }
        else {
            //Add 1 unit of water to each node in the path, if this helps increase the path
            //it will be discovered in the next iteration of the loop
            increment_water_height(&mut current_well, &mut current_path);
        }
    }

    //Loop should not break without returning a value, this is just for the compiler
    return None

}

pub fn path_exists(well: Well, current_path: Vec<(usize, usize)>, target_loc: (usize, usize)) -> bool {
    false //TODO
}

pub fn can_increase_path(well: Well, current_path: Vec<(usize, usize)>) -> bool {
    false //TODO
}

pub fn increase_path(current_well: &mut Well , current_path: &mut Vec<(usize, usize)>) -> (){
    //TODO
}

pub fn increment_water_height(current_well: &mut Well, current_path: &mut Vec<(usize, usize)>) -> () {
    //TODO
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

#[cfg(test)]
mod calculate_filling_time_tests {
    use super::*;

    #[test]
    fn test_find_starting_square() {
        let simple_input_path =
            "/mnt/c/dev/git/langlearn/rust/hard352/src/test_input/simple_input.txt";
        let expected_squares = vec![vec![1, 9, 6], vec![2, 8, 5], vec![3, 7, 4]];
        let another_expected_squares = expected_squares.clone();
        let simple_well = make_well(3, 3, expected_squares, 4);
        let another_simple_well =  simple_well.clone();
        let expected_output = Some((0, 0));
        assert_eq!(expected_output, find_square(another_simple_well, 1));
        assert_eq!(Some((2, 2)), find_square(simple_well, 4));
        let invalid_well =
            make_well(2, 2, vec![vec![6, 3], vec![2, 0]], 6);
        assert_eq!(None, find_square(invalid_well, 1))
    }
}
