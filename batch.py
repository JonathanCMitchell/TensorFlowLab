import math
def batches(batch_size, features, labels):
    """
    Create batches of features and labels
    :param batch_size: The batch size
    :param features: List of features
    :param labels: List of labels
    :return: Batches of (Features, Labels)
    """
    assert len(features) == len(labels)
    # TODO: Implement batching
    batches = []
    
    # for item in range(0, 4, 3) so go from 0 to 4 increment each 3
    for i in range(0, len(features), batch_size):
        end = i + batch_size
        batch = [features[i:end], labels[i:end]]
        batches.append(batch)
        
    return batches