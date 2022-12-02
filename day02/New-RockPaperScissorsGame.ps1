$Strategy = Get-Content -Path .\day02\input.txt

function PlayGameByRules($Rules) {
    $Score = 0
    foreach ($Play in $Strategy) {
        $Score += $Rules[$Play]
    }
    return $Score
}

$RulesPart1 = @{
    'A X' = 4;
    'A Y' = 8;
    'A Z' = 3;
    'B X' = 1;
    'B Y' = 5;
    'B Z' = 9;
    'C X' = 7;
    'C Y' = 2;
    'C Z' = 6    
}
$RulesPart2 = @{
    'A X' = 3;
    'A Y' = 4;
    'A Z' = 8;
    'B X' = 1;
    'B Y' = 5;
    'B Z' = 9;
    'C X' = 2;
    'C Y' = 6;
    'C Z' = 7
}
PlayGameByRules($RulesPart1)
PlayGameByRules($RulesPart2)