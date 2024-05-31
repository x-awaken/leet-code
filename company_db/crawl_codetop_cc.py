import requests
import pandas as pd
import math
import time
import random

companies = [
    {
        "id": 1,
        "name": "字节跳动",
        "is_new": False
    },
    {
        "id": 2,
        "name": "微软",
        "is_new": False
    },
    {
        "id": 3,
        "name": "美团",
        "is_new": False
    },
    {
        "id": 4,
        "name": "阿里巴巴",
        "is_new": False
    },
    {
        "id": 5,
        "name": "快手",
        "is_new": False
    },
    {
        "id": 6,
        "name": "腾讯",
        "is_new": False
    },
    {
        "id": 7,
        "name": "猿辅导",
        "is_new": False
    },
    {
        "id": 8,
        "name": "百度",
        "is_new": False
    },
    {
        "id": 9,
        "name": "滴滴",
        "is_new": False
    },
    {
        "id": 10,
        "name": "京东",
        "is_new": False
    },
    {
        "id": 11,
        "name": "华为",
        "is_new": False
    },
    {
        "id": 13,
        "name": "拼多多",
        "is_new": False
    },
    {
        "id": 16,
        "name": "网易",
        "is_new": False
    },
    {
        "id": 17,
        "name": "小米",
        "is_new": False
    },
    {
        "id": 18,
        "name": "商汤",
        "is_new": False
    },
    {
        "id": 19,
        "name": "旷视",
        "is_new": False
    },
    {
        "id": 20,
        "name": "亚马逊",
        "is_new": False
    },
    {
        "id": 21,
        "name": "虾皮",
        "is_new": False
    },
    {
        "id": 22,
        "name": "图森",
        "is_new": False
    },
    {
        "id": 23,
        "name": "携程",
        "is_new": False
    },
    {
        "id": 24,
        "name": "bilibili",
        "is_new": False
    }
]
jobs = [
    {
        "id": 1,
        "name": "后端"
    },
    {
        "id": 2,
        "name": "客户端"
    },
    {
        "id": 3,
        "name": "算法"
    },
    {
        "id": 4,
        "name": "前端"
    },
    {
        "id": 5,
        "name": "数据研发"
    },
    {
        "id": 6,
        "name": "测试"
    },
    {
        "id": 7,
        "name": "Software Engineer"
    }
]

def get_departments(company):
    url = f'https://codetop.cc/api/departments/?company={company["id"]}'
    ret = requests.get(url)
    departments = ret.json()
    return departments


def get_questions_all(job_id, company,department):
    def get_questions_one_page(page_num):
        job_name = [job['name'] for job in jobs if job['id']==job_id][0]
        url = f"https://codetop.cc/api/questions/?job={job_id}&company={company['id']}&department={department['id']}&page={page_num}&search=&ordering=-frequency"
        print(url)
        for i in range(1000):
            try:
                ret = requests.get(url)
                data = ret.json()
                if 'list' in data:
                    break
            except Exception as e:
                pass
            time.sleep(random.randint(30,70))
        
        questions = []
        questions_hit = []
        for e in data['list']:
            q = {}
            q['id'] = e['id']
            q['leetcode_id'] = e['leetcode']['question_id']
            q['title'] = e['leetcode']['title']
            q['content'] = e['leetcode']['content']
            q['slug_title'] = e['leetcode']['slug_title']
            q['hard_level'] = '简单' if e['leetcode']['level'] == 1 else '中等' if e['leetcode']['level'] == 2 else '困难' 
            q['url'] = f'https://leetcode.cn/problems/{q["slug_title"]}' if not e['leetcode']['expand'] else q['slug_title']
            questions.append(q)
            questions_hit.append({"job_name":job_name,"company_name":company['name'],"department_name":department['name'],'url':q['url'],'hit_count':e['value'],'last_hit_time':e['time']})
        return data['count'],questions,questions_hit
    i = 1
    total_cnt,_,_ = get_questions_one_page(1)
    page_count = math.ceil(total_cnt/20)
    questions_all = []
    questions_hit_all = []
    for i in range(1,page_count+1):
        _, questions,questions_hit = get_questions_one_page(i)
        questions_all += questions
        questions_hit_all += questions_hit
    return questions_all, questions_hit_all


def craw_all():
    q_set = set()
    questions_all = []
    questions_hit_all = []
    for job in jobs:
        job_id = job['id']
        for company in companies:
            departments = get_departments(company)
            for dep in departments:
                questions, questions_hit = get_questions_all(job_id, company, dep)
                for q in questions:
                    if q['url'] not in q_set:
                        q_set.add(q['url'])
                        questions_all.append(q)
                questions_hit_all += questions_hit

    return questions_all, questions_hit_all

if __name__ == "__main__":
    #print(get_departments('bilibili'))
    questions_all, questions_hit_all = craw_all()
    df = pd.DataFrame(questions_all)
    df.to_csv('company_db/questions.csv')
    df = pd.DataFrame(questions_hit_all)
    df.to_csv('company_db/question_hits.csv')
