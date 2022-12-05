using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Runtime.CompilerServices;

var content = await File.ReadAllTextAsync("./data");
var lines = content.Split("\n").Select(x => x.Trim()).ToArray();
var doubledItems = new List<char>();

for (var i = 0; i < lines.Length; i++)
{
    var line = lines[i];
    var compartmentSize = line.Length / 2;
    if (compartmentSize * 2 != line.Length) throw new Exception($"Line length it odd {line.Length}");

    var compartment1 = line[..compartmentSize];
    var compartment2 = line.Substring(compartmentSize, compartmentSize);

    if (compartment1.Length != compartment2.Length)
        throw new Exception($"Compartments not equal: {compartment1} - {compartment2}");
    
    char doubledItemsInRow = default;
    for (var j = 0; j < compartmentSize; j++)
    {
        if (compartment2.Any(x => x == compartment1[j]))
        {
            if(compartment1[j] == doubledItemsInRow) continue;
            if (doubledItemsInRow != default) throw new Exception($"found more then 1 for {i}");
            doubledItemsInRow = compartment1[j];
        }
    }

    if (doubledItemsInRow == default) throw new Exception($"not found for {i}");
    doubledItems.Add(doubledItemsInRow);
}

Console.WriteLine(doubledItems.Count);
var sum = 0;
foreach (var item in doubledItems)
{
    if (!char.IsLetter(item)) new Exception("not letter");
    if (char.IsLower(item))
        sum = sum + item - 96;
    else
        sum = sum + item - 64 + 26;
}
Console.WriteLine(sum);

var badges = new List<char>();

for (var i = 0; i < lines.Length; i += 3)
{
    var line1 = lines[i];
    var line2 = lines[i + 1];
    var line3 = lines[i + 2];

    for (var j = 0; j < line1.Length; j++)
    {
        if (line2.Any(x => x == line1[j]) && line3.Any(x => x == line1[j]))
        {
            badges.Add(line1[j]);
            break;
        }
    }
    
}

sum = 0;
foreach (var item in badges)
{
    if (!char.IsLetter(item)) new Exception("not letter");
    if (char.IsLower(item))
        sum = sum + item - 96;
    else
        sum = sum + item - 64 + 26;
}
Console.WriteLine(sum);