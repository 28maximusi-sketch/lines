// lines.go
package main

import (
	"flag"
	"fmt"
	"math/rand"
	"time"
)

type Puzzle struct {
	size  int
	pairs [][2][2]int
}

func NewPuzzle(size int, seed int64) *Puzzle {
	rand.Seed(seed)
	return &Puzzle{size: size}
}

func (p *Puzzle) generate() {
	// Простая генерация для демонстрации
	if p.size == 6 {
		p.pairs = [][2][2]int{
			{{0,0},{5,5}}, {{0,1},{4,3}}, {{1,0},{3,4}},
			{{2,2},{4,4}}, {{3,1},{5,3}}, {{0,5},{5,0}},
		}
	} else {
		// Случайные пары (не гарантируют решение)
		p.pairs = make([][2][2]int, p.size/2)
		for i := range p.pairs {
			p.pairs[i] = [2][2]int{
				{rand.Intn(p.size), rand.Intn(p.size)},
				{rand.Intn(p.size), rand.Intn(p.size)},
			}
		}
	}
}

func (p *Puzzle) display(showSolution bool) {
	letters := "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	fmt.Print("  ")
	for i := 0; i < p.size; i++ {
		fmt.Printf("%d ", i+1)
	}
	fmt.Println()
	for r := 0; r < p.size; r++ {
		fmt.Printf("%c ", letters[r])
		for c := 0; c < p.size; c++ {
			found := false
			for idx, pair := range p.pairs {
				if (r == pair[0][0] && c == pair[0][1]) ||
				   (r == pair[1][0] && c == pair[1][1]) {
					fmt.Printf("%d ", idx+1)
					found = true
					break
				}
			}
			if !found {
				fmt.Print(". ")
			}
		}
		fmt.Println()
	}
}

func main() {
	size := flag.Int("size", 6, "Размер поля")
	showSolution := flag.Bool("show-solution", false, "Показать решение")
	flag.Parse()

	seed := time.Now().UnixNano() // для ежедневности можно использовать день
	puzzle := NewPuzzle(*size, seed)
	puzzle.generate()
	puzzle.display(*showSolution)
}
