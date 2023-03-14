import csv

election_results='Election Results'
hline='-------------------------'
# read the data 
data=[]
with open('Resources/election_data.csv','r',newline='') as fr:
    reader=csv.reader(fr)
    for row in reader:
        data.append(row)
data=data[1:len(data)]

# find total number of votes cast 
number_votes=len(data)
number_votes_statement='Total Votes: '+str(number_votes) 

# complete list of candidates
candidate_dict={}
for d in data:
    candidate_dict[d[2]]=0
list_candidates=[]
for k in candidate_dict.keys():
    list_candidates.append(k)


# percentage of votes each candidate won
# total number of votes each candidate won
for d in data:
    candidate_dict[d[2]]=candidate_dict[d[2]]+1
percents=[]
for k in candidate_dict.keys():
    percents.append(candidate_dict[k]/number_votes)

# winner of election

#winner=list_candidates[0]
#print(candidate_dict[winner])
#for k in list_candidates:
    #if candidate_dict[winner]<candidate_dict[k]:
        #winner=candidate_dict[k]
#print(winner)

body=[]
for ii in range(len(list_candidates)):
    tmp_str=list_candidates[ii]+': '+str(percents[ii]*100)+'% ('+str(candidate_dict[list_candidates[ii]])+')'
    body.append(tmp_str)
print(election_results)
print(hline)
print(number_votes_statement)
print(hline)
new_body=[]
for b in body:
    print(b)
    new_body.append(b+'\n')
print(hline)

with open('analysis/results.txt','w') as fw:
    fw.writelines([election_results+'\n',hline+'\n',number_votes_statement+'\n',hline+'\n',new_body[0],new_body[1],new_body[2],hline+'\n'])
    

