// lines.cs
using System;
using System.Collections.Generic;

class Puzzle
{
    public int Size;
    public List<(int,int,int,int)> Pairs; // (r1,c1,r2,c2)

    public Puzzle(int size, int seed)
    {
        Size = size;
        var rand = new Random(seed);
        Pairs = new List<(int,int,int,int)>();
        if (size == 6)
        {
            var data = new (int,int,int,int)[]
            {
                (0,0,5,5), (0,1,4,3), (1,0,3,4),
                (2,2,4,4), (3,1,5,3), (0,5,5,0)
            };
            Pairs.AddRange(data);
        }
        else
        {
            for (int i=0; i<size/2; i++)
            {
                int r1=rand.Next(size), c1=rand.Next(size);
                int r2=rand.Next(size), c2=rand.Next(size);
                Pairs.Add((r1,c1,r2,c2));
            }
        }
    }

    public void Display(bool showSolution)
    {
        string letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        Console.Write("  ");
        for (int i=0; i<Size; i++) Console.Write((i+1)+" ");
        Console.WriteLine();
        for (int r=0; r<Size; r++)
        {
            Console.Write(letters[r]+" ");
            for (int c=0; c<Size; c++)
            {
                bool found = false;
                for (int idx=0; idx<Pairs.Count; idx++)
                {
                    var p = Pairs[idx];
                    if ((r==p.Item1 && c==p.Item2) || (r==p.Item3 && c==p.Item4))
                    {
                        Console.Write((idx+1)+" ");
                        found = true;
                        break;
                    }
                }
                if (!found) Console.Write(". ");
            }
            Console.WriteLine();
        }
    }
}

class Program
{
    static void Main(string[] args)
    {
        int size = 6;
        bool showSolution = false;
        for (int i=0; i<args.Length; i++)
        {
            if (args[i] == "--size" && i+1 < args.Length)
                size = int.Parse(args[++i]);
            else if (args[i] == "--show-solution")
                showSolution = true;
        }
        int seed = (int)DateTime.Now.Ticks;
        var p = new Puzzle(size, seed);
        p.Display(showSolution);
    }
}
