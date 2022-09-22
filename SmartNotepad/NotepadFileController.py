from typing import Text
import speech_recognition as sr
import NotepadFileModel


class File_Controller:
    def __init__(self):
        self.my_file_model = NotepadFileModel.File_Model()

    def save_file(self, msg):
        self.my_file_model.save_file(msg)

    def save_as(self, msg):
        self.my_file_model.save_as(msg)

    def read_file(self, url=''):
        file_details = self.my_file_model.read_file(url)
        if file_details is None:
            return
        self.msg, self.base = file_details
        return self.msg, self.base

    def new_file(self):
        self.my_file_model.new_file()

    def take_Query(self):
        r = sr.Recognizer()
        m = sr.Microphone()
        with m as source:
            r.adjust_for_ambient_noise(source)
        #print("say something")
        with m as source:
            audio = r.listen(source)
        text = r.recognize_google(audio, language='en-IN')
        return text
