import aiohttp


class HTTPError(Exception):
	pass


def user_choice(*choice):
	user_input = 0
	while not 1 <= user_input <= len(choice):
		for n in range(len(choice)):
			print("%d. %s" % (n + 1, choice[n]))
		user_input = int(input("Please Make a choice (only need to input the number): "))
	return choice[user_input - 1]


async def unu(url="https://vcinex.com", action="shorturl", format="json", keyword=""):
	"""
	Shorten a given URL.
	:param url: The URL to shorten.
	:param action: API action. Default: shorturl
	:param format: The return format (json, xml, simple)
	:param keyword: Keyword for the resulting URL (Optional)
	:return:
	"""
	if action != "shorturl":
		action = user_choice("shorturl")
	if format != "simple":
		format = user_choice("simple", "xml", "json")
	data = {
		"action": action,
		"format": format,
		"url": url,
		"keyword": keyword
	}
	session = aiohttp.ClientSession()
	async with session.get("https://u.nu/api.php", params=data) as resp:
		if resp.status != 200:
			raise HTTPError(f"HTTP returned code {resp.status} rather than 200")
		await session.close()
		return await resp.json()
