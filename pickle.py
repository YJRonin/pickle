import pickle

# 1. Leader Numbers
leader = {}
leader['Jacore'] = '(845) 200-6250'
leader['Andrew'] = '(925) 727-4611'
leader['Aris'] = '(510) 229-6359'
leader['Gabriel'] = '(510) 326-5834'
leader['Richard'] = '(510) 228-5623'

#2. Create/Open pod_nbrs.pk1 file
pod_file = open('pod_nbrs.pk1','wb')

#3. Write pod leader number to a file
pickle.dump(leader,pod_file)

#4 Member Numbers
member['Glenn'] = '(510) 328-8290'
member['Mallick'] = '(510) 409-8775'
member['Andrew'] = '(925) 727-4611'


#5. Write member numbers to pod_file
pickle.dump(member,pod_file)
 
#6. Close pod_file
pod_file.close()

#7. Open pod.file
pod_file = open('pod_nbrs.pk1', 'rb')

#8. Leader numbers
print('Leaders: ')
for key, value in leader.items():
    print(key, value)

print('\n')

#9 print POD members
print('Members')

print('\n')

#10 close pod_file

