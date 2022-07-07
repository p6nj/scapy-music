from os import system
system('COLOR 0C')
print('''
 .d8888b.                    888                        
d88P  Y88b                   888                        
Y88b.                        888                        
 "Y888b.    .d8888b  8888b.  88888b.  888  888 88888b.  
    "Y88b. d88P"        "88b 888 "88b 888  888 888 "88b 
      "888 888      .d888888 888  888 888  888 888  888 
Y88b  d88P Y88b.    888  888 888 d88P Y88b 888 888 d88P 
 "Y8888P"   "Y8888P "Y888888 88888P"   "Y88888 88888P"  
                                           888 888      
                                      Y8b d88P 888      
                                       "Y88P"  888      ''')
print('⛹️‍♂️ importing libs...')
from scapy.all import sniff,get_if_addr,conf
from numpy import sin,pi,linspace,float32
from contextlib import redirect_stdout
with redirect_stdout(None):from pygame.mixer import init,Sound

##SETTINGS
T=0.1 # duration of beeps
pitch_height_factor=7 # the pitch of beeps will be multiplied by this factor to cover a larger spectrum
pitch_height_offset=100 # the pitch of beeps will be summed with this value to be audible
fs = 44100 # sample rate used to generate, play and write audio
ignore_self=True # ignore packets generated by your interface
ignore_gateway=True # ignore packets generated by your router
volume=0.1 # volume of the audio output, from 0 to 1 but any value is acceptable
verbose=False # print IP adresses

x=linspace(0, T * 2 * pi, int(T * fs))
init(frequency=fs,size=32)
def play(hz):
    buffer = volume*sin(hz*x).astype(float32)
    sound = Sound(buffer)
    sound.play(0)

def beep(x):
	if verbose:print(x.src)
	for n in x['IP'].src.split('.'):play(int(n)*pitch_height_factor+pitch_height_offset)
print('\x1b[1A\x1b[2K✅ ready.')
system('COLOR 0A')
sniff(prn=lambda x:beep(x),filter='ip'+ignore_self*(' and not (ip src '+get_if_addr(conf.iface)+ignore_gateway*(' or ip src '+conf.route.route("0.0.0.0")[2])+')'),store=0)