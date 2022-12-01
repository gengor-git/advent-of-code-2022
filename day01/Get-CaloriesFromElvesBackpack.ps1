$InputFile = Get-Content -Path input.txt

$ElvesBackpack = @(0)

foreach ($Fruit in $InputFile) {
    if ($Fruit -eq "") {
        # new elf starting with an empty rucksack
        $ElvesBackpack += 0
    }
    else {
        # add fruit to last elves backpack
        $ElvesBackpack[-1] = $ElvesBackpack[-1] + $Fruit
    }
}

$ElvesBackpack | Sort-Object -Descending | Measure-Object -Maximum
$ElvesBackpack | Sort-Object -Descending | Select-Object -First 3 | Measure-Object -Sum