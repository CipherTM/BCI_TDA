# First Stage Function

def FeatureExtraction(FormattedData, TypeOfFeatures=['BandStopFilter-50-4-4'] WindowSize=1, SamplingFreqency=250):
    """
    Apply filters and dsp operations to the data.

    Arguments:
    FormattedData -- A numpy matrix of size (None, WindowSize*SamplingFreqency, 8).
    TypeOfFeatures -- A list containing information about the filters and the dsp operations needed to be done on the data.
    WindowSize -- Define the window size for the data set (ex: 2 sec WindowSize)
    SamplingFreqency -- the sampling frequency of the used kit
    
    Return:
    CleanedData -- The output data After applying any required filtering or dsp operations.
    """

    ### START CODE HERE ###
    
    ### END CODE HERE ###
    
    return CleanedData
    
    
    
    
    
### DEFINE ANY HELPING FUNCTIONS HERE ###
    
    
### ### ### ### ### ### ### ### ### ### #