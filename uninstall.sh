#!/usr/bin/bash

read -p "Do you want to remove the Calc application by deleting it from the /usr/bin directory? " answer

if [[ "$answer" == "y" || "$answer" == "Y" ]]; then
    sudo rm -f /usr/bin/calc
    echo "The Calc app has been successfully uninstalled."
else
    echo "The uninstallation of the Calc app has been canceled."
fi