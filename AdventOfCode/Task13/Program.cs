using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;

//6415

var lines = File.ReadLines("data").ToArray();
var counter = 0;
var pairId = 0;
if (false)
for (var i = 0; i < lines.Length; i += 3)
{
    pairId++;
    var leftLine = lines[i];
    var rightLine = lines[i + 1];
    if (string.IsNullOrEmpty(leftLine) || string.IsNullOrEmpty(rightLine)) continue;

    switch (CompareArrays(leftLine, rightLine))
    {
        case 1:
            counter += pairId;
            Console.WriteLine(leftLine);
            Console.WriteLine(rightLine);
            Console.WriteLine(true.ToString().ToLower());
            break;
        case -1:
            Console.WriteLine(leftLine);
            Console.WriteLine(rightLine);
            Console.WriteLine(false.ToString().ToLower());
            continue;
        default: throw new Exception(i.ToString());
    }
}

Console.WriteLine(counter);
Console.WriteLine("End");

var newLines = lines.Where(x => !string.IsNullOrEmpty(x)).Concat(new[] { "[[2]]", "[[6]]" });
var orderLines = newLines.OrderBy(x => x, new CustomComparer()).ToArray();

var result = 1;
for (var i = 0; i < orderLines.Length; i++)
{
    var line = orderLines[i];
    if (line is "[[2]]" or "[[6]]") result *= (i + 1);
}
Console.WriteLine(result);

int CompareArrays(string left, string right)
{
    var leftElements = SplitArray(left);
    var rightElements = SplitArray(right);

    var count = Math.Max(leftElements.Length, rightElements.Length);
    for (var j = 0; j < count; j++)
    {
        var leftElement = j < leftElements.Length ? leftElements[j] : null;
        var rightElement = j < rightElements.Length ? rightElements[j] : null;
        if (leftElement == rightElement) continue; 

        if (leftElement != null && rightElement == null) return -1;
        if (leftElement == null && rightElement != null) return 1;

        if (IsValue(leftElement) && IsValue(rightElement))
        {
            var comparison = CompareValues(leftElement, rightElement);
            if (comparison == 0) continue;
            return comparison;
        }

        if (IsArray(leftElement) && IsArray(rightElement))
        {
            var comparison = CompareArrays(leftElement, rightElement);
            if (comparison == 0) continue;
            return comparison;
        }

        if (IsValue(leftElement) && IsArray(rightElement))
        {
            var comparison = CompareArrays($"[{leftElement}]", rightElement);
            if (comparison == 0) continue;
            return comparison;
        }

        if (IsArray(leftElement) && IsValue(rightElement))
        {
            var comparison = CompareArrays(leftElement, $"[{rightElement}]");
            if (comparison == 0) continue;
            return comparison;
        }

        throw new Exception($"Not found: '{leftElement}' '{rightElement}'");
    }
    //Console.WriteLine($"{left}={right}");
    return 0;
}

bool IsValue(string element)
{
    return int.TryParse(element, out var _);
}

bool IsArray(string element)
{
    return element[0] == '[' && element[^1] == ']';
}

int CompareValues(string left, string right)
{
    var leftValue = int.Parse(left);
    var rightValue = int.Parse(right);
    return Math.Sign(rightValue - leftValue);
}

string[] SplitArray(string array)
{
    if (array.Count(x => x == ']') != array.Count(x => x == '[')) throw new Exception("1");
    var level = 0;
    var begin = 0;
    var result = new List<string>();
    for (var i = 1; i < array.Length - 1; i++)
    {
        if (array[i] == '[')
        {
            if (level == 0)
            {
                begin = i;
            }

            level++;
        }

        if (array[i] == ']')
        {
            level--;
            if (level == 0)
            {
                result.Add(array.Substring(begin, i - begin + 1));
                continue;
            }
        }

        if (level == 0 && char.IsNumber(array[i]))
        {
            var builder = new StringBuilder();
            do
            {
                builder.Append(array[i++]);
            } while (char.IsNumber(array[i]));
            result.Add(builder.ToString());
        }
    }

    return result.ToArray();
}

public class CustomComparer : IComparer<string>
{
    public int Compare(string x, string y)
    {
        return CompareArrays(x, y) * (-1);
    }
    
    int CompareArrays(string left, string right)
{
    var leftElements = SplitArray(left);
    var rightElements = SplitArray(right);

    var count = Math.Max(leftElements.Length, rightElements.Length);
    for (var j = 0; j < count; j++)
    {
        var leftElement = j < leftElements.Length ? leftElements[j] : null;
        var rightElement = j < rightElements.Length ? rightElements[j] : null;
        if (leftElement == rightElement) continue; 

        if (leftElement != null && rightElement == null) return -1;
        if (leftElement == null && rightElement != null) return 1;

        if (IsValue(leftElement) && IsValue(rightElement))
        {
            var comparison = CompareValues(leftElement, rightElement);
            if (comparison == 0) continue;
            return comparison;
        }

        if (IsArray(leftElement) && IsArray(rightElement))
        {
            var comparison = CompareArrays(leftElement, rightElement);
            if (comparison == 0) continue;
            return comparison;
        }

        if (IsValue(leftElement) && IsArray(rightElement))
        {
            var comparison = CompareArrays($"[{leftElement}]", rightElement);
            if (comparison == 0) continue;
            return comparison;
        }

        if (IsArray(leftElement) && IsValue(rightElement))
        {
            var comparison = CompareArrays(leftElement, $"[{rightElement}]");
            if (comparison == 0) continue;
            return comparison;
        }

        throw new Exception($"Not found: '{leftElement}' '{rightElement}'");
    }
    //Console.WriteLine($"{left}={right}");
    return 0;
}

bool IsValue(string element)
{
    return int.TryParse(element, out var _);
}

bool IsArray(string element)
{
    return element[0] == '[' && element[^1] == ']';
}

int CompareValues(string left, string right)
{
    var leftValue = int.Parse(left);
    var rightValue = int.Parse(right);
    return Math.Sign(rightValue - leftValue);
}

string[] SplitArray(string array)
{
    if (array.Count(x => x == ']') != array.Count(x => x == '[')) throw new Exception("1");
    var level = 0;
    var begin = 0;
    var result = new List<string>();
    for (var i = 1; i < array.Length - 1; i++)
    {
        if (array[i] == '[')
        {
            if (level == 0)
            {
                begin = i;
            }

            level++;
        }

        if (array[i] == ']')
        {
            level--;
            if (level == 0)
            {
                result.Add(array.Substring(begin, i - begin + 1));
                continue;
            }
        }

        if (level == 0 && char.IsNumber(array[i]))
        {
            var builder = new StringBuilder();
            do
            {
                builder.Append(array[i++]);
            } while (char.IsNumber(array[i]));
            result.Add(builder.ToString());
        }
    }

    return result.ToArray();
}

}