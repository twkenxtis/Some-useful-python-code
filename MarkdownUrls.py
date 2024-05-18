import asyncio
import os
import pickle
from concurrent.futures import ThreadPoolExecutor
from typing import List, Tuple

# orjson is used under the MIT License
# Copyright (c) 2024 Delgan
# For more details, see the LICENSE file included with the distribution
from loguru import logger


class MarkDownUrl:

    def __init__(self, url_string: str) -> None:
        self.url_string = url_string

    # 定義一個異步並行方法裝飾器
    def async_parallel(self, func):
        # 包裝器函數，接收一個函數參數列表
        async def wrapper(args):
            # 使用ThreadPoolExecutor來創建一個執行者
            with ThreadPoolExecutor() as executor:
                # 使用asyncio.gather來並行執行多個異步任務
                return await asyncio.gather(
                    *[
                        # 將每個函數參數列表中的元素作為參數執行func函數
                        asyncio.get_running_loop().run_in_executor(
                            executor, func, *any_arg
                        )
                        for any_arg in args
                    ]
                )

        return wrapper

    # 靜態方法，用於格式化單個URL為Markdown連結格式
    @staticmethod
    def format_single_url(num: int, url: str) -> Tuple[int, str]:
        try:
            # 嘗試將URL格式化為Markdown連結，並返回其編號和格式化後的URL
            return num, f"[{num+1}]({url})"
        except Exception as e:
            raise ValueError(f"Error formatting URL at position {num}: {e}")

    # 異步方法，用於格式化整個URL字串為完整Markdown連結
    def format_urls(self) -> str:
        # 定義一個異步函數來執行格式化操作
        async def run_formatting(list_urls: List[str]) -> str:
            # 使用排序和列表推導式來組合所有格式化後的URL
            return ' '.join([url for _, url in sorted(await self.async_parallel(self.format_single_url)([(num, url) for num, url in enumerate(list_urls)]))])

        if not self.url_string.split(" "):
            raise ValueError("URL string is empty or not properly formatted.")
        # 執行異步函數並返回結果
        return asyncio.run(run_formatting(self.url_string.split(" ")))


if __name__ == "__main__":

  # 示例用法
  url_string = "http://example1.com http://example2.com http://example3.com"
  formatter = MarkDownUrl(url_string)
  try:
      formatted_urls = formatter.format_urls()
      print(formatted_urls)
  except ValueError as e:
      logger.warning(e)
