#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2024.1.4),
    on July 15, 2024, at 16:39
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
prefs.hardware['audioLib'] = 'ptb'
prefs.hardware['audioLatencyMode'] = '3'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, hardware
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER, priority)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# --- Setup global variables (available in all functions) ---
# create a device manager to handle hardware (keyboards, mice, mirophones, speakers, etc.)
deviceManager = hardware.DeviceManager()
# ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# store info about the experiment session
psychopyVersion = '2024.1.4'
expName = 'task_switching_touch'  # from the Builder filename that created this script
# information about this experiment
expInfo = {
    '姓名': '王小明',
    '電話': '0900-012-345',
    '電子郵件': 'yourEmail@google.com',
    'date|hid': data.getDateStr(),
    'expName|hid': expName,
    'psychopyVersion|hid': psychopyVersion,
}

# --- Define some variables which will change depending on pilot mode ---
'''
To run in pilot mode, either use the run/pilot toggle in Builder, Coder and Runner, 
or run the experiment with `--pilot` as an argument. To change what pilot 
#mode does, check out the 'Pilot mode' tab in preferences.
'''
# work out from system args whether we are running in pilot mode
PILOTING = core.setPilotModeFromArgs()
# start off with values from experiment settings
_fullScr = True
_winSize = [1920, 1080]
_loggingLevel = logging.getLevel('warning')
# if in pilot mode, apply overrides according to preferences
if PILOTING:
    # force windowed mode
    if prefs.piloting['forceWindowed']:
        _fullScr = False
        # set window size
        _winSize = prefs.piloting['forcedWindowSize']
    # override logging level
    _loggingLevel = logging.getLevel(
        prefs.piloting['pilotLoggingLevel']
    )

def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # show participant info dialog
    dlg = gui.DlgFromDict(
        dictionary=expInfo, sortKeys=False, title=expName, alwaysOnTop=True
    )
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    # remove dialog-specific syntax from expInfo
    for key, val in expInfo.copy().items():
        newKey, _ = data.utils.parsePipeSyntax(key)
        expInfo[newKey] = expInfo.pop(key)
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s' % (expInfo['姓名'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath='C:\\Users\\fuchi\\Documents\\PsychoPy\\Task_switching_touch\\task_switching_touch_lastrun.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # this outputs to the screen, not a file
    logging.console.setLevel(_loggingLevel)
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log', level=_loggingLevel)
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if PILOTING:
        logging.debug('Fullscreen settings ignored as running in pilot mode.')
    
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=_winSize, fullscr=_fullScr, screen=0,
            winType='pyglet', allowStencil=False,
            monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height', 
            checkTiming=False  # we're going to do this ourselves in a moment
        )
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [0,0,0]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'height'
    win.mouseVisible = False
    win.hideMessage()
    # show a visual indicator if we're in piloting mode
    if PILOTING and prefs.piloting['showPilotingIndicator']:
        win.showPilotingIndicator()
    
    return win


def setupDevices(expInfo, thisExp, win):
    """
    Setup whatever devices are available (mouse, keyboard, speaker, eyetracker, etc.) and add them to 
    the device manager (deviceManager)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    bool
        True if completed successfully.
    """
    # --- Setup input devices ---
    ioConfig = {}
    
    # Setup iohub keyboard
    ioConfig['Keyboard'] = dict(use_keymap='psychopy')
    
    ioSession = '1'
    if 'session' in expInfo:
        ioSession = str(expInfo['session'])
    ioServer = io.launchHubServer(window=win, **ioConfig)
    # store ioServer object in the device manager
    deviceManager.ioServer = ioServer
    
    # create a default keyboard (e.g. to check for escape)
    if deviceManager.getDevice('defaultKeyboard') is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='iohub'
        )
    if deviceManager.getDevice('key_resp') is None:
        # initialise key_resp
        key_resp = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp',
        )
    if deviceManager.getDevice('key_resp_2') is None:
        # initialise key_resp_2
        key_resp_2 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_2',
        )
    if deviceManager.getDevice('NumberResponse') is None:
        # initialise NumberResponse
        NumberResponse = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='NumberResponse',
        )
    if deviceManager.getDevice('key_resp_3') is None:
        # initialise key_resp_3
        key_resp_3 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_3',
        )
    if deviceManager.getDevice('LetterResponse') is None:
        # initialise LetterResponse
        LetterResponse = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='LetterResponse',
        )
    if deviceManager.getDevice('key_resp_4') is None:
        # initialise key_resp_4
        key_resp_4 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_4',
        )
    if deviceManager.getDevice('MixedResponse') is None:
        # initialise MixedResponse
        MixedResponse = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='MixedResponse',
        )
    # return True if completed successfully
    return True

def pauseExperiment(thisExp, win=None, timers=[], playbackComponents=[]):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    playbackComponents : list, tuple
        List of any components with a `pause` method which need to be paused.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # pause any playback components
    for comp in playbackComponents:
        comp.pause()
    # prevent components from auto-drawing
    win.stashAutoDraw()
    # make sure we have a keyboard
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        defaultKeyboard = deviceManager.addKeyboard(
            deviceClass='keyboard',
            deviceName='defaultKeyboard',
            backend='ioHub',
        )
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win)
        # flip the screen
        win.flip()
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, win=win)
    # resume any playback components
    for comp in playbackComponents:
        comp.play()
    # restore auto-drawn components
    win.retrieveAutoDraw()
    # reset any timers
    for timer in timers:
        timer.reset()


