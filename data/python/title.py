import datetime
import pytz
import glob

utc_time = datetime.datetime.now(pytz.timezone('UTC'))
beijing_time = utc_time.astimezone(pytz.timezone('Asia/Shanghai')).strftime('%Y-%m-%d %H:%M:%S')

file_list = glob.glob('.././*.txt')

for file_path in file_list:
    with open(file_path, 'r') as file:
        content = file.read()

    line_count = content.count('\n') + 1

    new_content = f"[Adblock Plus 2.0]\n" \
                  f"! Title: ShuYiDNS\n" \
                  f"! Homepage: https://github.com/zly8686/ShuYiDNS\n" \
                  f"! Expires: 12 Hours\n" \
                  f"! Version: {beijing_time}（北京时间）\n" \
                  f"! Description: ShuYiDNS自用AdGuard Home去广告规则\n" \
                  f"! Total count: {line_count}\n" \
                  f"{content}"

    with open(file_path, 'w') as file:
        file.write(new_content)
