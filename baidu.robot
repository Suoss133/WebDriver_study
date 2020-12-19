*** Settings ***
Documentation       使用robot做百度自动化
Library             SeleniumLibrary

*** Test Cases ***
百度搜索
    Open Browser    url=https://www.baidu.com   browser=chrome  executable_path=./driver/chromedriver
    input Text      locator=id:kw   text=helloworld





