def get_names():
    elem_list_inp = []
    while len(elem_list_inp) != 5:
        element = input("Enter the name of an element: ")
        
        if element.lower() in [x.lower() for x in elem_list_inp]:
            print(element,"was already entered  <--no duplicates allowed")
        elif element != "":
            elem_list_inp.append(element)
    return elem_list_inp
    
################################
import requests

response = requests.get('https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/elements1_20.txt')
################################
  
elements_file = response.text
elemfile_list = elements_file.split('\n')


elem_list_inp = get_names()

corr_res = []
incorr_res = []
for item in elem_list_inp:
    if item.lower() in [element.lower() for element in elemfile_list]:
        corr_res.append(item)
    else:
        incorr_res.append(item)
CorrPerc = len(corr_res)*20 #Percentage of Correct Responses

print('\n'+str(CorrPerc) + '%','correct\n'+'Found: ',end='')
for items in corr_res:
    print(items.title(),end=" ")

if len(incorr_res) != 0:
    print("\nNot Found: ",end=' ')
    for items in incorr_res:
        print(items.title(),end=" ")