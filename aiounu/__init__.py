import aiohttp


class HTTPError(Exception):
	pass


async def unu(url="https://vcinex.com", action="shorturl", _format="json", keyword=""):
	"""
	Shorten a given URL.
	:param url: The URL to shorten.
	:param action: API action. Default: shorturl
	:param format: The return format (json, xml, simple)
	:param keyword: Keyword for the resulting URL (Optional)
	:return:
	"""
	if action != "shorturl":
		raise ValueError(f"Only 'shorturl' action is currently supported. Got: {action}")
	if _format not in ("simple", "xml", "json"):
		raise ValueError(f"_format must be one of: 'simple', 'xml', 'json'. Got: {_format}")
	data = {
		"action": action,
		"format": _format,
		"url": url,
		"keyword": keyword
	}
	session = aiohttp.ClientSession()
	async with session.post("https://u.nu/api.php", params=data) as resp:
		print(await resp.text())
		if resp.status != 200:
			raise HTTPError(f"HTTP returned code {resp.status} rather than 200")
		await session.close()
		return await resp.json()
