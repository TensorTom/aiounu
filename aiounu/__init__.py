import aiohttp
from mo_dots import to_data


class HTTPError(Exception):
	pass


async def shorten(url="https://example.com", output_format="json", keyword=""):
	"""
	Shorten a given URL.
	:param url: The URL to shorten.
	:param output_format: The return format (json, xml, simple)
	:param keyword: Keyword for the resulting URL (Optional)
	:return: Returns a dict-like dot.accessible.object if return-type is json,
			otherwise returns the result string (URL) from u.nu.
	"""

	if output_format not in ("simple", "xml", "json"):
		raise ValueError(f"_format must be one of: 'simple', 'xml', 'json'. Got: {output_format}")
	data = {
		"action": 'shorturl',
		"format": output_format,
		"url": url,
		"keyword": keyword
	}
	session = aiohttp.ClientSession()
	async with session.post("https://u.nu/api.php", params=data) as resp:
		print(await resp.text())
		if resp.status != 200:
			raise HTTPError(f"HTTP returned code {resp.status} rather than 200")
		await session.close()
		if output_format == 'json':
			return to_data(await resp.json())
		else:
			return await resp.text()
