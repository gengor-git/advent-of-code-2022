$Strategy = Get-Content -Path .\day02\input.txt

$Signs = [PSCustomObject]@{
    ROCK     = 1;
    PAPER    = 2;
    SCISSORS = 3
}

$Results = [PSCustomObject]@{
    WIN  = 6;
    DRAW = 3;
    LOSE = 0
}

function Resolve-Sign {
    [CmdletBinding()]
    param (
        [Parameter()]
        [String]
        $LetterCode
    )
    # Write-Warning "Resoving: $LetterCode"
    switch ($LetterCode) {
        'A' { return $Signs.ROCK }
        'X' { return $Signs.ROCK }
        'B' { return $Signs.PAPER }
        'Y' { return $Signs.PAPER }
        'C' { return $Signs.SCISSORS }
        'Z' { return $Signs.SCISSORS }
        Default {}
    }
}

function Resolve-Outcome {
    [CmdletBinding()]
    param (
        [Parameter()]
        [int]
        $OpponentSign,
        [String]
        $OutcomeCode
    )
    # Out-Host -InputObject "Searching for Outcome Code `"$OutcomeCode`""
    # Out-Host -InputObject "Opponent is using: `"$OpponentSign`""
    switch ($OpponentSign) {
        $Signs.ROCK {
            # Out-Host -InputObject "Opponent is using ROCK."
            switch ($OutcomeCode) {
                'X' { return $Signs.SCISSORS } # lose
                'Y' { return $Signs.ROCK }     # draw
                'Z' { return $Signs.PAPER }    # win
                Default {
                    Write-Warning "ERROR INNER"
                }
            }
        }
        $Signs.PAPER {
            # Out-Host -InputObject "Opponent is using PAPER."
            switch ($OutcomeCode) {
                'X' { return $Signs.ROCK }     # lose
                'Y' { return $Signs.PAPER }    # draw
                'Z' { return $Signs.SCISSORS } # win
                Default {
                    Write-Warning "ERROR INNER"
                }
            }
        }
        $Signs.SCISSORS {
            # Out-Host -InputObject "Opponent is using SCISSORS."
            switch ($OutcomeCode) {
                'X' { return $Signs.PAPER }    # lose
                'Y' { return $Signs.SCISSORS } # draw
                'Z' { return $Signs.ROCK }     # win
                Default {
                    Write-Warning "ERROR INNER"
                }
            }
        }
        Default {
            Write-Warning "ERROR OUTER"
        }

    }
}

function Get-ScoreByWhoWins {
    [CmdletBinding()]
    param (
        [Parameter()]
        [int]
        $OpponentSign,
        [Parameter()]
        [int]
        $SelfSign
    )
    switch ($OpponentSign) {
        $Signs.ROCK { 
            switch ($SelfSign) {
                $Signs.ROCK { 
                    return ($Results.DRAW + $SelfSign)
                }
                $Signs.PAPER { 
                    return ($Results.WIN + $SelfSign)
                }
                $Signs.SCISSORS { 
                    return ($Results.LOSE + $SelfSign)
                }
                Default {
                    Write-Warning "ERROR INNER"
                }
            }

        }
        $Signs.PAPER { 
            switch ($SelfSign) {
                $Signs.ROCK { 
                    return ($Results.LOSE + $SelfSign)
                }
                $Signs.PAPER { 
                    return ($Results.DRAW + $SelfSign)
                }
                $Signs.SCISSORS { 
                    return ($Results.WIN + $SelfSign)
                }
                Default {
                    Write-Warning "ERROR INNER"
                }
            }
        }
        $Signs.SCISSORS { 
            switch ($SelfSign) {
                $Signs.ROCK { 
                    return ($Results.WIN + $SelfSign)
                }
                $Signs.PAPER { 
                    return ($Results.LOSE + $SelfSign)
                }
                $Signs.SCISSORS { 
                    return ($Results.DRAW + $SelfSign)
                }
                Default {
                    Write-Warning "ERROR INNER"
                }
            }
        }
        Default {
            Write-Warning "ERROR OUTER"
        }
    }
}

function New-GameBySignStrategy {
    $Score = 0
    foreach ($Play in $Strategy) {
        $Opponent = Resolve-Sign -LetterCode ($Play -split " ")[0]
        $me = Resolve-Sign -LetterCode ($Play -split " ")[1]
        $Result = Get-ScoreByWhoWins -OpponentSign $Opponent -SelfSign $me
        $Score = $Score + $Result
    }
    return $Score
}

function New-GameByOutcomeStrategy {
    $Score = 0
    foreach ($Play in $Strategy) {
        $Opponent = Resolve-Sign -LetterCode ($Play -split " ")[0]
        $Outcome = ($Play -split " ")[1]
        $me = Resolve-Outcome -OpponentSign $Opponent -OutcomeCode $Outcome
        $Result = Get-ScoreByWhoWins -OpponentSign $Opponent -SelfSign $me
        $Score = $Score + $Result
    }
    return $Score
}

function New-GameByFixedRules($Rules) {
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
# This is the simple solution with hard coded result scores for all 9 outcomes
$part1 = New-GameByFixedRules($RulesPart1)
$part2 = New-GameByFixedRules($RulesPart2)

Out-Host -InputObject "Score based on stragey giving signs:   $part1"
Out-Host -InputObject "Score based on stragey giving result:  $part2"


# This is the complex version, where the result calulation is more dynamic via maps.
$part1long = New-GameBySignStrategy
$part2long = New-GameByOutcomeStrategy
Out-Host -InputObject "Re-Calulate part 1 the cumbersome way: $part1long"
Out-Host -InputObject "Re-Calulate part 2 the cumbersome way: $part2long"
