extern crate rabbit;

#[test]
fn basic_integration_test() {
    assert_eq!(true, true)
}

fn test_parse_input() {
    let path = "simple_input_test.txt".to_string();
    let parse_input = rabbit::parse_input(path);

    let expected_vector = vec![2, 4, 1000000000];

    assert_eq!(expected_vector, parse_input)
}

fn test_expected_output() {

}

fn test_simulate_month(){

}


