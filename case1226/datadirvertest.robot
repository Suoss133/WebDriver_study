*** Settings ***
Documentation    测试数据驱动
Test Template    用户登录失败的不同场景

*** Test Cases ***                 username        password
用户使用错误的用户名或密码登录失败       helloword       123456
用户使用空的用户名和密码登录失败        ${EMPTY}        ${EMPTY}
用户使用空用户名和非空密码登录         ${EMPTY}        123456


*** Keywords ***
用户登录失败的不同场景
    [Arguments]     ${username}     ${password}
    Log to console  ${username}
    Log to console  ${password}
