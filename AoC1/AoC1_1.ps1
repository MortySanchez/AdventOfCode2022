<#
    Author: MortySanchez
    Date: 02.12.2022
    Title: AoC1_1.ps1
    Description: AdventOfCode2022 Challenge Day 1 Part 1
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
for ([int] $index = 0; $index -lt $elfes.Length; $index++) {
    if ($elfes[$index] -gt $elfes[$indexHighElf]) {
        $indexHighElf = $index
    }
}

Write-Host ("Elf number {0} is the highest elf with {1} calories." -f ($indexHighElf + 1), $elfes[$indexHighElf])
