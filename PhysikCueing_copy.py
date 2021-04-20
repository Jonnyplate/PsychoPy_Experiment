#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Demo of MovieStim

Different systems have different sets of codecs.
avbin (which PsychoPy uses to load movies) seems not to load compressed audio on all systems.
To create a movie that will play on all systems I would recommend using the format:
    video: H.264 compressed,
    audio: Linear PCM
"""

from __future__ import division
from __future__ import print_function

from psychopy import visual, core, event, constants

import time, os


#window size and video position variables
movsizeX=int(2700/4)
movsizeY=int(900/4)
winsizeX=1440
winsizeY=900
buttonsize=30

#position variables
class pos:
    pass

pos.left=-movsizeX/2#-winsizeX/2
pos.right=movsizeX/2#+winsizeX/2
pos.top=movsizeY/2+100#+winsizeY/2
pos.bottom=-movsizeY/2-100#-winsizeY/2
pos.topleft=[pos.left,pos.top]
pos.topright=[pos.right,pos.top]
pos.bottomleft=[pos.left,pos.bottom]
pos.bottomright=[pos.right,pos.bottom]
#------------------------------------------


win = visual.Window((1440, 900)
,fullscr=True
,allowStencil=True)
mouse=event.Mouse()
globalClock = core.Clock()
mov=[1,2,3,4]
box=[1,2,3,4]
shouldflip=[1,2,3,4]
videopath=[1,2,3,4]
backbutton=[0,1,2,3]
forwardbutton=[0,1,2,3]
tobeginningbutton=[0,1,2,3]


videopath[0]=r'Videos/AT_otherPhase_easier_Nr35_auto.mp4'
videopath[1]=r'Videos/AT_otherPhase_easier_Nr35_auto.mp4'
videopath[2]=r'Videos/AT_otherPhase_easier_Nr35_auto.mp4'
videopath[3]=r'Videos/AT_otherPhase_easier_Nr35_auto.mp4'
for i in range(0,4,1):
    videopath[0] = os.path.join(os.getcwd(), videopath[0])
backbuttonpath=r'Buttons/Back.jpg'
backbuttonpath=os.path.join(os.getcwd(), backbuttonpath)
forwardbuttonpath=r'Buttons/Forward.jpg'
forwardbuttonpath=os.path.join(os.getcwd(), forwardbuttonpath)
tobeginningbuttonpath=r'Buttons/Tobeginning.jpg'
tobeginningbuttonpath=os.path.join(os.getcwd(), tobeginningbuttonpath)


mov[0] = visual.MovieStim3(win, videopath[0], size=(movsizeX, movsizeY), pos=pos.topleft,
    flipVert=False, flipHoriz=False, loop=False, noAudio=True)
mov[1] = visual.MovieStim3(win, videopath[1], size=(movsizeX, movsizeY), pos=pos.topright,
    flipVert=False, flipHoriz=False, loop=False, noAudio=True)
mov[2] = visual.MovieStim3(win, videopath[2], size=(movsizeX, movsizeY), pos=pos.bottomleft,
    flipVert=False, flipHoriz=False, loop=False, noAudio=True)
mov[3] = visual.MovieStim3(win, videopath[3], size=(movsizeX, movsizeY), pos=pos.bottomright,
    flipVert=False, flipHoriz=False, loop=False, noAudio=True)

box[0]=visual.Rect(win, width=25,height=25, units="pix", pos=[pos.topleft[0],pos.topleft[1]-movsizeY/2-50],fillColor="white")
box[1]=visual.Rect(win, width=25,height=25, units="pix", pos=[pos.topright[0],pos.topright[1]-movsizeY/2-50],fillColor="white")
box[2]=visual.Rect(win, width=25,height=25, units="pix", pos=[pos.bottomleft[0],pos.bottomleft[1]-movsizeY/2-50],fillColor="white")
box[3]=visual.Rect(win, width=25,height=25, units="pix", pos=[pos.bottomright[0],pos.bottomright[1]-movsizeY/2-50],fillColor="white")

backbutton[0]=visual.ImageStim(win,backbuttonpath, size=buttonsize, units="pix", pos=[pos.topleft[0]-100,pos.topleft[1]-movsizeY/2-50])
backbutton[1]=visual.ImageStim(win,backbuttonpath, size=buttonsize, units="pix", pos=[pos.topright[0]-100,pos.topright[1]-movsizeY/2-50])
backbutton[2]=visual.ImageStim(win,backbuttonpath, size=buttonsize, units="pix", pos=[pos.bottomleft[0]-100,pos.bottomleft[1]-movsizeY/2-50])
backbutton[3]=visual.ImageStim(win,backbuttonpath, size=buttonsize, units="pix", pos=[pos.bottomright[0]-100,pos.bottomright[1]-movsizeY/2-50])

forwardbutton[0]=visual.ImageStim(win,forwardbuttonpath, size=buttonsize, units="pix", pos=[pos.topleft[0]+100,pos.topleft[1]-movsizeY/2-50])
forwardbutton[1]=visual.ImageStim(win,forwardbuttonpath, size=buttonsize, units="pix", pos=[pos.topright[0]+100,pos.topright[1]-movsizeY/2-50])
forwardbutton[2]=visual.ImageStim(win,forwardbuttonpath, size=buttonsize, units="pix", pos=[pos.bottomleft[0]+100,pos.bottomleft[1]-movsizeY/2-50])
forwardbutton[3]=visual.ImageStim(win,forwardbuttonpath, size=buttonsize, units="pix", pos=[pos.bottomright[0]+100,pos.bottomright[1]-movsizeY/2-50])

tobeginningbutton[0]=visual.ImageStim(win,tobeginningbuttonpath, size=buttonsize, units="pix", pos=[pos.topleft[0]-150,pos.topleft[1]-movsizeY/2-50])
tobeginningbutton[1]=visual.ImageStim(win,tobeginningbuttonpath, size=buttonsize, units="pix", pos=[pos.topright[0]-150,pos.topright[1]-movsizeY/2-50])
tobeginningbutton[2]=visual.ImageStim(win,tobeginningbuttonpath, size=buttonsize, units="pix", pos=[pos.bottomleft[0]-150,pos.bottomleft[1]-movsizeY/2-50])
tobeginningbutton[3]=visual.ImageStim(win,tobeginningbuttonpath, size=buttonsize, units="pix", pos=[pos.bottomright[0]-150,pos.bottomright[1]-movsizeY/2-50])

answerlog=False
newvidaction=False
newboxaction=False
playlog=5
buttonWas = 'up'

#predraw boxes and movie images

shouldflip[0]= mov[0].play()
shouldflip[1]= mov[1].play()
shouldflip[2]= mov[2].play()
shouldflip[3]= mov[3].play()
mov[0].pause()
mov[1].pause()
mov[2].pause()
mov[3].pause()
while True: #mov[0].status != constants.FINISHED
    win.flip()
    if mouse.getPressed()[0]:
        if  buttonWas=='up':
            #check if mouse was pressed in a relevant space
            for i in range(0,4,1):
                if box[i].contains(mouse):
                    newboxaction=True
                    answerlog=i
                elif mov[i].contains(mouse):
                    newvidaction=True
                    playlog=i
                elif backbutton[i].contains(mouse):
                    ntime = max(mov[i].getCurrentFrameTime() - 1.0, 0.0)
                    mov[i].seek(ntime)
                elif forwardbutton[i].contains(mouse):
                    ntime = max(mov[i].getCurrentFrameTime() + 1.0, 0.0)
                    mov[i].seek(ntime)                   
                elif tobeginningbutton[i].contains(mouse):
                    mov[i].seek(0)
            buttonWas = 'down'
    else:
            buttonWas = 'up'
    if newboxaction:
        for b in box:
            b.fillColor="white"
        box[answerlog].fillColor="black"
    if shouldflip[0]:
        pass
        # Movie has already been drawn , so just draw text stim and flip
    else:
        # Give the OS a break if a flip is not needed
        time.sleep(0.001)
    # Drawn movie stim again. Updating of movie stim frames as necessary
    # is handled internally. 
    #check if the mouse was pressed on a video
    if newvidaction:
        newvidaction=False
        for i in range(0,4,1):
            if i != playlog:
                mov[i].pause()
        if mov[playlog].status== constants.PLAYING:
            mov[playlog].pause()
        else:
            mov[playlog].play()
    #draw buttons and videos before next flip
    for i in range(0,4,1):
        shouldflip[i]=mov[i].draw()
        box[i].draw()
        backbutton[i].draw()
        forwardbutton[i].draw()
        tobeginningbutton[i].draw()
        if mov[i].status not in [constants.PLAYING, constants.PAUSED]:
            mov[i].loadMovie(videopath[i])
            shouldflip[i] = mov[i].play()
            mov[i].pause()
    #check or escape key to exit experiment
    for key in event.getKeys():
        if key in ['escape', 'q']:
            win.close()
            core.quit()

win.close()
core.quit()

# The contents of this file are in the public domain.
#choose video 
# if mouse.buttons[0]:
#     if buttonWas=='up':
#         if box1.contains(mouse):
#             frame1on = not frame1on
#         elif box2.contains(mouse):
#             frame2on = not frame2on
#         elif box3.contains(mouse):
#             frame3on = not frame3on
#     buttonWas = 'down'
# else:
#     buttonWas = 'up'