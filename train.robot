*** Settings ***
Documentation    12306火车票查询
Library          SeleniumLibrary

*** Test Cases ***
if判断语句
     run keyword if     '1' == '2'
     ...                log to console      \n 123
    ...     ELSE        log to console      \n321

*** Test Cases ***
测试返回
    ${num}=     for语句
    log to console     ${num}



*** Keywords ***
for语句
    @{nums}=        Create List      1   2   3   4
    FOR     ${num}      IN          @{nums}
            run keyword if      '${num}' == '2'     R${num}      Exit for loop
    END