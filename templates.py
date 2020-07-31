#!/usr/bin/python

import sys, os

def main(argv):
    fileToIgnore = ['.DS_Store']

    if len(argv) < 2:
        sys.exit('Usage: templates <template_name> <destination_folder>')

    templateName = argv[0]
    templateDir = templateName
    programDir, programName = os.path.split(argv[1])

    act = True
    verbose = True

    for templateSubdir, _, fileNames in os.walk(templateDir):
        programSubdir = templateSubdir.replace(templateName, programName)
        programSubdir = formatName(programSubdir, programName)
        programSubdir = os.path.join(programDir, programSubdir)
        if verbose: print(templateSubdir + ' => ' + programSubdir)
        if act: os.mkdir(programSubdir)

        for templateFileName in fileNames:
            if templateFileName in fileToIgnore: continue

            templateFilePath = os.path.join(templateSubdir, templateFileName)
            templateFile = open(templateFilePath, "r")
            templateFileContent = templateFile.read()
            templateFile.close()

            programFileName = formatName(templateFileName, programName)
            programFilePath = os.path.join(programSubdir, programFileName)
            if verbose: print(templateFilePath + ' => ' + programFilePath)
            if act:
                programFileContent = formatName(templateFileContent, programName)
                programFile = open(programFilePath, "w")
                programFile.write(programFileContent)
                programFile.close()

def formatName(value, programName):
    result = value.replace('{{name}}', programName)
    result = result.replace('{{name.lowercase}}', programName.lower())
    return result

if __name__ == "__main__":
   main(sys.argv[1:])