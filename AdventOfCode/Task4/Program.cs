using System;
using System.IO;
using System.Linq;

var content = await File.ReadAllTextAsync("./data");

var lines = content.Split("\n").Select(x => x.Trim()).ToArray();

var counter = 0;

for (var i = 0; i < lines.Length; i++)
{
    var line = lines[i];
    var numbers = line.Split(',', '-').Select(int.Parse).ToArray();
    
    if (numbers.Length != 4) throw new Exception();

    if (numbers[0] <= numbers[2] && numbers[1] >= numbers[3] ||
        numbers[2] <= numbers[0] && numbers[3] >= numbers[1])
    {
        counter++;
    }
}

Console.WriteLine(counter);

counter = 0;
for (var i = 0; i < lines.Length; i++)
{
    var line = lines[i];
    var numbers = line.Split(',', '-').Select(int.Parse).ToArray();
    
    if (numbers.Length != 4) throw new Exception();

    if (numbers[2] >= numbers[0] && numbers[2] <= numbers[1] ||
        numbers[3] >= numbers[0] && numbers[3] <= numbers[1] ||
        numbers[0] >= numbers[2] && numbers[0] <= numbers[3] ||
        numbers[1] >= numbers[2] && numbers[1] <= numbers[3]
        )
    {
        counter++;
    }
}

Console.WriteLine(counter);