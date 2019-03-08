import pandas as pd
import numpy as np
# This script only contains the processing functions for each different 
# neuropsych test.
# This keeps the fiunctions from the separate functions for handling the file readings
# and checking whether the data has been scored yet.
#
def ProcessVSTMBlock(Data):
    if len(Data) > 0:
        Out = {}
        # If there is an entry that is -99 it is a missing value and needs to be changed to NaN
        Data = Data.replace(-99, np.nan)
        TabNResp = pd.pivot_table(Data, values = 'Corr', index = 'Load', aggfunc = 'count')
        TabRT = pd.pivot_table(Data, values = 'RT', index = 'Load', aggfunc = np.mean)    
        TabAcc = pd.pivot_table(Data, values = 'Corr', index = 'Load', aggfunc = np.mean)    
        Out['NResp'] = TabNResp
        Out['RT'] = TabRT
        Out['Acc'] = TabAcc
    else:
        Out = {}
        Out['NResp'] = -9999
        Out['Acc'] = -9999
        Out['RT'] = -9999
    return Out
    
def ProcessDMSBlock(Data):
    if len(Data) > 0:
        Out = {}
        # This finds the number of trials for which a response was made
        TabNResp = pd.pivot_table(Data, values = 'resp.corr', index = 'Load', aggfunc = 'count')
        # What is the average RT broken by load
        TabRT = pd.pivot_table(Data, values = 'resp.rt', index = 'Load', aggfunc = np.mean)    
        # What is the average accuracy
        TabAcc = pd.pivot_table(Data, values = 'resp.corr', index = 'Load', aggfunc = np.mean)    
        Out['NResp'] = TabNResp
        Out['RT'] = TabRT
        Out['Acc'] = TabAcc
    else:
        Out = {}
        Out['NResp'] = -9999
        Out['Acc'] = -9999
        Out['RT'] = -9999
    return Out  
    
def ProcessDMSBlockv2(Data):
    Out = {}
    if len(Data) > 0:
        #cycle over load levels and save as relative load and absolute load
        UniqueLoad = Data['Load'].unique()
        UniqueLoad = UniqueLoad[~np.isnan(UniqueLoad)]
        UniqueLoad.sort()
        count = 1
        for i in UniqueLoad:
            temp = Data[Data['Load']==i]
            # find acc
            Acc = (temp['resp.corr'].mean())
            RT = (temp['resp.rt'].mean())
            NResp = (temp['resp.corr'].count())
            Tag1 = 'RelLoad%02d'%(count)
            Tag2 = 'AbsLoad%02d'%(i)
            Out[Tag1+'_Acc'] = Acc
            Out[Tag2+'_Acc'] = Acc
            Out[Tag1+'_RT'] = RT
            Out[Tag2+'_RT'] = RT
            Out[Tag1+'_NResp'] = NResp
            Out[Tag2+'_NResp'] = NResp
            count += 1
    else:
        for i in range(1,6):
            Tag1 = 'RelLoad%02d'%(i)
            Tag2 = 'AbsLoad%02d'%(i)
            Out[Tag1+'_Acc'] = -9999
            Out[Tag2+'_Acc'] = -9999
            Out[Tag1+'_RT'] = -9999
            Out[Tag2+'_RT'] = -9999
            Out[Tag1+'_NResp'] = -9999
            Out[Tag2+'_NResp'] = -9999
    return Out
    
def CalculateDMSLoad(OneLineOfData):
    # calculate load from CSV results file
    Stim = OneLineOfData['TL']+OneLineOfData['TM']+OneLineOfData['TR']
    Stim = Stim + OneLineOfData['CL']+OneLineOfData['CM']+OneLineOfData['CR']
    Stim = Stim + OneLineOfData['BL']+OneLineOfData['BM']+OneLineOfData['BR']
    if  not OneLineOfData.isnull()['TL']:
        Load = 9 - Stim.count('*')
    else:
        Load = np.nan
    #OneLineOfData['Load'] = Load
    return Load

