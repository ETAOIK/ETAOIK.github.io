import re
import requests
import pandas as pd
import time
import random
from datetime import datetime
from bs4 import BeautifulSoup

# 请求用户输入Google Scholar主页的网址
url_base = input("请输入Google Scholar主页的网址: ")

# 定义HTTP请求头
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}
DOMAIN = "https://scholar.google.com"

def get_soup(url):
    """发送HTTP请求并获取BeautifulSoup对象"""
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()
    return BeautifulSoup(response.text, 'html.parser')

def get_full_authors(paper_url):
    """
    进入论文详情页获取所有作者的全名
    """
    try:
        # 增加随机延迟，保护IP
        time.sleep(random.uniform(0.5, 1.5)) 
        soup = get_soup(paper_url)
        # 详情页中，作者通常在 class 为 'gsc_oci_value' 的第一个 div 中
        # 对应标签是 "Authors"
        fields = soup.find_all('div', class_='gs_scl')
        for field in fields:
            field_name = field.find('div', class_='gsc_oci_field').text
            if 'Authors' in field_name or '作者' in field_name:
                return field.find('div', class_='gsc_oci_value').text
        return "N/A"
    except Exception as e:
        print(f"提取详情页失败: {e}")
        return "N/A"

def main():
    columns = ['年份', '期刊', '题目', '所有作者全名', '第一作者全名', '中文/英文']
    data_rows = []
    cstart = 0
    pagesize = 100

    while True:
        url = f'{url_base}&cstart={cstart}&pagesize={pagesize}'
        soup = get_soup(url)
        rows = soup.find_all('tr', class_='gsc_a_tr')
        
        if not rows: # 如果当前页没有数据，说明爬取完毕
            break

        for row in rows:
            # 1. 提取基本信息
            title_tag = row.find('a', class_='gsc_a_at')
            title = title_tag.text
            
            # 2. 获取详情页链接以提取全名
            relative_link = title_tag['href']
            full_paper_url = DOMAIN + relative_link
            print(f"正在深度提取题目：{title}")
            
            full_authors = get_full_authors(full_paper_url)
            
            # 3. 提取第一作者全名
            # 详情页返回的作者通常是 "Full Name, Full Name, Full Name"
            first_author_full = full_authors.split(',')[0].strip() if full_authors != 'N/A' else 'N/A'
            
            # 4. 提取年份和期刊
            year = row.find('span', class_='gsc_a_h gsc_a_hc gs_ibl').text
            journal_info = row.find_all('div', class_='gs_gray')[1].text.split(',')[0] if len(row.find_all('div', class_='gs_gray')) > 1 else 'N/A'
            journal_name = re.sub(r'\s\d+.*$', '', journal_info)

            # 5. 判断语种 (基于详情页全名判断)
            # 中文全名通常包含中文字符，英文包含逗号分隔
            if re.search(r'[\u4e00-\u9fa5]', full_authors):
                Chinese_English = '中'
            else:
                Chinese_English = '英'

            data = {
                '年份': year,
                '期刊': journal_name,
                '题目': title,
                '所有作者全名': full_authors,
                '第一作者全名': first_author_full,
                '中文/英文': Chinese_English
            }
            data_rows.append(data)
            
            # 打印进度
            print(f"作者全名：{full_authors}\n---")

        cstart += pagesize
        # 如果单页抓取的行数小于pagesize，说明到底了
        if len(rows) < pagesize:
            break
        
    # 保存文件
    papers_df = pd.DataFrame(data_rows, columns=columns)
    formatted_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f'papers_full_info_{formatted_time}.xlsx'
    papers_df.to_excel(filename, index=False)
    print(f'任务完成！文件已生成: {filename}')

if __name__ == "__main__":
    main()
