import asyncio
import aiounu as unu
import uuid


async def test_shorten():
	test_url = f"https://example.com/"
	short_url = await unu.shorten(url=test_url, output_format="json", keyword="")
	assert 'statusCode' in short_url
	assert short_url.statusCode == 200
	assert short_url.shorturl == 'https://u.nu/example'


async def test_shorten_unique():
	test_url = f"https://example.com/?test={uuid.uuid4()}"
	short_url = await unu.shorten(url=test_url, output_format="json", keyword="")
	assert 'statusCode' in short_url
	assert short_url.statusCode == 200




