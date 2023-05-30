$subred = (Get-NetRoute -DestinationPrefix 0.0.0.0/0).NextHop
Write-Host "== Determinando tu gateway ..."
Write-Host "Tu gateway: $subred"

$rango = $subred.Substring(0,$subred.IndexOf(".") + 1 + $subred.Substring($subred.IndexOf(".") + 1).IndexOf(".") + 3)
Write-Host "== Deteminando tu rango de subred ..."
echo $rango

$punto = $rango.EndsWith(".")
if ($punto -like "False" )
{
    $rango = $rango + "."
}

$rango_ip = @(1..254)

Write-Output ""
Write-Host "-- Subred actual:"
Write-Host "Escaneando: " -NoNewline ; Write-Host $rango -NoNewline; Write-Host "0/24" -ForegroundColor Red
Write-Output ""
foreach ($r in $rango_ip )
{
    $actual = $rango + $r 
    $rensponse = Test-Connection $actual -Quiet -Count 1
    if ( $rensponse -eq "True" )
    {
        Write-Output ""
        Write-Host "Host responde: " -NoNewline; Write-Host $Actual -ForegroundColor Green
    }
}