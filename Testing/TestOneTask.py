import os
import sys
from psychopy import core
BaseDir = '/home/jason/CognitiveTasksOnline'

sys.path.append(os.path.join(BaseDir,'ConfigFiles'))
sys.path.append(os.path.join(BaseDir,'GUI'))

import CheckExistingNeuroPsychData
from NCM_NeuroPsych_Config import *

PartID = '999111'


Task = '/DigitSpan/ForwardDigitSpanv3.py'

TaskPath = os.path.join(BaseDir, Task)

core.shellCall([sys.executable, TaskPath, PartID, BaseDir])