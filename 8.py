records=input('Введите рекорд Кирилла, Арины и Сергея ')
records=records.split(' ')
record_k=int(records[0])
record_a=int(records[1])
record_s=int(records[2])
score_list=[record_k, record_a, record_s]
score_list_new=sorted(score_list)
print(score_list_new[2])