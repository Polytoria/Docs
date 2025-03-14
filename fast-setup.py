import subprocess 
import sys

print("Please wait one moment while we check everything! :3")

p = subprocess.Popen(["pip", "install", "mkdocs", "mkdocs-macros-plugin", "mkdocs-material", "mkdocs-material", "mkdocs-nav-weight"])

p.communicate();