from pprint import pprint

m_dict = {
    "city": 'Moscow',
    'temperature': '20'
}

print(m_dict["city"])
m_dict['temperature'] = '15'

pprint(m_dict)

print(m_dict.get('country'))
print(m_dict.get('country', 'Russia'))

m_dict['date'] = '27.05.2019'

pprint(m_dict)

print(len(m_dict))
