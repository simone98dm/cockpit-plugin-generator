# Cockpit plugin generator

this repo contains a simple script to generate base files for a working plugin in [cockpit project dashboard](https://cockpit-project.org/).

## Usage

Generate
```bash
python3 generate.py -n <plugin-name>
```

To install on cockpit
```bash
cd <plugin-name>
ln -snf $PWD ~/.local/share/cockpit/<plugin-name>
```

