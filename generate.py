import sys
import getopt
import os
import json

def generate(name):
    path_name = "plugin-{}".format(name)

    # generate <name>.css
    style_file = "{}.css".format(name)
    style_content = ""

    # generate <name>.js
    script_file = "{}.js".format(name)
    script_content = "console.log('Hello, World!');"

    # generate <name>.html
    index_file = "{}.html".format(name)
    index_content = """<!DOCTYPE html>
<html>
<head>
    <title>{}</title>
    <meta charset="utf-8">
    <link href="../base1/cockpit.css" type="text/css" rel="stylesheet">
    <script src="../base1/cockpit.js"></script>
    <link href="{}" type="text/css" rel="stylesheet">
</head>
<body>
    <div class="pf-c-page">
       <!-- add content here -->
    </div>
    <script src="{}"></script>
</body>
</html>
""".format(name, style_file, script_file)

    # generate manifest.json
    manifest_file = "manifest.json"
    data = {}
    data["version"] = 0
    data["tools"] = {}
    data["tools"][name] = {}
    data["tools"][name]["label"] = name
    data["tools"][name]["path"] = index_file

    create_folder(path_name)
    save_file("{}/{}".format(path_name, index_file), index_content)
    save_file("{}/{}".format(path_name, style_file), style_content)
    save_file("{}/{}".format(path_name, script_file), script_content)
    save_file("{}/{}".format(path_name, manifest_file), json.dumps(data, indent=4))


def save_file(path, content):
    text_file = open(path, "w")
    text_file.write(content)
    text_file.close()
    return text_file


def create_folder(p):
    if not os.path.exists(p):
        os.makedirs(p)


def main(argv):
    try:
        opts, args = getopt.getopt(argv, "hn:", ["name="])
    except getopt.GetoptError:
        print("generate.py -n <api name>")
        sys.exit(2)

    name = ""
    code_type = ""
    path = "."

    for opt, arg in opts:
        if opt == "-h":
            print("generate.py -n <name>")
            sys.exit()
        elif opt in ("-n", "--name"):
            name = arg

    if name == "":
        print("name is empty")
        return

    generate(name)


if __name__ == "__main__":
    main(sys.argv[1:])
