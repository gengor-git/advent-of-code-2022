$input = Get-Content -Path .\day06\input.txt

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


for ($i = 3; $i -lt $input.Length; $i++) {
    $chunk = $input.substring($i - 3, 4)
    # Out-Host -InputObject "$i : $chunk"
    if (isUnique($chunk)) {
        $Result = $i + 1
        Out-Host -InputObject "Result Part 1: $Result"
        break
    }
}
for ($i = 13; $i -lt $input.Length; $i++) {
    $chunk = $input.substring($i - 13, 14)
    # Out-Host -InputObject "$i : $chunk"
    if (isUnique($chunk)) {
        $Result = $i + 1
        Out-Host -InputObject "Result Part 2: $Result"
        break
    }
}