import os
import shutil

class File :


    def __init__(self):
        self.files= []
        self.zip_files = []
        self.exe_files = []
        self.jpg_files = []


    def folder (self):
        self.user_folder=input("Enter the folder to organize it :\n")
        self.files = os.listdir(self.user_folder)


    def file_organize(self, user_folder):
        self.zip_files = []
        self.exe_files = []
        self.jpg_files = []

        for filename in self.files:
            if filename.endswith(".zip"):
                self.zip_folder_name = user_folder + "/Archives"

                if not os.path.exists(self.zip_folder_name):
                    os.makedirs(self.zip_folder_name)
                    print("Folder created!")
                else:
                     print("Folder already exists.")
                self.zip_files.append(filename)

            elif filename.endswith(".exe"):
                self.exe_folder_name = user_folder + "/Projects"

                if not os.path.exists(self.exe_folder_name):
                    os.makedirs(self.exe_folder_name)
                    print("Folder created!")
                self.exe_files.append(filename)

            elif filename.endswith(".jpg"):
                self.jpg_folder_name="Images"
                self.jpg_folder_name = user_folder + "/Images"
                if not os.path.exists(self.jpg_folder_name):
                    os.makedirs(self.jpg_folder_name)
                    print("Folder created!")

                self.jpg_files.append(filename)


    def file_move ( self, user_folder, filename, folder_name, ):
        source = user_folder + "/" + filename
        destination = folder_name + "/" + filename
        shutil.move(source, destination)

    
    def move_all_files(self, user_folder):
        for fil in self.zip_files:
            self.file_move(user_folder, fil, self.zip_folder_name)
        for fil in self.exe_files:
            self.file_move(user_folder, fil, self.exe_folder_name)
        for fil in self.jpg_files:
            self.file_move(user_folder, fil, self.jpg_folder_name)


file = File()
file.folder()
file.file_organize(file.user_folder)
file.move_all_files(file.user_folder)