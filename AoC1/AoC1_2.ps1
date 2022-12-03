<#
    Author: MortySanchez
    Date: 02.12.2022
    Title: AoC1_2.ps1
    Description: AdventOfCode2022 Challenge Day 1 Part 2
    Status: Solved!
#>

$filePath = "$PSScriptRoot\data.txt"
$fileContent = Get-Content -Path $filePath

$elfCounter = 0
for ([int] $index = 0; $index -lt $fileContent.Length; $index++) {
    if ($fileContent[$index] -eq '') {
        $elfCounter++
    }
}

$elfes = [int[]]::new(($elfCounter + 1))

[int] $elfIndex = 0

for ([int] $index = 0; $index -lt $fileContent.Length; $index++) {
    if ($null -eq $fileContent[$index] -or '' -eq $fileContent[$index]) {
        $elfIndex++
        continue
    }

    if ($fileContent[$index]) {
        $elfes[$elfIndex] += [Convert]::ToInt32($fileContent[$index])
    }
}

[int] $indexHighElf = 0
[int] $indexSecondElf = 0
[int] $indexThirdElf = 0
for ([int] $index = 0; $index -lt $elfes.Length; $index++) {
    if ($elfes[$index] -gt $elfes[$indexHighElf]) {
        $indexThirdElf = $indexSecondElf
        $indexSecondElf = $indexHighElf
        $indexHighElf = $index
        
    }
}

"Highest elf on index {0} with {1} calories." -f $indexHighElf, $elfes[$indexHighElf]
"Second highest elf on index {0} with {1} calories." -f $indexSecondElf, $elfes[$indexSecondElf]
"Third highest elf on index {0} with {1} calories." -f $indexThirdElf, $elfes[$indexThirdElf]

"Total calories: {0}" -f ($elfes[$indexHighElf] + $elfes[$indexSecondElf] + $elfes[$indexThirdElf])
