using System;
using System.IO;
using System.Linq;

var lines = File.ReadLines("data").ToArray();
var table = new int[lines.Length][];

for (var j = 0; j < lines.Length; j++)
{
    var trees = new int[lines[j].Length];
    for (var i = 0; i < lines[j].Length; i++)
    {
        trees[i] = int.Parse(lines[j][i].ToString());
    }

    table[j] = trees;
}

// for (var i = 0; i < table.Length; i++)
// {
//     for (var j = 0; j < table[i].Length; j++)
//     {
//         Console.Write(table[i][j]);
//     }
//     Console.WriteLine();
// }


var counter = 0;
for (var i = 0; i < table.Length; i++)
{
    for (var j = 0; j < table[i].Length; j++)
    {
        var item = table[i][j];
        
        if (i == 0 || j == 0 || i == table.Length - 1 || j == table[i].Length - 1)
        {
            counter++;
            continue;
        }
        
        //left
        var isVisible = true;
        for (var z = 0; z < j; z++)
        {
            if (table[i][z] >= table[i][j])
            {
                isVisible = false;
                break;
            }
        }

        if (isVisible)
        {
            counter++;
            continue;
        }
        
        
        //right
        isVisible = true;
        for (var z = j+1; z < table[i].Length; z++)
        {
            if (table[i][z] >= table[i][j])
            {
                isVisible = false;
                break;
            }
        }

        if (isVisible)
        {
            counter++;
            continue;
        }
        
        //top
        isVisible = true;
        for (var z = 0; z < i; z++)
        {
            if (table[z][j] >= table[i][j])
            {
                isVisible = false;
                break;
            }
        }

        if (isVisible)
        {
            counter++;
            continue;
        }
        
        //bottom
        isVisible = true;
        for (var z = i+1; z < table.Length; z++)
        {
            if (table[z][j] >= table[i][j])
            {
                isVisible = false;
                break;
            }
        }

        if (isVisible)
        {
            counter++;
        }
    }
}

Console.WriteLine(counter);

var maxScore = 0;

for (var i = 1; i < table.Length-1; i++)
{
    for (var j = 1; j < table[i].Length-1; j++)
    {
        var leftScore = 0;
        var rightScore = 0;
        var upScore = 0;
        var bottomScore = 0;
        
        //left 
        for (var z = j-1; z >= 0; z--)
        {
            leftScore++;
            if (table[i][z] >= table[i][j])
            {
                break;
            }
        }
        
        //right 
        for (var z = j+1; z < table[i].Length; z++)
        {
            rightScore++;
            if (table[i][z] >= table[i][j])
            {
                break;
            }
        }
        
        //up
        for (var z = i-1; z >= 0; z--)
        {
            upScore++;
            if (table[z][j] >= table[i][j])
            {
                break;
            }
        }
        
        //bottom
        for (var z = i+1; z < table.Length; z++)
        {
            bottomScore++;
            if (table[z][j] >= table[i][j])
            {
                break;
            }
        }

        var score = leftScore * rightScore * upScore * bottomScore;
        if (maxScore < score) maxScore = score;
    }
}

Console.WriteLine(maxScore);