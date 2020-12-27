*** Settings ***
Documentation   用户登录页面上的操作
Library         SeleniumLibrary


*** Variables ***
${HomePage_url}         http://49.233.108.117:3000/



*** Keywords ***
打开Chrome浏览器最大化并且导航到首页
    Open Browser    url=${HomePage_url}     browser=chrome      executable_path=./driver/chromedriver
    Set Selenium Implicit Wait       10s
    Maximize Browser Window


首页点击登录跳转到登录页面
    Click Element       xpath://ul[@class="nav pull-right"]/li[last()]/a


输入用户名和密码点击点击登录
    [Arguments]         ${username}         ${passwd}
    Input Text          xpath://*[@id="name"]       ${username}
    Input Text          xpath://*[@id="pass"]       ${passwd}
    Click Element       xpath://*[@type="submit"]


登录成功跳转到首页
    Location Should Be      ${HomePage_url}


用户登录失败提示的错误信息
    [Arguments]     ${erro_meesage}
    Element Text Should Be      xpath://div[@class="alert alert-error"]/strong      ${erro_meesage}


关闭所有浏览器
    Close All Browsers


清除浏览器cookie并导航到首页
    Set Screenshot Directory        ./screenshots
    Capture Page Screenshot
    Delete All Cookies
    Go To        ${HomePage_url}