def CheckDMSDataFrameForLoad(Data):
    if len(Data) > 0:
        # some versions of the DMS files do not have a column of load values
        if not 'Load' in Data.index:
            Load = []
            for index, row in Data.iterrows():
                Load.append(CalculateDMSLoad(row))
            Data['Load'] = Load
    return Data
    
def ProcessPattComp(Data):

    if len(Data) > 10:
        try:
            # First remove the practice rows from the data file
            Data_Run = Data[Data['Run.thisN'].notnull()]
            Out = {}
            LevelsOfDiff = Data_Run['Difficulty'].unique()
            LevelsOfDiff.sort()
            for i in LevelsOfDiff:
                temp = Data_Run[Data_Run['Difficulty'] == i]
                Tag = 'Load%02d'%(i)
                Out[Tag + '_Acc'] = temp['resp.corr'].mean()
                Out[Tag + '_RT'] = temp['resp.rt'].mean()
                Out[Tag + '_NResp'] = temp['resp.corr'].count()          
        except:
            Out = {}
            for i in range(1,4):
                Tag = 'Load%02d'%(i)
                Out[Tag + '_Acc'] = -9999
                Out[Tag + '_RT'] = -9999
                Out[Tag + '_NResp'] = -9999  
    else:
        Out = {}
        for i in range(1,4):
            Tag = 'Load%02d'%(i)
            Out[Tag + '_Acc'] = -9999
            Out[Tag + '_RT'] = -9999
            Out[Tag + '_NResp'] = -9999  

    return Out
    
def ProcessAntonym(Data):
    if len(Data) > 10:
        # First remove the practice rows from the data file
        Data_Run = Data[Data['trials.thisN'].notnull()]
        Out = {}
        Out['NResp'] = Data_Run['resp.corr'].count()
        Out['Acc'] = Data_Run['resp.corr'].mean()    
        Out['RT'] = Data_Run['resp.rt'].mean()

    else:
        Out = {}
        Out['NResp'] = -9999
        Out['Acc'] = -9999
        Out['RT'] = -9999
    return Out

def CheckWCSTErrors(CurrentRow, CurrentRule, PreviousRule):
    RuleList = []
    RuleList.append('Color')
    RuleList.append('Shape')
    RuleList.append('Count')   
    # Make this so it gets passed one row at a time because passing the entire DF is too much
    Sel = CurrentRow['Card%02d%s'%(int(CurrentRow['Card']),RuleList[CurrentRule])]
    Probe = CurrentRow['Probe%s'%(RuleList[CurrentRule])]
    # Do they match?
    Match = Sel == Probe
    Error = True
    PersError = False
    if Match:
        Error = False
    elif not Match:
    # If an error is made does it match the previous rule?
        Error = True
        PreviousProbe = CurrentRow['Probe%s'%(RuleList[PreviousRule])]
        if Sel == PreviousProbe:
            PersError = True
    return Error, PersError, Sel, Probe

