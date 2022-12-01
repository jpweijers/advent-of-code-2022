use std::cmp;
use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn main() {
    if let Ok(lines) = read_lines("./input.txt") {
        let mut max = 0;
        let mut _subtotal = 0;
        let mut totals = Vec::new();
        for line in lines {
            if let Ok(cal) = line {
                if cal == "" {
                    max = cmp::max(max, _subtotal);
                    totals.push(_subtotal);
                    _subtotal = 0;
                } else {
                    _subtotal += cal.parse::<i32>().unwrap();
                }
            }
        }
        println!("Solution part 1: {}", max);
        totals.sort();
        let top3 = &totals[totals.len() - 3..totals.len()];
        println!("{:?}", top3.iter().sum::<i32>());
    }
}

fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where
    P: AsRef<Path>,
{
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}
