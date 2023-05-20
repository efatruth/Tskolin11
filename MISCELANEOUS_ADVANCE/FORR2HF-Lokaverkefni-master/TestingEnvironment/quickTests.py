#workplaces = [['Hraun Hótel Reykjavík'], ['Hraun Hótel Akureyri'], ['Hraun Hótel Selfoss']]
workplaces = [['Hraun Hótel Reykjavík']]

tmp = str()
if len(workplaces) == 1: tmp = workplaces[0][0]
else:
    for i in workplaces:
        if workplaces[-1][0] != i[0]: tmp += i[0] + ", "
        else: tmp += i[0]
