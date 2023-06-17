"""
Contains various functions for computing statistics over 3D volumes
"""
import numpy as np

def Dice3d(a, b):
    """
    This will compute the Dice Similarity coefficient for two 3-dimensional volumes
    Volumes are expected to be of the same size. We are expecting binary masks -
    0's are treated as background and anything else is counted as data

    Arguments:
        a {Numpy array} -- 3D array with first volume
        
        b {Numpy array} -- 3D array with second volume

    Returns:
        float
    """
    if len(a.shape) != 3 or len(b.shape) != 3:
        raise Exception(f"Expecting 3 dimensional inputs, got {a.shape} and {b.shape}")

    if a.shape != b.shape:
        raise Exception(f"Expecting inputs of the same shape, got {a.shape} and {b.shape}")

    # TASK: Write implementation of Dice3D. If you completed exercises in the lessons
    # you should already have it.
    # <YOUR CODE HERE>
    b = np.array(b != 0, dtype=np.float32)
    a = np.array(a != 0, dtype=np.float32)
    
    intersection = np.sum(a * b)
    volume = np.sum(a) + np.sum(b)
    
    if volume == 0:
        return 1.0
   
    return 2 * float(intersection) / float(volume)

def Jaccard3d(a, b):
    """
    This will compute the Jaccard Similarity coefficient for two 3-dimensional volumes
    Volumes are expected to be of the same size. We are expecting binary masks - 
    0's are treated as background and anything else is counted as data

    Arguments:
        a {Numpy array} -- 3D array with first volume
        b {Numpy array} -- 3D array with second volume

    Returns:
        float
    """
    if len(a.shape) != 3 or len(b.shape) != 3:
        raise Exception(f"Expecting 3 dimensional inputs, got {a.shape} and {b.shape}")

    if a.shape != b.shape:
        raise Exception(f"Expecting inputs of the same shape, got {a.shape} and {b.shape}")

    # TASK: Write implementation of Jaccard similarity coefficient. Please do not use 
    # the Dice3D function from above to do the computation ;)
    # <YOUR CODE GOES HERE>
    b = np.array(b != 0, dtype=np.float32)
    a = np.array(a != 0, dtype=np.float32)
    
    
    intersection = np.sum(b * a)
    union = np.sum(np.clip(b + a, 0, 1))
    
    if union == 0:
        return 1.0
    
    jaccard = float(np.sum(intersection)) / float(np.sum(union))

    return jaccard

def Sensitivity3d(a, b):
    """
    This will compute the sensitivity metrics for two 3-dimensional volumes
    Volumes are expected to be of the same size. We are expecting binary masks - 
    0's are treated as background and anything else is counted as data

    Arguments:
        a {Numpy array} -- 3D array with first volume
        b {Numpy array} -- 3D array with second volume

    Returns:
        float
    """
    if len(a.shape) != 3 or len(b.shape) != 3:
        raise Exception(f"Expecting 3 dimensional inputs, got {a.shape} and {b.shape}")

    if a.shape != b.shape:
        raise Exception(f"Expecting inputs of the same shape, got {a.shape} and {b.shape}")
        
    b = np.array(b != 0, dtype=np.float32)
    a = np.array(a != 0, dtype=np.float32)
        
    tp = float(np.sum(b * a))
    fn = float(np.sum(b) -  tp)
    
    return tp/(tp + fn)

def Specificity3d(a, b):
    """
    This will compute the specificity metrics for two 3-dimensional volumes
    Volumes are expected to be of the same size. We are expecting binary masks - 
    0's are treated as background and anything else is counted as data

    Arguments:
        a {Numpy array} -- 3D array with first volume
        b {Numpy array} -- 3D array with second volume

    Returns:
        float
    """
    if len(a.shape) != 3 or len(b.shape) != 3:
        raise Exception(f"Expecting 3 dimensional inputs, got {a.shape} and {b.shape}")

    if a.shape != b.shape:
        raise Exception(f"Expecting inputs of the same shape, got {a.shape} and {b.shape}")
    
    b = np.array(b != 0, dtype=np.float32)
    a = np.array(a != 0, dtype=np.float32)
    
    tn = float(np.sum((b == 0) & (a == 0)))
    fp = float(np.sum((b == 0) & (a == 1)))
    
    return tn/(tn + fp)
        
       
        