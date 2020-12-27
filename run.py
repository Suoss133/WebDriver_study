from robot import run_cli
import time
import os

if __name__ == '__main__':
    current_day = time.strftime('%Y_%m_%d')
    report_dir = os.path.join(os.path.dirname(__file__), f'repotr/{current_day}')
    run_cli(['-d', report_dir, 'case1226/datadriverlogin.robot'])
