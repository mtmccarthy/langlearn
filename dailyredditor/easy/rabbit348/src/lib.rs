use std::error::Error;
use std::fs::File;
use std::io::prelude::*;
use std::path::Path;

/*
A solution to easy problem #348 - The Rabbit Problem

Rabbits are known for their fast breeding, but how soon will they dominate the earth?

Starting with a small population of male and female rabbits we have to figure out how long it will take for them to outnumber humans 2:1.

Every month a fertile female will have 14 offspring (5 males and 9 females).

A female rabbit is fertile when it has reached the age of 4 months, they never stop being fertile.

Rabbits die at the age of 8 years (96 months).


https://www.reddit.com/r/dailyprogrammer/comments/7s888w/20180122_challenge_348_easy_the_rabbit_problem/
*/



pub fn parse_input(path: String) -> Vec<i32> {
    let path = Path::new(&path);
    let display = path.display();
    // Open in read only mode via &path

    let file = match File::open(path){
        Err(e) => panic!("Could not open file {} because {}", display, e.description()),

        Ok(file) => file
    };

    let mut cloned_file = match file.try_clone(){
        Err(e) => panic!("Could not copy file {} because {}", display, e.description()),

        Ok(cloned_file) => cloned_file
    };

    let mut input = String::new();
    match cloned_file.read_to_string(&mut input) {
        Err(e) => panic!("Could not read from file {} because {}", display, e.description()),

        Ok(input) => print!("Content {} successfully copied from {}", input, display)
    };

    return parse_string_to_list_number(input)

}

#[derive(Debug)]
struct PopulationState {
    num_males: i32,
    num_females: i32,
    current_population: i32,
    goal_population: i32,
    males: Vec<Rabbit>,
    females: Vec<Rabbit>
}
#[derive(Debug)]
struct Rabbit {
    age_in_months: i32
}

impl Rabbit {
    fn make(age: i32) -> Rabbit {
        Rabbit {
            age_in_months: age
        }
    }
}

impl Clone for Rabbit {
    fn clone(&self) -> Self {
        Rabbit::make(self.age_in_months)
    }

    fn clone_from(&mut self, source: &Self) {
        Rabbit::make(self.age_in_months)
    }
}

impl Eq for Rabbit {}
impl Eq for PopulationState {}

impl PartialEq for Rabbit {
    fn eq(&self, other: &Rabbit) -> bool {
        self.age_in_months == other.age_in_months
    }
}

impl PartialEq for PopulationState {
    fn eq(&self, other: &PopulationState) -> bool{
        (self.num_males == other.num_males) &&
            (self.num_females == other.num_females) &&
            (self.current_population == other.current_population) &&
            (self.goal_population == other.goal_population) &&
            (self.males == other.males) &&
            (self.females == other.females)
    }
}

impl PopulationState {
    fn initialize_population_state(input_vector: Vec<i32>) -> PopulationState {
        let num_males = input_vector[0];
        let num_females = input_vector[1];
        let goal_pop = input_vector[2];

        let current_pop = num_males + num_females;
        let mut male_rabbits = Vec::new();

        //All inital rabbits are two months old

        for x in 0..num_males-1 {
            male_rabbits.push(Rabbit::make(2))
        }

        let mut female_rabbits = Vec::new();

        for x in 0..num_females-1 {
            female_rabbits.push(Rabbit::make(2))
        }

        return PopulationState {
            num_males: num_males,
            num_females: num_females,
            goal_population: goal_pop,
            current_population: current_pop,
            males: male_rabbits,
            females: female_rabbits
        }
    }

    fn has_surpassed_goal(&self){
        self.current_population >= self.goal_population
    }

    fn simulate_month(state: PopulationState) -> PopulationState {
        children = PopulationState::reproduce(state);
        next_state = state.increment_ages(); // Adds one month to each rabbit. Rabbit's over 8 months die
        next_state.add_children(children);
        return next_state;
    }

    fn reproduce(state: PopulationState) -> PopulationState {

    }

