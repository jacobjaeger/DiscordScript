#!/usr/bin/env python
# -*- coding: utf-8 -*-

# CAVEAT UTILITOR
#
# This file was automatically generated by TatSu.
#
#    https://pypi.python.org/pypi/tatsu/
#
# Any changes you make to it will be overwritten the next time
# the file is generated.


from __future__ import print_function, division, absolute_import, unicode_literals

import sys

from tatsu.buffering import Buffer
from tatsu.parsing import Parser
from tatsu.parsing import tatsumasu
from tatsu.util import re, generic_main  # noqa


KEYWORDS = {}  # type: ignore


class DiscordScriptBuffer(Buffer):
    def __init__(
        self,
        text,
        whitespace=None,
        nameguard=None,
        comments_re=None,
        eol_comments_re=None,
        ignorecase=None,
        namechars='',
        **kwargs
    ):
        super(DiscordScriptBuffer, self).__init__(
            text,
            whitespace=whitespace,
            nameguard=nameguard,
            comments_re=comments_re,
            eol_comments_re=eol_comments_re,
            ignorecase=ignorecase,
            namechars=namechars,
            **kwargs
        )


class DiscordScriptParser(Parser):
    def __init__(
        self,
        whitespace=None,
        nameguard=None,
        comments_re=None,
        eol_comments_re=None,
        ignorecase=None,
        left_recursion=True,
        parseinfo=True,
        keywords=None,
        namechars='',
        buffer_class=DiscordScriptBuffer,
        **kwargs
    ):
        if keywords is None:
            keywords = KEYWORDS
        super(DiscordScriptParser, self).__init__(
            whitespace=whitespace,
            nameguard=nameguard,
            comments_re=comments_re,
            eol_comments_re=eol_comments_re,
            ignorecase=ignorecase,
            left_recursion=left_recursion,
            parseinfo=parseinfo,
            keywords=keywords,
            namechars=namechars,
            buffer_class=buffer_class,
            **kwargs
        )

    @tatsumasu()
    def _start_(self):  # noqa

        def block0():
            with self._choice():
                with self._option():
                    self._command_main_()
                with self._option():
                    self._config_dir_()
                self._error('no available options')
        self._positive_closure(block0)
        self._check_eof()

    @tatsumasu()
    def _command_main_(self):  # noqa
        self._constant('command')
        self.name_last_node('type')
        self._token('!')
        self._pattern(r'[^{]+')
        self.name_last_node('name')
        self._token('{')
        self._generic_body_()
        self.name_last_node('content')
        self._token('}')
        self.ast._define(
            ['content', 'name', 'type'],
            []
        )

    @tatsumasu()
    def _generic_body_(self):  # noqa

        def block0():
            self._all_stmt_()
        self._positive_closure(block0)

    @tatsumasu()
    def _all_stmt_(self):  # noqa
        with self._choice():
            with self._option():
                self._func_main_()
            with self._option():
                self._if_stmt_()
            with self._option():
                self._assign_main_()
            self._error('no available options')

    @tatsumasu()
    def _config_dir_(self):  # noqa
        self._constant('config')
        self.name_last_node('type')
        self._token('@')
        self._pattern(r'[A-Za-z_]+')
        self.name_last_node('name')
        self._token(':')
        self._pattern(r'[^;]+')
        self.name_last_node('content')
        self._token(';')
        self.ast._define(
            ['content', 'name', 'type'],
            []
        )

    @tatsumasu()
    def _assign_main_(self):  # noqa
        self._constant('assignment')
        self.name_last_node('type')
        self._pattern(r'[A-Za-z_]+')
        self.name_last_node('name')
        self._token('=')
        self._assign_cont_()
        self.name_last_node('content')
        self.ast._define(
            ['content', 'name', 'type'],
            []
        )

    @tatsumasu()
    def _assign_cont_(self):  # noqa
        with self._choice():
            with self._option():
                self._func_main_()
            with self._option():
                self._item_()
                self.name_last_node('@')
                self._token(';')
            self._error('no available options')

    @tatsumasu()
    def _if_stmt_(self):  # noqa
        self._constant('if')
        self.name_last_node('type')
        self._token('if')
        self._token('(')
        self._logic_main_()
        self.name_last_node('condition')
        self._token(')')
        self._token('{')
        self._generic_body_()
        self.name_last_node('content')
        self._token('}')

        def block4():
            self._elif_stmt_()
        self._closure(block4)
        self.name_last_node('elif_')
        with self._optional():
            self._else_stmt_()
            self.name_last_node('else_')
        self.ast._define(
            ['condition', 'content', 'elif_', 'else_', 'type'],
            []
        )

    @tatsumasu()
    def _elif_stmt_(self):  # noqa
        self._constant('elif')
        self.name_last_node('type')
        self._token('elif')
        self._token('(')
        self._logic_main_()
        self.name_last_node('condition')
        self._token(')')
        self._token('{')
        self._generic_body_()
        self.name_last_node('content')
        self._token('}')
        self.ast._define(
            ['condition', 'content', 'type'],
            []
        )

    @tatsumasu()
    def _else_stmt_(self):  # noqa
        self._constant('else')
        self.name_last_node('type')
        self._token('else')
        self._token('{')
        self._generic_body_()
        self.name_last_node('content')
        self._token('}')
        self.ast._define(
            ['content', 'type'],
            []
        )

    @tatsumasu()
    def _func_embedded_(self):  # noqa
        self._constant('function_embedded')
        self.name_last_node('type')
        self._token('(')
        with self._group():
            self._pattern(r'[A-Za-z_]+')

            def block2():
                self._item_()
            self._closure(block2)
        self.name_last_node('content')
        self._token(')')
        self.ast._define(
            ['content', 'type'],
            []
        )

    @tatsumasu()
    def _func_main_(self):  # noqa
        self._constant('function')
        self.name_last_node('type')
        with self._group():
            self._pattern(r'[A-Za-z_]+')

            def block2():
                self._item_()
            self._closure(block2)
        self.name_last_node('content')
        self._token(';')
        self.ast._define(
            ['content', 'type'],
            []
        )

    @tatsumasu()
    def _logic_main_(self):  # noqa
        with self._choice():
            with self._option():
                self._constant('logic')
                self.name_last_node('type')
                with self._group():
                    self._item_()
                    self._logic_op_()
                    self._item_()
                self.name_last_node('content')
            with self._option():
                self._constant('logic')
                self.name_last_node('type')
                self._logic_bool_()
                self.name_last_node('content')
            self._error('no available options')
        self.ast._define(
            ['content', 'type'],
            []
        )

    @tatsumasu()
    def _logic_op_(self):  # noqa
        with self._choice():
            with self._option():
                self._constant('logic_op')
                self.name_last_node('type')
                self._token('is')
                self.name_last_node('content')
            with self._option():
                self._constant('logic_op')
                self.name_last_node('type')
                self._token('in')
                self.name_last_node('content')
            with self._option():
                self._constant('logic_op')
                self.name_last_node('type')
                self._token('!is')
                self.name_last_node('content')
            with self._option():
                self._constant('logic_op')
                self.name_last_node('type')
                self._token('!in')
                self.name_last_node('content')
            self._error('no available options')
        self.ast._define(
            ['content', 'type'],
            []
        )

    @tatsumasu()
    def _logic_bool_(self):  # noqa
        with self._choice():
            with self._option():
                self._constant('bool')
                self.name_last_node('type')
                self._token('true')
                self.name_last_node('content')
            with self._option():
                self._constant('bool')
                self.name_last_node('type')
                self._token('false')
                self.name_last_node('content')
            self._error('no available options')
        self.ast._define(
            ['content', 'type'],
            []
        )

    @tatsumasu()
    def _item_(self):  # noqa
        with self._choice():
            with self._option():
                self._arg_()
            with self._option():
                self._logic_bool_()
            with self._option():
                self._string_()
            with self._option():
                self._keyword_()
            with self._option():
                self._id_()
            with self._option():
                self._func_embedded_()
            self._error('no available options')

    @tatsumasu()
    def _keyword_(self):  # noqa
        self._constant('object')
        self.name_last_node('type')

        def sep2():
            self._token('.')

        def block2():
            self._pattern(r'[A-Za-z_]+')
        self._positive_gather(block2, sep2)
        self.name_last_node('content')
        self.ast._define(
            ['content', 'type'],
            []
        )

    @tatsumasu()
    def _id_(self):  # noqa
        self._constant('id')
        self.name_last_node('type')
        self._pattern(r'\d+')
        self.name_last_node('content')
        self.ast._define(
            ['content', 'type'],
            []
        )

    @tatsumasu()
    def _string_(self):  # noqa
        self._constant('string')
        self.name_last_node('type')
        self._token('"')
        self._pattern(r'([^"]|\s)+')
        self.name_last_node('content')
        self._token('"')
        self.ast._define(
            ['content', 'type'],
            []
        )

    @tatsumasu()
    def _arg_(self):  # noqa
        self._constant('argument')
        self.name_last_node('type')
        self._token('$')
        self._pattern(r'(\d+|@|[A-Za-z_]+)')
        self.name_last_node('content')
        self.ast._define(
            ['content', 'type'],
            []
        )


