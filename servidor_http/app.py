import web
import json

urls = ('/upload', 'Upload')

def write_json(new_data, index, filename, i):
    with open(filename,'r+') as file:
        # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data
        file_data[index].append(new_data)
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent = i)

class Upload:
    def GET(self):
        return """<html><head></head><body>
<form method="POST" enctype="multipart/form-data" action="">
<input type="file" name="myfile" />
<br/>
<input type="submit" />
</form>
</body></html>"""

    def POST(self):
        x = web.input(myfile={})
        raw = x['myfile'].value

        data = json.loads(raw)
        for i in range(len(data['data'])):
            write_json(data['data'][i], 'data','data_base.json', 1)
        raise web.seeother('/upload')


if __name__ == "__main__":
   app = web.application(urls, globals())
   app.run()