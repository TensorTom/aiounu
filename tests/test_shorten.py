import asyncio
import aiounu
import json


async def test_shorten():
	short_url = await aiounu.unu(url="https://example.com/", action="shorturl", _format="json", keyword="")
	assert 'statusCode' in short_url
	assert short_url['statusCode'] == 200
	assert short_url['shorturl'] == 'https://u.nu/example'


