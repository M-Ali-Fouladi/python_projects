import requests

def create_todo(data,api_url):
  
    response = requests.post(api_url, data=data)
    if response.status_code == 201:
        print('Todo created successfully!')
        return response.json()
    else:
        print('Failed to create todo.')
        return None
    
def update_todo(update_data,api_url):
    response = requests.put(api_url + str(update_data['id'])+'/', json=update_data)
    if response.status_code == 200:
        updated_data=response.json()
        print("updated")
        return updated_data
    else:
        return None


    
def gettodos(api_url):
    response=requests.get(api_url)
    if response.status_code==200:
        data=response.json()
        return data
    else:
        return None

   
        

    
# Example usage
if __name__ == '__main__': #to run this script lonely as a main script

    while True:
        api_url = 'http://127.0.0.1:8000/api/todos/'
        data={'title':"mohammadali",
          'completed':True}
        print('1- update_data'+'\n'+'2- create_data'+'\n'+'3- show_all_data'+'\n'+'4- Exit_Menu'+'\n')
        selected_num=input('enter number >>> ')
        if selected_num == "1":
            update_data={'id':6,'title':'nima','completed':True}
            update_todo_1=update_todo(update_data,api_url)
        elif selected_num == '2':
            created_todo = create_todo(data,api_url)   
            if created_todo:
               print(f'Todo ID: {created_todo["id"]}, Title: {created_todo["title"]}, Completed: {created_todo["completed"]}')          
        elif selected_num == '3':
            data=gettodos(api_url)
            if data:
                print(data)
        elif selected_num == "4":
            print('you are excited from menu.')
            break 
        else:
            print('invalid choice. please select a valid option.')




         
