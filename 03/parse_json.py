import json

calls_result = []

def parse_json(json_str: str, keyword_callback, required_fields=None, keywords=None):
    report = []
    if len(json_str) == 0 or not required_fields or not keywords:
        calls_result.append([])
        return None
    
    json_doc = json.loads(json_str)
    
    if len(json_doc) == 0:
        calls_result.append([])
        return None
    
    for key in required_fields:
        if key in json_doc.keys():
            for keyword in keywords:
                if keyword in json_doc[key].split():
                    report.append([keyword, keyword_callback(keyword)])
                    keyword_callback(keyword)
    calls_result.append(report)
                    

def add_dot(s):
    return s + '.'



json_str1 = '{"key1": "Word1 word2", "key2": "word2 word3"}'
parse_json(json_str1, add_dot, required_fields=['key1'], keywords=['word2'])

assert calls_result[0] == [['word2', 'word2.']]

json_str2 = '{"key1": "Word1 word3", "key2": "word3 word3"}'
parse_json(json_str2, add_dot, required_fields=['key1'], keywords=['word2'])

assert calls_result[1] == []

json_str3 = '{"key1": "Word1 word2", "key2": "word2 word3"}'
parse_json(json_str3, add_dot, required_fields=['key1', 'key2'], keywords=['word2'])

assert calls_result[2] == [['word2', 'word2.'], ['word2', 'word2.']]

json_str4 = '{"key1": "Word1 word2", "key2": "word2 word3"}'
parse_json(json_str4, add_dot, required_fields=['key2'], keywords=['word2', 'word3'])

assert calls_result[3] == [['word2', 'word2.'], ['word3', 'word3.']]

json_str5= '{"key1": "Word1 word2", "key2": "word2 word3"}'
parse_json(json_str5, add_dot, required_fields=None, keywords=[])

assert calls_result[4] == []
