using System;
using System.IO;
using System.Linq;
using System.Text.RegularExpressions;

var lines = File.ReadLines("data").ToArray();
var strengths = new Point[6];
var i = 0;

for (i = 0; i < strengths.Length; i++)
{
    strengths[i] = new Point()
    {
        X = 20 + 40 * i,
        Y = 0
    };
}

var counter = 1;
var value = 1;

for (i = 0; i < lines.Length; i++)
{
    if (lines[i].StartsWith("addx"))
    {
        CheckStrength();

        var amount = int.Parse(Regex.Match(lines[i], "-?\\d+").Value);
        value += amount;
        CheckStrength();
    }
    else
    {
        CheckStrength();
    }
}


// for (i = 0; i < strengths.Length; i++)
// {
//     Console.WriteLine($"{strengths[i].X}:{strengths[i].Y}");
// }

Console.WriteLine(strengths.Sum(x => x.Y));

void CheckStrength()
{
    counter++;
    if (strengths.Any(x => x.X == counter))
    {
        var element = strengths.First(x => x.X == counter);
        element.Y = value * counter;
        Console.WriteLine($"{i}  -  {element.X}:{element.Y}  -  {value}");
    }
}

var crt = new char[40][];
for (var x = 0; x < crt.Length; x++)
{
    crt[x] = new []
    {
        '.','.','.','.','.','.'
    };
}

var pixel = new Point { X = 0, Y = 0 };
var sprite = 1;

for (i = 0; i < lines.Length; i++)
{
    if (lines[i].StartsWith("addx"))
    {
        if (Math.Abs(sprite - pixel.X) <= 1)
        {
            crt[pixel.X][pixel.Y] = '#';
        }
        pixel.X++;
        if (pixel.X > 39)
        {
            pixel.X = 0;
            pixel.Y++;
        }

        if (Math.Abs(sprite - pixel.X) <= 1)
        {
            crt[pixel.X][pixel.Y] = '#';
        }
        pixel.X++;
        if (pixel.X > 39)
        {
            pixel.X = 0;
            pixel.Y++;
        }
        var amount = int.Parse(Regex.Match(lines[i], "-?\\d+").Value);
        sprite += amount;
    }
    else
    {
        if (Math.Abs(sprite - pixel.X) <= 1)
        {
            crt[pixel.X][pixel.Y] = '#';
        }
        pixel.X++;
        if (pixel.X > 39)
        {
            pixel.X = 0;
            pixel.Y++;
        }
    }
}

for (var x = 0; x < 6; x++)
{
    for (var y = 0; y < 40; y++)
    {
        Console.Write(crt[y][x]);
    }
    Console.WriteLine();
}

// EHBZLRJR

class Point
{
    public int X { get; set; }
    public int Y { get; set; }
}