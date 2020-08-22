#!/usr/bin/bash
#################### font colors ####################
w="\033[00m"
r="\033[31;1m"
g="\033[32;1m"
y="\033[33;1m"
b="\033[34;1m"
p="\033[35;1m"
c="\033[36;1m"
W="\033[47m"
R="\033[41m"
B="\033[0;30m"

cat << EOF
EOF

#################### list commands ####################

run() {
        cd ~/saydog-framework/.core/ && python3 saydog.py --run
}

usage() {
        echo -e $w""
        echo -e $w"{"$B$W" SAYDOG FRAMEWORK "$w"}"
        echo -e $w""
        echo -e $w" usage with commands: saydog <"$g"options"$w">"
        echo -e $w" example: "$g"saydog run"$w
        echo -e $w""
        echo -e $g" Options:              Descriptions:"
        echo -e $w"---------------------------------------------------"
        echo -e $w" run                   running saydog framework"
        echo -e $w" install               installing all dependencies"
        echo -e $w" report                report about this tools"
        echo -e $w" update                update tools"
        echo -e $w"---------------------------------------------------"
        echo -e $w""
        exit
}

install() {
        echo
        echo -e " \033[41m  "$w$c" Toolname: "$p"saydog framework   \033[44m  "$w$c" Author: "$p"iqbalmh18"
        echo -e " \033[42m  "$w$c" Release : "$w"05-07-2020         \033[45m  "$w$c" Github: "$w"saydog.official"
        echo -e " \033[43m  "$w$c" Version : "$w"1.4.0              \033[46m  "$w$c" Region: "$w"Indonesia ["$r"ID"$w"]"
        echo
        echo -e $p"[*]"$w" prepare for installing all dependencies"
        echo -e $p"[*]"$w" this could take a while, do you want to continue?"
        echo -n -e $w"    press enter for continue and ("$y"ctrl+c"$w") for exiting ";read ask
        echo
        echo -e $p"[*]"$w" installing dependencies"
                if [ -f /data/data/com.termux/files/usr/bin/proot ]; then
                        echo -e $p"[*]"$w" proot is already exists!"
                else
                        echo -e $p"[*]"$w" installing proot package"
                        pkg install -y proot wget &> /dev//null
                        fi
                if [ -f /data/data/com.termux/files/usr/bin/java ]; then
                        echo -e $p"[*]"$w" java is already exists!"
                else
                        echo -e $p"[*]"$w" installing java package"
                        wget https://raw.githubusercontent.com/MasterDevX/java/master/installjava &> /dev//null && bash installjava &> /dev//null
                        fi
                if [ -f /data/data/com.termux/files/usr/bin/aapt ]; then
                        echo -e $p"[*]"$w" aapt is already exists!"
                else
                        echo -e $p"[*]"$w" installing aapt package"
                        pkg install -y aapt &> /dev//null
                        fi
                if [ -f /data/data/com.termux/files/usr/bin/npm ]; then
                        echo -e $p"[*]"$w" nodejs-lts is already exists!"
                else
                        echo -e $p"[*]"$w" installing nodejs-lts package"
                        pkg install -y nodejs-lts &> /dev//null
                        fi
                if [ -f /data/data/com.termux/files/usr/bin/apktool241 ]; then
                        echo -e $p"[*]"$w" apktool is already exists!"
                else
                        echo -e $p"[*]"$w" installing apktool package"
                        wget https://github.com/Lexiie/Termux-Apktool/raw/master/apktool_2.3.4_all.deb &> /dev//null && dpkg -i apktool_2.3.4_all.deb &> /dev//null;rm apktool_2.3.4_all.deb
                        wget -O apktool.jar https://bitbucket.org/iBotPeaches/apktool/downloads/apktool_2.3.4.jar &> /dev//null;mv apktool.jar ~/../usr/bin;chmod +x ~/../usr/bin/apktool.jar
                        wget -O apktool241 https://raw.githubusercontent.com/iBotPeaches/Apktool/master/scripts/linux/apktool &> /dev//null;wget -O apktool241.jar https://bitbucket.org/iBotPeaches/apktool/downloads/apktool_2.4.1.jar &> /dev//null;mv apktool241 ~/../usr/bin;mv apktool241.jar ~/../usr/bin;chmod +x ~/../usr/bin/apktool241;chmod +x ~/../usr/bin/apktool241.jar
                        fi
                if [ -f /data/data/com.termux/files/usr/bin/apk-signer ]; then
                        echo -e $p"[*]"$w" apk-signer is already exists!"
                else
                        echo -e $p"[*]"$w" installing apk-signer package"
                        npm install -g apk-signer &> /dev//null
                        fi
                if [ -f /data/data/com.termux/files/usr/bin/python ]; then
                        echo -e $p"[*]"$w" python is already exists!"
                else
                        echo -e $p"[*]"$w" installing python package"
                        pkg install -y python &> /dev//null
                        fi
                if [ -f /data/data/com.termux/files/usr/bin/python2 ]; then
                        echo -e $p"[*]"$w" python2 is already exists!"
                else
                        echo -e $p"[*]"$w" installing python2 package"
                        pkg install -y python2 &> /dev//null
                        fi
                if [ -f /data/data/com.termux/files/usr/bin/php ]; then
                        echo -e $p"[*]"$w" php is already exists!"
                else
                        echo -e $p"[*]"$w" installing php package"
                        pkg install -y php &> /dev//null
                        fi
                if [ -f /data/data/com.termux/files/usr/bin/nano ]; then
                        echo -e $p"[*]"$w" nano is already exists!"
                else
                        echo -e $p"[*]"$w" installing nano package"
                        pkg install -y nano &> /dev//null
                        fi
                if [ -f /data/data/com.termux/files/usr/bin/wget ]; then
                        echo -e $p"[*]"$w" wget is already exists!"
                else
                        echo -e $p"[*]"$w" installing wget package"
                        pkg install -y wget &> /dev//null
                        fi
                if [ -f /data/data/com.termux/files/usr/bin/curl ]; then
                        echo -e $p"[*]"$w" curl is already exists!"
                else
                        echo -e $p"[*]"$w" installing curl package"
                        pkg install -y curl &> /dev//null
                        fi
                if [ -f /data/data/com.termux/files/usr/bin/zip ]; then
                        echo -e $p"[*]"$w" zip is already exists!"
                else
                        echo -e $p"[*]"$w" installing zip package"
                        pkg install -y zip unzip &> /dev//null
                        fi
                if [ -f /data/data/com.termux/files/usr/bin/gpg ]; then
                        echo -e $p"[*]"$w" gpg is already exists!"
                else
                        echo -e $p"[*]"$w" installing gpg package"
                        pkg install -y gnupg &> /dev//null
                        fi
                if [ -f /data/data/com.termux/files/usr/bin/tor ]; then
                        echo -e $p"[*]"$w" tor is already exists!"
                else
                        echo -e $p"[*]"$w" installing tor package"
                        pkg install -y tor &> /dev//null
                        fi
                if [ -f /data/data/com.termux/files/usr/bin/which ]; then
                        echo -e $p"[*]"$w" which is already exists!"
                else
                        echo -e $p"[*]"$w" installing which package"
                        pkg install -y debianutils &> /dev//null
                        fi
                if [ -f /data/data/com.termux/files/usr/bin/espeak ]; then
                        echo -e $p"[*]"$w" espeak is already exists!"
                else
                        echo -e $p"[*]"$w" installing espeak package"
                        pkg install -y espeak &> /dev//null
                        fi
                if [ -f /data/data/com.termux/files/usr/bin/msfconsole ]; then
                        echo -e $p"[*]"$w" metasploit is already exists!"
                else
                        echo -e $p"[*]"$w" metasploit is doesn't exists"
                        echo -e $p"[*]"$w" install it with cmd:"
                        echo -e $g"    pkg install unstable-repo"
                        echo -e $g"    pkg install metasploit"
                        fi
        echo
        echo -e $p"[*]"$w" package has been installed"
        echo -e $p"[*]"$w" prepare for installing python module:"
        echo
        pip2 install requests mechanize uncompyle6 &> /dev//null
        python3 -m pip install --upgrade pip &> /dev//null
        python3 -m pip install yagmail &> /dev//null
        python3 -m pip install -r requirements.txt &> /dev//null
        python3 -m pip list
        echo
        echo -e $g"[*]"$w" All dependencies successfuly installed"
        echo -e $g"[*]"$w" thank you for installing saydog-framework :D"
        echo -e $g"[*]"$w" for information about update saydog framework"
        echo -e $g"[*]"$w" follow me on instagram:- "$g"@saydog.official"$w
        saydog
        python3 ~/saydog-framework/.core/main/config_apktool241.py
}

update() {
        bash ~/saydog-framework/update.sh
}
#################### main argv ####################

ARGS=$(printf '%q ' "$@")

if [ -z "$*" ]; then
        usage
elif [ $1 == "run" ]; then
        run
elif [ $1 == "install" ]; then
        install
elif [ $1 == "report" ]; then
        xdg-open https://github.com/saydog-official/saydog-framework/issues
elif [ $1 == "update" ]; then
        update
        echo -e $g"[+]"$w" successfully update saydog framework"
        echo -e $g"[+]"$w" please (exit) and restart the tools"
else
        usage
fi
