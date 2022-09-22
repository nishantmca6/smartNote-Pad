import NotepadDbModel


class Db_Controller:
    def __init__(self):
        self.my_db_model = NotepadDbModel.Db_Model()

    def get_db_status(self):
        return self.my_db_model.db_status

    def close_notepad(self):
        self.my_db_model.close_db_connection()

    def get_file_path(self, file_name):
        return self.my_db_model.get_file_path(file_name)

    def get_file_count(self):
        return self.my_db_model.get_file_count()

    def get_file_pwd(self, file_name):
        return self.my_db_model.get_file_pwd(file_name)

    def is_secure_file(self, file_name):
        return self.my_db_model.is_secure_file(file_name)

    def add_file(self, file_name, file_path, file_owner, file_pwd):
        if file_path == '':
            return ''
        if file_name in self.my_db_model.file_dict:
            return "File Already Present"
        self.my_db_model.add_file(file_name,
                                  file_path, file_owner, file_pwd)
        self.my_db_model.add_file_to_db(
            file_name, file_path, file_owner, file_pwd)
        return "File Added Successfully"

    def load_files_from_db(self):
        self.my_db_model.load_files_from_db()
        return self.my_db_model.file_dict

    def remove_file(self, file_name):
        return self.my_db_model.remove_file_from_db(file_name)

    def get_file_owner(self, file_name):
        return self.my_db_model.get_file_pwd(file_name)[2]
