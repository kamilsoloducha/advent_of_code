var content = await File.ReadAllTextAsync("./data");
var games = content.Split("\n").Select(x => x.Trim());
var points = 0;

string[][] OPTIONS =
{
    new []{"A", "A", "Y"},
    new []{"A", "B", "Z"},
    new []{"A", "C", "X"},
    
    new []{"B", "A", "X"},
    new []{"B", "B", "Y"},
    new []{"B", "C", "Z"},
    
    new []{"C", "A", "Z"},
    new []{"C", "B", "X"},
    new []{"C", "C", "Y"}
    
};

foreach (var result in games)
{
    var decisions = result.Split(" ").Select(Convert).ToArray();

    points += decisions[1];
    if (decisions[0] == decisions[1])
    {
        points += 3;
    }
    else if (IsWin(decisions[0], decisions[1]))
    {
        points += 6;
    }
}

Console.WriteLine(points); //15523

points = 0;
foreach (var result in games)
{
    var decisions = result.Split(" ").ToArray();

    var mySelection = OPTIONS.First(x => x[0] == decisions[0] && x[2] == decisions[1])[1];

    var opp = Convert(decisions[0]);
    var own = Convert(mySelection);
    
    points += own;
    if (opp == own)
    {
        points += 3;
    }
    else if (IsWin(opp, own))
    {
        points += 6;
    }
}

Console.WriteLine(points);


bool IsWin(int opp, int own)
{
    switch (opp)
    {
        case 1 when own == 2:
        case 2 when own == 3:
        case 3 when own == 1:
            return true;
        default:
            return false;
    }
}

int Convert(string letter) =>
    letter switch
    {
        "A" or "X" => 1,
        "B" or "Y" => 2,
        "C" or "Z" => 3,
        _ => throw new Exception()
    };

