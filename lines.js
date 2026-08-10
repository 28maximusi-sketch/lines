// lines.js
const yargs = require('yargs');
const { hideBin } = require('yargs/helpers');
const chalk = require('chalk');

class Puzzle {
    constructor(size, seed) {
        this.size = size;
        this.pairs = [];
        const rand = this.seededRandom(seed);
        if (size === 6) {
            this.pairs = [
                [[0,0],[5,5]], [[0,1],[4,3]], [[1,0],[3,4]],
                [[2,2],[4,4]], [[3,1],[5,3]], [[0,5],[5,0]]
            ];
        } else {
            for (let i=0; i<size/2; i++) {
                const a = [Math.floor(rand()*size), Math.floor(rand()*size)];
                const b = [Math.floor(rand()*size), Math.floor(rand()*size)];
                this.pairs.push([a,b]);
            }
        }
    }

    seededRandom(seed) {
        return function() {
            seed = (seed * 9301 + 49297) % 233280;
            return seed / 233280;
        };
    }

    display(showSolution) {
        const letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
        process.stdout.write('  ');
        for (let i=0; i<this.size; i++) process.stdout.write(`${i+1} `);
        console.log();
        for (let r=0; r<this.size; r++) {
            process.stdout.write(`${letters[r]} `);
            for (let c=0; c<this.size; c++) {
                let found = false;
                for (let idx=0; idx<this.pairs.length; idx++) {
                    const p = this.pairs[idx];
                    if ((r===p[0][0] && c===p[0][1]) || (r===p[1][0] && c===p[1][1])) {
                        process.stdout.write(chalk.green(`${idx+1} `));
                        found = true;
                        break;
                    }
                }
                if (!found) process.stdout.write('. ');
            }
            console.log();
        }
    }
}

const argv = yargs(hideBin(process.argv))
    .option('size', { type: 'number', default: 6 })
    .option('show-solution', { type: 'boolean', default: false })
    .argv;

const seed = Date.now();
const puzzle = new Puzzle(argv.size, seed);
puzzle.display(argv.showSolution);
