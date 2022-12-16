using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text.RegularExpressions;

var target = 2000000;
//target = 10;
var size = 20;
size = 4000000;
var file = size == 20 ? "testdata" : "data";
var pairs = File.ReadLines(file).Select(x =>
{
    var matches = Regex.Matches(x, "-?\\d+");
    return new Pair(new Point
    {
        X = int.Parse(matches[0].Value),
        Y = int.Parse(matches[1].Value),
    }, new Point
    {
        X = int.Parse(matches[2].Value),
        Y = int.Parse(matches[3].Value),
    });
}).ToArray();

var isInside = false;
Point point = default;
for (var i = 0; i < size; i++)
{
    for (var j = 0; j < size; j++)
    {
        isInside = false;
        for (var z = 0; z < pairs.Length; z++)
        {
            isInside = pairs[z].IsInside(i,j);
            if (isInside)
            {
                j += pairs[z].Distance - pairs[z].SensorDistance(i, j);
                break;
            }
        }

        if (!isInside)
        {
            Console.WriteLine($"i = {i}, j = {j}");
            point = new Point(i, j);
            break;
        }
    }

    if (i % 1000 == 0)
    {
        Console.WriteLine(i);
    }
    if (!isInside)
    {
        break;
    }
}

Console.WriteLine((long)point.X*4000000 + point.Y);

var pointToCheck = point;// new Point(14, 11);
foreach (var pair in pairs)
{
    Console.WriteLine($"{pair} - {pair.IsInside(pointToCheck.X, pointToCheck.Y)}");
}
Console.WriteLine($"IsTarget? - {pairs.Any(x => !x.IsInside(pointToCheck.X, pointToCheck.Y))}");

return;


var allPoints = pairs.Select(x => x.Beacon).Concat(pairs.Select(x => x.Sensor)).ToArray();
var xToIgnore = allPoints.Where(x => x.Y == target).Select(x => x.X).Distinct().ToArray();

var interestingPoints = new List<Point>();
var hashset = new HashSet<int>();

for (var i = 0; i < pairs.Length; i++)
{
    var pair = pairs[i];

    var sensorTargetDistance = Math.Abs(target - pair.Sensor.Y);
    var sensorBeaconDistance = Math.Abs(pair.Beacon.X - pair.Sensor.X) + Math.Abs(pair.Beacon.Y - pair.Sensor.Y);
    if (sensorTargetDistance > sensorBeaconDistance) continue;

    var remains = sensorBeaconDistance - sensorTargetDistance;
    var newPoints = new List<Point>();
    for (int j = 0; j <= remains; j++)
    {
        var x = pair.Sensor.X + j;
        hashset.Add(x);
        //newPoints.Add(new Point{X = x, Y = target});
        x = pair.Sensor.X - j;
        hashset.Add(x);
        //newPoints.Add(new Point{X = x, Y = target});
    }

    //Console.WriteLine($"For {pair}: " + string.Join(", ", newPoints));

    //interestingPoints.AddRange(newPoints);
}


//Console.WriteLine($"results: {string.Join(", ", interestingPoints.Select(x=> x.X).Distinct().OrderBy(x => x))}");
Console.WriteLine($"Answer: {hashset.Count() - xToIgnore.Count()}");

return;
Console.WriteLine(pairs.Length);
var result = new List<int>();
for (var i = 0; i < pairs.Length; i++)
{
    var pair = pairs[i];
    Console.WriteLine($"pari: {i}. {pair}");
    result.AddRange(SetPair(pair, target));
}

var known = allPoints.Where(x => x.Y == target).DistinctBy(x => x.X).Count();

Console.WriteLine($"results: {string.Join(", ", result.Distinct().OrderBy(x => x))}");
Console.WriteLine($"Answer: {result.Distinct().Count() - known}");


List<int> SetPair(Pair pair, int question)
{
    var result2 = new List<int>();

    var isMet = false;
    var distance = Math.Abs(question - pair.Sensor.Y);
    var pairDistance = Math.Abs(pair.Beacon.X - pair.Sensor.X) + Math.Abs(pair.Beacon.Y - pair.Sensor.Y);

    while (!isMet && pairDistance >= distance)
    {
        var points = FindAllInDistance(pair.Sensor, distance, question, pair.Beacon, ref isMet);
        result2.AddRange(points.Select(x => x.X));
        distance++;
        if (distance % 1000 == 0)
        {
            Console.WriteLine("Distance:" + distance + " points: " + result2.Count);
        }
    }

    return result2;
}

IEnumerable<Point> FindAllInDistance(Point point, int distance, int question, Point beacon, ref bool isMet)
{
    var result = new List<Point>();
    var x = point.X;
    var y = point.Y + distance;
    if (y == question)
        result.Add(new Point { X = x, Y = y });
    do
    {
        ++x;
        --y;
        if (beacon.X == x && beacon.Y == y) isMet = true;
        if (y == question)
            result.Add(new Point { X = x, Y = y });
    } while (y != point.Y);

    do
    {
        --x;
        --y;
        if (beacon.X == x && beacon.Y == y) isMet = true;
        if (y == question)
            result.Add(new Point { X = x, Y = y });
    } while (x != point.X);

    do
    {
        --x;
        ++y;
        if (beacon.X == x && beacon.Y == y) isMet = true;
        if (y == question)
            result.Add(new Point { X = x, Y = y });
    } while (y != point.Y);

    do
    {
        ++x;
        ++y;
        if (beacon.X == x && beacon.Y == y) isMet = true;
        if (y == question)
            result.Add(new Point { X = x, Y = y });
    } while (x != point.X);

    return result;
}


void PrintMap(char[][] array)
{
    for (var i = 0; i < array.Length; i++)
    {
        for (var j = 0; j < array[i].Length; j++)
        {
            Console.Write(array[i][j]);
        }

        Console.WriteLine();
    }

    Console.WriteLine();
}

class Pair
{
    public Point Sensor { get; set; }
    public Point Beacon { get; set; }
    public int Distance { get; }

    public Pair()
    {
    }

    public Pair(Point sensor, Point beacon)
    {
        Sensor = sensor;
        Beacon = beacon;
        Distance = Math.Abs(Beacon.X - Sensor.X) + Math.Abs(Beacon.Y - Sensor.Y);
    }

    public int SensorDistance(int x, int y)
    {
        return Math.Abs(x - Sensor.X) + Math.Abs(y - Sensor.Y);
    }

    public bool IsInside(int x, int y)
    {
        var targetSensorDistance = Math.Abs(x - Sensor.X) + Math.Abs(y - Sensor.Y);
        return targetSensorDistance <= Distance;
    }

    public override string ToString()
    {
        return $"S {Sensor} B {Beacon}";
    }
}

class Point
{
    public int X { get; set; }
    public int Y { get; set; }

    public Point(int x, int y)
    {
        X = x;
        Y = y;
    }

    public Point()
    {
    }

    public override string ToString()
    {
        return $"{X}:{Y}";
    }
}