def ProcessWCST(Data):
    if len(Data) > 10:
        # Remove the practice trials
        # The data file has two parts, one for practice and one for the actual task
        try:
            FindTask = Data[Data['TrialNum'].str.match('TrialNum')].index[0]
            Data_Run = Data.iloc[FindTask+1:]
            PreviousRule = -1
            # Start counters for the number of errors
            NumTrials = 0
            NumErrors = 0
            NumPersErrors = 0
            # Cycle over each data row
            for i, CurrentRow in Data_Run.iterrows():
                NumTrials += 1
                # extrcat the current rule
                CurrentRule = int(CurrentRow['Rule'])
                if (PreviousRule != -1) and (CurrentRule != LastTrialRule):
                    # If previous rule is -1 then leave it
                    # if the current rule is different from the rule on the last trial, then change the previous rule
                    # Then update the previous rule because the rules have changed
                    PreviousRule = LastTrialRule
                # Check for errors on this row
                (Error, PersError, Sel, Probe) = CheckWCSTErrors(CurrentRow, CurrentRule, PreviousRule)
                # update error counters
                if Error: 
                    NumErrors += 1
                if PersError:
                    NumPersErrors += 1
                LastTrialRule = CurrentRule
                #print('%d, CurrentRule = %d, Probe = %d, Sel = %d, Error = %r, PerError = %r'%(i, CurrentRule, Probe, Sel, Error, PersError))    
            #print('Number of Trials: %d, Number of Errors: %d, Number Pers Errors: %d'%(NumTrials, NumErrors, NumPersErrors))
            Out = {}
            Out['NTrials'] = NumTrials
            Out['NErrors'] = NumErrors
            Out['NPersErrors'] = NumPersErrors
        except:
            Out = {}
            Out['NTrials'] = NumTrials
            Out['NErrors'] = NumErrors
            Out['NPersErrors'] = NumPersErrors
    else:
        Out = {}
        Out['NTrials'] = -9999
        Out['NErrors'] = -9999
        Out['NPersErrors'] = -9999
    return Out
    
def ProcessMatrices(Data):
    if len(Data) > 0:
        # How many trials were completed
        NTrials = Data['key_resp_2.corr'].count()
        # How many trials were answered correctly
        NCorr = Data['key_resp_2.corr'].sum()
        # What is the percent accuracy
        Acc = Data['key_resp_2.corr'].mean()
        Out = {}
        Out['Acc'] = Acc
        Out['NTrials'] = NTrials
        Out['NCorr'] = NCorr 
    else:
        Out = {}
        Out['Acc'] = -9999
        Out['NTrials'] = -9999
        Out['NCorr'] = -9999       
    return Out


def ProcessStroopColor(Data):
    # Stroop color uses the shape color to determine the test colors which is the 
    # same as the TEXT color
    # Mapping is
    # Red -- v
    # Green -- b
    # Yellow - n
    # Blue - m
    if len(Data) > 0:
        # First remove the practice rows from the data file
        Data_Run = Data[Data['trials.thisN'].notnull()]
        Out = {}
        Out['Acc'] =   Data_Run['resp.corr'].mean()
        Out['NTrials'] = Data_Run['resp.corr'].count()
        Out['NCorr'] = Data_Run['resp.corr'].sum()
        Out['RT'] = Data_Run['resp.rt'].mean()
    else:
        Out = {}
        Out['Acc'] = -9999
        Out['NTrials'] = -9999
        Out['NCorr'] = -9999   
        Out['RT'] = -9999
    return Out
    
def ProcessStroopWord(Data):
    # Stroop color uses the shape color to determine the test colors which is the 
    # same as the TEXT color
    # Mapping is
    # Red -- v
    # Green -- b
    # Yellow - n
    # Blue - m
    if len(Data) > 0:
        # First remove the practice rows from the data file
        Data_Run = Data[Data['trials.thisN'].notnull()]
        Out = {}
        Out['Acc'] =   Data_Run['resp.corr'].mean()
        Out['NTrials'] = Data_Run['resp.corr'].count()
        Out['NCorr'] = Data_Run['resp.corr'].sum()
        Out['RT'] = Data_Run['resp.rt'].mean()
    else:
        Out = {}
        Out['Acc'] = -9999
        Out['NTrials'] = -9999
        Out['NCorr'] = -9999   
        Out['RT'] = -9999         
    return Out    
    
