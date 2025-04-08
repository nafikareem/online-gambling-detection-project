def calculate_accuracy(y_true, y_pred):
    correct_predictions = sum(y_t == y_p for y_t, y_p in zip(y_true, y_pred))
    accuracy = correct_predictions / len(y_true)
    return accuracy

def generate_report(y_true, y_pred):
    from sklearn.metrics import classification_report
    report = classification_report(y_true, y_pred)
    return report