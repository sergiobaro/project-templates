#!/usr/bin/python

import sys, os, shutil

def main(argv):
    ignoredFiles = ['.DS_Store']

    if len(argv) < 2:
        sys.exit('missing args')

    templateName = argv[0]
    programName = argv[1]

    templateDir = './' + templateName
    programNameDir = './' + programName

    for subdir, _, files in os.walk(templateDir):
        programSubdir = subdir.replace(templateDir, programNameDir)
        programSubdir = formatName(programSubdir, programName)
        print(programSubdir)
        os.mkdir(programSubdir)
        for file in files:
            if file not in ignoredFiles:
                print('  ' + subdir + '/' + file)
                fileContent = open(subdir + '/' + file, "r")
                programFile = formatName(file, programName)
                print(fileContent.read())

def formatName(value, programName):
    result = value.replace('{{name}}', programName)
    result = result.replace('{{name.lowercase}}', programName.lower())
    return result

if __name__ == "__main__":
   main(sys.argv[1:])