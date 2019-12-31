from flask import Flask , request , url_for 
from flask_pymongo import PyMongo 

app = Flask(__name__)  

app.config['MONGO_URI'] = 'mongodb+srv://oum:123456KK@oum-kcdhs.mongodb.net/test?retryWrites=true&w=majority'
mongo = PyMongo(app) 

#la page d'index
@app.route('/') 
def index():  
    
    return '''  
    
        <form method="POST" action="/create" enctype="multipart/form-data"> 
           <label for="file">Choose a file</label> 
            <input type="file" name="file">  
            
            <input type="submit" value="submit">  
        </form> 
    ''' 
#importer le fichier à la base de données
@app.route('/create',methods=['POST'])
def create(): 
    if 'file' in request.files:  
        file = request.files['file'] 
        mongo.save_file(file.filename,file) 
        mongo.db.users.insert({'username' : 'oum', 'file_name' : file.filename})
    return 'The file is in your database !' 

#visualiser ou telecharger le fichier
@app.route('/file/<filename>') 
def file(filename): 
    return mongo.send_file(filename) 


