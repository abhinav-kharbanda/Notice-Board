#!/bin/bash

FILE="/tmp/out.$$"
GREP="/bin/grep"
#....
# Make sure only root can run our script
if [ "$(id -u)" != "0" ]; then
   echo "This script must be run as root, run -> sudo install.sh " 1>&2
   exit 1
fi
echo "Installing... do not exit"
#
cd
echo "sudo ./startSlides.sh" >> .bashrc
printf "Enter the URL you want to configure?  -> "
read URL

cat <<EOF >startSlides.sh
#!/bin/bash
if [ -a /home/pi/.config/epiphany/session_state.xml ]; 
	then
		rm /home/pi/.config/epiphany/session_state.xml;
fi
# echo "third if"
unclutter -display :0 -noevents -grab &
# echo "unclutter"
epiphany "$URL" &
sleep 40
xdotool search --class epiphany windowactivate
xdotool key F11
xdotool key F5
sleep 40
while ps ax|grep -v grep| grep epiphany && ifconfig $ipadd | grep inet; do
	sleep 20
	# "still sleepin";
done

sudo shutdown -r now


EOF

echo "rebooting"
reboot
