#[derive(Debug)]
pub struct kolakoski {
    current_output: Vec<usize>,
    iteration: usize,
    limit: usize
}

impl kolakoski {

    pub fn kolakoski(&mut self) -> Vec<usize>{
        if self.has_calculated_enough() {
            return self.current_output.clone()
        }
        else {
            return self._kolakoski()
        }
    }

    fn _kolakoski(&mut self) -> Vec<usize>{
        if self.iteration == 0 {
            self.current_output.push(1);
        }
        else if self.iteration == 1 {
            self.current_output.push(2);
            self.current_output.push(2);
        }
        else {
            //General Case
            println!("{:?}", self);
            let ith = self.current_output[self.iteration];
            println!("ith = {}", ith);
            if (self.iteration + 1) % 2 == 1 {
                // Add i copies of 1 to the current output
                for i in 0 .. ith {
                    self.current_output.push(1);
                }
            }
                else {
                    // Add i copies of 2 to the current output
                    for i in 0 .. ith {
                        self.current_output.push(2);
                    }
                }

        }
        self.iteration += 1;
        return self.kolakoski()
    }

    fn has_calculated_enough(&mut self) -> bool{
        if self.current_output.len() >= self.limit {
            self.current_output = take(self.current_output.clone(), self.limit);
            return true;
        }
        else {
            return false;
        }
    }

}


pub fn calculate_analysis(seq: Vec<usize>) -> (usize, usize){
    let mut ones = 0;
    let mut twos = 0;

    for num in seq {
        if num == 1 {
            ones += 1;
        }
        else if num == 2 {
            twos += 1;
        }
    }

    return (ones, twos)

}


pub fn take(x: Vec<usize>, limit: usize) -> Vec<usize>{
    let mut limited_output: Vec<usize> = vec![];
    for i in 0 .. limit {
        limited_output.push(x[i].clone());
    }

    return limited_output
}


pub fn make_k(limit: usize) -> kolakoski{
    kolakoski {
        current_output: vec![],
        limit,
        iteration: 0
    }
}

#[cfg(test)]
mod tests {

    use kolakoski;
    use make_k;
    use calculate_analysis;
    #[test]
    fn it_works() {
        assert_eq!(2 + 2, 4);
    }

    #[test]
    fn test_kolaski() {
        let mut expected_output = vec![1, 2, 2, 1, 1, 2, 1, 2, 2, 1];

        let mut k = kolakoski {
            current_output: vec![],
            limit: 10,
            iteration: 0
        };

        assert_eq!(10, expected_output.len());
        assert_eq!(expected_output, k.kolakoski())
    }

    fn test_ratio_analysis() {

        let mut k1 = make_k(10);
        let mut k2 = make_k(100);
        let mut k3 = make_k(1000);

        assert_eq!((5, 5), calculate_analysis(k1.kolakoski()));
        assert_eq!((49, 51), calculate_analysis(k2.kolakoski()));
        assert_eq!((502, 498), calculate_analysis(k3.kolakoski()));
    }
}


