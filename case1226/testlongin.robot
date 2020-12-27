*** Settings ***
Documentation    测试用户登录
Library         SeleniumLibrary
Resource        ../pom/longinpage.robot
Suite Setup     打开Chrome浏览器最大化并且导航到首页
Suite Teardown  关闭所有浏览器
Test Setup      首页点击登录跳转到登录页面
Test Teardown   清除浏览器cookie并导航到首页


*** Test Cases ***
测试用户登录
    输入用户名和密码点击点击登录          fanmao1     123456
    登录成功跳转到首页


测试用户错误用户名或密码登录失败
    输入用户名和密码点击点击登录      helloworld     123456
    用户登录失败提示的错误信息        用户名或密码错误


测试用户登录输入空的用户名或密码登录失败
    输入用户名和密码点击点击登录      ${EMPTY}     ${EMPTY}
    用户登录失败提示的错误信息        信息不完整。