    fn increment_ages(&self) -> PopulationState{

    }


}




pub fn main(){
    let path = "./tests/simple_input_test.txt".to_string();
    let input_vector = parse_input(path);

    let mut current_pop_state = PopulationState::initialize_population_state(input_vector);

    while !PopulationState::has_surpassed_goal {
        current_pop_state = PopulationState::simulate_month(current_pop_state);
    }


}


pub fn parse_string_to_list_number(line: String) -> Vec<i32> {
    let split_line = line.split(' ');
    let number_mapping = split_line.map(|num_str|
        match num_str.parse::<i32>(){
            Err(e) => panic!("Failed to parse {} to i32 because {}", num_str, e.description()),
            Ok(num) => num
        });
    let number_list: Vec<i32> = number_mapping.collect();

    return number_list
}



//Unit tests, integration tests can be found in rabbit348/test/rabbit348_tests.rs
//Unit tests, integration tests can be found in rabbit348/test/rabbit348_tests.rs
#[cfg(test)]
mod testParseInput {
    use super::*;
    #[test]
    fn it_works() {
    }
    #[test]
    fn test_parse_string_to_list_number() {
        let input_string = "1 2 10000".to_string();
        assert_eq!(vec![1,2,10000], parse_string_to_list_number(input_string))
    }
}

#[cfg(test)]
mod testDataStructures {
    use super::*;

    #[test]
    fn test_rabbit_init(){
        let expected_rabbit_age = 0;
        let rabbit = Rabbit::make(0);
        assert_eq!(expected_rabbit_age, rabbit.age_in_months)

    }
    #[test]
    fn test_pop_state_init(){
        let expected_age_of_rabbits = 2;
        let input_vector = vec![3, 2, 10];
        let males = vec![Rabbit::make(2), Rabbit::make(2), Rabbit::make(2)];
        let females = vec![Rabbit::make(2), Rabbit::make(2)];
        let expected_pop_state = PopulationState {
            num_males: 3,
            num_females: 2,
            goal_population: 10,
            current_population: 5,
            males: males,
            females: females,

        };

        assert_eq!(expected_pop_state, PopulationState::initialize_population_state(input_vector))
    }


}

#[cfg(test)]
mod testPopulationState {
    use super::*;
    #[test]
    fn test_has_surpassed_goal(){
        let example_vector = vec![2, 4, 100];
        let example_false_struct = PopulationState::initialize_population_state(input_vector);

        assert!(!example_false_struct.has_surpassed_goal());

        let another_vector = vec![1,1,0];
        let another_example = PopulationState::initialize_population_state(another_vector);
        assert!(another_example.has_surpassed_goal())
    }


    fn test_reproduce() {
        let example_vector = vec![2,2,10];
        let initial_state = PopulationState::initialize_population_state(example_vector);
        // 2 females create 10 males and 18 females
        let expected_children = vec![Rabbit::make(2); 28];

        assert_eq!(expected_children, PopulationState::reproduce(initial_state));

        let no_females_vec = vec![2, 0, 10];
        let no_females_state = PopulationState::initialize_population_state(no_females_vec);

        assert_eq!(vec![], PopulationState::reproduce(no_females_state))

    }

    fn test_increment_ages(){
        let example_vector = vec![2,2,10];
        let initial_state = PopulationState::initialize_population_state(example_vector);

        let incremented_rabbits = vec![Rabbit::make(4), 2];

        assert_eq!(incremented_rabbits, initial_state.increment_ages().males);
        assert_eq!(incremented_rabbits, initial_state.increment_ages().females);

        let too_old_rabbits = [Rabbit::make(95), Rabbit::make(93), Rabbit::make(96)];
        let too_told_state = PopulationState {
            num_males: 3,
            num_females: 3,
            current_population: 6,
            goal_population: 10,
            males: too_old_rabbits,
            females: too_old_rabbits
        };

        assert_eq!(too_old_rabbits, too_told_state.increment_ages().males);
        assert_eq!(too_old_rabbits, too_told_state.increment_ages().females)
    }

}
