// Lines.java
import java.util.*;

public class Lines {
    static class Puzzle {
        int size;
        List<int[][]> pairs; // каждая пара: [ [r1,c1], [r2,c2] ]
        Puzzle(int size, long seed) {
            this.size = size;
            Random rand = new Random(seed);
            pairs = new ArrayList<>();
            if (size == 6) {
                int[][][] data = {
                    {{0,0},{5,5}}, {{0,1},{4,3}}, {{1,0},{3,4}},
                    {{2,2},{4,4}}, {{3,1},{5,3}}, {{0,5},{5,0}}
                };
                for (int[][] d : data) pairs.add(d);
            } else {
                for (int i=0; i<size/2; ++i) {
                    int[][] p = {
                        {rand.nextInt(size), rand.nextInt(size)},
                        {rand.nextInt(size), rand.nextInt(size)}
                    };
                    pairs.add(p);
                }
            }
        }
        void display(boolean showSolution) {
            String letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
            System.out.print("  ");
            for (int i=0; i<size; ++i) System.out.print((i+1)+" ");
            System.out.println();
            for (int r=0; r<size; ++r) {
                System.out.print(letters.charAt(r)+" ");
                for (int c=0; c<size; ++c) {
                    boolean found = false;
                    for (int idx=0; idx<pairs.size(); ++idx) {
                        int[][] p = pairs.get(idx);
                        if ((r==p[0][0] && c==p[0][1]) ||
                            (r==p[1][0] && c==p[1][1])) {
                            System.out.print((idx+1)+" ");
                            found = true;
                            break;
                        }
                    }
                    if (!found) System.out.print(". ");
                }
                System.out.println();
            }
        }
    }

    public static void main(String[] args) {
        int size = 6;
        boolean showSolution = false;
        for (int i=0; i<args.length; ++i) {
            if (args[i].equals("--size") && i+1<args.length) {
                size = Integer.parseInt(args[++i]);
            } else if (args[i].equals("--show-solution")) {
                showSolution = true;
            }
        }
        long seed = System.currentTimeMillis();
        Puzzle p = new Puzzle(size, seed);
        p.display(showSolution);
    }
}
