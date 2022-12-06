$input_file = Get-Content -Path .\day06\input.txt

function isUnique($datastream) {
    # Out-Host -InputObject "Datastream: $datastream"
    $val = $datastream[-1]
    $compare = $datastream.substring(0, $datastream.Length - 1)
    # Out-Host -InputObject "Searching for `"$val`" in `"$compare`""
    if (-not ($compare.contains($val))) {
        if ($datastream.Length -ge 3) {
            return isUnique($compare)
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

function Find-Marker($datastream, $markerSize) {
    $Result = 0
    # Out-Host -InputObject "Marker size: $markerSize"
    $markerSizeS = $markerSize - 1

    for ($i = $markerSizeS; $i -lt $input_file.Length; $i++) {
        $chunk = $input_file.substring($i - $markerSizeS, $markerSize)
        # Out-Host -InputObject "$i : $chunk"
        if (isUnique($chunk)) {
            $Result = $i + 1
            break
        }
    }

    return $Result
}

$part1 = Find-Marker -datastream $datastream -markerSize 4
$part2 = Find-Marker -datastream $datastream -markerSize 14

Out-Host -InputObject "Result Part 1: $part1"
Out-Host -InputObject "Result Part 2: $part2"