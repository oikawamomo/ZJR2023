import csv
import json

if __name__ == "__main__":
    with open("corefer_train.csv") as f1:
        d1 = csv.reader(f1)
        ignore=1
        out = open("corefer_train_final.csv", "a", newline='')
        csv_writer = csv.writer(out, dialect="excel")
        cnt=0
        last_new_id = 0
        coref_sten_set={}
        for r1 in d1:
            if ignore==1:
                csv_writer.writerow(r1)
                ignore=2
                continue
            text_s = r1[11]
            if text_s:
                csv_writer.writerow(r1)
