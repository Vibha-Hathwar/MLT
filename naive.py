import csv
from collections import Counter
def calculate(data, row):
    target = [i[row] for i in data]
    return Counter(target)
def count_it(target, data, att):
    yes = 0
    no = 0
    for i in range(len(target)):
        if data[i] == att:
            if target[i] == 'Yes':
                yes += 1
            else:
                no += 1
    return [yes, no]
def probability(head, data, row):
    temp = [i[row] for i in data]
    tar = [i[-1] for i in data]
    yes = 0
    no = 0
    att = set(temp)
    dic = {}
    print(head)
    for i in att:
        dic[i] = count_it(tar, temp, i)
        print(i, count_it(tar, temp, i))
    print()
    return dic
def predict_class(data_dict, target, new_instance):
    yes = target['Yes'] / len(data)
    no = target['No'] / len(data)
    for i in range(len(new_instance)):
        t = data_dict[i][new_instance[i]]
        yes *= t[0] / target['Yes']
        no *= t[1] / target['No']
    return {'Yes': yes, 'No': no}
data_file = input('Enter the data file name: ')
with open(data_file) as f:
    data = list(csv.reader(f))
    heading = data[0]
    data = data[1:]
    target = calculate(data, -1)
    print(target)
    data_dict = {}
    for i in range(len(data[0]) - 1):
        data_dict[i] = probability(heading[i], data, i)
test_file = input('Enter the test file name: ')
with open(test_file) as f:
    test_data = list(csv.reader(f))
    test_heading = test_data[0]
    test_data = test_data[1:]
actual_labels = [instance[-1] for instance in test_data]
for idx, instance in enumerate(test_data):
    new_instance = instance[:-1]  
    print(f'\nInstance {idx + 1}: {new_instance}')
    probs = predict_class(data_dict, target, new_instance)
    print('Probabilities:', probs)
predicted_labels = []
for instance in test_data:
    new_instance = instance[:-1]  
    predicted_label = predict_class(data_dict, target, new_instance)
    predicted_labels.append('Yes' if predicted_label['Yes'] > predicted_label['No'] else 'No')
print(actual_labels)
print(predicted_labels)
correct_predictions = sum(1 for actual, predicted in zip(actual_labels, predicted_labels) if actual == predicted)
accuracy = correct_predictions / len(actual_labels) * 100
print(f"\nAccuracy: {accuracy:.2f}%")
