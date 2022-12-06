using System;
using System.IO;
using System.Linq;

var file = File.Open("data", FileMode.Open);
var counter = 0;
var marker = new int[4];

while ((!CheckMarker(marker) || marker.Any(x => x == 0)) && file.CanWrite)
{
    MoveMarker(marker);
    marker[3] = file.ReadByte();
    counter++;
}

Console.WriteLine(counter);

file.Position = 0;
counter = 0;

marker = new int[14];

while ((!CheckMarker(marker) || marker.Any(x => x == 0)) && file.CanWrite)
{
    MoveMarker(marker);
    marker[13] = file.ReadByte();
    counter++;
}

Console.WriteLine(counter);

void MoveMarker(int[] marker)
{
    for (var i = 0; i < marker.Length - 1; i++)
    {
        marker[i] = marker[i + 1];
    }
}

bool CheckMarker(int[] marker)
{
    for (var i = 0; i < marker.Length; i++)
    {
        for (var j = i + 1; j < marker.Length; j++)
        {
            if (marker[i] == marker[j]) return false;
        }
    }
    return true;
}