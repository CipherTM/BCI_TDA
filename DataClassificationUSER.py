# First Stage Function

def DataClassificationUSER(CleanedData, Classes, WindowSize=1, SamplingFreqency=250):
    """
    provide a platform for the user to classify the data and prepare the final data set.

    Arguments:
    CleanedData -- The data after the feature extraction phase of size (None, WindowSize*SamplingFreqency, 8).
    Classes -- A dictionary containing the classes and thier representaion (Ex: ['cat':1, 'dog':2, 'trash_data':3])
    WindowSize -- Define the window size for the data set (ex: 2 sec WindowSize)
    SamplingFreqency -- the sampling frequency of the used kit
    
    Return:
    DataSet -- The output formatted data in the form (None, WindowSize*SamplingFreqency, Y, 8)
    """

    ### START CODE HERE ###
    
    ### END CODE HERE ###
    
    return FormattedData
    
    
    
    
    
### DEFINE ANY HELPING FUNCTIONS HERE ###
    
    
### ### ### ### ### ### ### ### ### ### #