import telepot

doorbellBot = telepot.Bot('5488078961:AAFaJivap_jWBhUzhWMHzKn7p_KTUw9bpF0')

doorbellBot.sendPhoto('@DoorbellCamTest', photo=open('/home/pi/Pictures/testImage.jpg', 'rb'))
    