def ProcessStroopColorWord(Data):
    # Stroop color uses the shape color to determine the test colors which is the 
    # same as the TEXT color
    # Mapping is
    # Red -- v
    # Green -- b
    # Yellow - n
    # Blue - m
    if len(Data) > 0:
        # First remove the practice rows from the data file
        Data_Run = Data[Data['trials.thisN'].notnull()]
        Data_Run_Con = Data[Data['Congruency']=='Con']
        Data_Run_Incon = Data[Data['Congruency']=='Incon']
        Out = {}
        Out['All_Acc'] = Data_Run['resp.corr'].mean()
        Out['All_NTrials'] = Data_Run['resp.corr'].count()
        Out['All_NCorr'] = Data_Run['resp.corr'].sum()
        Out['All_RT'] = Data_Run['resp.rt'].mean()
        Out['Con_Acc'] = Data_Run_Con['resp.corr'].mean()
        Out['Con_NTrials'] = Data_Run_Con['resp.corr'].count()
        Out['Con_NCorr'] = Data_Run_Con['resp.corr'].sum()
        Out['Con_RT'] = Data_Run_Con['resp.rt'].mean()  
        Out['Incon_Acc'] = Data_Run_Incon['resp.corr'].mean()
        Out['Incon_NTrials'] = Data_Run_Incon['resp.corr'].count()
        Out['Incon_NCorr'] = Data_Run_Incon['resp.corr'].sum()
        Out['Incon_RT'] = Data_Run_Incon['resp.rt'].mean()  
        #               
        # Out['Acc'] = pd.pivot_table(Data_Run, values = 'resp.corr', index = 'Congruency', aggfunc = np.mean)
        # Out['NCorr'] = pd.pivot_table(Data_Run, values = 'resp.corr', index = 'Congruency', aggfunc = np.sum)
        # Out['NTrials'] = pd.pivot_table(Data_Run, values = 'resp.corr', index = 'Congruency', aggfunc = 'count')
        # Out['RT'] = pd.pivot_table(Data_Run, values = 'resp.rt', index = 'Congruency', aggfunc = np.mean)
    else:
        Out = {}
        Out['Acc'] = -9999
        Out['NTrials'] = -9999
        Out['NCorr'] = -9999   
        Out['RT'] = -9999    
    return Out        

def ProcessDigitSpan(Data, Dir):
    StairLoad = []
    Correct = []
    if len(Data) > 0:
        # cycle over each row 
        for i, CurrentRow in Data.iterrows():
            match, Load = ProcessDigitSpanOneRow(CurrentRow, Dir)
            StairLoad.append(Load)
            print(match)
            if match:
                Correct.append(1)
            else:
                Correct.append(0)
        Capacity, NReversals = CalculateCapacity(StairLoad)
        NTrials = len(Data)
        Out = {}
        Out['Capacity'] = Capacity
        Out['NReversals'] = NReversals
        Out['NTrials'] = NTrials
        Out['NCorrect'] = sum(Correct)
    else:
        Out = {}
        Out['Capacity'] = -9999
        Out['NReversals'] = -9999
        Out['NTrials'] = -9999
        Out['NCorrect'] = -9999
    print(Correct)
    return Out
            
def ProcessDigitSpanOneRow(Row, Dir):
    StrTest = Row['Digits']
    Test = [];
    for i in StrTest:
        if i.isdigit():
            Test.append(int(i))
    # This is stored as a string
    StrResp = Row['resp.keys']
    Resp = [];
    for i in StrResp:
        if i.isdigit():
            Resp.append(int(i))
    # If this is the backward span, flip the list
    if Dir == 'Backward':
        # Are the test sequence and the response the same?
        Test.reverse()
        match = Test == Resp
    else:
        match = Test == Resp
    # What is the load?
    Load = len(Test)
    return match, Load

def CalculateCapacity(StairLoad):
    # Take as input the load levels
    Rev = []
    # find out when the load is increasing and when it is decreasing
    Up = False
    Down = False
    Previous = 0
    for i in StairLoad:
        if i > Previous:
            Up = True
            Rev.append(1)
        elif i < Previous:
            Down = True
            Rev.append(-1)
        else:
            Rev.append(Rev[-1])
        Previous = i
        # any changes in the direction are reversals
    Rev = np.diff(Rev)
    Rev = np.nonzero(Rev)[0]
    RevLoads = np.array(StairLoad)[Rev]
    NReversals = len(RevLoads)
    Capacity = RevLoads.mean()
    return Capacity, NReversals