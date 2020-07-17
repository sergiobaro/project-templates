#!/usr/bin/python

import sys, os, shutil

def main(argv):
    ignoredFiles = ['.DS_Store']

    if len(argv) < 2:
        sys.exit('missing args')

    templateName = argv[0]
    programName = argv[1]

    templateDir = templateName
    programDir = programName

    for templateSubdir, _, files in os.walk(templateDir):
        programSubdir = templateSubdir.replace(templateName, programDir)
        programSubdir = formatName(programSubdir, programName)
        print(programSubdir)
        os.mkdir(programSubdir)

        for templateFileName in files:
            if templateFileName not in ignoredFiles:
                templateFilePath = templateSubdir + '/' + templateFileName
                templateFile = open(templateFilePath, "r")
                templateFileContent = templateFile.read()
                templateFile.close()

                programFileName = formatName(templateFileName, programName)
                programFileContent = formatName(templateFileContent, programName)
                programFile = open(programSubdir + '/' + programFileName, "w")
                programFile.write(programFileContent)
                programFile.close()

def formatName(value, programName):
    result = value.replace('{{name}}', programName)
    result = result.replace('{{name.lowercase}}', programName.lower())
    return result

if __name__ == "__main__":
   main(sys.argv[1:])