
# aiounu

An asyncio module for [unu](https://u.nu/) in Python3 using aiohttp. Forked from
[vcinex/unu](https://github.com/vcinex/unu).

## Install

        pip install aiounu
        
## Import

        from unu import unu  

## Use

        short_url = await unu(url="https://example.com/", action="shorturl", format="simple",keyword="")

Only the "url" variable is necessary.
