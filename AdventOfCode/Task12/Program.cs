using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text.Json;

var data = GetData();
var distancePart1 = FindDistance(data, GetStart(data));
Console.WriteLine(distancePart1);

data = GetData();
var nodes = LinearArray(data).ToList();
var starts = nodes.Where(x =>
        (x.Height is 'a' or 'S') && (x.X == 0 || x.Y == 0 || x.X == data.Length - 1 || x.Y == data.First().Length - 1))
    .ToList();
var distances = new List<int>();
for (var i = 0; i < starts.Count; i++)
{
    var start = starts[i];
    var newDistance = FindDistance(data, start);
    distances.Add(newDistance);
    nodes.ForEach(x => x.Distance = 0);
}

Console.WriteLine(distances.Where(x => x != 0).Min());


int FindDistance(Node[][] data, Node start)
{
    start.Height = 'a';
    Queue<Node> queue = new Queue<Node>();
    queue.Enqueue(start);

    while (queue.Any())
    {
        var currentNode = queue.Dequeue();

        if (CheckNext(data, queue, currentNode, -1, 0)) break;
        if (CheckNext(data, queue, currentNode, 1, 0)) break;
        if (CheckNext(data, queue, currentNode, 0, -1)) break;
        if (CheckNext(data, queue, currentNode, 0, 1)) break;
    }

    var list = new List<Node>();
    for (int i = 0; i < data.Length; i++)
    {
        list.AddRange(data[i]);
    }

    return list.First(x => x.Height == 'E').Distance;
}

IEnumerable<Node> LinearArray(Node[][] table)
{
    for (int i = 0; i < data.Length; i++)
    {
        for (int j = 0; j < data[i].Length; j++)
        {
            yield return data[i][j];
        }
    }
}

bool CheckNext(Node[][] data, Queue<Node> queue, Node currentNode, int deltaX, int deltaY)
{
    var xToCheck = currentNode.X + deltaX;
    if (xToCheck < 0 || xToCheck >= data.Length)
        return false;
    var yToCheck = currentNode.Y + deltaY;
    if (yToCheck < 0 || yToCheck >= data[xToCheck].Length)
        return false;

    var next = data[xToCheck][yToCheck];
    if (next.Distance != 0 || next.Height - currentNode.Height > 1)
        return false;

    next.Distance = currentNode.Distance + 1;
    if (next.Height == 'E') return true;
    queue.Enqueue(next);
    return false;
}

void PrintArray(Node[][] data)
{
    for (int i = 0; i < data.Length; i++)
    {
        for (int j = 0; j < data[i].Length; j++)
        {
            Console.Write("{0,4}", data[i][j].Distance);
            Console.Write("{0,1}", data[i][j].Height);
        }

        Console.WriteLine();
    }

    Console.WriteLine();
}

void PrintHeight(Node[][] data)
{
    for (int i = 0; i < data.Length; i++)
    {
        for (int j = 0; j < data[i].Length; j++)
        {
            Console.Write("{0,4}", data[i][j].Height);
        }

        Console.WriteLine();
    }

    Console.WriteLine();
}

Node[][] GetData()
{
    var lines = File.ReadAllLines("data").ToArray();
    var result = new Node[lines.Length][];
    for (var i = 0; i < lines.Length; i++)
    {
        var line = lines[i];
        result[i] = new Node[line.Length];
        for (var j = 0; j < line.Length; j++)
        {
            result[i][j] = new Node
            {
                X = i,
                Y = j,
                Height = line[j]
            };
        }
    }

    return result;
}

Node GetStart(Node[][] data)
{
    for (var i = 0; i < data.Length; i++)
    {
        for (var j = 0; j < data[i].Length; j++)
        {
            if (data[i][j].Height == 'S')
                return data[i][j];
        }
    }

    throw new Exception("Start is not found");
}

class Node
{
    public int X { get; set; }
    public int Y { get; set; }
    public int Distance { get; set; }
    public char Height { get; set; }

    public override string ToString()
    {
        return JsonSerializer.Serialize(this);
    }
}