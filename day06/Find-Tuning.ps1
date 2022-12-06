$input_file = Get-Content -Path .\day06\input.txt

function isUnique($DataStream) {
    # Out-Host -InputObject "Datastream: $DataStream"
    $LastLetter = $DataStream[-1]
    $RestOfString = $DataStream.substring(0, $DataStream.Length - 1)
    # Out-Host -InputObject "Searching for `"$LastLetter`" in `"$RestOfString`""
    if (-not ($RestOfString.contains($LastLetter))) {
        if ($DataStream.Length -ge 3) {
            return isUnique($RestOfString)
        }
        else {
            return $true
        }
    }
    else {
        return $false
    }
    return $false
}

function Find-Marker($DataStream, $MarkerSIze) {
    $Result = 0
    # Out-Host -InputObject "Marker size: $MarkerSIze"
    $MarkerSIzeS = $MarkerSIze - 1

    for ($i = $MarkerSIzeS; $i -lt $input_file.Length; $i++) {
        $chunk = $input_file.substring($i - $MarkerSIzeS, $MarkerSIze)
        # Out-Host -InputObject "$i : $chunk"
        if (isUnique($chunk)) {
            $Result = $i + 1
            break
        }
    }
    return $Result
}

$part1 = Find-Marker -DataStream $DataStream -MarkerSize 4
$part2 = Find-Marker -DataStream $DataStream -MarkerSize 14

Out-Host -InputObject "Result Part 1: $part1"
Out-Host -InputObject "Result Part 2: $part2"