// lines.rs
use clap::Parser;
use rand::Rng;
use std::collections::HashMap;

#[derive(Parser)]
#[command(name = "lines")]
struct Args {
    #[arg(short, long, default_value_t = 6)]
    size: usize,
    #[arg(long)]
    show_solution: bool,
    #[arg(long)]
    date: Option<String>,
}

struct Puzzle {
    size: usize,
    pairs: Vec<((usize, usize), (usize, usize))>,
}

impl Puzzle {
    fn new(size: usize, seed: u64) -> Self {
        let mut rng = rand::thread_rng();
        let mut pairs = Vec::new();
        if size == 6 {
            pairs = vec![
                ((0,0), (5,5)), ((0,1), (4,3)), ((1,0), (3,4)),
                ((2,2), (4,4)), ((3,1), (5,3)), ((0,5), (5,0)),
            ];
        } else {
            for _ in 0..size/2 {
                let a = (rng.gen_range(0..size), rng.gen_range(0..size));
                let b = (rng.gen_range(0..size), rng.gen_range(0..size));
                pairs.push((a, b));
            }
        }
        Puzzle { size, pairs }
    }

    fn display(&self, _show_solution: bool) {
        let letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        print!("  ");
        for i in 0..self.size {
            print!("{} ", i+1);
        }
        println!();
        for r in 0..self.size {
            print!("{} ", letters.chars().nth(r).unwrap());
            for c in 0..self.size {
                let mut found = false;
                for (idx, (a, b)) in self.pairs.iter().enumerate() {
                    if (r, c) == *a || (r, c) == *b {
                        print!("{} ", idx+1);
                        found = true;
                        break;
                    }
                }
                if !found {
                    print!(". ");
                }
            }
            println!();
        }
    }
}

fn main() {
    let args = Args::parse();
    let seed = match args.date {
        Some(d) => d.chars().fold(0, |acc, c| acc ^ (c as u64)),
        None => std::time::SystemTime::now()
                .duration_since(std::time::UNIX_EPOCH)
                .unwrap()
                .as_secs(),
    };
    let puzzle = Puzzle::new(args.size, seed);
    puzzle.display(args.show_solution);
}
