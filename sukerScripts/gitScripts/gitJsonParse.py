# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 10:10:47 2017

@author: choonghyun.jeon

In Jenkins Usage:
  build script : 
    python gitJsonParse.py u-boot-2016.01 ${GERRIT_PATCHSET_REVISION}
"""

import subprocess
import sys
import json

gerritQueryProjectList = {"u-boot-2016.01":"nexell/linux/u-boot/u-boot-2016.01",
                          "kernel-4.4.19": "nexell/linux/kernel/kernel-4.4.19",
                          "bl1-s5p4418":   "nexell/bl1/bl1-s5p4418",
                          "bl1-s5p6818":   "nexell/bl1/bl1-s5p6818",
                          }

_S_ = ' '
_userID = 'suker@git.nexell.co.kr'

# i.e : "ssh -p 29418 suker@git.nexell.co.kr gerrit query --format JSON status:open project:nexell/linux/u-boot/u-boot-2016.01 --patch-sets"
gerritQuerySSHCmd = 'ssh -p 29418'
gerritQueryID = _userID
gerritQueryCmd = 'gerrit query'
gerritQueryFormat = 'JSON'
gerritQueryStatus = 'open'
gerritQueryProject = ''
gerritQueryAppendixParam = '--patch-sets'
_gerritQuery = ''

# i.e : git fetch ssh://suker@git.nexell.co.kr:29418/nexell/linux/u-boot/u-boot-2016.01 refs/changes/16/2816/1 && git cherry-pick FETCH_HEAD
cherrypickGitFetchCmd = 'git fetch ssh://'
cherrypickGitFetchID = _userID
cherrypickGitFetchPort = '29418'
cherrypickGitFetchProject = ''
cherrypickGitFetchRefs = ''
cherrypickGitFetchCherryParam = '&& git cherry-pick FETCH_HEAD'

_Colors={"BOLD":"\033[1m", "GREEN":"\033[32m", "RED":"\033[31m", "ENDC":"\033[0m"}

_projectInfo = []
_cherrypickInfo = []
_latestPatchsets = []
_indexGroup = []

def makeGerritQueryCmd(projectName):
    global _gerritQuery
    
    gerritQueryProjectFullName = gerritQueryProjectList[projectName]
    _gerritQuery = gerritQuerySSHCmd + _S_ + gerritQueryID +_S_ + gerritQueryCmd + _S_ + "--format" + _S_  + gerritQueryFormat + \
                   _S_ + "status:"+gerritQueryStatus + _S_ + "project:"+gerritQueryProjectFullName + _S_ + gerritQueryAppendixParam
        
    print _gerritQuery

def makeCherryPickCmd(refs, project):
    global cherrypickGitFetchProject
    global cherrypickGitFetchRefs
    
    cherrypickGitFetchRefs = refs
    cherrypickGitFetchProject = project
    _cherrypickCmd = cherrypickGitFetchCmd + _S_ + cherrypickGitFetchID + ':' + cherrypickGitFetchPort + '/' + cherrypickGitFetchProject + _S_ + \
                     cherrypickGitFetchRefs + _S_ + cherrypickGitFetchCherryParam
    print "make done cherrypick : " + _cherrypickCmd
    return _cherrypickCmd

def getLatestPatchset(patchsets):
    index = 0
    for patchset in patchsets :
        temp = int(patchset['number'])
        if index < temp:
            index = temp

    return patchsets[index-1]

def getInfo():
    global _projectInfo
    
    print "gerritQuery cmd : " +  _gerritQuery
    output=subprocess.check_output(_gerritQuery,shell=True)
    values = []
    for x in output.split('\n') :
        values.append(x)

    del values[-1]
    del values[-1]

    _projectInfo = [json.loads(y) for y in values]

    for pInfo in _projectInfo:
        _latestPatchsets.append(getLatestPatchset(pInfo['patchSets']))

def debugprint(self) :
    # For debugging
    for i in _latestPatchsets:
        print "----------------------------------------------"
        print "ref : " + i['ref']
        print "revision : " + i['revision']
        for j in i['parents'] :
            print "parents : " + j

def constructCherryPickIndexGroup(revision):
    #Current patchset make cherrypick
    index = searchRevision(revision)
    if index == -1 :
        print "There is no exist revision infomation!"
        return -1

    _indexGroup.append(index)

    parentRevision = _latestPatchsets[index]['parents'][0]
    print " --> %s "%_latestPatchsets[index]['revision'] + " --> parent : " + parentRevision

    constructCherryPickIndexGroup(parentRevision)

def constructCherryPickInfo():
    for index in _indexGroup :
        _cherrypickInfo.append(makeCherryPickCmd(_latestPatchsets[index]['ref'], _projectInfo[index]['project']))
        print _latestPatchsets[index]['ref']

    for i in _cherrypickInfo:
        print i

def searchRevision(revision):
    index = 0
    print "search revision ..."
    for info in _latestPatchsets :
        if info['revision']==revision :
            return index
        else :
            index = index + 1
    return -1

def printInfo(status) :
    if status=='ready' :
        print "==========================================================="
        print _Colors["GREEN"]+" Make CherryPick Info Running..." + _Colors["ENDC"]
        print "===========================================================\n"
    elif status=='run' :
        print "==========================================================="
        print _Colors["GREEN"]+" Apply CherryPick ..." + _Colors["ENDC"]
        print "===========================================================\n"
    elif status=='end' :
        print "==========================================================="
        print _Colors["GREEN"]+" Success CherryPick..." + _Colors["ENDC"]
        print "===========================================================\n"
    else:
        pass

def doCherryPick() :
    for cmd in _cherrypickInfo :
        output=subprocess.check_output(cmd,shell=True)
        print output

def main(args):
    #arg0 : project name postfix, i.e : u-boot-2016.01
    printInfo('ready')
    makeGerritQueryCmd(args[0])
    getInfo()
    constructCherryPickIndexGroup(args[1])
    constructCherryPickInfo()
    printInfo('run')
    doCherryPick()
    printInfo('end')
    
if __name__ == "__main__":
    args = sys.argv[1:]
    try :         
        main(args)
    finally : 
        pass
