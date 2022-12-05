using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text.RegularExpressions;

var content = await File.ReadAllTextAsync("./data");
var lines = content.Split("\n").ToArray();

int numberLineIndex;
for (var i = 0;; i++)
{
    if (lines[i][0] == ' ')
    {
        numberLineIndex = i;
        break;
    }
}

var numbersLine = lines[numberLineIndex];
var numbers = numbersLine.Split(" ").Where(x => !string.IsNullOrWhiteSpace(x)).Select(x => int.Parse(x.Trim()))
    .ToArray();

var stacks = new Stack<char>[numbers[^1]];

for (var i = 0; i < stacks.Length; i++)
{
    stacks[i] = new Stack<char>();
    var letterIndex = 1 + i * 4;
    var level = numberLineIndex - 1;
    while (level >= 0)
    {
        var character = lines[level][letterIndex];
        if (character == ' ') break;
        stacks[i].Push(character);
        level--;
    }
}

var regex = new Regex(@"\d+");
if (false)
for (var i = numberLineIndex + 2; i < lines.Length; i++)
{
    var line = lines[i];
    var matches = regex.Matches(line);
    var count = int.Parse(matches[0].Value);
    var from = int.Parse(matches[1].Value) - 1;
    var to = int.Parse(matches[2].Value) - 1;

    var stackFrom = stacks[from];
    var stackTo = stacks[to];

    for (var j = 0; j < count; j++)
    {
        stackTo.Push(stackFrom.Pop());
    }
}

foreach (var stack in stacks)
{
    Console.Write(stack.Peek());
}

Console.WriteLine();
Console.WriteLine();
Console.WriteLine();
var helpingStack = new Stack<char>();

for (var i = numberLineIndex + 2; i < lines.Length; i++)
{
    var line = lines[i];
    var matches = regex.Matches(line);
    var count = int.Parse(matches[0].Value);
    var from = int.Parse(matches[1].Value) - 1;
    var to = int.Parse(matches[2].Value) - 1;

    var stackFrom = stacks[from];
    var stackTo = stacks[to];

    for (var j = 0; j < count; j++)
    {
        helpingStack.Push(stackFrom.Pop());
    }
    
    for (var j = 0; j < count; j++)
    {
        stackTo.Push(helpingStack.Pop());
    }

    if (helpingStack.Count != 0) throw new Exception();
}

foreach (var stack in stacks)
{
    Console.Write(stack.Peek());
}

