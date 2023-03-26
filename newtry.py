import os
import shutil

fromdir = 'C:/Users/angel/Downloads'
todir = "C:/Users/angel/OneDrive/Documents/archivos_pdf"
fileslist = os.listdir(fromdir)

#print(os.listdir(fromdir))

for filename in fileslist:
    name, extension = os.path.splitext(filename)
    #print(name)
    #print(extension)
    if extension == '':
        continue
    if extension in ['.pdf', '.doc', '.docx']:
        path1 = fromdir + '/' + filename
        path2 = todir + '/' + 'archivos_formato_pdf'
        path3 = todir + '/' + 'archivos_formato_pdf'+ filename

        if os.path.exists(path2):
            print('moving ' + filename + '...' )
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print('moving ' + filename + '...')
            shutil.move(path1, path3)