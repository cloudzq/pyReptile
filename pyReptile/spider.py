import asyncio
import aiohttp

# Setting parameters
TIMEOUT = 40
REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
}

loop = asyncio.get_event_loop()


# Define spider
class Request(object):
    async def httpGet(self, url, **kwargs):
        cookies = kwargs.get('cookies', {})
        params = kwargs.get('params', {})
        proxy = kwargs.get('proxy', '')
        timeout = kwargs.get('timeout', TIMEOUT)
        headers = kwargs.get('headers', REQUEST_HEADERS)
        if proxy:
            async with aiohttp.ClientSession(cookies=cookies) as session:
                async with session.get(url, params=params, proxy=proxy, timeout=timeout,
                                       headers=headers) as response:
                    result = dict(
                        content=await response.read(),
                        text=await response.text(),
                        status=response.status,
                        headers=response.headers,
                        url=response.url
                    )
                    return result
        else:
            async with aiohttp.ClientSession(cookies=cookies) as session:
                async with session.get(url, params=params, timeout=timeout,
                                       headers=headers) as response:
                    result = dict(
                        content=await response.read(),
                        text=await response.text(),
                        status=response.status,
                        headers=response.headers,
                        url=response.url
                    )
                    return result

    async def httpPost(self, url, **kwargs):
        cookies = kwargs.get('cookies', {})
        data = kwargs.get('data', {})
        proxy = kwargs.get('proxy', '')
        timeout = kwargs.get('timeout', TIMEOUT)
        headers = kwargs.get('headers', REQUEST_HEADERS)
        if proxy:
            async with aiohttp.ClientSession(cookies=cookies) as session:
                async with session.post(url, data=data, proxy=proxy, timeout=timeout,
                                        headers=headers) as response:
                    result = dict(
                        content=await response.read(),
                        text=await response.text(),
                        status=response.status,
                        headers=response.headers,
                        url=response.url
                    )
                    return result
        else:
            async with aiohttp.ClientSession(cookies=cookies) as session:
                async with session.post(url, data=data, timeout=timeout,
                                        headers=headers) as response:
                    result = dict(
                        content=await response.read(),
                        text=await response.text(),
                        status=response.status,
                        headers=response.headers,
                        url=response.url
                    )
                    return result

    # Define HTTP GET
    def get(self, url, **kwargs):
        tasks = []
        if isinstance(url, list):
            for u in url:
                task = asyncio.ensure_future(self.httpGet(u, **kwargs))
                tasks.append(task)
            result = loop.run_until_complete(asyncio.gather(*tasks))
        else:
            result = loop.run_until_complete(self.httpGet(url, **kwargs))
        return result

    # Define HTTP POST
    def post(self, url, **kwargs):
        tasks = []
        if isinstance(url, list):
            for u in url:
                task = asyncio.ensure_future(self.httpPost(u, **kwargs))
                tasks.append(task)
            result = loop.run_until_complete(asyncio.gather(*tasks))
        else:
            result = loop.run_until_complete(self.httpPost(url, **kwargs))
        return result


request = Request()