class DiscordScriptSemantics(object):
    def start(self, ast):  # noqa
        return ast

    def command_main(self, ast):  # noqa
        return ast

    def generic_body(self, ast):  # noqa
        return ast

    def all_stmt(self, ast):  # noqa
        return ast

    def config_dir(self, ast):  # noqa
        return ast

    def assign_main(self, ast):  # noqa
        return ast

    def assign_cont(self, ast):  # noqa
        return ast

    def if_stmt(self, ast):  # noqa
        return ast

    def elif_stmt(self, ast):  # noqa
        return ast

    def else_stmt(self, ast):  # noqa
        return ast

    def func_embedded(self, ast):  # noqa
        return ast

    def func_main(self, ast):  # noqa
        return ast

    def logic_main(self, ast):  # noqa
        return ast

    def logic_op(self, ast):  # noqa
        return ast

    def logic_bool(self, ast):  # noqa
        return ast

    def item(self, ast):  # noqa
        return ast

    def keyword(self, ast):  # noqa
        return ast

    def id(self, ast):  # noqa
        return ast

    def string(self, ast):  # noqa
        return ast

    def arg(self, ast):  # noqa
        return ast


def main(filename, start=None, **kwargs):
    if start is None:
        start = 'start'
    if not filename or filename == '-':
        text = sys.stdin.read()
    else:
        with open(filename) as f:
            text = f.read()
    parser = DiscordScriptParser()
    return parser.parse(text, rule_name=start, filename=filename, **kwargs)


if __name__ == '__main__':
    import json
    from tatsu.util import asjson

    ast = generic_main(main, DiscordScriptParser, name='DiscordScript')
    print('AST:')
    print(ast)
    print()
    print('JSON:')
    print(json.dumps(asjson(ast), indent=2))
    print()
