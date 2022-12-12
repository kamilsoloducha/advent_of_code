using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text.RegularExpressions;

var roundCount = 10000;

var lines = File.ReadLines("data").ToArray();

var monkey1 = PrepareList(lines);
var result1 = CalculateMonkeyBusiness(monkey1, 20, item => item / 3);
Console.WriteLine(result1);

var monkey2 = PrepareList(lines);
var products = monkey2.Select(x => x.TestValue).Aggregate((long)1, (a, b) => (a * b));
var result2 = CalculateMonkeyBusiness(monkey2, 10000, item => item % products);
Console.WriteLine(string.Join(", ", monkey2.Select(x => x.Counter)));

Console.WriteLine(result2);

long CalculateMonkeyBusiness(Monkey[] monkeys, int rounds, Func<long, long> reduceFunc)
{
    for (var i = 0; i < rounds; i++)
    {
        foreach (var monkey in monkeys)
        {
            monkey.Counter += monkey.Items.Count;
            foreach(var item in monkey.Items)
            {
                var newValue = monkey.Action(item);
                newValue = reduceFunc(newValue);
                var destination = monkey.Test(newValue);
                monkeys[destination].AddItem(newValue);
            }
            monkey.Items = new List<long>();
        }
    }

    var mostUsable = monkeys.OrderByDescending(x => x.Counter).Take(2).ToArray();

    return mostUsable[0].Counter * mostUsable[1].Counter;
}

Monkey[] PrepareList(string[] lines)
{
    var monkeys = new List<Monkey>();
    var index = 0;

    foreach (var line in lines)
    {
        if (line.StartsWith("Monkey"))
        {
            index = int.Parse(Regex.Match(line, "\\d+").Value);
            var currentMonkey = new Monkey();
            monkeys.Add(currentMonkey);
        }
    
        if (line.TrimStart().StartsWith("Starting items"))
        {
            var items = Regex.Matches(line, "\\d+").Select(x => int.Parse(x.Value)).ToList();
            //monkeys.ElementAt(index).Items = items;
            foreach (var item in items)
            {
                monkeys.ElementAt(index).AddItem(item);    
            }
        }
    
        if (line.TrimStart().StartsWith("Operation"))
        {
            
            Func<long, long> action = default;
            if (line.Contains("old * old"))
            {
                action = x => x * x;
            }
            else if (line.Contains('*'))
            {
                var value = int.Parse(Regex.Match(line, "\\d+").Value);
                action = x => x * value;
            }
            else
            {
                var value = int.Parse(Regex.Match(line, "\\d+").Value);
                action = x => x + value;
            }
    
            monkeys.ElementAt(index).Action = action;
        }
    
        if (line.TrimStart().StartsWith("Test"))
        {
            var value = int.Parse(Regex.Match(line, "\\d+").Value);
            monkeys.ElementAt(index).TestValue = value;
        }
    
        if (line.TrimStart().StartsWith("If true"))
        {
            var destination = int.Parse(Regex.Match(line, "\\d+").Value);
            monkeys.ElementAt(index).DestinationIfTrue = destination;
        }
    
        if (line.TrimStart().StartsWith("If false"))
        {
            var destination = int.Parse(Regex.Match(line, "\\d+").Value);
            monkeys.ElementAt(index).DestinationIfFalse = destination;
        }
    }

    return monkeys.ToArray();
}

class Monkey
{
    public List<long> Items { get; set; } = new();
    public Func<long, long> Action { get; set; }
    public int DestinationIfTrue { get; set; }
    public int DestinationIfFalse { get; set; }
    public long TestValue { get; set; }
    
    public long Counter { get; set; }

    public int Test(long value) => value % TestValue == 0 ? DestinationIfTrue : DestinationIfFalse;

    public void AddItem(long item)
    {
        Items.Add(item);
    }

    public override string ToString()
    {
        return string.Join(", ", Items);
    }

    public string PrintCounter()
    {
        return $"{Counter}";
    }
}

