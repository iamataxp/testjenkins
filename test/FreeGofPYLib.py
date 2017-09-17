#-*-coding:utf-8 -*-
import jpype
import os

def robot_test_echoName(jar_path, name):
    jar_path=os.path.abspath(jar_path)
    print jar_path
    jpype.startJVM(jpype.getDefaultJVMPath(), "-ea", "-Djava.class.path=%s" % jar_path)
    test = jpype.JClass('TestJenkins')
    t = test()
    res = t.echoName(name)
    jpype.shutdownJVM()
    return res

# print robot_test_echoName("F:\PythonFiles\CommonTest\jenkins-tester.jar", "Terry")