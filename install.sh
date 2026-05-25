#!/usr/bin/bash

echo "OpenSoftware-World cannot be held responsible for any data loss that may occur during the installation of the calculator. (This script copies the calc file to the /usr/bin directory, so please make sure there is no file named calc in that directory.)"
read -p "Would you like to download the Calc app by copying it to the /usr/bin directory? " answer
read -p "Please select the calculator language. (TR/EN) " lang

if [[ "$answer" == "y" || "$answer" == "Y" ]]; then
    full_path="Install/$lang/calc"
    sudo cp $full_path /usr/bin/
    sudo chmod +x /usr/bin/calc
    echo "The Calc app has been successfully downloaded."
else
    echo "The download of the Calc app has been canceled."
fi

# Changes will be made to the uninstall files for Linux.