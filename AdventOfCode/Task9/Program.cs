using System.Drawing;
using System.Numerics;
using System.Text.RegularExpressions;

var lines = File.ReadLines("data").ToArray();
var visited = new List<Point>();

var head = new Vector2(0, 0);
var tail = new Vector2(0, 0);

foreach (var line in lines)
{
    var direction = line[0];
    var amountMatch = Regex.Match(line, "\\d+");
    var amount = int.Parse(amountMatch.Value);

    for (var i = 0; i < amount; i++)
    {
        switch (direction)
        {
            case 'R':
                head.X++;
                break;
            case 'L':
                head.X--;
                break;
            case 'U':
                head.Y++;
                break;
            case 'D':
                head.Y--;
                break;
        }

        UpdateTail(direction);
        visited.Add(new Point((int)tail.X, (int)tail.Y));
    }
}

var count = visited.Distinct().Count();

Console.WriteLine(count);

void UpdateTail(char direction)
{
    var distance = Math.Sqrt(Math.Pow(head.X - tail.X, 2) + Math.Pow(head.Y - tail.Y, 2));
    if (distance < 1.5) return;

    if (Math.Abs(head.X - tail.X) > 0.2 && Math.Abs(head.Y - tail.Y) > 0.2)
    {
        switch (direction)
        {
            case 'R':
                tail.X = head.X - 1;
                tail.Y = head.Y;
                break;
            case 'L':
                tail.X = head.X + 1;
                tail.Y = head.Y;
                break;
            case 'U':
                tail.X = head.X;
                tail.Y = head.Y - 1;
                break;
            case 'D':
                tail.X = head.X;
                tail.Y = head.Y + 1;
                break;
        }
    }
    else
    {
        switch (direction)
        {
            case 'R':
                tail.X++;
                break;
            case 'L':
                tail.X--;
                break;
            case 'U':
                tail.Y++;
                break;
            case 'D':
                tail.Y--;
                break;
        }
    }
}

visited.Clear();
var points = new Point[10];
for (var i = 0; i < points.Length; i++)
{
    points[i] = new Point(0, 0);
}

foreach (var line in lines)
{
    var direction = line[0];
    var amountMatch = Regex.Match(line, "\\d+");
    var amount = int.Parse(amountMatch.Value);

    for (var i = 0; i < amount; i++)
    {
        switch (direction)
        {
            case 'R':
                points[0].X++;
                break;
            case 'L':
                points[0].X--;
                break;
            case 'U':
                points[0].Y++;
                break;
            case 'D':
                points[0].Y--;
                break;
        }

        for (var j = 0; j < points.Length - 1; j++)
        {
            UpdateNext(ref points[j], ref points[j + 1]);
        }

        visited.Add(new Point(points.Last().X, points.Last().Y));
    }
}

Console.WriteLine(visited.Distinct().Count());

void UpdateNext(ref Point first, ref Point second)
{
    var distance = Math.Sqrt(Math.Pow(first.X - second.X, 2) + Math.Pow(first.Y - second.Y, 2));
    if (distance < 1.5) return;

    if (first.X != second.X && first.Y != second.Y)
    {
        var xDistance = Math.Abs(first.X - second.X);
        var yDistance = Math.Abs(first.Y - second.Y);
        if (xDistance == yDistance)
        {
            if (IsBelow(first, second))
            {
                second.Y = first.Y - 1;
            }
            else
            {
                second.Y= first.Y + 1;
            }
            
            if (IsOnLeft(first, second))
            {
                second.X = first.X - 1;
            }
            else
            {
                second.X = first.X + 1;
            }
        }
        else if (xDistance < yDistance)
        {
            second.X = first.X;
            if (IsBelow(first, second))
            {
                second.Y = first.Y - 1;
            }
            else
            {
                second.Y= first.Y + 1;
            }
        }
        else
        {
            second.Y = first.Y;
            if (IsOnLeft(first, second))
            {
                second.X = first.X - 1;
            }
            else
            {
                second.X = first.X + 1;
            }
        }
    }
    else if (first.X != second.X && first.Y == second.Y)
    {
        if (IsOnLeft(first, second))
        {
            second.X++;
        }
        else
        {
            second.X--;
        }
    }
    else if (first.X == second.X && first.Y != second.Y)
    {
        if (IsBelow(first, second))
        {
            second.Y++;
        }
        else
        {
            second.Y--;
        }
    }
}

bool IsOnLeft(Point first, Point second)
{
    return first.X - second.X > 0;
}

bool IsBelow(Point first, Point second)
{
    return first.Y - second.Y > 0;
}