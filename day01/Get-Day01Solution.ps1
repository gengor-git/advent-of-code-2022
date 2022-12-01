$InputFile = Get-Content -Path input.txt

$ElvesBackpack = @(0)

foreach ($Entry in $InputFile) {
    if ($Entry -eq "") {
        # new elf starting
        $ElvesBackpack += 0

    }
    else {
        # add to last elves backpack
        $ElvesBackpack[-1] = $ElvesBackpack[-1] + $Entry
    }
}

$ElvesBackpack | Sort-Object -Descending | Select-Object -First 3
$ElvesBackpack | Sort-Object -Descending | Select-Object -First 3 | Measure-Object -Sum