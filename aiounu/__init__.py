import aiohttp


class HTTPError(Exception):
	pass


async def shorten(url="https://example.com", output_format="json", keyword=""):
	"""
	Shorten a given URL.
	:param url: The URL to shorten.
	:param output_format: The return format (json, xml, simple)
	:param keyword: Keyword for the resulting URL (Optional)
	:return:
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
			return await resp.json()
		else:
			return await resp.text()
