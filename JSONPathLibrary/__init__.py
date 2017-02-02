#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import jsonpath

class JSONPathLibrary(object):
    def jsonpath_items(self, json_string, json_path):
        """
        Returns list of items from the provided json according to the provided JSONPath (http://goessner.net/articles/JsonPath/)
        Also, you can use online query tester at http://www.jsonquerytool.com/
     
        *Args:*\n
        _json_string_ - json-string;\n
        _json_path_ - JSONPath expression;
        
        *Return:*\n
        List of items according to the JSONPath query
        
        *Example:*\n
        | *Settings* | *Value* |
        | Library    | JSONPathLibrary |
        | *Variables* | *Value* |
        | ${test_str} | {"items":[{"name":"item1","status":{"id":1,"name":"opened"}},{"name":"item2","status":{"id":2,"name":"closed"}},{"name":"item3","status":{"id":3,"name":"closed"}}]} |
        | ${query}    | $.items[?(@.status.name=="closed")].name |
        | *Test Cases* | *Action* | *Argument* | *Argument* |
        | Find first item | ${answer}=      | JsonPath Items | ${test_str} | ${query} |
        |                  | Should be Equal | ${answer[0]}  | item2       |
        """
        json_object = json.loads(json_string)
        match_list = jsonpath.jsonpath(json_object, json_path)
        return match_list