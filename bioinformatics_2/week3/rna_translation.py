from Bio.Seq import Seq


seqs = [
    "CCGAGGACCGAAAUCAAC",
    "CCACGUACUGAAAUUAAC",
    "CCAAGAACAGAUAUCAAU",
    "CCAAGUACAGAGAUUAAC",
]
for seq in seqs:
    print(Seq(seq).translate() == "")
