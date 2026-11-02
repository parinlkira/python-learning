s1 = 'snooze alarms'
s2 = "alas, no more Z's"

s1 = s1.lower()
s2 = s2.lower()

for x in s1:
    if x.isalpha():
        if s1.count(x) != s2.count(x):
            print("Not anagrams")
            break
else:
    print("Anagrams")



