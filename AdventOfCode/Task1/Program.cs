using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

var content = await File.ReadAllTextAsync("./data");

var lines = content.Split("\n").Select(x => x.Trim());
var elfs = new List<int>{0};

foreach (var line in lines)
{
    if(string.IsNullOrEmpty(line))
    {
        elfs.Add(0);
        continue;
    }

    var cals = int.Parse(line);
    elfs[^1] += cals;
}

Console.WriteLine(elfs.Max()); // 67016

var result = elfs.OrderByDescending(x => x).Take(3).Sum();
Console.WriteLine(result);
