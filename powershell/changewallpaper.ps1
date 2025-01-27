# Define the Imgur URL of the image
$imgurUrl = "https://i.imgur.com/pOd3crl.png"  # Replace with your Imgur image URL

# Define the local path where the image will be saved
$localPath = "$env:TEMP\wallpaper.jpg"

# Download the image
Invoke-WebRequest -Uri $imgurUrl -OutFile $localPath

# Function to set the wallpaper
function Set-Wallpaper {
    param (
        [string]$path
    )

    # Use the SystemParametersInfo function from user32.dll to set the wallpaper
    $SPI_SETDESKWALLPAPER = 20
    $SPIF_UPDATEINIFILE = 0x01
    $SPIF_SENDCHANGE = 0x02

    Add-Type @"
    using System;
    using System.Runtime.InteropServices;
    public class Wallpaper {
        [DllImport("user32.dll", CharSet = CharSet.Auto)]
        public static extern int SystemParametersInfo(int uAction, int uParam, string lpvParam, int fuWinIni);
    }
"@

    [Wallpaper]::SystemParametersInfo($SPI_SETDESKWALLPAPER, 0, $path, $SPIF_UPDATEINIFILE -bor $SPIF_SENDCHANGE)
}

# Set the downloaded image as wallpaper
Set-Wallpaper -path $localPath
