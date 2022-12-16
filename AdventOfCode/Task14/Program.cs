using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Threading;

var map = new Map();
var lines = File.ReadLines("data");
foreach (var line in lines)
{
    map.Vectors.AddRange(ReadLine(line));
}

var maxX = map.MaxX() * 3;
var maxY = map.MaxY();
var minX = map.MinX();
var minY = map.MinY();
var floor = maxY + 2;
map.Vectors.Add(Vector.Create(new Point { X = 1, Y = floor }, new Point { X = maxX, Y = floor }));
var mapArray = CreateMap(maxX, floor + 1);
PrintMap(mapArray);
FillMap(mapArray, map.Vectors);
PrintMap(mapArray);
var isOutside = false;
var counter = 0;
while (!isOutside)
{
    counter++;
    // Console.WriteLine(counter);
    try
    {
        isOutside = DropSand(mapArray);
    }
    catch (Exception e)
    {
        Console.WriteLine(e.Message);
        break;
    }
}

Console.WriteLine(counter - 1);

// foreach (var vector in map.Vectors)
// //
// {
// //
// Console.WriteLine(vector);
// // }
bool DropSand(char[][] array)
{
    var newSandPoint = new Point { X = 500 - 1, Y = 0 };
    if (array[newSandPoint.Y][newSandPoint.X] == 'o')
    {
        return true;
    }
    else
    {
        array[newSandPoint.Y][newSandPoint.X] = 'o';
    }

    while (newSandPoint.X <= maxX || newSandPoint.Y <= maxY)
    {
        var stillMoving = false;
        if (CanMoveDown(array, newSandPoint))
        {
            stillMoving = true;
            newSandPoint = MoveDown(array, newSandPoint);
        }
        else if (CanMoveDownLeft(array, newSandPoint))
        {
            stillMoving = true;
            newSandPoint = MoveDownLeft(array, newSandPoint);
        }
        else if (CanMoveDownRight(array, newSandPoint))
        {
            stillMoving = true;
            newSandPoint = MoveDownRight(array, newSandPoint);
        }

        PrintMap(array);
        if (!stillMoving) return false;
    }

    return true;
}

bool CanMoveDown(char[][] array, Point point) => array[point.Y + 1][point.X] == '.';

Point MoveDown(char[][] array, Point point)
{
    array[point.Y][point.X] = '.';
    array[point.Y + 1][point.X] = 'o';
    return new Point { X = point.X, Y = point.Y + 1 };
}

bool
    CanMoveDownLeft(char[][] array,
        Point point) =>
//array[point.Y][point.X - 1] == '.' &&
    array[point.Y + 1][point.X - 1] == '.';

Point MoveDownLeft(char[][] array, Point point)
{
    array[point.Y][point.X] = '.';
    array[point.Y + 1][point.X - 1] = 'o';
    return new Point { X = point.X - 1, Y = point.Y + 1 };
}

bool
    CanMoveDownRight(char[][] array,
        Point point) =>
//array[point.Y][point.X + 1] == '.' &&
    array[point.Y + 1][point.X + 1] == '.';

Point MoveDownRight(char[][] array, Point point)
{
    array[point.Y][point.X] = '.';
    array[point.Y + 1][point.X + 1] = 'o';
    return new Point { X = point.X + 1, Y = point.Y + 1 };
}

List<Vector> ReadLine(string line)
{
    var result = new List<Vector>();
    var points = line.Split(" -> ").Select(GetPoint).ToArray();
    for (var i = 0; i < points.Length - 1; i++)
    {
        var begin = points[i];
        var end = points[i + 1];
        var vector = Vector.Create(begin, end);
        result.Add(vector);
    }

    return result;
}

Point GetPoint(string text)
{
    var coordinates = text.Split(',');
    return new Point { X = int.Parse(coordinates[0]), Y = int.Parse(coordinates[1]) };
}

char[][] CreateMap(int x, int y)
{
    var result = new char[y][];
    for (var i = 0; i < result.Length; i++)
    {
        result[i] = new char[x];
        for (var j = 0; j < result[i].Length; j++)
        {
            result[i][j] = '.';
        }
    }

    return result;
}

void FillMap(char[][] array, IEnumerable<Vector> vectors)
{
    foreach (var vector in vectors)
    {
        foreach (var point in vector.GetAllPoints())
        {
            array[point.Y][point.X - 1] = '#';
        }
    }
}

void PrintMap(char[][] array)
{
    return;
    for (var i = minX - 1; i < 510; i++)
    {
        for (var j = 0; j < array.Length; j++)
        {
            Console.Write(array[j][i]);
        }

        Console.WriteLine();
    }

    Console.WriteLine();
    Console.WriteLine();
    Thread.Sleep(50);
}

struct Point
{
    public int X { get; set; }
    public int Y { get; set; }

    public override string ToString()
    {
        return $"X:{X}, Y:{Y}";
    }
}

class Vector
{
    public Point Begin { get; private set; }
    public Point End { get; private set; }

    public static Vector Create(Point point1, Point point2)
    {
        if (point1.X == point2.X)
        {
            if (point1.Y == point2.Y) throw new Exception($"Points the same: {point1} - {point2}");
            return point1.Y < point2.Y
                ? new Vector { Begin = point1, End = point2 }
                : new Vector { Begin = point2, End = point1 };
        }

        if (point1.Y == point2.Y)
        {
            if (point1.X == point2.X) throw new Exception($"Points the same: {point1} - {point2}");
            return point1.X < point2.X
                ? new Vector { Begin = point1, End = point2 }
                : new Vector { Begin = point2, End = point1 };
        }

        throw new Exception("Vector looks wrong");
    }

    public override string ToString()
    {
        return $"{Begin} -> {End}";
    }

    public IEnumerable<Point> GetAllPoints()
    {
        if (Begin.X == End.X)
        {
            for (var i = Begin.Y; i <= End.Y; i++)
            {
                yield return Begin with { Y = i };
            }
        }
        else if (Begin.Y == End.Y)
        {
            for (var i = Begin.X; i <= End.X; i++)
            {
                yield return Begin with { X = i };
            }
        }
        else
        {
            throw new Exception("Vector looks wrong");
        }
    }
}

class Map
{
    private IEnumerable<Point> Points => Vectors.Select(x => x.Begin).Concat(Vectors.Select(x => x.End));
    public List<Vector> Vectors { get; } = new();

    public int MaxX()
    {
        return Points.Select(x => x.X).Max();
    }

    public int MaxY()
    {
        return Points.Select(x => x.Y).Max();
    }

    public int MinX()
    {
        return Points.Select(x => x.X).Min();
    }

    public int MinY()
    {
        return Points.Select(x => x.Y).Min();
    }
}