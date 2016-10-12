import random

with open(PresTweets.csv) as data:
    with open(test_output, 'w') as test:
        with open(train_output, 'w') as train:
            header = next(data)
            test.write(header)
            train.write(header)
            for line in data:
                if random.random() > 0.85:
                    train.write(line)
                else:
                    test.write(line)