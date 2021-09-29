# -*- coding: utf-8 -*-
from logging import getLogger, config, StreamHandler, DEBUG
import os

import sys
from logutil import LogUtil
from importenv import ImportEnvKeyEnum
import importenv as setting

import ast
import subprocess

PYTHON_APP_HOME = os.getenv('PYTHON_APP_HOME')
logger = getLogger(__name__)
log_conf = LogUtil.get_log_conf(PYTHON_APP_HOME + '/config/log_config.json')
config.dictConfig(log_conf)
handler = StreamHandler()
handler.setLevel(DEBUG)
logger.setLevel(DEBUG)
logger.addHandler(handler)
logger.propagate = False

if __name__ == '__main__':

  package_name = 'aws-sdk'
  result = subprocess.run(['npm', 'search', package_name ,'--json=true'], stdout=subprocess.PIPE)

  # bytesとして帰ってくる。
  print(result.stdout)
  print(type(result.stdout))
  
  # bytes -> str変換
  to_str = result.stdout.decode('utf-8')
  print(type(to_str))
  
  # str -> dict or list変換
  # ここでdictどの型に変換されるかは元の文字列による。
  # npm search --json=trueは配列型のjsonで帰ってくるので、listに変換される。
  to_list = ast.literal_eval(to_str)
  print(type(to_list))
  
  # listの中身を確認
  for item in to_list:
    # こっちはdict
    print(type(item))
    if item['name'] == package_name:
      print(item['description'])