def run(expInfo, thisExp, win, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = deviceManager.ioServer
    # get/create a default keyboard (e.g. to check for escape)
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='ioHub'
        )
    eyetracker = deviceManager.getDevice('eyetracker')
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "Instruction" ---
    # Run 'Begin Experiment' code from code
    # Initialize the previousTask variable
    previousTask = None
    slideN = 1
    maxSlideN = 5
    minSlideN = 1
    backimgSize=[0.98,1.68]
    imgpth='stimuli/iphone_back.png'
    key_resp = keyboard.Keyboard(deviceName='key_resp')
    back_img = visual.ImageStim(
        win=win,
        name='back_img', 
        image=imgpth, mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=backimgSize,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    instr_image = visual.ImageStim(
        win=win,
        name='instr_image', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, -0.05), size=(1.5, 0.75),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    Right_Rectangle_2 = visual.Rect(
        win=win, name='Right_Rectangle_2',units='norm', 
        width=(1,2)[0], height=(1,2)[1],
        ori=0.0, pos=(0.5, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[1.0000, 0.7882, 0.5373], fillColor=[1.0000, 0.7882, 0.5373],
        opacity=0.0, depth=-4.0, interpolate=True)
    Left_Rectangle_2 = visual.Rect(
        win=win, name='Left_Rectangle_2',units='norm', 
        width=(1,2)[0], height=(1,2)[1],
        ori=0.0, pos=(-0.5, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-1.0000, -1.0000, -1.0000], fillColor=[-1.0000, -1.0000, -1.0000],
        opacity=0.0, depth=-5.0, interpolate=True)
    mouse = event.Mouse(win=win)
    x, y = [None, None]
    mouse.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "ReadyNumbers" ---
    back_img_6 = visual.ImageStim(
        win=win,
        name='back_img_6', 
        image=imgpth, mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=backimgSize,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    Instr_numbers_Only = visual.ImageStim(
        win=win,
        name='Instr_numbers_Only', 
        image='stimuli/readynumbers.png', mask=None, anchor='center',
        ori=0.0, pos=(0, -0.05), size=(1.5, 0.75),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    key_resp_2 = keyboard.Keyboard(deviceName='key_resp_2')
    mouse_2 = event.Mouse(win=win)
    x, y = [None, None]
    mouse_2.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "NumberTask_Practice" ---
    back_img_2 = visual.ImageStim(
        win=win,
        name='back_img_2', 
        image=imgpth, mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=backimgSize,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    grid = visual.ImageStim(
        win=win,
        name='grid', 
        image='stimuli/grid.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(0.5, 0.5),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    left = visual.Rect(
        win=win, name='left',units='norm', 
        width=(1,2)[0], height=(1,2)[1],
        ori=0.0, pos=(-0.5, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-1.0000, -1.0000, -1.0000], fillColor=[-1.0000, -1.0000, -1.0000],
        opacity=0.0, depth=-2.0, interpolate=True)
    right = visual.Rect(
        win=win, name='right',units='norm', 
        width=(1,2)[0], height=(1,2)[1],
        ori=0.0, pos=(0.5, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[1.0000, 0.7882, 0.5373], fillColor=[1.0000, 0.7882, 0.5373],
        opacity=0.0, depth=-3.0, interpolate=True)
    # Run 'Begin Experiment' code from NumberTask_Code
    # Initialize previous values to None for the first trial
    previousNumber = None
    previousLetter = None
    NumberStim = visual.TextStim(win=win, name='NumberStim',
        text='',
        font='Arial',
        pos=[0,0], height=0.1, wrapWidth=None, ori=0.0, 
        color=[-0.6078, -0.6706, -0.0118], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-5.0);
    NumberResponse = keyboard.Keyboard(deviceName='NumberResponse')
    NumberClickResponse = event.Mouse(win=win)
    x, y = [None, None]
    NumberClickResponse.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "Feedback" ---
    back_img_3 = visual.ImageStim(
        win=win,
        name='back_img_3', 
        image=imgpth, mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=backimgSize,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    FeedBack_NumberTask = visual.TextStim(win=win, name='FeedBack_NumberTask',
        text='',
        font='Arial',
        pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
        color=[-0.6078, -0.6706, -0.0118], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    ErrorImage = visual.ImageStim(
        win=win,
        name='ErrorImage', 
        image='stimuli/task2.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], size=(0.6, 0.4),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    
    # --- Initialize components for Routine "ReadyLetters" ---
    back_img_7 = visual.ImageStim(
        win=win,
        name='back_img_7', 
        image=imgpth, mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=backimgSize,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    Readyletter_img = visual.ImageStim(
        win=win,
        name='Readyletter_img', 
        image='stimuli/readyletters.png', mask=None, anchor='center',
        ori=0.0, pos=(0, -0.05), size=(1.5, 0.75),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    key_resp_3 = keyboard.Keyboard(deviceName='key_resp_3')
    mouse_3 = event.Mouse(win=win)
    x, y = [None, None]
    mouse_3.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "LetterTask_Practice" ---
    back_img_5 = visual.ImageStim(
        win=win,
        name='back_img_5', 
        image=imgpth, mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=backimgSize,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    grid_3 = visual.ImageStim(
        win=win,
        name='grid_3', 
        image='stimuli/grid.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(0.5, 0.5),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    # Run 'Begin Experiment' code from LetterTask_Code
    # Initialize previous values to None for the first trial
    previousNumber = None
    previousLetter = None
    LetterStim = visual.TextStim(win=win, name='LetterStim',
        text='',
        font='Arial',
        pos=[0,0], height=0.1, wrapWidth=None, ori=0.0, 
        color=[-0.6078, -0.6706, -0.0118], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    LetterResponse = keyboard.Keyboard(deviceName='LetterResponse')
    left_2 = visual.Rect(
        win=win, name='left_2',units='norm', 
        width=(1,2)[0], height=(1,2)[1],
        ori=0.0, pos=(-0.5, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-1.0000, -1.0000, -1.0000], fillColor=[-1.0000, -1.0000, -1.0000],
        opacity=0.0, depth=-5.0, interpolate=True)
    right_2 = visual.Rect(
        win=win, name='right_2',units='norm', 
        width=(1,2)[0], height=(1,2)[1],
        ori=0.0, pos=(0.5, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[1.0000, 0.7882, 0.5373], fillColor=[1.0000, 0.7882, 0.5373],
        opacity=0.0, depth=-6.0, interpolate=True)
    NumberClickResponse_2 = event.Mouse(win=win)
    x, y = [None, None]
    NumberClickResponse_2.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "Letter_Feedback" ---
    back_img_8 = visual.ImageStim(
        win=win,
        name='back_img_8', 
        image=imgpth, mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=backimgSize,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    FeedBack_LetterTask = visual.TextStim(win=win, name='FeedBack_LetterTask',
        text='',
        font='Arial',
        pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
        color=[-0.6078, -0.6706, -0.0118], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    ErrorImage_2 = visual.ImageStim(
        win=win,
        name='ErrorImage_2', 
        image='stimuli/task1.png', mask=None, anchor='center',
        ori=0.0, pos=[0.5,0.125], size=(0.5, 0.4),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    
    # --- Initialize components for Routine "ReadyMixed" ---
    back_img_9 = visual.ImageStim(
        win=win,
        name='back_img_9', 
        image=imgpth, mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=backimgSize,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    ReadyMix_img = visual.ImageStim(
        win=win,
        name='ReadyMix_img', 
        image='stimuli/readylettersnumbers.png', mask=None, anchor='center',
        ori=0.0, pos=(0, -0.05), size=(1.5, 0.75),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    key_resp_4 = keyboard.Keyboard(deviceName='key_resp_4')
    mouse_4 = event.Mouse(win=win)
    x, y = [None, None]
    mouse_4.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "reset_Mixed" ---
    
    # --- Initialize components for Routine "Mixed_Task" ---
    back_img_4 = visual.ImageStim(
        win=win,
        name='back_img_4', 
        image=imgpth, mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=backimgSize,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    grid_2 = visual.ImageStim(
        win=win,
        name='grid_2', 
        image='stimuli/grid.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(0.5, 0.5),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    Task_switch_stim = visual.TextStim(win=win, name='Task_switch_stim',
        text='',
        font='Arial',
        pos=[0,0], height=0.1, wrapWidth=None, ori=0.0, 
        color=[-0.6078, -0.6706, -0.0118], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    MixedResponse = keyboard.Keyboard(deviceName='MixedResponse')
    left_3 = visual.Rect(
        win=win, name='left_3',units='norm', 
        width=(1,2)[0], height=(1,2)[1],
        ori=0.0, pos=(-0.5, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-1.0000, -1.0000, -1.0000], fillColor=[-1.0000, -1.0000, -1.0000],
        opacity=0.0, depth=-5.0, interpolate=True)
    right_3 = visual.Rect(
        win=win, name='right_3',units='norm', 
        width=(1,2)[0], height=(1,2)[1],
        ori=0.0, pos=(0.5, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[1.0000, 0.7882, 0.5373], fillColor=[1.0000, 0.7882, 0.5373],
        opacity=0.0, depth=-6.0, interpolate=True)
    NumberClickResponse_3 = event.Mouse(win=win)
    x, y = [None, None]
    NumberClickResponse_3.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "Mixed_Feedback" ---
    back_img_10 = visual.ImageStim(
        win=win,
        name='back_img_10', 
        image=imgpth, mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=backimgSize,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    FeedBack_LetterTask_2 = visual.TextStim(win=win, name='FeedBack_LetterTask_2',
        text='',
        font='Arial',
        pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
        color=[-0.6078, -0.6706, -0.0118], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    ErrorImage_3 = visual.ImageStim(
        win=win,
        name='ErrorImage_3', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], size=(0.5, 0.4),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    
    # --- Initialize components for Routine "end" ---
    back_img_11 = visual.ImageStim(
        win=win,
        name='back_img_11', 
        image=imgpth, mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=backimgSize,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    Thank_you = visual.TextStim(win=win, name='Thank_you',
        text='',
        font='Arial',
        pos=[0,0], height=0.05, wrapWidth=None, ori=0.0, 
        color=[-0.6078, -0.6706, -0.0118], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    
    # create some handy timers
    
    # global clock to track the time since experiment started
    if globalClock is None:
        # create a clock if not given one
        globalClock = core.Clock()
    if isinstance(globalClock, str):
        # if given a string, make a clock accoridng to it
        if globalClock == 'float':
            # get timestamps as a simple value
            globalClock = core.Clock(format='float')
        elif globalClock == 'iso':
            # get timestamps in ISO format
            globalClock = core.Clock(format='%Y-%m-%d_%H:%M:%S.%f%z')
        else:
            # get timestamps in a custom format
            globalClock = core.Clock(format=globalClock)
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    # routine timer to track time remaining of each (possibly non-slip) routine
    routineTimer = core.Clock()
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(
        format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6
    )
    
    # set up handler to look after randomisation of conditions etc
    Instruction_Loop = data.TrialHandler(nReps=1000.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='Instruction_Loop')
    thisExp.addLoop(Instruction_Loop)  # add the loop to the experiment
    thisInstruction_Loop = Instruction_Loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisInstruction_Loop.rgb)
    if thisInstruction_Loop != None:
        for paramName in thisInstruction_Loop:
            globals()[paramName] = thisInstruction_Loop[paramName]
    
    for thisInstruction_Loop in Instruction_Loop:
        currentLoop = Instruction_Loop
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisInstruction_Loop.rgb)
        if thisInstruction_Loop != None:
            for paramName in thisInstruction_Loop:
                globals()[paramName] = thisInstruction_Loop[paramName]
        
        # --- Prepare to start Routine "Instruction" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('Instruction.started', globalClock.getTime(format='float'))
        key_resp.keys = []
        key_resp.rt = []
        _key_resp_allKeys = []
        instr_image.setImage('stimuli/instructions'+str(slideN)+'.png')
        # setup some python lists for storing info about the mouse
        mouse.x = []
        mouse.y = []
        mouse.leftButton = []
        mouse.midButton = []
        mouse.rightButton = []
        mouse.time = []
        mouse.clicked_name = []
        gotValidClick = False  # until a click is received
        # keep track of which components have finished
        InstructionComponents = [key_resp, back_img, instr_image, Right_Rectangle_2, Left_Rectangle_2, mouse]
        for thisComponent in InstructionComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Instruction" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *key_resp* updates
            waitOnFlip = False
            
            # if key_resp is starting this frame...
            if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp.frameNStart = frameN  # exact frame index
                key_resp.tStart = t  # local t and not account for scr refresh
                key_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp.started')
                # update status
                key_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp.status == STARTED and not waitOnFlip:
                theseKeys = key_resp.getKeys(keyList=['left','right','q','space'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_allKeys.extend(theseKeys)
                if len(_key_resp_allKeys):
                    key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                    key_resp.rt = _key_resp_allKeys[-1].rt
                    key_resp.duration = _key_resp_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # *back_img* updates
            
            # if back_img is starting this frame...
            if back_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                back_img.frameNStart = frameN  # exact frame index
                back_img.tStart = t  # local t and not account for scr refresh
                back_img.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(back_img, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'back_img.started')
                # update status
                back_img.status = STARTED
                back_img.setAutoDraw(True)
            
            # if back_img is active this frame...
            if back_img.status == STARTED:
                # update params
                pass
            
            # *instr_image* updates
            
            # if instr_image is starting this frame...
            if instr_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                instr_image.frameNStart = frameN  # exact frame index
                instr_image.tStart = t  # local t and not account for scr refresh
                instr_image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(instr_image, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'instr_image.started')
                # update status
                instr_image.status = STARTED
                instr_image.setAutoDraw(True)
            
            # if instr_image is active this frame...
            if instr_image.status == STARTED:
                # update params
                pass
            
            # *Right_Rectangle_2* updates
            
            # if Right_Rectangle_2 is starting this frame...
            if Right_Rectangle_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Right_Rectangle_2.frameNStart = frameN  # exact frame index
                Right_Rectangle_2.tStart = t  # local t and not account for scr refresh
                Right_Rectangle_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Right_Rectangle_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Right_Rectangle_2.started')
                # update status
                Right_Rectangle_2.status = STARTED
                Right_Rectangle_2.setAutoDraw(True)
            
            # if Right_Rectangle_2 is active this frame...
            if Right_Rectangle_2.status == STARTED:
                # update params
                pass
            
            # *Left_Rectangle_2* updates
            
            # if Left_Rectangle_2 is starting this frame...
            if Left_Rectangle_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Left_Rectangle_2.frameNStart = frameN  # exact frame index
                Left_Rectangle_2.tStart = t  # local t and not account for scr refresh
                Left_Rectangle_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Left_Rectangle_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Left_Rectangle_2.started')
                # update status
                Left_Rectangle_2.status = STARTED
                Left_Rectangle_2.setAutoDraw(True)
            
            # if Left_Rectangle_2 is active this frame...
            if Left_Rectangle_2.status == STARTED:
                # update params
                pass
            # *mouse* updates
            
            # if mouse is starting this frame...
            if mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mouse.frameNStart = frameN  # exact frame index
                mouse.tStart = t  # local t and not account for scr refresh
                mouse.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.addData('mouse.started', t)
                # update status
                mouse.status = STARTED
                mouse.mouseClock.reset()
                prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
            if mouse.status == STARTED:  # only update if started and not finished!
                buttons = mouse.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        clickableList = environmenttools.getFromNames([Right_Rectangle_2,Left_Rectangle_2], namespace=locals())
                        for obj in clickableList:
                            # is this object clicked on?
                            if obj.contains(mouse):
                                gotValidClick = True
                                mouse.clicked_name.append(obj.name)
                        x, y = mouse.getPos()
                        mouse.x.append(x)
                        mouse.y.append(y)
                        buttons = mouse.getPressed()
                        mouse.leftButton.append(buttons[0])
                        mouse.midButton.append(buttons[1])
                        mouse.rightButton.append(buttons[2])
                        mouse.time.append(mouse.mouseClock.getTime())
                        if gotValidClick:
                            continueRoutine = False  # end routine on response
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in InstructionComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Instruction" ---
        for thisComponent in InstructionComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('Instruction.stopped', globalClock.getTime(format='float'))
        # Run 'End Routine' code from code
        if key_resp.keys == 'left'or 'Left_Rectangle_2' in mouse.clicked_name:
            slideN -= 1
        elif key_resp.keys == 'right' or 'Right_Rectangle_2' in mouse.clicked_name:
            slideN += 1
        elif key_resp.keys == 'space':
            slideN += 1
        elif key_resp.keys == 'q':
            Instruction_Loop.finished = True
        
        
        # Constrain slideN within the valid range
        if slideN < minSlideN:
            slideN = minSlideN
        elif slideN > maxSlideN:
            Instruction_Loop.finished = True
        # check responses
        if key_resp.keys in ['', [], None]:  # No response was made
            key_resp.keys = None
        Instruction_Loop.addData('key_resp.keys',key_resp.keys)
        if key_resp.keys != None:  # we had a response
            Instruction_Loop.addData('key_resp.rt', key_resp.rt)
            Instruction_Loop.addData('key_resp.duration', key_resp.duration)
        # store data for Instruction_Loop (TrialHandler)
        Instruction_Loop.addData('mouse.x', mouse.x)
        Instruction_Loop.addData('mouse.y', mouse.y)
        Instruction_Loop.addData('mouse.leftButton', mouse.leftButton)
        Instruction_Loop.addData('mouse.midButton', mouse.midButton)
        Instruction_Loop.addData('mouse.rightButton', mouse.rightButton)
        Instruction_Loop.addData('mouse.time', mouse.time)
        Instruction_Loop.addData('mouse.clicked_name', mouse.clicked_name)
        # the Routine "Instruction" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 1000.0 repeats of 'Instruction_Loop'
    
    
    # --- Prepare to start Routine "ReadyNumbers" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('ReadyNumbers.started', globalClock.getTime(format='float'))
    key_resp_2.keys = []
    key_resp_2.rt = []
    _key_resp_2_allKeys = []
    # setup some python lists for storing info about the mouse_2
    mouse_2.x = []
    mouse_2.y = []
    mouse_2.leftButton = []
    mouse_2.midButton = []
    mouse_2.rightButton = []
    mouse_2.time = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    ReadyNumbersComponents = [back_img_6, Instr_numbers_Only, key_resp_2, mouse_2]
    for thisComponent in ReadyNumbersComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "ReadyNumbers" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *back_img_6* updates
        
        # if back_img_6 is starting this frame...
        if back_img_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            back_img_6.frameNStart = frameN  # exact frame index
            back_img_6.tStart = t  # local t and not account for scr refresh
            back_img_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(back_img_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'back_img_6.started')
            # update status
            back_img_6.status = STARTED
            back_img_6.setAutoDraw(True)
        
        # if back_img_6 is active this frame...
        if back_img_6.status == STARTED:
            # update params
            pass
        
        # *Instr_numbers_Only* updates
        
        # if Instr_numbers_Only is starting this frame...
        if Instr_numbers_Only.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Instr_numbers_Only.frameNStart = frameN  # exact frame index
            Instr_numbers_Only.tStart = t  # local t and not account for scr refresh
            Instr_numbers_Only.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Instr_numbers_Only, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Instr_numbers_Only.started')
            # update status
            Instr_numbers_Only.status = STARTED
            Instr_numbers_Only.setAutoDraw(True)
        
        # if Instr_numbers_Only is active this frame...
        if Instr_numbers_Only.status == STARTED:
            # update params
            pass
        
        # *key_resp_2* updates
        waitOnFlip = False
        
        # if key_resp_2 is starting this frame...
        if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.tStart = t  # local t and not account for scr refresh
            key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_2.started')
            # update status
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_2.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_2.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_2_allKeys.extend(theseKeys)
            if len(_key_resp_2_allKeys):
                key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
                key_resp_2.rt = _key_resp_2_allKeys[-1].rt
                key_resp_2.duration = _key_resp_2_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        # *mouse_2* updates
        
        # if mouse_2 is starting this frame...
        if mouse_2.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_2.frameNStart = frameN  # exact frame index
            mouse_2.tStart = t  # local t and not account for scr refresh
            mouse_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse_2.started', t)
            # update status
            mouse_2.status = STARTED
            mouse_2.mouseClock.reset()
            prevButtonState = mouse_2.getPressed()  # if button is down already this ISN'T a new click
        if mouse_2.status == STARTED:  # only update if started and not finished!
            buttons = mouse_2.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    pass
                    x, y = mouse_2.getPos()
                    mouse_2.x.append(x)
                    mouse_2.y.append(y)
                    buttons = mouse_2.getPressed()
                    mouse_2.leftButton.append(buttons[0])
                    mouse_2.midButton.append(buttons[1])
                    mouse_2.rightButton.append(buttons[2])
                    mouse_2.time.append(mouse_2.mouseClock.getTime())
                    
                    continueRoutine = False  # end routine on response
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ReadyNumbersComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ReadyNumbers" ---
    for thisComponent in ReadyNumbersComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('ReadyNumbers.stopped', globalClock.getTime(format='float'))
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
        key_resp_2.keys = None
    thisExp.addData('key_resp_2.keys',key_resp_2.keys)
    if key_resp_2.keys != None:  # we had a response
        thisExp.addData('key_resp_2.rt', key_resp_2.rt)
        thisExp.addData('key_resp_2.duration', key_resp_2.duration)
    # store data for thisExp (ExperimentHandler)
    thisExp.addData('mouse_2.x', mouse_2.x)
    thisExp.addData('mouse_2.y', mouse_2.y)
    thisExp.addData('mouse_2.leftButton', mouse_2.leftButton)
    thisExp.addData('mouse_2.midButton', mouse_2.midButton)
    thisExp.addData('mouse_2.rightButton', mouse_2.rightButton)
    thisExp.addData('mouse_2.time', mouse_2.time)
    thisExp.nextEntry()
    # the Routine "ReadyNumbers" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=5.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='trials')
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            globals()[paramName] = thisTrial[paramName]
    
    for thisTrial in trials:
        currentLoop = trials
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                globals()[paramName] = thisTrial[paramName]
        
        # --- Prepare to start Routine "NumberTask_Practice" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('NumberTask_Practice.started', globalClock.getTime(format='float'))
        # Run 'Begin Routine' code from NumberTask_Code
        # Define the base position
        basePos = 0.125
        
        # Define the possible bottom quadrants
        bottomQuadrants = [
            [-basePos, -basePos],  # Bottom-left
            [basePos, -basePos]    # Bottom-right
        ]
        
        
        def get_new_combination(previousNumber, previousLetter):
            # Shuffle the quadrants, numbers, and letters
            shuffle(bottomQuadrants)
            shuffle(number)
            shuffle(letter)
        
            # Ensure the new combination is different from the previous one
            newNumber = number[0]
            newLetter = letter[0]
        
            while newNumber == previousNumber or newLetter == previousLetter:
                shuffle(number)
                shuffle(letter)
                newNumber = number[0]
                newLetter = letter[0]
        
            return newNumber, newLetter
        
        # Example usage:
        number = ['1','2','3','4','5','6','7','8']
        letter = ['A','E','I','U','G','M','K','R']
        
        # Get a new combination ensuring it's different from the previous one
        number, letter = get_new_combination(previousNumber, previousLetter)
        
        # Randomly select a quadrant
        selectedQuadrant = bottomQuadrants[0]
        
        # Set the stimulus position
        stimPos = selectedQuadrant
        
        # Determine the correct key based on the number (since it's NumberTask_Practice)
        if int(number) % 2 == 0:  # Even number
            correctKey = 'right'
            correctkeyformouse = 'right'
        else:  # Odd number
            correctKey = 'left'
            correctkeyformouse = 'left'
        
        
        NumberStim.setPos(stimPos)
        NumberStim.setText(letter+str(number))
        NumberResponse.keys = []
        NumberResponse.rt = []
        _NumberResponse_allKeys = []
        # setup some python lists for storing info about the NumberClickResponse
        NumberClickResponse.x = []
        NumberClickResponse.y = []
        NumberClickResponse.leftButton = []
        NumberClickResponse.midButton = []
        NumberClickResponse.rightButton = []
        NumberClickResponse.time = []
        NumberClickResponse.clicked_name = []
        gotValidClick = False  # until a click is received
        # keep track of which components have finished
        NumberTask_PracticeComponents = [back_img_2, grid, left, right, NumberStim, NumberResponse, NumberClickResponse]
        for thisComponent in NumberTask_PracticeComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "NumberTask_Practice" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *back_img_2* updates
            
            # if back_img_2 is starting this frame...
            if back_img_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                back_img_2.frameNStart = frameN  # exact frame index
                back_img_2.tStart = t  # local t and not account for scr refresh
                back_img_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(back_img_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'back_img_2.started')
                # update status
                back_img_2.status = STARTED
                back_img_2.setAutoDraw(True)
            
            # if back_img_2 is active this frame...
            if back_img_2.status == STARTED:
                # update params
                pass
            
            # *grid* updates
            
            # if grid is starting this frame...
            if grid.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                grid.frameNStart = frameN  # exact frame index
                grid.tStart = t  # local t and not account for scr refresh
                grid.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(grid, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'grid.started')
                # update status
                grid.status = STARTED
                grid.setAutoDraw(True)
            
            # if grid is active this frame...
            if grid.status == STARTED:
                # update params
                pass
            
            # *left* updates
            
            # if left is starting this frame...
            if left.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                left.frameNStart = frameN  # exact frame index
                left.tStart = t  # local t and not account for scr refresh
                left.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(left, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'left.started')
                # update status
                left.status = STARTED
                left.setAutoDraw(True)
            
            # if left is active this frame...
            if left.status == STARTED:
                # update params
                pass
            
            # *right* updates
            
            # if right is starting this frame...
            if right.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                right.frameNStart = frameN  # exact frame index
                right.tStart = t  # local t and not account for scr refresh
                right.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(right, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'right.started')
                # update status
                right.status = STARTED
                right.setAutoDraw(True)
            
            # if right is active this frame...
            if right.status == STARTED:
                # update params
                pass
            
            # *NumberStim* updates
            
            # if NumberStim is starting this frame...
            if NumberStim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                NumberStim.frameNStart = frameN  # exact frame index
                NumberStim.tStart = t  # local t and not account for scr refresh
                NumberStim.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(NumberStim, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'NumberStim.started')
                # update status
                NumberStim.status = STARTED
                NumberStim.setAutoDraw(True)
            
            # if NumberStim is active this frame...
            if NumberStim.status == STARTED:
                # update params
                pass
            
            # *NumberResponse* updates
            waitOnFlip = False
            
            # if NumberResponse is starting this frame...
            if NumberResponse.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                NumberResponse.frameNStart = frameN  # exact frame index
                NumberResponse.tStart = t  # local t and not account for scr refresh
                NumberResponse.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(NumberResponse, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'NumberResponse.started')
                # update status
                NumberResponse.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(NumberResponse.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(NumberResponse.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if NumberResponse.status == STARTED and not waitOnFlip:
                theseKeys = NumberResponse.getKeys(keyList=['left', 'right'], ignoreKeys=["escape"], waitRelease=False)
                _NumberResponse_allKeys.extend(theseKeys)
                if len(_NumberResponse_allKeys):
                    NumberResponse.keys = _NumberResponse_allKeys[-1].name  # just the last key pressed
                    NumberResponse.rt = _NumberResponse_allKeys[-1].rt
                    NumberResponse.duration = _NumberResponse_allKeys[-1].duration
                    # was this correct?
                    if (NumberResponse.keys == str(correctKey)) or (NumberResponse.keys == correctKey):
                        NumberResponse.corr = 1
                    else:
                        NumberResponse.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            # *NumberClickResponse* updates
            
            # if NumberClickResponse is starting this frame...
            if NumberClickResponse.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                NumberClickResponse.frameNStart = frameN  # exact frame index
                NumberClickResponse.tStart = t  # local t and not account for scr refresh
                NumberClickResponse.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(NumberClickResponse, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.addData('NumberClickResponse.started', t)
                # update status
                NumberClickResponse.status = STARTED
                NumberClickResponse.mouseClock.reset()
                prevButtonState = NumberClickResponse.getPressed()  # if button is down already this ISN'T a new click
            if NumberClickResponse.status == STARTED:  # only update if started and not finished!
                buttons = NumberClickResponse.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        clickableList = environmenttools.getFromNames([left,right], namespace=locals())
                        for obj in clickableList:
                            # is this object clicked on?
                            if obj.contains(NumberClickResponse):
                                gotValidClick = True
                                NumberClickResponse.clicked_name.append(obj.name)
                        x, y = NumberClickResponse.getPos()
                        NumberClickResponse.x.append(x)
                        NumberClickResponse.y.append(y)
                        buttons = NumberClickResponse.getPressed()
                        NumberClickResponse.leftButton.append(buttons[0])
                        NumberClickResponse.midButton.append(buttons[1])
                        NumberClickResponse.rightButton.append(buttons[2])
                        NumberClickResponse.time.append(NumberClickResponse.mouseClock.getTime())
                        if gotValidClick:
                            continueRoutine = False  # end routine on response
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in NumberTask_PracticeComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "NumberTask_Practice" ---
        for thisComponent in NumberTask_PracticeComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('NumberTask_Practice.stopped', globalClock.getTime(format='float'))
        # Run 'End Routine' code from NumberTask_Code
        # Store the current values for the next trial
        previousNumber = number
        previousLetter = letter
        
        # check responses
        if NumberResponse.keys in ['', [], None]:  # No response was made
            NumberResponse.keys = None
            # was no response the correct answer?!
            if str(correctKey).lower() == 'none':
               NumberResponse.corr = 1;  # correct non-response
            else:
               NumberResponse.corr = 0;  # failed to respond (incorrectly)
        # store data for trials (TrialHandler)
        trials.addData('NumberResponse.keys',NumberResponse.keys)
        trials.addData('NumberResponse.corr', NumberResponse.corr)
        if NumberResponse.keys != None:  # we had a response
            trials.addData('NumberResponse.rt', NumberResponse.rt)
            trials.addData('NumberResponse.duration', NumberResponse.duration)
        # store data for trials (TrialHandler)
        trials.addData('NumberClickResponse.x', NumberClickResponse.x)
        trials.addData('NumberClickResponse.y', NumberClickResponse.y)
        trials.addData('NumberClickResponse.leftButton', NumberClickResponse.leftButton)
        trials.addData('NumberClickResponse.midButton', NumberClickResponse.midButton)
        trials.addData('NumberClickResponse.rightButton', NumberClickResponse.rightButton)
        trials.addData('NumberClickResponse.time', NumberClickResponse.time)
        trials.addData('NumberClickResponse.clicked_name', NumberClickResponse.clicked_name)
        # the Routine "NumberTask_Practice" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "Feedback" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('Feedback.started', globalClock.getTime(format='float'))
        # Run 'Begin Routine' code from FeedBack_Code
        # Define the base position
        basePos = 0.125
        
        # Determine the error image position based on the quadrant
        if stimPos[1] > 0:  # Top quadrants
            errorImagePos = [0.125 + 0.25, basePos]
        else:  # Bottom quadrants
            errorImagePos = [-0.125 + 0.25, -basePos]
        
        # Check if the response was correct
        if NumberResponse.corr or correctkeyformouse in NumberClickResponse.clicked_name:
            feedbackText = '正確!'
            showErrorImage = False
        else:
            feedbackText = '錯誤!'
            showErrorImage = True
        
        # Control the visibility of the error image
        if showErrorImage:
            ErrorImage.setAutoDraw(True)
        else:
            ErrorImage.setAutoDraw(False)
        
        FeedBack_NumberTask.setText(feedbackText)
        ErrorImage.setPos([0.5,-0.125])
        # keep track of which components have finished
        FeedbackComponents = [back_img_3, FeedBack_NumberTask, ErrorImage]
        for thisComponent in FeedbackComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Feedback" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 2.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *back_img_3* updates
            
            # if back_img_3 is starting this frame...
            if back_img_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                back_img_3.frameNStart = frameN  # exact frame index
                back_img_3.tStart = t  # local t and not account for scr refresh
                back_img_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(back_img_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'back_img_3.started')
                # update status
                back_img_3.status = STARTED
                back_img_3.setAutoDraw(True)
            
            # if back_img_3 is active this frame...
            if back_img_3.status == STARTED:
                # update params
                pass
            
            # if back_img_3 is stopping this frame...
            if back_img_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > back_img_3.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    back_img_3.tStop = t  # not accounting for scr refresh
                    back_img_3.tStopRefresh = tThisFlipGlobal  # on global time
                    back_img_3.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'back_img_3.stopped')
                    # update status
                    back_img_3.status = FINISHED
                    back_img_3.setAutoDraw(False)
            
            # *FeedBack_NumberTask* updates
            
            # if FeedBack_NumberTask is starting this frame...
            if FeedBack_NumberTask.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                FeedBack_NumberTask.frameNStart = frameN  # exact frame index
                FeedBack_NumberTask.tStart = t  # local t and not account for scr refresh
                FeedBack_NumberTask.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(FeedBack_NumberTask, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'FeedBack_NumberTask.started')
                # update status
                FeedBack_NumberTask.status = STARTED
                FeedBack_NumberTask.setAutoDraw(True)
            
            # if FeedBack_NumberTask is active this frame...
            if FeedBack_NumberTask.status == STARTED:
                # update params
                pass
            
            # if FeedBack_NumberTask is stopping this frame...
            if FeedBack_NumberTask.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > FeedBack_NumberTask.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    FeedBack_NumberTask.tStop = t  # not accounting for scr refresh
                    FeedBack_NumberTask.tStopRefresh = tThisFlipGlobal  # on global time
                    FeedBack_NumberTask.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'FeedBack_NumberTask.stopped')
                    # update status
                    FeedBack_NumberTask.status = FINISHED
                    FeedBack_NumberTask.setAutoDraw(False)
            
            # *ErrorImage* updates
            
            # if ErrorImage is starting this frame...
            if ErrorImage.status == NOT_STARTED and showErrorImage:
                # keep track of start time/frame for later
                ErrorImage.frameNStart = frameN  # exact frame index
                ErrorImage.tStart = t  # local t and not account for scr refresh
                ErrorImage.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ErrorImage, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ErrorImage.started')
                # update status
                ErrorImage.status = STARTED
                ErrorImage.setAutoDraw(True)
            
            # if ErrorImage is active this frame...
            if ErrorImage.status == STARTED:
                # update params
                pass
            
            # if ErrorImage is stopping this frame...
            if ErrorImage.status == STARTED:
                # is it time to stop? (based on local clock)
                if tThisFlip > 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    ErrorImage.tStop = t  # not accounting for scr refresh
                    ErrorImage.tStopRefresh = tThisFlipGlobal  # on global time
                    ErrorImage.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'ErrorImage.stopped')
                    # update status
                    ErrorImage.status = FINISHED
                    ErrorImage.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in FeedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Feedback" ---
        for thisComponent in FeedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('Feedback.stopped', globalClock.getTime(format='float'))
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-2.000000)
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 5.0 repeats of 'trials'
    
    
    # --- Prepare to start Routine "ReadyLetters" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('ReadyLetters.started', globalClock.getTime(format='float'))
    key_resp_3.keys = []
    key_resp_3.rt = []
    _key_resp_3_allKeys = []
    # setup some python lists for storing info about the mouse_3
    mouse_3.x = []
    mouse_3.y = []
    mouse_3.leftButton = []
    mouse_3.midButton = []
    mouse_3.rightButton = []
    mouse_3.time = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    ReadyLettersComponents = [back_img_7, Readyletter_img, key_resp_3, mouse_3]
    for thisComponent in ReadyLettersComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "ReadyLetters" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *back_img_7* updates
        
        # if back_img_7 is starting this frame...
        if back_img_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            back_img_7.frameNStart = frameN  # exact frame index
            back_img_7.tStart = t  # local t and not account for scr refresh
            back_img_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(back_img_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'back_img_7.started')
            # update status
            back_img_7.status = STARTED
            back_img_7.setAutoDraw(True)
        
        # if back_img_7 is active this frame...
        if back_img_7.status == STARTED:
            # update params
            pass
        
        # *Readyletter_img* updates
        
        # if Readyletter_img is starting this frame...
        if Readyletter_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Readyletter_img.frameNStart = frameN  # exact frame index
            Readyletter_img.tStart = t  # local t and not account for scr refresh
            Readyletter_img.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Readyletter_img, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Readyletter_img.started')
            # update status
            Readyletter_img.status = STARTED
            Readyletter_img.setAutoDraw(True)
        
        # if Readyletter_img is active this frame...
        if Readyletter_img.status == STARTED:
            # update params
            pass
        
        # *key_resp_3* updates
        waitOnFlip = False
        
        # if key_resp_3 is starting this frame...
        if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_3.frameNStart = frameN  # exact frame index
            key_resp_3.tStart = t  # local t and not account for scr refresh
            key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_3.started')
            # update status
            key_resp_3.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_3.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_3.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_3_allKeys.extend(theseKeys)
            if len(_key_resp_3_allKeys):
                key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
                key_resp_3.rt = _key_resp_3_allKeys[-1].rt
                key_resp_3.duration = _key_resp_3_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        # *mouse_3* updates
        
        # if mouse_3 is starting this frame...
        if mouse_3.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_3.frameNStart = frameN  # exact frame index
            mouse_3.tStart = t  # local t and not account for scr refresh
            mouse_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse_3.started', t)
            # update status
            mouse_3.status = STARTED
            mouse_3.mouseClock.reset()
            prevButtonState = mouse_3.getPressed()  # if button is down already this ISN'T a new click
        if mouse_3.status == STARTED:  # only update if started and not finished!
            buttons = mouse_3.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    pass
                    x, y = mouse_3.getPos()
                    mouse_3.x.append(x)
                    mouse_3.y.append(y)
                    buttons = mouse_3.getPressed()
                    mouse_3.leftButton.append(buttons[0])
                    mouse_3.midButton.append(buttons[1])
                    mouse_3.rightButton.append(buttons[2])
                    mouse_3.time.append(mouse_3.mouseClock.getTime())
                    
                    continueRoutine = False  # end routine on response
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ReadyLettersComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ReadyLetters" ---
    for thisComponent in ReadyLettersComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('ReadyLetters.stopped', globalClock.getTime(format='float'))
    # check responses
    if key_resp_3.keys in ['', [], None]:  # No response was made
        key_resp_3.keys = None
    thisExp.addData('key_resp_3.keys',key_resp_3.keys)
    if key_resp_3.keys != None:  # we had a response
        thisExp.addData('key_resp_3.rt', key_resp_3.rt)
        thisExp.addData('key_resp_3.duration', key_resp_3.duration)
    # store data for thisExp (ExperimentHandler)
    thisExp.addData('mouse_3.x', mouse_3.x)
    thisExp.addData('mouse_3.y', mouse_3.y)
    thisExp.addData('mouse_3.leftButton', mouse_3.leftButton)
    thisExp.addData('mouse_3.midButton', mouse_3.midButton)
    thisExp.addData('mouse_3.rightButton', mouse_3.rightButton)
    thisExp.addData('mouse_3.time', mouse_3.time)
    thisExp.nextEntry()
    # the Routine "ReadyLetters" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials_2 = data.TrialHandler(nReps=5.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='trials_2')
    thisExp.addLoop(trials_2)  # add the loop to the experiment
    thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2:
            globals()[paramName] = thisTrial_2[paramName]
    
    for thisTrial_2 in trials_2:
        currentLoop = trials_2
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
        if thisTrial_2 != None:
            for paramName in thisTrial_2:
                globals()[paramName] = thisTrial_2[paramName]
        
        # --- Prepare to start Routine "LetterTask_Practice" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('LetterTask_Practice.started', globalClock.getTime(format='float'))
        # Run 'Begin Routine' code from LetterTask_Code
        number = ['1','2','3','4','5','6','7','8']
        letter = ['A','E','I','U','G','M','K','R']
        # Define the base position
        basePos = 0.125
        
        # Define the possible quadrants
        quadrants = [
            [basePos, basePos],    # Top-right
            [-basePos, basePos],   # Top-left
        ]
        
        def get_new_combination(previousNumber, previousLetter):
            # Shuffle the quadrants, numbers, and letters
            shuffle(quadrants)
            shuffle(number)
            shuffle(letter)
        
            # Ensure the new combination is different from the previous one
            newNumber = number[0]
            newLetter = letter[0]
        
            while newNumber == previousNumber or newLetter == previousLetter:
                shuffle(number)
                shuffle(letter)
                newNumber = number[0]
                newLetter = letter[0]
        
            return newNumber, newLetter
        
        # Get a new combination ensuring it's different from the previous one
        number, letter = get_new_combination(previousNumber, previousLetter)
        
        # Randomly select a quadrant
        selectedQuadrant = quadrants[0]
        
        # Set the stimulus position
        stimPos = selectedQuadrant
        
        # Determine the correct key based on the quadrant and the task
        if stimPos[1] > 0:  # Top quadrants (letter task)
            if letter in ['A', 'E', 'I', 'U']:  # Vowel
                correctKey = 'right'
                correctkeyformouse = 'right_2'
            else:  # Consonant
                correctKey = 'left'
                correctkeyformouse = 'left_2'
        
        LetterStim.setPos(stimPos)
        LetterStim.setText(letter+str(number))
        LetterResponse.keys = []
        LetterResponse.rt = []
        _LetterResponse_allKeys = []
        # setup some python lists for storing info about the NumberClickResponse_2
        NumberClickResponse_2.x = []
        NumberClickResponse_2.y = []
        NumberClickResponse_2.leftButton = []
        NumberClickResponse_2.midButton = []
        NumberClickResponse_2.rightButton = []
        NumberClickResponse_2.time = []
        NumberClickResponse_2.clicked_name = []
        gotValidClick = False  # until a click is received
        # keep track of which components have finished
        LetterTask_PracticeComponents = [back_img_5, grid_3, LetterStim, LetterResponse, left_2, right_2, NumberClickResponse_2]
        for thisComponent in LetterTask_PracticeComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "LetterTask_Practice" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *back_img_5* updates
            
            # if back_img_5 is starting this frame...
            if back_img_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                back_img_5.frameNStart = frameN  # exact frame index
                back_img_5.tStart = t  # local t and not account for scr refresh
                back_img_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(back_img_5, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'back_img_5.started')
                # update status
                back_img_5.status = STARTED
                back_img_5.setAutoDraw(True)
            
            # if back_img_5 is active this frame...
            if back_img_5.status == STARTED:
                # update params
                pass
            
            # *grid_3* updates
            
            # if grid_3 is starting this frame...
            if grid_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                grid_3.frameNStart = frameN  # exact frame index
                grid_3.tStart = t  # local t and not account for scr refresh
                grid_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(grid_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'grid_3.started')
                # update status
                grid_3.status = STARTED
                grid_3.setAutoDraw(True)
            
            # if grid_3 is active this frame...
            if grid_3.status == STARTED:
                # update params
                pass
            
            # *LetterStim* updates
            
            # if LetterStim is starting this frame...
            if LetterStim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                LetterStim.frameNStart = frameN  # exact frame index
                LetterStim.tStart = t  # local t and not account for scr refresh
                LetterStim.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(LetterStim, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'LetterStim.started')
                # update status
                LetterStim.status = STARTED
                LetterStim.setAutoDraw(True)
            
            # if LetterStim is active this frame...
            if LetterStim.status == STARTED:
                # update params
                pass
            
            # *LetterResponse* updates
            waitOnFlip = False
            
            # if LetterResponse is starting this frame...
            if LetterResponse.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                LetterResponse.frameNStart = frameN  # exact frame index
                LetterResponse.tStart = t  # local t and not account for scr refresh
                LetterResponse.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(LetterResponse, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'LetterResponse.started')
                # update status
                LetterResponse.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(LetterResponse.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(LetterResponse.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if LetterResponse.status == STARTED and not waitOnFlip:
                theseKeys = LetterResponse.getKeys(keyList=['left', 'right'], ignoreKeys=["escape"], waitRelease=False)
                _LetterResponse_allKeys.extend(theseKeys)
                if len(_LetterResponse_allKeys):
                    LetterResponse.keys = _LetterResponse_allKeys[-1].name  # just the last key pressed
                    LetterResponse.rt = _LetterResponse_allKeys[-1].rt
                    LetterResponse.duration = _LetterResponse_allKeys[-1].duration
                    # was this correct?
                    if (LetterResponse.keys == str(correctKey)) or (LetterResponse.keys == correctKey):
                        LetterResponse.corr = 1
                    else:
                        LetterResponse.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # *left_2* updates
            
            # if left_2 is starting this frame...
            if left_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                left_2.frameNStart = frameN  # exact frame index
                left_2.tStart = t  # local t and not account for scr refresh
                left_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(left_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'left_2.started')
                # update status
                left_2.status = STARTED
                left_2.setAutoDraw(True)
            
            # if left_2 is active this frame...
            if left_2.status == STARTED:
                # update params
                pass
            
            # *right_2* updates
            
            # if right_2 is starting this frame...
            if right_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                right_2.frameNStart = frameN  # exact frame index
                right_2.tStart = t  # local t and not account for scr refresh
                right_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(right_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'right_2.started')
                # update status
                right_2.status = STARTED
                right_2.setAutoDraw(True)
            
            # if right_2 is active this frame...
            if right_2.status == STARTED:
                # update params
                pass
            # *NumberClickResponse_2* updates
            
            # if NumberClickResponse_2 is starting this frame...
            if NumberClickResponse_2.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                NumberClickResponse_2.frameNStart = frameN  # exact frame index
                NumberClickResponse_2.tStart = t  # local t and not account for scr refresh
                NumberClickResponse_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(NumberClickResponse_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.addData('NumberClickResponse_2.started', t)
                # update status
                NumberClickResponse_2.status = STARTED
                NumberClickResponse_2.mouseClock.reset()
                prevButtonState = NumberClickResponse_2.getPressed()  # if button is down already this ISN'T a new click
            if NumberClickResponse_2.status == STARTED:  # only update if started and not finished!
                buttons = NumberClickResponse_2.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        clickableList = environmenttools.getFromNames([left_2,right_2], namespace=locals())
                        for obj in clickableList:
                            # is this object clicked on?
                            if obj.contains(NumberClickResponse_2):
                                gotValidClick = True
                                NumberClickResponse_2.clicked_name.append(obj.name)
                        x, y = NumberClickResponse_2.getPos()
                        NumberClickResponse_2.x.append(x)
                        NumberClickResponse_2.y.append(y)
                        buttons = NumberClickResponse_2.getPressed()
                        NumberClickResponse_2.leftButton.append(buttons[0])
                        NumberClickResponse_2.midButton.append(buttons[1])
                        NumberClickResponse_2.rightButton.append(buttons[2])
                        NumberClickResponse_2.time.append(NumberClickResponse_2.mouseClock.getTime())
                        if gotValidClick:
                            continueRoutine = False  # end routine on response
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in LetterTask_PracticeComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "LetterTask_Practice" ---
        for thisComponent in LetterTask_PracticeComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('LetterTask_Practice.stopped', globalClock.getTime(format='float'))
        # check responses
        if LetterResponse.keys in ['', [], None]:  # No response was made
            LetterResponse.keys = None
            # was no response the correct answer?!
            if str(correctKey).lower() == 'none':
               LetterResponse.corr = 1;  # correct non-response
            else:
               LetterResponse.corr = 0;  # failed to respond (incorrectly)
        # store data for trials_2 (TrialHandler)
        trials_2.addData('LetterResponse.keys',LetterResponse.keys)
        trials_2.addData('LetterResponse.corr', LetterResponse.corr)
        if LetterResponse.keys != None:  # we had a response
            trials_2.addData('LetterResponse.rt', LetterResponse.rt)
            trials_2.addData('LetterResponse.duration', LetterResponse.duration)
        # store data for trials_2 (TrialHandler)
        trials_2.addData('NumberClickResponse_2.x', NumberClickResponse_2.x)
        trials_2.addData('NumberClickResponse_2.y', NumberClickResponse_2.y)
        trials_2.addData('NumberClickResponse_2.leftButton', NumberClickResponse_2.leftButton)
        trials_2.addData('NumberClickResponse_2.midButton', NumberClickResponse_2.midButton)
        trials_2.addData('NumberClickResponse_2.rightButton', NumberClickResponse_2.rightButton)
        trials_2.addData('NumberClickResponse_2.time', NumberClickResponse_2.time)
        trials_2.addData('NumberClickResponse_2.clicked_name', NumberClickResponse_2.clicked_name)
        # the Routine "LetterTask_Practice" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "Letter_Feedback" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('Letter_Feedback.started', globalClock.getTime(format='float'))
        # Run 'Begin Routine' code from FeedBack_Code_2
        # Define the base position
        basePos = 0.125
        
        # Determine the error image position based on the quadrant
        if stimPos[1] > 0:  # Top quadrants
            errorImagePos = [0.125 + 0.35, basePos]
        else:  # Bottom quadrants
            errorImagePos = [-0.125 + 0.35, -basePos]
        
        # Check if the response was correct
        if LetterResponse.corr or correctkeyformouse in NumberClickResponse_2.clicked_name:
            feedbackText = '正確!'
            showErrorImage = False
        else:
            feedbackText = '錯誤!'
            showErrorImage = True
        
        # Control the visibility of the error image
        if showErrorImage:
            ErrorImage_2.setAutoDraw(True)
        else:
            ErrorImage_2.setAutoDraw(False)
        
        FeedBack_LetterTask.setText(feedbackText)
        # keep track of which components have finished
        Letter_FeedbackComponents = [back_img_8, FeedBack_LetterTask, ErrorImage_2]
        for thisComponent in Letter_FeedbackComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Letter_Feedback" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 2.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *back_img_8* updates
            
            # if back_img_8 is starting this frame...
            if back_img_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                back_img_8.frameNStart = frameN  # exact frame index
                back_img_8.tStart = t  # local t and not account for scr refresh
                back_img_8.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(back_img_8, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'back_img_8.started')
                # update status
                back_img_8.status = STARTED
                back_img_8.setAutoDraw(True)
            
            # if back_img_8 is active this frame...
            if back_img_8.status == STARTED:
                # update params
                pass
            
            # if back_img_8 is stopping this frame...
            if back_img_8.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > back_img_8.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    back_img_8.tStop = t  # not accounting for scr refresh
                    back_img_8.tStopRefresh = tThisFlipGlobal  # on global time
                    back_img_8.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'back_img_8.stopped')
                    # update status
                    back_img_8.status = FINISHED
                    back_img_8.setAutoDraw(False)
            
            # *FeedBack_LetterTask* updates
            
            # if FeedBack_LetterTask is starting this frame...
            if FeedBack_LetterTask.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                FeedBack_LetterTask.frameNStart = frameN  # exact frame index
                FeedBack_LetterTask.tStart = t  # local t and not account for scr refresh
                FeedBack_LetterTask.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(FeedBack_LetterTask, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'FeedBack_LetterTask.started')
                # update status
                FeedBack_LetterTask.status = STARTED
                FeedBack_LetterTask.setAutoDraw(True)
            
            # if FeedBack_LetterTask is active this frame...
            if FeedBack_LetterTask.status == STARTED:
                # update params
                pass
            
            # if FeedBack_LetterTask is stopping this frame...
            if FeedBack_LetterTask.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > FeedBack_LetterTask.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    FeedBack_LetterTask.tStop = t  # not accounting for scr refresh
                    FeedBack_LetterTask.tStopRefresh = tThisFlipGlobal  # on global time
                    FeedBack_LetterTask.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'FeedBack_LetterTask.stopped')
                    # update status
                    FeedBack_LetterTask.status = FINISHED
                    FeedBack_LetterTask.setAutoDraw(False)
            
            # *ErrorImage_2* updates
            
            # if ErrorImage_2 is starting this frame...
            if ErrorImage_2.status == NOT_STARTED and showErrorImage:
                # keep track of start time/frame for later
                ErrorImage_2.frameNStart = frameN  # exact frame index
                ErrorImage_2.tStart = t  # local t and not account for scr refresh
                ErrorImage_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ErrorImage_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ErrorImage_2.started')
                # update status
                ErrorImage_2.status = STARTED
                ErrorImage_2.setAutoDraw(True)
            
            # if ErrorImage_2 is active this frame...
            if ErrorImage_2.status == STARTED:
                # update params
                pass
            
            # if ErrorImage_2 is stopping this frame...
            if ErrorImage_2.status == STARTED:
                # is it time to stop? (based on local clock)
                if tThisFlip > 2-frameTolerance:
                    # keep track of stop time/frame for later
                    ErrorImage_2.tStop = t  # not accounting for scr refresh
                    ErrorImage_2.tStopRefresh = tThisFlipGlobal  # on global time
                    ErrorImage_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'ErrorImage_2.stopped')
                    # update status
                    ErrorImage_2.status = FINISHED
                    ErrorImage_2.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Letter_FeedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Letter_Feedback" ---
        for thisComponent in Letter_FeedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('Letter_Feedback.stopped', globalClock.getTime(format='float'))
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-2.000000)
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 5.0 repeats of 'trials_2'
    
    
    # --- Prepare to start Routine "ReadyMixed" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('ReadyMixed.started', globalClock.getTime(format='float'))
    key_resp_4.keys = []
    key_resp_4.rt = []
    _key_resp_4_allKeys = []
    # setup some python lists for storing info about the mouse_4
    mouse_4.x = []
    mouse_4.y = []
    mouse_4.leftButton = []
    mouse_4.midButton = []
    mouse_4.rightButton = []
    mouse_4.time = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    ReadyMixedComponents = [back_img_9, ReadyMix_img, key_resp_4, mouse_4]
    for thisComponent in ReadyMixedComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "ReadyMixed" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *back_img_9* updates
        
        # if back_img_9 is starting this frame...
        if back_img_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            back_img_9.frameNStart = frameN  # exact frame index
            back_img_9.tStart = t  # local t and not account for scr refresh
            back_img_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(back_img_9, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'back_img_9.started')
            # update status
            back_img_9.status = STARTED
            back_img_9.setAutoDraw(True)
        
        # if back_img_9 is active this frame...
        if back_img_9.status == STARTED:
            # update params
            pass
        
        # *ReadyMix_img* updates
        
        # if ReadyMix_img is starting this frame...
        if ReadyMix_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ReadyMix_img.frameNStart = frameN  # exact frame index
            ReadyMix_img.tStart = t  # local t and not account for scr refresh
            ReadyMix_img.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ReadyMix_img, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ReadyMix_img.started')
            # update status
            ReadyMix_img.status = STARTED
            ReadyMix_img.setAutoDraw(True)
        
        # if ReadyMix_img is active this frame...
        if ReadyMix_img.status == STARTED:
            # update params
            pass
        
        # *key_resp_4* updates
        waitOnFlip = False
        
        # if key_resp_4 is starting this frame...
        if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_4.frameNStart = frameN  # exact frame index
            key_resp_4.tStart = t  # local t and not account for scr refresh
            key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_4.started')
            # update status
            key_resp_4.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_4.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_4.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_4_allKeys.extend(theseKeys)
            if len(_key_resp_4_allKeys):
                key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
                key_resp_4.rt = _key_resp_4_allKeys[-1].rt
                key_resp_4.duration = _key_resp_4_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        # *mouse_4* updates
        
        # if mouse_4 is starting this frame...
        if mouse_4.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_4.frameNStart = frameN  # exact frame index
            mouse_4.tStart = t  # local t and not account for scr refresh
            mouse_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse_4.started', t)
            # update status
            mouse_4.status = STARTED
            mouse_4.mouseClock.reset()
            prevButtonState = mouse_4.getPressed()  # if button is down already this ISN'T a new click
        if mouse_4.status == STARTED:  # only update if started and not finished!
            buttons = mouse_4.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    pass
                    x, y = mouse_4.getPos()
                    mouse_4.x.append(x)
                    mouse_4.y.append(y)
                    buttons = mouse_4.getPressed()
                    mouse_4.leftButton.append(buttons[0])
                    mouse_4.midButton.append(buttons[1])
                    mouse_4.rightButton.append(buttons[2])
                    mouse_4.time.append(mouse_4.mouseClock.getTime())
                    
                    continueRoutine = False  # end routine on response
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ReadyMixedComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ReadyMixed" ---
    for thisComponent in ReadyMixedComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('ReadyMixed.stopped', globalClock.getTime(format='float'))
    # check responses
    if key_resp_4.keys in ['', [], None]:  # No response was made
        key_resp_4.keys = None
    thisExp.addData('key_resp_4.keys',key_resp_4.keys)
    if key_resp_4.keys != None:  # we had a response
        thisExp.addData('key_resp_4.rt', key_resp_4.rt)
        thisExp.addData('key_resp_4.duration', key_resp_4.duration)
    # store data for thisExp (ExperimentHandler)
    thisExp.addData('mouse_4.x', mouse_4.x)
    thisExp.addData('mouse_4.y', mouse_4.y)
    thisExp.addData('mouse_4.leftButton', mouse_4.leftButton)
    thisExp.addData('mouse_4.midButton', mouse_4.midButton)
    thisExp.addData('mouse_4.rightButton', mouse_4.rightButton)
    thisExp.addData('mouse_4.time', mouse_4.time)
    thisExp.nextEntry()
    # the Routine "ReadyMixed" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    Block = data.TrialHandler(nReps=6.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='Block')
    thisExp.addLoop(Block)  # add the loop to the experiment
    thisBlock = Block.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
    if thisBlock != None:
        for paramName in thisBlock:
            globals()[paramName] = thisBlock[paramName]
    
    for thisBlock in Block:
        currentLoop = Block
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
        if thisBlock != None:
            for paramName in thisBlock:
                globals()[paramName] = thisBlock[paramName]
        
        # --- Prepare to start Routine "reset_Mixed" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('reset_Mixed.started', globalClock.getTime(format='float'))
        # Run 'Begin Routine' code from code_2
        # Initialize global variables
        previousTask = None
        trialCounter = 0
        switchInterval = randint(3, 5)
        
        if Block.thisN % 2 ==0:
            taskOrder = 'letter'
        elif Block.thisN %2 ==1:
            taskOrder = 'number'
        # keep track of which components have finished
        reset_MixedComponents = []
        for thisComponent in reset_MixedComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "reset_Mixed" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in reset_MixedComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "reset_Mixed" ---
        for thisComponent in reset_MixedComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('reset_Mixed.stopped', globalClock.getTime(format='float'))
        # the Routine "reset_Mixed" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        trials_3 = data.TrialHandler(nReps=switchInterval, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='trials_3')
        thisExp.addLoop(trials_3)  # add the loop to the experiment
        thisTrial_3 = trials_3.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
        if thisTrial_3 != None:
            for paramName in thisTrial_3:
                globals()[paramName] = thisTrial_3[paramName]
        
        for thisTrial_3 in trials_3:
            currentLoop = trials_3
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
            )
            # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
            if thisTrial_3 != None:
                for paramName in thisTrial_3:
                    globals()[paramName] = thisTrial_3[paramName]
            
            # --- Prepare to start Routine "Mixed_Task" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('Mixed_Task.started', globalClock.getTime(format='float'))
            # Run 'Begin Routine' code from code_3
            # Presetting the variables used in Task-switching
            number = ['1','2','3','4','5','6','7','8']
            letter = ['A','E','I','U','G','M','K','R']
            
            # Define the base position
            basePos = 0.125
            
            # Define the possible quadrants
            topPositions = [
                [-basePos, basePos],  # Top-left
                [basePos, basePos]    # Top-right
            ]
            bottomPositions = [
                [-basePos, -basePos], # Bottom-left
                [basePos, -basePos]   # Bottom-right
            ]
            
            def get_new_combination(previousNumber, previousLetter):
                # Shuffle the quadrants, numbers, and letters
                shuffle(topPositions)
                shuffle(bottomPositions)
                shuffle(number)
                shuffle(letter)
            
                # Ensure the new combination is different from the previous one
                newNumber = number[0]
                newLetter = letter[0]
            
                while newNumber == previousNumber or newLetter == previousLetter:
                    shuffle(number)
                    shuffle(letter)
                    newNumber = number[0]
                    newLetter = letter[0]
            
                return newNumber, newLetter
            
            # Get a new combination ensuring it's different from the previous one
            number, letter = get_new_combination(previousNumber, previousLetter)
            
            if taskOrder == 'letter':
                selectedQuadrant = topPositions[0]
            elif taskOrder == 'number':
                selectedQuadrant = bottomPositions[0]
            
            # Set the stimulus position
            stimPos = selectedQuadrant
            
            # Determine the correct key based on the quadrant and the task
            if stimPos[1] > 0:  # Top quadrants (letter task)
                taskType = 'letter'
                if letter in ['A', 'E', 'I', 'U']:  # Vowel
                    correctKey = 'right'
                    correctkeyformouse = 'right_3'
                else:  # Consonant
                    correctKey = 'left'
                    correctkeyformouse = 'left_3'
            else:  # Bottom quadrants (number task)
                taskType = 'number'
                if int(number) % 2 == 0:  # Even number
                    correctKey = 'right'
                    correctkeyformouse = 'right_3'
                else:  # Odd number
                    correctKey = 'left'
                    correctkeyformouse = 'left_3'
                    
            # Determine if the trial is a repeat or a switch
            if Block.thisN ==0 and trials_3.thisN == 0:
                previousTask = taskType  # Initialize on first trial
                trialType = 'first'
                RT_list=[]
                trialtypelist=[]
                tasktypelist=[]
                acc_list=[]
            else:
                if taskType == previousTask:
                    trialType = 'repeat'
                else:
                    trialType = 'switch'
                previousTask = taskType  # Update for next trial
            Task_switch_stim.setPos(stimPos)
            Task_switch_stim.setText(letter + str(number))
            MixedResponse.keys = []
            MixedResponse.rt = []
            _MixedResponse_allKeys = []
            # setup some python lists for storing info about the NumberClickResponse_3
            NumberClickResponse_3.x = []
            NumberClickResponse_3.y = []
            NumberClickResponse_3.leftButton = []
            NumberClickResponse_3.midButton = []
            NumberClickResponse_3.rightButton = []
            NumberClickResponse_3.time = []
            NumberClickResponse_3.clicked_name = []
            gotValidClick = False  # until a click is received
            # keep track of which components have finished
            Mixed_TaskComponents = [back_img_4, grid_2, Task_switch_stim, MixedResponse, left_3, right_3, NumberClickResponse_3]
            for thisComponent in Mixed_TaskComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "Mixed_Task" ---
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *back_img_4* updates
                
                # if back_img_4 is starting this frame...
                if back_img_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    back_img_4.frameNStart = frameN  # exact frame index
                    back_img_4.tStart = t  # local t and not account for scr refresh
                    back_img_4.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(back_img_4, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'back_img_4.started')
                    # update status
                    back_img_4.status = STARTED
                    back_img_4.setAutoDraw(True)
                
                # if back_img_4 is active this frame...
                if back_img_4.status == STARTED:
                    # update params
                    pass
                
                # *grid_2* updates
                
                # if grid_2 is starting this frame...
                if grid_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    grid_2.frameNStart = frameN  # exact frame index
                    grid_2.tStart = t  # local t and not account for scr refresh
                    grid_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(grid_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'grid_2.started')
                    # update status
                    grid_2.status = STARTED
                    grid_2.setAutoDraw(True)
                
                # if grid_2 is active this frame...
                if grid_2.status == STARTED:
                    # update params
                    pass
                
                # *Task_switch_stim* updates
                
                # if Task_switch_stim is starting this frame...
                if Task_switch_stim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    Task_switch_stim.frameNStart = frameN  # exact frame index
                    Task_switch_stim.tStart = t  # local t and not account for scr refresh
                    Task_switch_stim.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Task_switch_stim, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Task_switch_stim.started')
                    # update status
                    Task_switch_stim.status = STARTED
                    Task_switch_stim.setAutoDraw(True)
                
                # if Task_switch_stim is active this frame...
                if Task_switch_stim.status == STARTED:
                    # update params
                    pass
                
                # *MixedResponse* updates
                waitOnFlip = False
                
                # if MixedResponse is starting this frame...
                if MixedResponse.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    MixedResponse.frameNStart = frameN  # exact frame index
                    MixedResponse.tStart = t  # local t and not account for scr refresh
                    MixedResponse.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(MixedResponse, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'MixedResponse.started')
                    # update status
                    MixedResponse.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(MixedResponse.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(MixedResponse.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if MixedResponse.status == STARTED and not waitOnFlip:
                    theseKeys = MixedResponse.getKeys(keyList=['left','right'], ignoreKeys=["escape"], waitRelease=False)
                    _MixedResponse_allKeys.extend(theseKeys)
                    if len(_MixedResponse_allKeys):
                        MixedResponse.keys = _MixedResponse_allKeys[-1].name  # just the last key pressed
                        MixedResponse.rt = _MixedResponse_allKeys[-1].rt
                        MixedResponse.duration = _MixedResponse_allKeys[-1].duration
                        # was this correct?
                        if (MixedResponse.keys == str(correctKey)) or (MixedResponse.keys == correctKey):
                            MixedResponse.corr = 1
                        else:
                            MixedResponse.corr = 0
                        # a response ends the routine
                        continueRoutine = False
                
                # *left_3* updates
                
                # if left_3 is starting this frame...
                if left_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    left_3.frameNStart = frameN  # exact frame index
                    left_3.tStart = t  # local t and not account for scr refresh
                    left_3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(left_3, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'left_3.started')
                    # update status
                    left_3.status = STARTED
                    left_3.setAutoDraw(True)
                
                # if left_3 is active this frame...
                if left_3.status == STARTED:
                    # update params
                    pass
                
                # *right_3* updates
                
                # if right_3 is starting this frame...
                if right_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    right_3.frameNStart = frameN  # exact frame index
                    right_3.tStart = t  # local t and not account for scr refresh
                    right_3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(right_3, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'right_3.started')
                    # update status
                    right_3.status = STARTED
                    right_3.setAutoDraw(True)
                
                # if right_3 is active this frame...
                if right_3.status == STARTED:
                    # update params
                    pass
                # *NumberClickResponse_3* updates
                
                # if NumberClickResponse_3 is starting this frame...
                if NumberClickResponse_3.status == NOT_STARTED and t >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    NumberClickResponse_3.frameNStart = frameN  # exact frame index
                    NumberClickResponse_3.tStart = t  # local t and not account for scr refresh
                    NumberClickResponse_3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(NumberClickResponse_3, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.addData('NumberClickResponse_3.started', t)
                    # update status
                    NumberClickResponse_3.status = STARTED
                    NumberClickResponse_3.mouseClock.reset()
                    prevButtonState = NumberClickResponse_3.getPressed()  # if button is down already this ISN'T a new click
                if NumberClickResponse_3.status == STARTED:  # only update if started and not finished!
                    buttons = NumberClickResponse_3.getPressed()
                    if buttons != prevButtonState:  # button state changed?
                        prevButtonState = buttons
                        if sum(buttons) > 0:  # state changed to a new click
                            # check if the mouse was inside our 'clickable' objects
                            gotValidClick = False
                            clickableList = environmenttools.getFromNames([left_3,right_3], namespace=locals())
                            for obj in clickableList:
                                # is this object clicked on?
                                if obj.contains(NumberClickResponse_3):
                                    gotValidClick = True
                                    NumberClickResponse_3.clicked_name.append(obj.name)
                            x, y = NumberClickResponse_3.getPos()
                            NumberClickResponse_3.x.append(x)
                            NumberClickResponse_3.y.append(y)
                            buttons = NumberClickResponse_3.getPressed()
                            NumberClickResponse_3.leftButton.append(buttons[0])
                            NumberClickResponse_3.midButton.append(buttons[1])
                            NumberClickResponse_3.rightButton.append(buttons[2])
                            NumberClickResponse_3.time.append(NumberClickResponse_3.mouseClock.getTime())
                            if gotValidClick:
                                continueRoutine = False  # end routine on response
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in Mixed_TaskComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "Mixed_Task" ---
            for thisComponent in Mixed_TaskComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('Mixed_Task.stopped', globalClock.getTime(format='float'))
            # Run 'End Routine' code from code_3
            thisExp.addData('taskType', taskType)
            thisExp.addData('trialType', trialType)
            thisExp.addData('reactiontime',NumberClickResponse_3.time)
            RT_list.append(NumberClickResponse_3.time[0])
            trialtypelist.append(trialType)
            tasktypelist.append(taskType)
            
            
            # Store the current values for the next trial
            previousNumber = number
            previousLetter = letter
            previousTask = taskType
            # check responses
            if MixedResponse.keys in ['', [], None]:  # No response was made
                MixedResponse.keys = None
                # was no response the correct answer?!
                if str(correctKey).lower() == 'none':
                   MixedResponse.corr = 1;  # correct non-response
                else:
                   MixedResponse.corr = 0;  # failed to respond (incorrectly)
            # store data for trials_3 (TrialHandler)
            trials_3.addData('MixedResponse.keys',MixedResponse.keys)
            trials_3.addData('MixedResponse.corr', MixedResponse.corr)
            if MixedResponse.keys != None:  # we had a response
                trials_3.addData('MixedResponse.rt', MixedResponse.rt)
                trials_3.addData('MixedResponse.duration', MixedResponse.duration)
            # store data for trials_3 (TrialHandler)
            trials_3.addData('NumberClickResponse_3.x', NumberClickResponse_3.x)
            trials_3.addData('NumberClickResponse_3.y', NumberClickResponse_3.y)
            trials_3.addData('NumberClickResponse_3.leftButton', NumberClickResponse_3.leftButton)
            trials_3.addData('NumberClickResponse_3.midButton', NumberClickResponse_3.midButton)
            trials_3.addData('NumberClickResponse_3.rightButton', NumberClickResponse_3.rightButton)
            trials_3.addData('NumberClickResponse_3.time', NumberClickResponse_3.time)
            trials_3.addData('NumberClickResponse_3.clicked_name', NumberClickResponse_3.clicked_name)
            # the Routine "Mixed_Task" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "Mixed_Feedback" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('Mixed_Feedback.started', globalClock.getTime(format='float'))
            # Run 'Begin Routine' code from FeedBack_Code_3
            # Define the base position
            basePos = 0.125
            
            # Determine the error image position based on the quadrant
            if stimPos[1] > 0:  # Top quadrants
                errorImagePos = [0.125 + 0.35, basePos]
                errorimgpth = 'stimuli/task1.png'
            else:  # Bottom quadrants
                errorImagePos = [0.125 + 0.35, -basePos]
                errorimgpth = 'stimuli/task2.png'
                
                
            # Check if the response was correct
            if MixedResponse.corr or correctkeyformouse in NumberClickResponse_3.clicked_name:
                feedbackText = '正確!'
                showErrorImage = False
                acc_list.append(1)
            else:
                feedbackText = '錯誤!'
                showErrorImage = True
                acc_list.append(0)
                
            
            
            # Control the visibility of the error image
            if showErrorImage:
                ErrorImage_3.setAutoDraw(True)
            else:
                ErrorImage_3.setAutoDraw(False)
            
            FeedBack_LetterTask_2.setText(feedbackText)
            ErrorImage_3.setPos(errorImagePos)
            ErrorImage_3.setImage(errorimgpth)
            # keep track of which components have finished
            Mixed_FeedbackComponents = [back_img_10, FeedBack_LetterTask_2, ErrorImage_3]
            for thisComponent in Mixed_FeedbackComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "Mixed_Feedback" ---
            routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 2.0:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *back_img_10* updates
                
                # if back_img_10 is starting this frame...
                if back_img_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    back_img_10.frameNStart = frameN  # exact frame index
                    back_img_10.tStart = t  # local t and not account for scr refresh
                    back_img_10.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(back_img_10, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'back_img_10.started')
                    # update status
                    back_img_10.status = STARTED
                    back_img_10.setAutoDraw(True)
                
                # if back_img_10 is active this frame...
                if back_img_10.status == STARTED:
                    # update params
                    pass
                
                # if back_img_10 is stopping this frame...
                if back_img_10.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > back_img_10.tStartRefresh + 2-frameTolerance:
                        # keep track of stop time/frame for later
                        back_img_10.tStop = t  # not accounting for scr refresh
                        back_img_10.tStopRefresh = tThisFlipGlobal  # on global time
                        back_img_10.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'back_img_10.stopped')
                        # update status
                        back_img_10.status = FINISHED
                        back_img_10.setAutoDraw(False)
                
                # *FeedBack_LetterTask_2* updates
                
                # if FeedBack_LetterTask_2 is starting this frame...
                if FeedBack_LetterTask_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    FeedBack_LetterTask_2.frameNStart = frameN  # exact frame index
                    FeedBack_LetterTask_2.tStart = t  # local t and not account for scr refresh
                    FeedBack_LetterTask_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(FeedBack_LetterTask_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'FeedBack_LetterTask_2.started')
                    # update status
                    FeedBack_LetterTask_2.status = STARTED
                    FeedBack_LetterTask_2.setAutoDraw(True)
                
                # if FeedBack_LetterTask_2 is active this frame...
                if FeedBack_LetterTask_2.status == STARTED:
                    # update params
                    pass
                
                # if FeedBack_LetterTask_2 is stopping this frame...
                if FeedBack_LetterTask_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > FeedBack_LetterTask_2.tStartRefresh + 2-frameTolerance:
                        # keep track of stop time/frame for later
                        FeedBack_LetterTask_2.tStop = t  # not accounting for scr refresh
                        FeedBack_LetterTask_2.tStopRefresh = tThisFlipGlobal  # on global time
                        FeedBack_LetterTask_2.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'FeedBack_LetterTask_2.stopped')
                        # update status
                        FeedBack_LetterTask_2.status = FINISHED
                        FeedBack_LetterTask_2.setAutoDraw(False)
                
                # *ErrorImage_3* updates
                
                # if ErrorImage_3 is starting this frame...
                if ErrorImage_3.status == NOT_STARTED and showErrorImage:
                    # keep track of start time/frame for later
                    ErrorImage_3.frameNStart = frameN  # exact frame index
                    ErrorImage_3.tStart = t  # local t and not account for scr refresh
                    ErrorImage_3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(ErrorImage_3, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'ErrorImage_3.started')
                    # update status
                    ErrorImage_3.status = STARTED
                    ErrorImage_3.setAutoDraw(True)
                
                # if ErrorImage_3 is active this frame...
                if ErrorImage_3.status == STARTED:
                    # update params
                    pass
                
                # if ErrorImage_3 is stopping this frame...
                if ErrorImage_3.status == STARTED:
                    # is it time to stop? (based on local clock)
                    if tThisFlip > 2-frameTolerance:
                        # keep track of stop time/frame for later
                        ErrorImage_3.tStop = t  # not accounting for scr refresh
                        ErrorImage_3.tStopRefresh = tThisFlipGlobal  # on global time
                        ErrorImage_3.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'ErrorImage_3.stopped')
                        # update status
                        ErrorImage_3.status = FINISHED
                        ErrorImage_3.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in Mixed_FeedbackComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "Mixed_Feedback" ---
            for thisComponent in Mixed_FeedbackComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('Mixed_Feedback.stopped', globalClock.getTime(format='float'))
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if routineForceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-2.000000)
            thisExp.nextEntry()
            
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
        # completed switchInterval repeats of 'trials_3'
        
    # completed 6.0 repeats of 'Block'
    
    
    # --- Prepare to start Routine "end" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('end.started', globalClock.getTime(format='float'))
    # Run 'Begin Routine' code from code_4
    # Provided arrays
    RT_array = np.array(RT_list)
    trialarray = np.array(trialtypelist)
    taskarray = np.array(tasktypelist)
    acc_array = np.array(acc_list)
    
    # Initialize variables
    repeat_rts = []
    switch_rts = []
    repeat_correct = 0
    switch_correct = 0
    repeat_total = 0
    switch_total = 0
    
    # Calculate metrics based on trial type
    for i in range(len(trialarray)):
        if trialarray[i] == 'repeat':
            repeat_rts.append(RT_array[i])
            repeat_correct += acc_array[i]
            repeat_total += 1
        elif trialarray[i] == 'switch':
            switch_rts.append(RT_array[i])
            switch_correct += acc_array[i]
            switch_total += 1
    
    # Calculate means
    mean_repeat_rt = np.mean(repeat_rts) if len(repeat_rts) > 0 else 0
    mean_switch_rt = np.mean(switch_rts) if len(switch_rts) > 0 else 0
    
    # Calculate accuracy
    repeat_accuracy = (repeat_correct / repeat_total) * 100 if repeat_total > 0 else 0
    switch_accuracy = (switch_correct / switch_total) * 100 if switch_total > 0 else 0
    
    # Calculate switch cost
    switch_cost = mean_switch_rt - mean_repeat_rt
    
    # Store metrics in the experiment
    thisExp.addData('mean_repeat_rt', mean_repeat_rt)
    thisExp.addData('mean_switch_rt', mean_switch_rt)
    thisExp.addData('repeat_accuracy', repeat_accuracy)
    thisExp.addData('switch_accuracy', switch_accuracy)
    thisExp.addData('switch_cost', switch_cost)
    
    # Store metrics in variables for display in traditional Chinese
    # Combine metrics into one text component
    performance_report_text = (
        f"重複試驗平均反應時間: {mean_repeat_rt:.2f} 秒\n\n"
        f"切換試驗平均反應時間: {mean_switch_rt:.2f} 秒\n\n"
        f"重複試驗正確率: {repeat_accuracy:.2f}%\n\n"
        f"切換試驗正確率: {switch_accuracy:.2f}%\n\n"
        f"切換成本: {switch_cost:.2f} 秒"
    )
    Thank_you.setPos((0,0))
    Thank_you.setText(performance_report_text)
    # keep track of which components have finished
    endComponents = [back_img_11, Thank_you]
    for thisComponent in endComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "end" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *back_img_11* updates
        
        # if back_img_11 is starting this frame...
        if back_img_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            back_img_11.frameNStart = frameN  # exact frame index
            back_img_11.tStart = t  # local t and not account for scr refresh
            back_img_11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(back_img_11, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'back_img_11.started')
            # update status
            back_img_11.status = STARTED
            back_img_11.setAutoDraw(True)
        
        # if back_img_11 is active this frame...
        if back_img_11.status == STARTED:
            # update params
            pass
        
        # *Thank_you* updates
        
        # if Thank_you is starting this frame...
        if Thank_you.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Thank_you.frameNStart = frameN  # exact frame index
            Thank_you.tStart = t  # local t and not account for scr refresh
            Thank_you.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Thank_you, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Thank_you.started')
            # update status
            Thank_you.status = STARTED
            Thank_you.setAutoDraw(True)
        
        # if Thank_you is active this frame...
        if Thank_you.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in endComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "end" ---
    for thisComponent in endComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('end.stopped', globalClock.getTime(format='float'))
    thisExp.nextEntry()
    # the Routine "end" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # mark experiment as finished
    endExperiment(thisExp, win=win)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # mark experiment handler as finished
    thisExp.status = FINISHED
    # shut down eyetracker, if there is one
    if deviceManager.getDevice('eyetracker') is not None:
        deviceManager.removeDevice('eyetracker')
    logging.flush()


def quit(thisExp, win=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    # shut down eyetracker, if there is one
    if deviceManager.getDevice('eyetracker') is not None:
        deviceManager.removeDevice('eyetracker')
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    setupDevices(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win,
        globalClock='float'
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win)
