#! /usr/bin/python3
import os
import cgi

uploaded = cgi.FieldStorage()
path = os.path


def check_file() -> str:
    if "image_input" in uploaded:
        uploaded_file = uploaded["image_input"]
        if not path.exists("./cgi/tmp"):
            os.makedirs("./cgi/tmp")
        file_path = "./cgi/tmp/" + path.basename(uploaded_file.filename)
        open(file_path, "wb").write(uploaded_file.file.read())
        return os.getcwd() + "/cgi/tmp/" + path.basename(uploaded_file.filename)
    else:
        return "Error: uploading failed"


image_path = check_file()
response_body = [
    "HTTP/1.1 200 OK",
    "Content-type: text/html;charset=utf-8\n",
    "<html>",
    "<head>",
    "<title>Successful upload</title>",
    '<script src="https://cdn.tailwindcss.com"></script>',
    "</head>",
    '<body class="bg-slate-900 h-screen w-screen flex justify-center items-center text-slate-100">',
    '<div class="flex flex-col space-y-7 flex justify-center items-center p-10">',
    '<img src="https://raw.githubusercontent.com/EduardaDT/Webserv/main/www/assets/success.svg?token=GHSAT0AAAAAACJQY76JGTMKPNKPHWIMSOSKZK6K56A" class="w-2/5" />',
    '<div class="flex flex-col justify-center items-center space-y-3">',
    '<h1 class="font-bold text-3xl text-slate-400">Image uploaded to:</h1>',
    f'<code class="font-bold text-sm bg-slate-800 text-cyan-400 p-3 rounded-md md:text-xl">{image_path}</code>',
    "</div>",
    '<a href="../index.html"class="py-2 px-7 text-center ring-2 ring-cyan-500 rounded-full transition-all duration-300">Back to home</a>',
    "</div>",
    "</body>",
    "</html>",
]
[print(i) for i in response_body]
