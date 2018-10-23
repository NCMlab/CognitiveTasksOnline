#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.85.1),
    on Mon Oct 22 15:01:08 2018
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, gui, visual, core, data, event, logging, sound
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = u'PaperFolding'  # from the Builder filename that created this script
expInfo = {u'session': u'001', u'participant': u''}
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=u'/Users/jasonsteffener/Documents/GitHub/CognitiveTasks/PaperFolding/PaperFolding.psyexp',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1440, 900), fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor=u'testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    units='pix')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "Instructions"
InstructionsClock = core.Clock()
Instruct = visual.TextStim(win=win, name='Instruct',
    text=u'Paper Folding\n\nFor this task you will see a drawing of a piece of paper that gets folded multiple times. \nAfter folding, a hole is punched through the paper. \n\nDecide which of the five options at the bottom of the screen reflects the pattern of holes in the paper once it has been unfolded.\n\nPress any key to perform practice trials.',
    font=u'Arial',
    pos=(0, 0), height=40, wrapWidth=1000, ori=0, 
    color=u'black', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()
image = visual.ImageStim(
    win=win, name='image',
    image='sin', mask=None,
    ori=0, pos=(0, 200), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
CFig1 = visual.ImageStim(
    win=win, name='CFig1',
    image='sin', mask=None,
    ori=0, pos=(-350, -75), size=(150, 150),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
CFig2 = visual.ImageStim(
    win=win, name='CFig2',
    image='sin', mask=None,
    ori=0, pos=(-175, -75), size=(150, 150),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
CFig3 = visual.ImageStim(
    win=win, name='CFig3',
    image='sin', mask=None,
    ori=0, pos=(0, -75), size=(150, 150),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
CFig4 = visual.ImageStim(
    win=win, name='CFig4',
    image='sin', mask=None,
    ori=0, pos=(175, -75), size=(150, 150),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
CFig5 = visual.ImageStim(
    win=win, name='CFig5',
    image='sin', mask=None,
    ori=0, pos=(350, -75), size=(150,150),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
Opt1 = visual.TextStim(win=win, name='Opt1',
    text=u'1',
    font=u'Arial',
    pos=(-365, -175), height=40, wrapWidth=None, ori=0, 
    color=u'black', colorSpace='rgb', opacity=1,
    depth=-6.0);
Opt2 = visual.TextStim(win=win, name='Opt2',
    text=u'2',
    font=u'Arial',
    pos=(-190, -175), height=40, wrapWidth=None, ori=0, 
    color=u'black', colorSpace='rgb', opacity=1,
    depth=-7.0);
Opt3 = visual.TextStim(win=win, name='Opt3',
    text=u'3',
    font=u'Arial',
    pos=(0, -175), height=40, wrapWidth=None, ori=0, 
    color=u'black', colorSpace='rgb', opacity=1,
    depth=-8.0);
Opt4 = visual.TextStim(win=win, name='Opt4',
    text=u'4',
    font=u'Arial',
    pos=(190, -175), height=40, wrapWidth=None, ori=0, 
    color=u'black', colorSpace='rgb', opacity=1,
    depth=-9.0);
OPt5 = visual.TextStim(win=win, name='OPt5',
    text=u'5',
    font=u'Arial',
    pos=(365, -175), height=40, wrapWidth=None, ori=0, 
    color=u'black', colorSpace='rgb', opacity=1,
    depth=-10.0);

# Initialize components for Routine "Feedback1"
Feedback1Clock = core.Clock()
Prac1Feedback = visual.TextStim(win=win, name='Prac1Feedback',
    text=u'Here the correct answer is 2. \nThe paper is folded over once at a diagonal, starting from the upper right. Then the upper left corner is folded down. Therefore, the  hole punch gores through 4 total sheets symmetrically on each side of the diagonal.\n\nPress any key to continue.',
    font=u'Arial',
    pos=(300, 0), height=30, wrapWidth=600, ori=0, 
    color=u'black', colorSpace='rgb', opacity=1,
    depth=0.0);
Prac1Fold = visual.ImageStim(
    win=win, name='Prac1Fold',
    image=u'altAfold3.bmp', mask=None,
    ori=0, pos=(0, 200), size=(556, 144),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
Prac1Choice = visual.ImageStim(
    win=win, name='Prac1Choice',
    image='sin', mask=None,
    ori=0, pos=(-175, -75), size=(150,150),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

# Initialize components for Routine "crosshair"
crosshairClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text=u'+',
    font=u'Arial',
    pos=(0, 0), height=40, wrapWidth=None, ori=0, 
    color=u'black', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()
image = visual.ImageStim(
    win=win, name='image',
    image='sin', mask=None,
    ori=0, pos=(0, 200), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
CFig1 = visual.ImageStim(
    win=win, name='CFig1',
    image='sin', mask=None,
    ori=0, pos=(-350, -75), size=(150, 150),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
CFig2 = visual.ImageStim(
    win=win, name='CFig2',
    image='sin', mask=None,
    ori=0, pos=(-175, -75), size=(150, 150),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
CFig3 = visual.ImageStim(
    win=win, name='CFig3',
    image='sin', mask=None,
    ori=0, pos=(0, -75), size=(150, 150),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
CFig4 = visual.ImageStim(
    win=win, name='CFig4',
    image='sin', mask=None,
    ori=0, pos=(175, -75), size=(150, 150),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
CFig5 = visual.ImageStim(
    win=win, name='CFig5',
    image='sin', mask=None,
    ori=0, pos=(350, -75), size=(150,150),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
Opt1 = visual.TextStim(win=win, name='Opt1',
    text=u'1',
    font=u'Arial',
    pos=(-365, -175), height=40, wrapWidth=None, ori=0, 
    color=u'black', colorSpace='rgb', opacity=1,
    depth=-6.0);
Opt2 = visual.TextStim(win=win, name='Opt2',
    text=u'2',
    font=u'Arial',
    pos=(-190, -175), height=40, wrapWidth=None, ori=0, 
    color=u'black', colorSpace='rgb', opacity=1,
    depth=-7.0);
Opt3 = visual.TextStim(win=win, name='Opt3',
    text=u'3',
    font=u'Arial',
    pos=(0, -175), height=40, wrapWidth=None, ori=0, 
    color=u'black', colorSpace='rgb', opacity=1,
    depth=-8.0);
Opt4 = visual.TextStim(win=win, name='Opt4',
    text=u'4',
    font=u'Arial',
    pos=(190, -175), height=40, wrapWidth=None, ori=0, 
    color=u'black', colorSpace='rgb', opacity=1,
    depth=-9.0);
OPt5 = visual.TextStim(win=win, name='OPt5',
    text=u'5',
    font=u'Arial',
    pos=(365, -175), height=40, wrapWidth=None, ori=0, 
    color=u'black', colorSpace='rgb', opacity=1,
    depth=-10.0);

# Initialize components for Routine "Feedback2"
Feedback2Clock = core.Clock()
Prac2Feedback = visual.TextStim(win=win, name='Prac2Feedback',
    text=u'Here the correct answer is 2. The paper is folded from the bottom right corner once, then folded again from the tapered right side. However, the hold punch misses the second fold.\n\nPress any key to continue.',
    font=u'Arial',
    pos=(300, 0), height=30, wrapWidth=600, ori=0, 
    color=u'black', colorSpace='rgb', opacity=1,
    depth=0.0);
Prac2Fold = visual.ImageStim(
    win=win, name='Prac2Fold',
    image=u'altAfold8.bmp', mask=None,
    ori=0, pos=(0, 200), size=(556, 144),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
Prac2Choice = visual.ImageStim(
    win=win, name='Prac2Choice',
    image=u'altAchoice82.bmp', mask=None,
    ori=0, pos=(-175, -75), size=(150, 150),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

# Initialize components for Routine "crosshair"
crosshairClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text=u'+',
    font=u'Arial',
    pos=(0, 0), height=40, wrapWidth=None, ori=0, 
    color=u'black', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "GetReady"
GetReadyClock = core.Clock()
GetReady2 = visual.TextStim(win=win, name='GetReady2',
    text=u'Get ready to perform the task with no feedback.\nPlease try to respond as quickly and accurately as possible.\n\nPress any key to begin.',
    font=u'Arial',
    pos=(0, 0), height=40, wrapWidth=None, ori=0, 
    color=u'black', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "crosshair"
crosshairClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text=u'+',
    font=u'Arial',
    pos=(0, 0), height=40, wrapWidth=None, ori=0, 
    color=u'black', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()
image = visual.ImageStim(
    win=win, name='image',
    image='sin', mask=None,
    ori=0, pos=(0, 200), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
CFig1 = visual.ImageStim(
    win=win, name='CFig1',
    image='sin', mask=None,
    ori=0, pos=(-350, -75), size=(150, 150),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
CFig2 = visual.ImageStim(
    win=win, name='CFig2',
    image='sin', mask=None,
    ori=0, pos=(-175, -75), size=(150, 150),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
CFig3 = visual.ImageStim(
    win=win, name='CFig3',
    image='sin', mask=None,
    ori=0, pos=(0, -75), size=(150, 150),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
CFig4 = visual.ImageStim(
    win=win, name='CFig4',
    image='sin', mask=None,
    ori=0, pos=(175, -75), size=(150, 150),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
CFig5 = visual.ImageStim(
    win=win, name='CFig5',
    image='sin', mask=None,
    ori=0, pos=(350, -75), size=(150,150),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
Opt1 = visual.TextStim(win=win, name='Opt1',
    text=u'1',
    font=u'Arial',
    pos=(-365, -175), height=40, wrapWidth=None, ori=0, 
    color=u'black', colorSpace='rgb', opacity=1,
    depth=-6.0);
Opt2 = visual.TextStim(win=win, name='Opt2',
    text=u'2',
    font=u'Arial',
    pos=(-190, -175), height=40, wrapWidth=None, ori=0, 
    color=u'black', colorSpace='rgb', opacity=1,
    depth=-7.0);
Opt3 = visual.TextStim(win=win, name='Opt3',
    text=u'3',
    font=u'Arial',
    pos=(0, -175), height=40, wrapWidth=None, ori=0, 
    color=u'black', colorSpace='rgb', opacity=1,
    depth=-8.0);
Opt4 = visual.TextStim(win=win, name='Opt4',
    text=u'4',
    font=u'Arial',
    pos=(190, -175), height=40, wrapWidth=None, ori=0, 
    color=u'black', colorSpace='rgb', opacity=1,
    depth=-9.0);
OPt5 = visual.TextStim(win=win, name='OPt5',
    text=u'5',
    font=u'Arial',
    pos=(365, -175), height=40, wrapWidth=None, ori=0, 
    color=u'black', colorSpace='rgb', opacity=1,
    depth=-10.0);

# Initialize components for Routine "crosshair"
crosshairClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text=u'+',
    font=u'Arial',
    pos=(0, 0), height=40, wrapWidth=None, ori=0, 
    color=u'black', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "ThankYou"
ThankYouClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text=u'Thank You',
    font=u'Arial',
    pos=(0, 0), height=40, wrapWidth=None, ori=0, 
    color=u'black', colorSpace='rgb', opacity=1,
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Instructions"-------
t = 0
InstructionsClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
StartPractice = event.BuilderKeyResponse()
# keep track of which components have finished
InstructionsComponents = [Instruct, StartPractice]
for thisComponent in InstructionsComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Instructions"-------
while continueRoutine:
    # get current time
    t = InstructionsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Instruct* updates
    if t >= 0.0 and Instruct.status == NOT_STARTED:
        # keep track of start time/frame for later
        Instruct.tStart = t
        Instruct.frameNStart = frameN  # exact frame index
        Instruct.setAutoDraw(True)
    
    # *StartPractice* updates
    if t >= 0.0 and StartPractice.status == NOT_STARTED:
        # keep track of start time/frame for later
        StartPractice.tStart = t
        StartPractice.frameNStart = frameN  # exact frame index
        StartPractice.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(StartPractice.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if StartPractice.status == STARTED:
        theseKeys = event.getKeys()
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            StartPractice.keys = theseKeys[-1]  # just the last key pressed
            StartPractice.rt = StartPractice.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instructions"-------
for thisComponent in InstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if StartPractice.keys in ['', [], None]:  # No response was made
    StartPractice.keys=None
thisExp.addData('StartPractice.keys',StartPractice.keys)
if StartPractice.keys != None:  # we had a response
    thisExp.addData('StartPractice.rt', StartPractice.rt)
thisExp.nextEntry()
# the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(u'CognitiveTaskSetupFiles - PaperFold.csv', selection=u'[0]'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial.keys():
        exec(paramName + '= thisTrial.' + paramName)

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial.keys():
            exec(paramName + '= thisTrial.' + paramName)
    
    # ------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    image.setImage(Stimulus)
    image.setSize((556,144))
    CFig1.setImage(Choice1)
    CFig2.setImage(Choice2)
    CFig3.setImage(Choice3)
    CFig4.setImage(Choice4)
    key_resp_2 = event.BuilderKeyResponse()
    # keep track of which components have finished
    trialComponents = [image, CFig1, CFig2, CFig3, CFig4, CFig5, Opt1, Opt2, Opt3, Opt4, OPt5, key_resp_2]
    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "trial"-------
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image* updates
        if t >= 0.0 and image.status == NOT_STARTED:
            # keep track of start time/frame for later
            image.tStart = t
            image.frameNStart = frameN  # exact frame index
            image.setAutoDraw(True)
        
        # *CFig1* updates
        if t >= 0.0 and CFig1.status == NOT_STARTED:
            # keep track of start time/frame for later
            CFig1.tStart = t
            CFig1.frameNStart = frameN  # exact frame index
            CFig1.setAutoDraw(True)
        
        # *CFig2* updates
        if t >= 0.0 and CFig2.status == NOT_STARTED:
            # keep track of start time/frame for later
            CFig2.tStart = t
            CFig2.frameNStart = frameN  # exact frame index
            CFig2.setAutoDraw(True)
        
        # *CFig3* updates
        if t >= 0.0 and CFig3.status == NOT_STARTED:
            # keep track of start time/frame for later
            CFig3.tStart = t
            CFig3.frameNStart = frameN  # exact frame index
            CFig3.setAutoDraw(True)
        
        # *CFig4* updates
        if t >= 0.0 and CFig4.status == NOT_STARTED:
            # keep track of start time/frame for later
            CFig4.tStart = t
            CFig4.frameNStart = frameN  # exact frame index
            CFig4.setAutoDraw(True)
        
        # *CFig5* updates
        if t >= 0.0 and CFig5.status == NOT_STARTED:
            # keep track of start time/frame for later
            CFig5.tStart = t
            CFig5.frameNStart = frameN  # exact frame index
            CFig5.setAutoDraw(True)
        if CFig5.status == STARTED:  # only update if drawing
            CFig5.setImage(Choice5, log=False)
        
        # *Opt1* updates
        if t >= 0.0 and Opt1.status == NOT_STARTED:
            # keep track of start time/frame for later
            Opt1.tStart = t
            Opt1.frameNStart = frameN  # exact frame index
            Opt1.setAutoDraw(True)
        
        # *Opt2* updates
        if t >= 0.0 and Opt2.status == NOT_STARTED:
            # keep track of start time/frame for later
            Opt2.tStart = t
            Opt2.frameNStart = frameN  # exact frame index
            Opt2.setAutoDraw(True)
        
        # *Opt3* updates
        if t >= 0.0 and Opt3.status == NOT_STARTED:
            # keep track of start time/frame for later
            Opt3.tStart = t
            Opt3.frameNStart = frameN  # exact frame index
            Opt3.setAutoDraw(True)
        
        # *Opt4* updates
        if t >= 0.0 and Opt4.status == NOT_STARTED:
            # keep track of start time/frame for later
            Opt4.tStart = t
            Opt4.frameNStart = frameN  # exact frame index
            Opt4.setAutoDraw(True)
        
        # *OPt5* updates
        if t >= 0.0 and OPt5.status == NOT_STARTED:
            # keep track of start time/frame for later
            OPt5.tStart = t
            OPt5.frameNStart = frameN  # exact frame index
            OPt5.setAutoDraw(True)
        
        # *key_resp_2* updates
        if t >= 0.0 and key_resp_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_2.tStart = t
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if key_resp_2.status == STARTED:
            theseKeys = event.getKeys(keyList=['1', '2', '3', '4', '5'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_2.keys = theseKeys[-1]  # just the last key pressed
                key_resp_2.rt = key_resp_2.clock.getTime()
                # was this 'correct'?
                if (key_resp_2.keys == str(Corr)) or (key_resp_2.keys == Corr):
                    key_resp_2.corr = 1
                else:
                    key_resp_2.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
        key_resp_2.keys=None
        # was no response the correct answer?!
        if str(Corr).lower() == 'none':
           key_resp_2.corr = 1  # correct non-response
        else:
           key_resp_2.corr = 0  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('key_resp_2.keys',key_resp_2.keys)
    trials.addData('key_resp_2.corr', key_resp_2.corr)
    if key_resp_2.keys != None:  # we had a response
        trials.addData('key_resp_2.rt', key_resp_2.rt)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Feedback1"-------
    t = 0
    Feedback1Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    Prac1Choice.setImage(u'altAchoice32.bmp')
    Prac1End = event.BuilderKeyResponse()
    # keep track of which components have finished
    Feedback1Components = [Prac1Feedback, Prac1Fold, Prac1Choice, Prac1End]
    for thisComponent in Feedback1Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Feedback1"-------
    while continueRoutine:
        # get current time
        t = Feedback1Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Prac1Feedback* updates
        if t >= 0.0 and Prac1Feedback.status == NOT_STARTED:
            # keep track of start time/frame for later
            Prac1Feedback.tStart = t
            Prac1Feedback.frameNStart = frameN  # exact frame index
            Prac1Feedback.setAutoDraw(True)
        
        # *Prac1Fold* updates
        if t >= 0.0 and Prac1Fold.status == NOT_STARTED:
            # keep track of start time/frame for later
            Prac1Fold.tStart = t
            Prac1Fold.frameNStart = frameN  # exact frame index
            Prac1Fold.setAutoDraw(True)
        
        # *Prac1Choice* updates
        if t >= 0.0 and Prac1Choice.status == NOT_STARTED:
            # keep track of start time/frame for later
            Prac1Choice.tStart = t
            Prac1Choice.frameNStart = frameN  # exact frame index
            Prac1Choice.setAutoDraw(True)
        
        # *Prac1End* updates
        if t >= 0.0 and Prac1End.status == NOT_STARTED:
            # keep track of start time/frame for later
            Prac1End.tStart = t
            Prac1End.frameNStart = frameN  # exact frame index
            Prac1End.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(Prac1End.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if Prac1End.status == STARTED:
            theseKeys = event.getKeys()
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                Prac1End.keys = theseKeys[-1]  # just the last key pressed
                Prac1End.rt = Prac1End.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Feedback1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Feedback1"-------
    for thisComponent in Feedback1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if Prac1End.keys in ['', [], None]:  # No response was made
        Prac1End.keys=None
    trials.addData('Prac1End.keys',Prac1End.keys)
    if Prac1End.keys != None:  # we had a response
        trials.addData('Prac1End.rt', Prac1End.rt)
    # the Routine "Feedback1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "crosshair"-------
    t = 0
    crosshairClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    crosshairComponents = [text]
    for thisComponent in crosshairComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "crosshair"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = crosshairClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if t >= 0.0 and text.status == NOT_STARTED:
            # keep track of start time/frame for later
            text.tStart = t
            text.frameNStart = frameN  # exact frame index
            text.setAutoDraw(True)
        frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text.status == STARTED and t >= frameRemains:
            text.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in crosshairComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "crosshair"-------
    for thisComponent in crosshairComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'


# set up handler to look after randomisation of conditions etc
trials_3 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(u'CognitiveTaskSetupFiles - PaperFold.csv', selection=[1]),
    seed=None, name='trials_3')
thisExp.addLoop(trials_3)  # add the loop to the experiment
thisTrial_3 = trials_3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
if thisTrial_3 != None:
    for paramName in thisTrial_3.keys():
        exec(paramName + '= thisTrial_3.' + paramName)

for thisTrial_3 in trials_3:
    currentLoop = trials_3
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
    if thisTrial_3 != None:
        for paramName in thisTrial_3.keys():
            exec(paramName + '= thisTrial_3.' + paramName)
    
    # ------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    image.setImage(Stimulus)
    image.setSize((556,144))
    CFig1.setImage(Choice1)
    CFig2.setImage(Choice2)
    CFig3.setImage(Choice3)
    CFig4.setImage(Choice4)
    key_resp_2 = event.BuilderKeyResponse()
    # keep track of which components have finished
    trialComponents = [image, CFig1, CFig2, CFig3, CFig4, CFig5, Opt1, Opt2, Opt3, Opt4, OPt5, key_resp_2]
    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "trial"-------
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image* updates
        if t >= 0.0 and image.status == NOT_STARTED:
            # keep track of start time/frame for later
            image.tStart = t
            image.frameNStart = frameN  # exact frame index
            image.setAutoDraw(True)
        
        # *CFig1* updates
        if t >= 0.0 and CFig1.status == NOT_STARTED:
            # keep track of start time/frame for later
            CFig1.tStart = t
            CFig1.frameNStart = frameN  # exact frame index
            CFig1.setAutoDraw(True)
        
        # *CFig2* updates
        if t >= 0.0 and CFig2.status == NOT_STARTED:
            # keep track of start time/frame for later
            CFig2.tStart = t
            CFig2.frameNStart = frameN  # exact frame index
            CFig2.setAutoDraw(True)
        
        # *CFig3* updates
        if t >= 0.0 and CFig3.status == NOT_STARTED:
            # keep track of start time/frame for later
            CFig3.tStart = t
            CFig3.frameNStart = frameN  # exact frame index
            CFig3.setAutoDraw(True)
        
        # *CFig4* updates
        if t >= 0.0 and CFig4.status == NOT_STARTED:
            # keep track of start time/frame for later
            CFig4.tStart = t
            CFig4.frameNStart = frameN  # exact frame index
            CFig4.setAutoDraw(True)
        
        # *CFig5* updates
        if t >= 0.0 and CFig5.status == NOT_STARTED:
            # keep track of start time/frame for later
            CFig5.tStart = t
            CFig5.frameNStart = frameN  # exact frame index
            CFig5.setAutoDraw(True)
        if CFig5.status == STARTED:  # only update if drawing
            CFig5.setImage(Choice5, log=False)
        
        # *Opt1* updates
        if t >= 0.0 and Opt1.status == NOT_STARTED:
            # keep track of start time/frame for later
            Opt1.tStart = t
            Opt1.frameNStart = frameN  # exact frame index
            Opt1.setAutoDraw(True)
        
        # *Opt2* updates
        if t >= 0.0 and Opt2.status == NOT_STARTED:
            # keep track of start time/frame for later
            Opt2.tStart = t
            Opt2.frameNStart = frameN  # exact frame index
            Opt2.setAutoDraw(True)
        
        # *Opt3* updates
        if t >= 0.0 and Opt3.status == NOT_STARTED:
            # keep track of start time/frame for later
            Opt3.tStart = t
            Opt3.frameNStart = frameN  # exact frame index
            Opt3.setAutoDraw(True)
        
        # *Opt4* updates
        if t >= 0.0 and Opt4.status == NOT_STARTED:
            # keep track of start time/frame for later
            Opt4.tStart = t
            Opt4.frameNStart = frameN  # exact frame index
            Opt4.setAutoDraw(True)
        
        # *OPt5* updates
        if t >= 0.0 and OPt5.status == NOT_STARTED:
            # keep track of start time/frame for later
            OPt5.tStart = t
            OPt5.frameNStart = frameN  # exact frame index
            OPt5.setAutoDraw(True)
        
        # *key_resp_2* updates
        if t >= 0.0 and key_resp_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_2.tStart = t
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if key_resp_2.status == STARTED:
            theseKeys = event.getKeys(keyList=['1', '2', '3', '4', '5'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_2.keys = theseKeys[-1]  # just the last key pressed
                key_resp_2.rt = key_resp_2.clock.getTime()
                # was this 'correct'?
                if (key_resp_2.keys == str(Corr)) or (key_resp_2.keys == Corr):
                    key_resp_2.corr = 1
                else:
                    key_resp_2.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
        key_resp_2.keys=None
        # was no response the correct answer?!
        if str(Corr).lower() == 'none':
           key_resp_2.corr = 1  # correct non-response
        else:
           key_resp_2.corr = 0  # failed to respond (incorrectly)
    # store data for trials_3 (TrialHandler)
    trials_3.addData('key_resp_2.keys',key_resp_2.keys)
    trials_3.addData('key_resp_2.corr', key_resp_2.corr)
    if key_resp_2.keys != None:  # we had a response
        trials_3.addData('key_resp_2.rt', key_resp_2.rt)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Feedback2"-------
    t = 0
    Feedback2Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    Prac2End = event.BuilderKeyResponse()
    # keep track of which components have finished
    Feedback2Components = [Prac2Feedback, Prac2Fold, Prac2Choice, Prac2End]
    for thisComponent in Feedback2Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Feedback2"-------
    while continueRoutine:
        # get current time
        t = Feedback2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Prac2Feedback* updates
        if t >= 0.0 and Prac2Feedback.status == NOT_STARTED:
            # keep track of start time/frame for later
            Prac2Feedback.tStart = t
            Prac2Feedback.frameNStart = frameN  # exact frame index
            Prac2Feedback.setAutoDraw(True)
        
        # *Prac2Fold* updates
        if t >= 0.0 and Prac2Fold.status == NOT_STARTED:
            # keep track of start time/frame for later
            Prac2Fold.tStart = t
            Prac2Fold.frameNStart = frameN  # exact frame index
            Prac2Fold.setAutoDraw(True)
        
        # *Prac2Choice* updates
        if t >= 0.0 and Prac2Choice.status == NOT_STARTED:
            # keep track of start time/frame for later
            Prac2Choice.tStart = t
            Prac2Choice.frameNStart = frameN  # exact frame index
            Prac2Choice.setAutoDraw(True)
        
        # *Prac2End* updates
        if t >= 0.0 and Prac2End.status == NOT_STARTED:
            # keep track of start time/frame for later
            Prac2End.tStart = t
            Prac2End.frameNStart = frameN  # exact frame index
            Prac2End.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(Prac2End.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if Prac2End.status == STARTED:
            theseKeys = event.getKeys()
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                Prac2End.keys = theseKeys[-1]  # just the last key pressed
                Prac2End.rt = Prac2End.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Feedback2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Feedback2"-------
    for thisComponent in Feedback2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if Prac2End.keys in ['', [], None]:  # No response was made
        Prac2End.keys=None
    trials_3.addData('Prac2End.keys',Prac2End.keys)
    if Prac2End.keys != None:  # we had a response
        trials_3.addData('Prac2End.rt', Prac2End.rt)
    # the Routine "Feedback2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "crosshair"-------
    t = 0
    crosshairClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    crosshairComponents = [text]
    for thisComponent in crosshairComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "crosshair"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = crosshairClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if t >= 0.0 and text.status == NOT_STARTED:
            # keep track of start time/frame for later
            text.tStart = t
            text.frameNStart = frameN  # exact frame index
            text.setAutoDraw(True)
        frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text.status == STARTED and t >= frameRemains:
            text.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in crosshairComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "crosshair"-------
    for thisComponent in crosshairComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_3'


# ------Prepare to start Routine "GetReady"-------
t = 0
GetReadyClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
GetReadyResp = event.BuilderKeyResponse()
# keep track of which components have finished
GetReadyComponents = [GetReady2, GetReadyResp]
for thisComponent in GetReadyComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "GetReady"-------
while continueRoutine:
    # get current time
    t = GetReadyClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *GetReady2* updates
    if t >= 0.0 and GetReady2.status == NOT_STARTED:
        # keep track of start time/frame for later
        GetReady2.tStart = t
        GetReady2.frameNStart = frameN  # exact frame index
        GetReady2.setAutoDraw(True)
    
    # *GetReadyResp* updates
    if t >= 0.0 and GetReadyResp.status == NOT_STARTED:
        # keep track of start time/frame for later
        GetReadyResp.tStart = t
        GetReadyResp.frameNStart = frameN  # exact frame index
        GetReadyResp.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(GetReadyResp.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if GetReadyResp.status == STARTED:
        theseKeys = event.getKeys()
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            GetReadyResp.keys = theseKeys[-1]  # just the last key pressed
            GetReadyResp.rt = GetReadyResp.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in GetReadyComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "GetReady"-------
for thisComponent in GetReadyComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if GetReadyResp.keys in ['', [], None]:  # No response was made
    GetReadyResp.keys=None
thisExp.addData('GetReadyResp.keys',GetReadyResp.keys)
if GetReadyResp.keys != None:  # we had a response
    thisExp.addData('GetReadyResp.rt', GetReadyResp.rt)
thisExp.nextEntry()
# the Routine "GetReady" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "crosshair"-------
t = 0
crosshairClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(0.500000)
# update component parameters for each repeat
# keep track of which components have finished
crosshairComponents = [text]
for thisComponent in crosshairComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "crosshair"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = crosshairClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if t >= 0.0 and text.status == NOT_STARTED:
        # keep track of start time/frame for later
        text.tStart = t
        text.frameNStart = frameN  # exact frame index
        text.setAutoDraw(True)
    frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text.status == STARTED and t >= frameRemains:
        text.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in crosshairComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "crosshair"-------
for thisComponent in crosshairComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
trials_2 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(u'CognitiveTaskSetupFiles - PaperFold.csv', selection=[2,3,4,5,6,7,8,9,10,11,12,13]),
    seed=None, name='trials_2')
thisExp.addLoop(trials_2)  # add the loop to the experiment
thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
if thisTrial_2 != None:
    for paramName in thisTrial_2.keys():
        exec(paramName + '= thisTrial_2.' + paramName)

for thisTrial_2 in trials_2:
    currentLoop = trials_2
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2.keys():
            exec(paramName + '= thisTrial_2.' + paramName)
    
    # ------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    image.setImage(Stimulus)
    image.setSize((556,144))
    CFig1.setImage(Choice1)
    CFig2.setImage(Choice2)
    CFig3.setImage(Choice3)
    CFig4.setImage(Choice4)
    key_resp_2 = event.BuilderKeyResponse()
    # keep track of which components have finished
    trialComponents = [image, CFig1, CFig2, CFig3, CFig4, CFig5, Opt1, Opt2, Opt3, Opt4, OPt5, key_resp_2]
    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "trial"-------
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image* updates
        if t >= 0.0 and image.status == NOT_STARTED:
            # keep track of start time/frame for later
            image.tStart = t
            image.frameNStart = frameN  # exact frame index
            image.setAutoDraw(True)
        
        # *CFig1* updates
        if t >= 0.0 and CFig1.status == NOT_STARTED:
            # keep track of start time/frame for later
            CFig1.tStart = t
            CFig1.frameNStart = frameN  # exact frame index
            CFig1.setAutoDraw(True)
        
        # *CFig2* updates
        if t >= 0.0 and CFig2.status == NOT_STARTED:
            # keep track of start time/frame for later
            CFig2.tStart = t
            CFig2.frameNStart = frameN  # exact frame index
            CFig2.setAutoDraw(True)
        
        # *CFig3* updates
        if t >= 0.0 and CFig3.status == NOT_STARTED:
            # keep track of start time/frame for later
            CFig3.tStart = t
            CFig3.frameNStart = frameN  # exact frame index
            CFig3.setAutoDraw(True)
        
        # *CFig4* updates
        if t >= 0.0 and CFig4.status == NOT_STARTED:
            # keep track of start time/frame for later
            CFig4.tStart = t
            CFig4.frameNStart = frameN  # exact frame index
            CFig4.setAutoDraw(True)
        
        # *CFig5* updates
        if t >= 0.0 and CFig5.status == NOT_STARTED:
            # keep track of start time/frame for later
            CFig5.tStart = t
            CFig5.frameNStart = frameN  # exact frame index
            CFig5.setAutoDraw(True)
        if CFig5.status == STARTED:  # only update if drawing
            CFig5.setImage(Choice5, log=False)
        
        # *Opt1* updates
        if t >= 0.0 and Opt1.status == NOT_STARTED:
            # keep track of start time/frame for later
            Opt1.tStart = t
            Opt1.frameNStart = frameN  # exact frame index
            Opt1.setAutoDraw(True)
        
        # *Opt2* updates
        if t >= 0.0 and Opt2.status == NOT_STARTED:
            # keep track of start time/frame for later
            Opt2.tStart = t
            Opt2.frameNStart = frameN  # exact frame index
            Opt2.setAutoDraw(True)
        
        # *Opt3* updates
        if t >= 0.0 and Opt3.status == NOT_STARTED:
            # keep track of start time/frame for later
            Opt3.tStart = t
            Opt3.frameNStart = frameN  # exact frame index
            Opt3.setAutoDraw(True)
        
        # *Opt4* updates
        if t >= 0.0 and Opt4.status == NOT_STARTED:
            # keep track of start time/frame for later
            Opt4.tStart = t
            Opt4.frameNStart = frameN  # exact frame index
            Opt4.setAutoDraw(True)
        
        # *OPt5* updates
        if t >= 0.0 and OPt5.status == NOT_STARTED:
            # keep track of start time/frame for later
            OPt5.tStart = t
            OPt5.frameNStart = frameN  # exact frame index
            OPt5.setAutoDraw(True)
        
        # *key_resp_2* updates
        if t >= 0.0 and key_resp_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_2.tStart = t
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if key_resp_2.status == STARTED:
            theseKeys = event.getKeys(keyList=['1', '2', '3', '4', '5'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_2.keys = theseKeys[-1]  # just the last key pressed
                key_resp_2.rt = key_resp_2.clock.getTime()
                # was this 'correct'?
                if (key_resp_2.keys == str(Corr)) or (key_resp_2.keys == Corr):
                    key_resp_2.corr = 1
                else:
                    key_resp_2.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
        key_resp_2.keys=None
        # was no response the correct answer?!
        if str(Corr).lower() == 'none':
           key_resp_2.corr = 1  # correct non-response
        else:
           key_resp_2.corr = 0  # failed to respond (incorrectly)
    # store data for trials_2 (TrialHandler)
    trials_2.addData('key_resp_2.keys',key_resp_2.keys)
    trials_2.addData('key_resp_2.corr', key_resp_2.corr)
    if key_resp_2.keys != None:  # we had a response
        trials_2.addData('key_resp_2.rt', key_resp_2.rt)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "crosshair"-------
    t = 0
    crosshairClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    crosshairComponents = [text]
    for thisComponent in crosshairComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "crosshair"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = crosshairClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if t >= 0.0 and text.status == NOT_STARTED:
            # keep track of start time/frame for later
            text.tStart = t
            text.frameNStart = frameN  # exact frame index
            text.setAutoDraw(True)
        frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text.status == STARTED and t >= frameRemains:
            text.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in crosshairComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "crosshair"-------
    for thisComponent in crosshairComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_2'


# ------Prepare to start Routine "ThankYou"-------
t = 0
ThankYouClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
ThankYouComponents = [text_2]
for thisComponent in ThankYouComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "ThankYou"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ThankYouClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if t >= 0.0 and text_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_2.tStart = t
        text_2.frameNStart = frameN  # exact frame index
        text_2.setAutoDraw(True)
    frameRemains = 0.0 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_2.status == STARTED and t >= frameRemains:
        text_2.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ThankYouComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ThankYou"-------
for thisComponent in ThankYouComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
