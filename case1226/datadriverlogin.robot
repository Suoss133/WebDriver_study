*** Settings ***
Documentation    测试用户登录
Library         SeleniumLibrary
Resource        ../pom/longinpage.robot
Suite Setup     打开Chrome浏览器最大化并且导航到首页
Suite Teardown  关闭所有浏览器
Test Setup      首页点击登录跳转到登录页面
Test Teardown   清除浏览器cookie并导航到首页
Test Template   用户输入不同的登录数据登录失败


*** Test Cases ***                 username       password     erro_message
测试用户错误用户名或密码登录失败        helloword      123456       用户名或密码错误
测试用户登录输入空的用户名或密码登录失败        ${EMPTY}     ${EMPTY}       信息不完整。



*** Keywords ***
用户输入不同的登录数据登录失败
    [Arguments]     ${username}     ${password}     ${erro_message}
    输入用户名和密码点击点击登录      ${username}     ${username}
    用户登录失败提示的错误信息        ${erro_message}