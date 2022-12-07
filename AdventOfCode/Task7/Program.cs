using System;
using System.Collections.Generic;
using System.Linq;

var allDirs = new List<Directory>();
var mainDir = new Directory()
{
    Name = "/",
};
allDirs.Add(mainDir);
var content = await System.IO.File.ReadAllTextAsync("./data");
var lines = content.Split("\n").Select(x => x.Trim()).ToArray();

var current = mainDir;
foreach (var line in lines)
{
    if (line.StartsWith("$ ls"))
        continue;
    else if (line.StartsWith("$ cd"))
    {
        var dirName = line.Substring("$ cd".Length).Trim();
        current = dirName switch
        {
            ".." => current.Parent,
            "/" => mainDir,
            _ => current.Directories.First(x => x.Name == dirName)
        };
    }

    else if (line.StartsWith("dir"))
    {
        var dirName = line.Substring("dir".Length).Trim();
        var newDir = current.AddDir(dirName);
        
        if (newDir is not null)
        {
            allDirs.Add(newDir);
        }
    }

    else
    {
        var items = line.Split(" ");
        var newFile = new File
        {
            Size = long.Parse(items[0].Trim()),
            Name = items[1].Trim()
        };
        current.AddFile(newFile);
    }
}

long wholeSize = 0;

foreach (var dir in allDirs)
{
    var size = dir.Size();
    if(size > 100000) continue;
    wholeSize += size;
}

Console.WriteLine(wholeSize);

var totalWeight = mainDir.Size();
const long totalSpace = 70000000;
const long atLeast = 30000000;
const long available = totalSpace - atLeast;

Console.WriteLine($"totalWeight: {totalWeight}");

var toRemove = totalWeight - available;

Console.WriteLine($"toRemove: {toRemove}");

var dirToRemove = allDirs.Where(x => x.Size() > toRemove).OrderBy(x => x.Size()).First();

Console.WriteLine($"toRemove: {dirToRemove.Size()}");


class Directory
{
    public string Name { get; set; }
    public List<File> Files { get; set; } = new();
    public List<Directory> Directories { get; set; } = new();
    public Directory Parent { get; set; } = null;

    public long Size()
    {
        long size = 0;
        size += Files.Sum(x => x.Size);
        size += Directories.Sum(x => x.Size());
        return size;
    }

    public Directory AddDir(string dirName)
    {
        if (Directories.Any(x => x.Name == dirName))
        {
            return null;
        }

        var newDir = new Directory
        {
            Parent = this,
            Name = dirName
        };
        Directories.Add(newDir);
        return newDir;
    }

    public void AddFile(File newFile)
    {
        if (Files.Any(x => x.Name == newFile.Name))
        {
            return;
        }
        Files.Add(newFile);
    }
    
    
}

class File
{
    public string Name { get; set; }
    public long Size { get; set; }
}

