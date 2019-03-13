def binary_classification_metrics(prediction, ground_truth):
    '''
    Computes metrics for binary classification

    Arguments:
    prediction, np array of bool (num_samples) - model predictions
    ground_truth, np array of bool (num_samples) - true labels

    Returns:
    precision, recall, f1, accuracy - classification metrics
    '''
    precision = 0
    recall = 0
    accuracy = 0
    f1 = 0

    # TODO: implement metrics!
    # Some helpful links:
    # https://en.wikipedia.org/wiki/Precision_and_recall
    # https://en.wikipedia.org/wiki/F1_score
    
    TP = ground_truth[(prediction == 1) & (ground_truth == 1)].shape[0]
    FP = ground_truth[(prediction == 1) & (ground_truth == 0)].shape[0]
    FN = ground_truth[(prediction == 0) & (ground_truth == 1)].shape[0]
    TN = ground_truth[(prediction == 0) & (ground_truth == 0)].shape[0]
    
    precision = TP / (TP + FP)
    recall = TP / (TP + FN)
    
    f1 = 2 / (1 / precision + 1 / recall)
    
    accuracy = (TP + TN) / (TP + TN + FP + FN)
    
    return precision, recall, f1, accuracy


def multiclass_accuracy(prediction, ground_truth):
    '''
    Computes metrics for multiclass classification

    Arguments:
    prediction, np array of int (num_samples) - model predictions
    ground_truth, np array of int (num_samples) - true labels

    Returns:
    accuracy - ratio of accurate predictions to total samples
    '''
    # TODO: Implement computing accuracy
    accuracy = sum(prediction == ground_truth) / len(prediction)
    return accuracy
