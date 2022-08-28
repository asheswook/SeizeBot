import re
import os
from typing import Optional
from dataclasses import dataclass, field
from src.utils.logger import logger

"""
from component.default import *
from component.page import *

index = Index()
index.find_variable()
index.list_variables()
print(index.variables[0])
index.replace_variable(By.VAR, index.variables[0], "Hello1")
index.replace_variable(By.NUMBER, 1, "Hello2")
index.replace_variable(By.NAME, "ABC2", "Hello3")
"""


@dataclass
class Var:
    name: str
    edited: Optional[bool] = field(default=False)


class By:
    VAR = "var_object"
    NUMBER = "number"
    NAME = "name"


class Engine:
    def __init__(self):
        self.index = os.path.join(os.getcwd(), "src", "assets", "index.html")
        self.template = os.path.join(
            os.getcwd(), "src", "assets", "template.html")
        self.variables: list[Var] = []
        self.data = ""

    """var must be {{ABC1}}} not {{ABCD1}} or {{ABC11}}"""

    def find_variable(self):
        with open(self.template, 'r', encoding='utf-8') as page:
            if not self.data:
                self.data = page.read()

            regex = r"{{([a-zA-Z][a-zA-Z][a-zA-Z][0-9])}}"
            result = re.findall(regex, self.data)
            for name in result:
                self.variables.append(Var(name))

    def list_variables(self):
        for var in self.variables:
            logger.warning(var.name)

    # replace variable with value in index.html (write)
    def replace_variable(self, by, target, value: str):
        with open(self.template, 'r+', encoding='utf-8') as page:
            if not self.data:
                self.data = page.read()

            if by == By.VAR:  # target must be Var() object

                assert isinstance(
                    target, Var), "The target must be VarObject"
                assert target.edited is False, "This VarObject is already edited"

                self.data = self.data.replace("{{%s}}" % target.name, value)
                with open(self.index, 'w', encoding='utf-8') as page:
                    page.write(self.data)
                    target.edited = True

            elif by == By.NUMBER:  # target must be number

                assert isinstance(target, int), "The target must be number"
                assert target < len(
                    self.variables), "The target must be less than the length of VarObjects"
                assert self.variables[target].edited is False, "This VarObject is already edited"

                self.data = self.data.replace(
                    "{{%s}}" % self.variables[target].name, value)

                with open(self.index, 'w', encoding='utf-8') as page:
                    page.write(self.data)
                    self.variables[target].edited = True

            elif by == By.NAME:  # target must be string

                assert isinstance(
                    target, str), "The target must be string which is the name of VarObject"

                for i, var in enumerate(self.variables):
                    if var.name == target:
                        self.replace_variable(By.VAR, var, value)
                        break
                    else:
                        assert i != len(self.variables) - \
                            1, "The target must be exist in VarObjects"

    def add_content(self, content: str):
        with open(self.template, 'r+', encoding='utf-8') as page:
            if not self.data:
                self.data = page.read()

            self.data = self.data.replace("<!-- Line -->", content)

    def repeat_add_content(self, var_names: list):
        result = ""
        for var in var_names:
            content = """
            <!--""" + var + """-->
            <tr align="center" width="100px" height="30px" bgcolor="white">
                <td rowspan="2" width="100px"><img src="{{""" + var + """0}}"/></td>
                <td>{{""" + var + """1}}</td>
            </tr>
            <tr align="center" width="580px" height="60px" bgcolor="white">
                <td>조회수 {{""" + var + """2}}회 (+{{""" + var + """3}})</td>
            </tr>
            """
            result += content

        self.add_content(result)
