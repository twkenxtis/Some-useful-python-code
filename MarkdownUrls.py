import asyncio
import aiofiles
import os
import pickle

from aiocache import cached, Cache
# aiocache - BSD 3-Clause License
# Copyright (c) 2016, Manuel Miranda de Cid
# For more details, see the LICENSE file included with the distribution
from loguru import logger
# loguru is used under the MIT License
# Copyright (c) 2024 Delgan
# For more details, see the LICENSE file included with the distribution


# 不使用class 加快運作速度
def markdown_urls(url_string):
    return " ".join(
        [f"[{index+1}]({url})" for index,
            url in enumerate(url_string.split(" "))]
    )


class PickleLoader:

    @staticmethod
    @cached(ttl=1200, cache=Cache.MEMORY)
    async def load_pickle_dict(md5: str | None = None) -> str:
        pkl_file = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..",
                         "assets", "Twitter_dict.pkl")
        )
        if not os.path.isfile(pkl_file):
            logger.error(f"pkl_file: {pkl_file} 文件不存在")
            raise FileNotFoundError(f"pkl_file: {pkl_file} 文件不存在")

        async with aiofiles.open(pkl_file, "rb") as pkl:
            pkl_data = pickle.loads(await pkl.read(), fix_imports=True)

        value = pkl_data.get(md5)
        if value is not None:
            return value[6]

        logger.error("MD5 不正確!，字典中沒有此MD5")
        raise ValueError("MD5 not found")


if __name__ == "__main__":

    # 避免競爭條件
    async def run_PickleLoader():
        md5 = '8b384f75bedf6d97fdf3103375dff44c'
        return await PickleLoader.load_pickle_dict(md5)

    # asycio 只能啟動一個異步程式，剩下丟給函式處理
    tweet_image_urls = asyncio.run(
        run_PickleLoader()
    )  # 輸出字典中所有的 Tweet image urls
#
#
#
    # 放到Markdown計算 返回 str -> Markdown過的Url給Discord
    markdown = markdown_urls(tweet_image_urls)
    print(markdown)
