import os
import PySimpleGUI as sg

sg.ChangeLookAndFeel('Dark')

class Main_Gui:
    
    def __init__(self):
        self.layout = [  
            [sg.Text('Target Path : '),sg.Input(key='PATH'),sg.FolderBrowse(button_text='Browse',initial_folder='C:'),sg.Button('Ok',key='PATH_OK')],
            [sg.Text('Give the search term to be search in files on Target path : '),sg.Input(key='SEARCH_TERM'),sg.Button('Ok',key='SEARCH_TERM_OK')],
            [sg.Text('Give a keyword to be replcaed with above search term : '),sg.Input(key='REPLACE'),sg.Button('Ok',key='REPLACE_KEY_OK')],
            [sg.Button('Run',key='RUN'),sg.Button('Cancel',key='CANCEL')],
            [sg.Output(size=(100,30),font=('Bookman Old Style',10))] 
            ]
        
        self.window = sg.Window('QC Automation',resizable=True).Layout(self.layout)
        
        
class Main_Task:
    
    def __init__(self):
        
        #default value of root paths will be string so keeping as blank
        self.root_path ,self.search_index ,self.replace_index = '' , '' , '' 
        
        #count to have total files in root_path and to store the path+file_names
        self.count_of_files, self.all_files = 0 , list()
        
        #count to store only text file and its path+file_name 
        self.text_files = list()
        
        #count to have search term in text files and its path+file_name
        self.search_term_text_files = list()
        
        
        
    def setting_up_new_index(self,values):
        self.root_path = values['PATH']
        print("\n Successfully choosen the path below path : \n",self.root_path)
        
        
    def setting_up_search_index(self,values):
        self.search_index = values['SEARCH_TERM']
        print("\n Successfully written the search term : \n",self.search_index)
        
        
    def setting_up_replace_index(self,values):
        self.replace_index = values['REPLACE']
        print("\n Successfully written the replace term : \n",self.replace_index)
        
        
        
    def counting_text_files(self):
        #self.root_path = values ['PATH']
        #self.search_index = values ['SEARCH_TERM']
        
        for path,dir_root,files in os.walk(self.root_path):
            if (len(files)>=1):
                self.count_of_files+=len(files)
                
                for file in files:
                    self.all_files.append(path+'\\'+file)
            else:
                continue
            
                    
        print(" \n The total count of files in root_path is : \n ",self.count_of_files)
        print(" \n Below are the files which is in root_path : \n ")
        for file in self.all_files:
            print(file)
        
        
        print("\n Filtering only text files from the root path : \n")
        for file in self.all_files:
            if(file.endswith('.txt')):
                self.text_files.append(file)
                
            else:
                continue
            
        print("\n Counting only text files from the root path is :{} ".format(len(self.text_files)))
        
        for file in self.text_files:
            print(file)
            
            
            
    def searching_keyword_files(self):
        
        
        for file in self.text_files:
            with open(file,'r') as f:
                if(self.search_index in f.read()):
                    self.search_term_text_files.append(file)
                else:
                    continue
          
        print("\n Total '{}' Text files which has '{}' keyword in it ".format(len(self.search_term_text_files),self.search_index))
        print("\n Listing those files which has search string in it : \n")
        for file in self.search_term_text_files:
            print(file)
        
        
    def replacing_keyword_files(self):
            
        for file in self.search_term_text_files:
            with open(file,'r+') as out_file:
                out_lines = out_file.readlines()
                
                with open(file,'w') as in_file:
                    for line in out_lines:
                        if(self.search_index in line):
                            print("\nKeyword found !")
                            in_file.write(line.replace(self.search_index, self.replace_index))
                            print("\nReplacing a keyword '{}' from a input search string '{}' on a file '{}' ".format(self.replace_index,self.search_index,file))
                        else:
                            in_file.write(line)
                 
            

def main():
    
    gui_window = Main_Gui()
    
    file_operation = Main_Task()
    
    
    
    while True:
        event , values = gui_window.window.read()
        
        if event is None:
            break;
        
        if event == 'CANCEL':
            break;
        
        if event == 'PATH_OK':
            file_operation.setting_up_new_index(values)
            
        if event == 'SEARCH_TERM_OK':
            file_operation.setting_up_search_index(values)
            
        if event == 'REPLACE_KEY_OK':
            file_operation.setting_up_replace_index(values)
            
        if event == 'RUN':
            file_operation.counting_text_files()
            file_operation.searching_keyword_files()
            file_operation.replacing_keyword_files()
            print("\n \n You can close the window \n")
            


if __name__ == "__main__":
    main()