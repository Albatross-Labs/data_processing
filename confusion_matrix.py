import os
import re
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
import itertools

#confusion matrix 그리는 함수 정의하기
def plot_confusion_matrix(cm, target_names=None, cmap=None, normalize=True, labels=True, title=None):
    accuracy = np.trace(cm) / float(np.sum(cm))
    misclass = 1-accuracy


    if cmap is None:
        cmap = plt.get_cmap('Blues')

    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]

    plt.figure(figsize=(8, 6))
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()

    thresh = cm.max() / 1.5 if normalize else cm.max() / 2

    if target_names is not None:
        tick_marks = np.arange(len(target_names))
        plt.xticks(tick_marks, target_names)
        plt.yticks(tick_marks, target_names)

    if labels:
        for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
            if normalize:
                plt.text(j, i, "{:0.4f}".format(cm[i, j]),
                         horizontalalignment="center",
                         color="white" if cm[i, j] > thresh else "black")
            else:
                plt.text(j, i, "{:,}".format(cm[i, j]),
                         horizontalalignment="center",
                         color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('Real label')
    plt.xlabel('Predicted label\naccuracy={:0.4f}; misclass={:0.4f}'.format(accuracy, misclass))
    plt.gcf().subplots_adjust(bottom=0.20)
    #plt.show()
    plt.savefig('./matrix_image/'+title+'.png')

#confusion matrix 그릴 파일들
matrix_path='./matrix'
files=os.listdir(matrix_path)

#matrix 폴더 안에 있는 모든 file에 대해
for file in files:
    file_path = os.path.join(matrix_path, file)

    # matrix file 열기
    with open(file_path, 'r', encoding='utf-8') as f:
        data_file=f.readlines()

        #real_label과 predict_label 리스트 뽑기
        current=None
        real_label=[]
        predict_label=[]

        for line in data_file:
            if re.match('acc', line):
                acc=line.split()[2]
                continue

            real, predict=re.findall('\d+', line)
            real_label=[i for i in real]
            predict_label=[i for i in predict]

        '''
        #real_label과 predict_label 리스트 뽑기
        current=None
        real_label=[]
        predict_label=[]

        for line in data_file:
            if re.match('acc', line):
                acc=line.split()[2]
                continue

            if re.match('ckpt', line):
                ckpt=line.split()[2]
                continue

            elif re.match('real_label', line):
                current='real'

            elif re.match('predict_label', line):
                current='predict'

            for i in line.split():
                if i.isnumeric():
                    if current=='real':
                        real_label.append(i)
                    else:
                        predict_label.append(i)
        '''
    print(real_label)
    print(predict_label)

    #confusion matrix 그리기
    if '-1' in real_label: ### sentiment
        confusion_mat = confusion_matrix(real_label, predict_label)
        label = ["-1", "0", "1"]
        plot_confusion_matrix(confusion_mat, target_names=label, normalize=False, title=file[:-4] + 'confusion matrix')

    if '7' in real_label: ### theme
        confusion_mat = confusion_matrix(real_label, predict_label)
        label = np.arange(7)
        plot_confusion_matrix(confusion_mat, target_names=label, normalize=False, title=file[:-4] + 'confusion matrix')
    else: ### da
        confusion_mat = confusion_matrix(real_label, predict_label)
        label = np.arange(5)
        plot_confusion_matrix(confusion_mat, target_names=label, normalize=False, title=file[:-4] + 'confusion matrix')


'''
#label_dict 정의하기
theme_labels=["캐릭터", "아이템", "레이드", "업데이트", "이벤트", "버그", "해킹", "점검", "굿즈", "유저", "회사", "기타"]
da_labels=["질문", "의견", "건의", "인증", "친목", "정보"]
theme_label_dict={}
da_label_dict={}

for index, label in enumerate(theme_labels):
    theme_label_dict[index]=label

for index, label in enumerate(da_labels):
    da_label_dict[index]=label

'''

