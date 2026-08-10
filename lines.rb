# lines.rb
class Puzzle
  attr_reader :size, :pairs

  def initialize(size, seed)
    @size = size
    srand(seed)
    @pairs = []
    if size == 6
      @pairs = [
        [[0,0],[5,5]], [[0,1],[4,3]], [[1,0],[3,4]],
        [[2,2],[4,4]], [[3,1],[5,3]], [[0,5],[5,0]]
      ]
    else
      (size/2).times do
        a = [rand(size), rand(size)]
        b = [rand(size), rand(size)]
        @pairs << [a,b]
      end
    end
  end

  def display(show_solution)
    letters = ('A'..'Z').to_a
    print "  "
    size.times { |i| print "#{i+1} " }
    puts
    size.times do |r|
      print "#{letters[r]} "
      size.times do |c|
        found = false
        pairs.each_with_index do |pair, idx|
          if (r == pair[0][0] && c == pair[0][1]) ||
             (r == pair[1][0] && c == pair[1][1])
            print "#{idx+1} "
            found = true
            break
          end
        end
        print ". " unless found
      end
      puts
    end
  end
end

if ARGV.include?('--size') && ARGV.index('--size')+1 < ARGV.size
  size = ARGV[ARGV.index('--size')+1].to_i
else
  size = 6
end

show_solution = ARGV.include?('--show-solution')
seed = Time.now.to_i
puzzle = Puzzle.new(size, seed)
puzzle.display(show_solution)
